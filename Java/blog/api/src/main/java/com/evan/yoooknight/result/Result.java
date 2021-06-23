package com.evan.yoooknight.result;

import lombok.Data;

@Data
public class Result {
    private int code;

    public Result(int code) {
        this.code = code;
    }
}