package com.evan.yoooknight.service;

import com.evan.yoooknight.dao.BookDao;
import com.evan.yoooknight.dao.CategoryDao;
import com.evan.yoooknight.pojo.Book;
import com.evan.yoooknight.pojo.Category;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoryService {
    @Autowired
    CategoryDao categoryDao;

    public List<Category> list() {
        // springboot 2.2.1已经不支持sort实例化了
//        Sort sort = new Sort(Sort.Direction.DESC, "id");
        return categoryDao.findAll(Sort.by(Sort.Direction.DESC, "id"));
    }

    public Category get(int id) {
        return categoryDao.findById(id).orElse(null);
    }
}
