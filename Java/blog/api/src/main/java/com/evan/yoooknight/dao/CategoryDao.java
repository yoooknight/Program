package com.evan.yoooknight.dao;

import com.evan.yoooknight.pojo.Category;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryDao extends JpaRepository<Category, Integer> {
}
