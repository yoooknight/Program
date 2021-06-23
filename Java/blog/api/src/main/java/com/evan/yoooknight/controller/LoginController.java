package com.evan.yoooknight.controller;

import com.evan.yoooknight.pojo.User;
import com.evan.yoooknight.result.Result;
import com.evan.yoooknight.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.util.HtmlUtils;

import javax.servlet.http.HttpSession;
import java.util.Objects;


@Controller
public class LoginController {
    @Autowired
    UserService userService;

    @CrossOrigin
    @PostMapping(value = "api/login")
    @ResponseBody
    public Result login(@RequestBody User requestUser, HttpSession session) {
        // 对html 标签进行转义，防止xss攻击
        String username = requestUser.getUsername();
        username = HtmlUtils.htmlEscape(username);

//        if (!Objects.equals("admin", username) || !Objects.equals("123456", requestUser.getPassword())) {
//            String message = "账号密码错误";
//            System.out.println("test");
//            return new Result(400);
//        } else {
//            return new Result(200);
//        }

        User user = userService.get(username, requestUser.getPassword());
        if(null == user) {
            return new Result(400);
        } else {
            session.setAttribute("user", user);
            return new Result(200);
        }
    }
}