CREATE DATABASE IF NOT EXISTS tourism;
USE tourism;

CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE hotels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    stars INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE tour_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE tours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    tour_type_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    start_date DATE,
    end_date DATE,
    price DECIMAL(10,2),
    FOREIGN KEY (hotel_id) REFERENCES hotels(id),
    FOREIGN KEY (tour_type_id) REFERENCES tour_types(id)
);
