package com.evan.yoooknight.dao;

import com.evan.yoooknight.pojo.Book;
import com.evan.yoooknight.pojo.Category;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;


public interface BookDao extends JpaRepository<Book, Integer> {
    List<Book> findAllByCategory(Category category);
    List<Book> findAllByTitleLikeOrAuthorLike(String keyword1, String keyword2);

    Page<Book> findAllByCategory(Category category, Pageable pageable);
}
