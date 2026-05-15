# from DrissionPage import ChromiumPage
import time
# from webdriver_manager.chrome import ChromeDriverManager
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import random
import re
from openpyxl import load_workbook
import pandas as pd
import os
import sys
import datetime
import pygetwindow as gw
import pyautogui
# from bs4 import BeautifulSoup

# global page
# global browser

FAILED_VALUE = "--"
DEFAULT_MAX_LINKS_PER_RUN = 10
DEFAULT_BATCH_WAIT_SECONDS = 150


def get_int_env(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        write_log(f"环境变量[{name}]不是有效整数，使用默认值[{default}]")
        return default


def get_bool_env(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "y", "on")


# def getUrls ():
#     # 加载 Excel 文件
#     file_path = "test.xlsx"  # 替换为你的文件路径
#     wb = load_workbook(file_path)
#
#     # 选择工作表
#     sheet = wb["Sheet1"]  # 替换为你的工作表名称
#
#     # 读取数据
#     for row in sheet.iter_rows(values_only=True):  # 逐行读取
#         print(row)
#
#     # 读取特定单元格
#     cell_value = sheet["A1"].value  # 读取 A1 单元格的值
#     print(f"A1 单元格的值: {cell_value}")


# def countdown(n):
#     for i in range(n, 0, -1):
#         print(f"倒计时{i}秒")
#         time.sleep(1)
#     else:
#         print("倒计时结束")

def check_login_success(page):
    # 等待可能出现的登录后元素（如用户头像）
    try:
        # 小红书用户头像的选择器示例（需通过浏览器开发者工具确认）
        page.wait_for_selector(".reds-avatar", timeout=5000)  # 替换为实际选择器
        write_log("检测到用户头像，登录成功！")
        return True
    except:
        write_log("未检测到登录状态")
        return False


def build_failed_result(author_url):
    return {
        "url": author_url,
        "liked_count": FAILED_VALUE,
        "collected_count": FAILED_VALUE,
        "comment_count": FAILED_VALUE,
        "share_count": FAILED_VALUE
    }


def build_blank_result():
    return {
        "url": "空白链接",
        "liked_count": 0,
        "collected_count": 0,
        "comment_count": 0,
        "share_count": 0
    }



def craw_web(page, author_url):
    try:
        page.goto(author_url, wait_until="domcontentloaded", timeout=30000)

        write_log("正在加载笔记页面...")

        data = page.content()

        # 四个统计字段都允许缺失，缺失时按 0 处理
        patterns = {
            "liked_count": r'"likedCount":"(\d+)"',
            "collected_count": r'"collectedCount":"(\d+)"',
            "comment_count": r'"commentCount":"(\d+)"',
            "share_count": r'"shareCount":"(\d+)"'
        }

        dic_ret = {"url": author_url}
        for key, pattern in patterns.items():
            match = re.search(pattern, data)
            if match:
                dic_ret[key] = match.group(1)
            else:
                write_log(f"链接[{author_url}]缺少字段[{key}]，按0写入")
                dic_ret[key] = 0

        write_log(dic_ret)
        return dic_ret
    except PlaywrightTimeoutError:
        write_log(f"链接[{author_url}]打开超时，已写入[{FAILED_VALUE}]并继续")
    except Exception as e:
        write_log(f"链接[{author_url}]抓取异常: {str(e)}，已写入[{FAILED_VALUE}]并继续")

    failed_result = build_failed_result(author_url)
    write_log(failed_result)
    return failed_result

    # print(like_button)

def resource_path(relative_path):
    """ 获取资源文件的绝对路径 """
    if hasattr(sys, '_MEIPASS'):
        # 打包后的程序运行时
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # 开发环境运行时
        return os.path.join(os.path.dirname(__file__), relative_path)


def find_chromium_executable():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    candidates = [
        os.path.join(base_path, "chrome.exe"),
        os.path.join(base_path, "chrome-win64", "chrome.exe"),
        os.path.join(base_path, "chrome-win", "chrome.exe"),
    ]

    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate

    raise FileNotFoundError(
        "未找到 Chromium 浏览器文件 chrome.exe，已检查路径: " + " | ".join(candidates)
    )


def write_log(logStr):
    print(logStr)
    currentDate = datetime.datetime.now().strftime("%m%d")

    with open("crawl_"+currentDate+".log", "a", encoding="utf-8") as file:
        print(logStr, file=file)


if __name__ == '__main__':
    max_links_per_run = get_int_env("CRAW_MAX_LINKS_PER_RUN", DEFAULT_MAX_LINKS_PER_RUN)
    batch_wait_seconds = get_int_env("CRAW_BATCH_WAIT_SECONDS", DEFAULT_BATCH_WAIT_SECONDS)
    confirm_each_link = get_bool_env("CRAW_CONFIRM_EACH_LINK", False)
    write_log("提示：请确认你的使用方式符合平台规则。程序已关闭伪装参数，并默认分批访问。")
    write_log(f"每批最多处理链接数: {max_links_per_run}")
    write_log(f"每批结束等待秒数: {batch_wait_seconds}")
    write_log(f"逐条确认: {'开启' if confirm_each_link else '关闭'}")

    # 获取屏幕分辨率
    # screen_width, screen_height = pyautogui.size()
    with sync_playwright() as p:
        browser_path = find_chromium_executable()
        write_log(browser_path)
        # 启动浏览器
        browser = p.chromium.launch(
            executable_path=browser_path,
            headless=False,
            args=[
                "--start-maximized"
            ],
            # proxy={
            #     "server": "http://127.0.0.1:1080",
            # }
        )

        page = browser.new_page()

        # 打开小红书官网
        page.goto("https://www.xiaohongshu.com")

        # # 获取浏览器窗口句柄
        # window = gw.getWindowsWithTitle("example.com")[0]
        #
        # # 将浏览器窗口移到屏幕右边
        # window_width, window_height = window.width, window.height
        # x_pos = screen_width - window_width  # 计算窗口的位置
        # window.moveTo(x_pos, 100)

        # 这里可以继续操作页面，例如登录、点击等
        input("请手动完成登录后，按回车键继续...")

        # 2. 检查登录状态
        if check_login_success(page):
            write_log("执行登录后的操作...")
            # 获取登录后的 Cookies
            cookies = page.context.cookies()

        # open(page)
        else:
            write_log("登录失败，请重试")
            browser.close()
            time.sleep(20)
            exit(-1)

        # 访问页面
        # author_url = "https://www.xiaohongshu.com/explore/67b54abb0000000029008e1f?xsec_token=ABhGUlMbVhtkDFyQtQ2-8ckY_zTib7bzgAJOKYrdKBg-E=&xsec_source=pc_search&source=web_search_result_notes"

        # 加载 Excel 文件
        file_path = "input.xlsx"  # 替换为你的文件路径

        if not os.path.exists(file_path):
            write_log(f'文件[{file_path}]不存在')
            time.sleep(20)
            exit(-1)

        wb = load_workbook(file_path)

        # 选择工作表
        sheet = wb["Sheet1"]  # 替换为你的工作表名称

        # 读取数
        dataList = []
        processed_links = 0
        for row in sheet.iter_rows(values_only=True):  # 逐行读取
            if not row:
                write_log("检测到空白行，写入[空白链接]")
                dataList.append(build_blank_result())
                continue

            row_url = row[0]
            if row_url == "链接":
                continue

            if row_url is None:
                write_log("检测到空白行，写入[空白链接]")
                dataList.append(build_blank_result())
                continue

            if isinstance(row_url, str):
                row_url = row_url.strip()

            if isinstance(row_url, str) and row_url == "":
                write_log("检测到空白行，写入[空白链接]")
                dataList.append(build_blank_result())
            elif isinstance(row_url, str) and "https://www.xiaohongshu.com/" in row_url:
                if processed_links >= max_links_per_run:
                    write_log(f"已处理[{max_links_per_run}]条链接，暂停[{batch_wait_seconds}]秒后继续。")
                    time.sleep(batch_wait_seconds)
                    processed_links = 0

                if confirm_each_link:
                    try:
                        confirm_value = input(f"即将打开链接：{row_url}\n确认继续请按回车，跳过请输入 s 后回车：").strip().lower()
                    except EOFError:
                        confirm_value = "s"
                    if confirm_value == "s":
                        write_log(f"用户跳过链接[{row_url}]")
                        dataList.append(build_failed_result(row_url))
                        continue

                write_log(row_url)
                try:
                    temp = craw_web(page, row_url)
                except Exception as e:
                    write_log(f"主循环处理链接[{row_url}]异常: {str(e)}，已写入[{FAILED_VALUE}]并继续")
                    temp = build_failed_result(row_url)
                dataList.append(temp)
                processed_links += 1
            else:
                dataList.append({
                    "url": row_url,
                    "liked_count": 0,
                    "collected_count": 0,
                    "comment_count": 0,
                    "share_count": 0
                })
            time.sleep(random.randint(1,20))

        # print(dataList)

        file_path = './output.xlsx'
        if os.path.exists(file_path):
            # 检查新文件名是否存在，如果存在则继续修改
            timestamp = int(time.time())
            new_name = f"output_{timestamp}.xlsx"

            # 修改文件名
            os.rename(file_path, new_name)
            write_log(f"文件已重命名为: {new_name}")
        else:
            write_log("文件不存在")

        # 示例字典列表
        # 将字典列表转换为DataFrame
        df = pd.DataFrame(dataList)

        # 将DataFrame写入Excel文件
        df.to_excel(file_path, index=False)

        write_log("文件已导出[output.xlsx]")
        time.sleep(20)
        exit()

        # cell_value = sheet["A1"].value  # 读取 A1 单元格的值
        # print(f"A1 单元格的值: {cell_value}")
