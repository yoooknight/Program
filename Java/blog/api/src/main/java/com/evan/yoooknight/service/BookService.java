package com.evan.yoooknight.service;

import com.evan.yoooknight.dao.BookDao;
import com.evan.yoooknight.pojo.Book;
import com.evan.yoooknight.pojo.Category;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    BookDao bookDao;

    @Autowired
    CategoryService categoryService;

    public List<Book> list() {
        return bookDao.findAll(Sort.by(Sort.Direction.DESC, "id"));
    }

    public void addOrUpdate(Book book) {
        bookDao.save(book);
    }

    public void deleteById(int id) {
        bookDao.deleteById(id);
    }

    public List<Book> listByCategory (int cid) {
        Category category = categoryService.get(cid);
        return bookDao.findAllByCategory(category);
    }
}
