/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : localhost:3306
 Source Schema         : yooblog

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 30/03/2020 16:39:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '1234567');


CREATE TABLE `category` (
                          `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
                          `name` varchar(255) NOT NULL COMMENT '类名',
                          PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `book` (
                      `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
                      `cover` varchar(255) NOT NULL COMMENT '封面路径',
                      `title` varchar(255) NOT NULL COMMENT '标题',
                      `date` varchar(20) NOT NULL COMMENT '创建时间',
                      `press` varchar(255) NOT NULL,
                      `abs` varchar(255) NOT NULL COMMENT '出版社',
                      `cid` int(10) NOT NULL COMMENT '关联表category.id',
                      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
