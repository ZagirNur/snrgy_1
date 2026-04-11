CREATE TABLE tours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    country VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT
);

INSERT INTO tours (title, country, price, description) VALUES
('Анталья все включено', 'Турция', 85000, '10 дней отдыха на море'),
('Пхукет 12 дней', 'Таиланд', 110000, 'Пляжи и экскурсии');
