package com.evan.yoooknight.service;

import com.evan.yoooknight.dao.BookDao;
import com.evan.yoooknight.pojo.Book;
import com.evan.yoooknight.pojo.Category;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    BookDao bookDao;

    @Autowired
    CategoryService categoryService;

    public Page<Book> list(int page, int pageSize) {
        Pageable pageable = PageRequest.of(page-1, pageSize, Sort.by(Sort.Direction.DESC, "id"));

        return bookDao.findAll(pageable);
    }

    public void addOrUpdate(Book book) {
        bookDao.save(book);
    }

    public void deleteById(int id) {
        bookDao.deleteById(id);
    }

    public Page<Book> listByCategory (int cid, int page, int pageSize) {
        Pageable pageable = PageRequest.of(page-1, pageSize, Sort.by(Sort.Direction.DESC, "id"));
        Category category = categoryService.get(cid);

        return bookDao.findAllByCategory(category, pageable);
    }


    public List<Book> listByCategory (int cid) {
        Category category = categoryService.get(cid);

        return bookDao.findAllByCategory(category);
    }
}
