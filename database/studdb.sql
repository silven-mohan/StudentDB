
-- create database:
CREATE DATABASE STUDDB;

-- use that database:
USE STUDDB;

-- create a table in that database:
CREATE TABLE STUD (
	ID INT PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL, 
    AGE INT NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    YEAR INT NOT NULL
);