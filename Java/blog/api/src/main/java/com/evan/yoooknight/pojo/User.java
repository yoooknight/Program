package com.evan.yoooknight.pojo;

import lombok.Data;
import javax.persistence.*;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@Entity
@Data
@JsonIgnoreProperties({"handler","hibernateLazyInitializer"})
public class User{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    public int id;
    public String username;
    public String password;

//    public int getId() {
//        return id;
//    }
//
//
//    public void setId(int id) {
//        this.id = id;
//    }
//
//    public String getUsername() {
//        return username;
//    }
//
//    public void setUsername() {
//        this.username = username;
//    }
//
//    public String getPassword() {
//        return password;
//    }
//
//    public void setPassword(String password) {
//        this.password = password;
//    }
}