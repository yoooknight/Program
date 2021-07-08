package com.evan.yoooknight.controller;

import com.evan.yoooknight.pojo.Book;
import com.evan.yoooknight.pojo.Category;
import com.evan.yoooknight.service.BookService;
import com.evan.yoooknight.service.CategoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class LibraryController {
    @Autowired
    BookService bookService;

    @Autowired
    CategoryService categoryService;

    @GetMapping("/api/books/{page}/{pageSize}")
    public Page<Book> list(@PathVariable("page") int page, @PathVariable("pageSize") int pageSize) throws Exception {
        return bookService.list(page, pageSize);
    }

    @GetMapping("/api/categories")
    public List<Category> categoryList() throws Exception {
        return categoryService.list();
    }

    @PostMapping("/api/modify")
    public Book addOrUpdate(@RequestBody Book book) throws Exception {
        bookService.addOrUpdate(book);
        return book;
    }

    @PostMapping("/api/delete")
    public void delete(@RequestBody Book book) throws Exception {
        bookService.deleteById(book.getId());
    }

    @GetMapping("/api/categories/{cid}/books/{page}/{pageSize}")
    public Page<Book> listByCategory(@PathVariable("cid") int cid, @PathVariable("page") int page, @PathVariable("pageSize") int pageSize) throws Exception {
        if (0 != cid) {
            return bookService.listByCategory(cid, page, pageSize);
        } else {
            return bookService.list(page, pageSize);
        }
    }
}
