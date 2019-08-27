from tkinter import *
from sourceSpider.pinghaoche import spider as pingSpider
from sourceSpider.staticPage import spider as pageSpider

class myGui:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def setInitWindow(self):
        self.init_window_name.title("百度网盘资源搜索")

        self.init_window_name.geometry('500x400')

        self.init_search_Text = Text(self.init_window_name, width=30, height=2)
        self.init_search_Text.grid(row=0, column=1, padx=20, pady=10)

        # 结果集
        self.init_result_data = Text(self.init_window_name, width=50, height=20)
        self.init_result_data.config(state=DISABLED)
        self.init_result_data.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky=W)

        #滚动条
        scroll = Scrollbar(command=self.init_result_data.yview)
        self.init_result_data.config(yscrollcommand=scroll.set)
        scroll.grid(row=1,column=3, sticky=S + W + E + N)

        # 查询按钮
        # lm = init_search_Text.get(1.0, END)
        self.searchButton = Button(self.init_window_name, text="查询", bg='lightblue', command=self.abc)
        self.searchButton.grid(row=0, column=2)

    def abc(self):
        search = self.init_search_Text.get(1.0, END)

        # 这里写入的接口没有生效,不明白为什么
        # with open('wangsong.txt', 'a+') as f:
        #     f.write("======" + search + "00000000")

        a = pingSpider.Spider(search)
        ret = a.getlinkList()
        index = 1
        self.init_result_data.config(state=NORMAL)
        self.init_result_data.delete(1.0, END)
        if ret:
            for temp in ret:
                tempIndex = format(index, '0.1f')
                self.init_result_data.insert(tempIndex, "链接地址：" + temp['link'] + "\n")
                index += 1
                tempIndex = format(index, '0.1f')
                self.init_result_data.insert(tempIndex, "提取码：" + temp['code'] + "\n\n")
                index += 2
        else:
            self.init_result_data.insert(1.0, "非常抱歉，没有找到你要的影片")


        # for i in list(range(20)):
        #     tempIndex = format(i, '0.1f')
        #     self.init_result_data.insert(tempIndex, "lalalla\n")
        self.init_result_data.config(state=DISABLED)




# init_window = Tk()
# a = myGui(init_window)
# a.setInitWindow()
# init_window.mainloop()


# lj = Label(init_window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=35, height=2)

# lj.grid(row=0, column=6)

# Label(init_window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=35, height=2).grid(row=0, column=6)
# Label(init_window,text="sECOND").grid(row=0, column=1, columnspan=10, sticky=W+E, padx=100)
# Label(init_window, text='third').grid(row=0, column=11)

# init_data_Text = Text(init_window, width=10, height=2)
# init_data_Text.grid(row=9, column=0, rowspan=10, columnspan=10)

# init_search_Text = Text(init_window, width=30, height=2)
# init_search_Text.grid(row=0, column=1, padx=20, pady=10)
#
# init_result_data = Text(init_window, width=50, height=30)
# init_result_data.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky=W)
#
# # 查询按钮
# # lm = init_search_Text.get(1.0, END)
# searchButton = Button(init_window, text="查询", bg='lightblue', command=abc(init_search_Text, init_result_data))
# searchButton.grid(row=0, column=2)
#
# init_window.mainloop()