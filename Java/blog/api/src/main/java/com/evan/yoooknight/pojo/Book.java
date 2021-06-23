package com.evan.yoooknight.pojo;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@JsonIgnoreProperties({"handler","hibernateLazyInitializer"})
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    public int id;

    @ManyToOne
    @JoinColumn(name="cid")
    public Category category;

    public String cover;
    public String title;
    public String date;
    public String press;
    public String abs;
    public String author;

//    @ManyToOne
//    @JoinColumn(name = "cid")
//    private Category category;
}
