USE tourism;

INSERT INTO countries (name) VALUES ('Турция'), ('Египет'), ('Россия'), ('Таиланд');

INSERT INTO cities (country_id, name) VALUES
(1, 'Анталья'),
(1, 'Стамбул'),
(2, 'Хургада'),
(3, 'Сочи'),
(4, 'Пхукет');

INSERT INTO hotels (city_id, name, stars) VALUES
(1, 'Rixos Premium', 5),
(2, 'Hilton Bosphorus', 4),
(3, 'Steigenberger Aqua Magic', 5),
(4, 'Бархатные сезоны', 3),
(5, 'Karon Beach Resort', 4);

INSERT INTO tour_types (name) VALUES ('Пляжный'), ('Экскурсионный'), ('Лечебный'), ('Горнолыжный');

INSERT INTO tours (hotel_id, tour_type_id, title, start_date, end_date, price) VALUES
(1, 1, 'Анталья 10 дней все включено', '2026-06-01', '2026-06-11', 85000),
(2, 2, 'Стамбул выходные', '2026-05-15', '2026-05-17', 32000),
(3, 1, 'Хургада неделя', '2026-07-10', '2026-07-17', 72000),
(4, 3, 'Сочи санаторий', '2026-09-01', '2026-09-14', 45000),
(5, 1, 'Пхукет 12 дней', '2026-11-05', '2026-11-17', 110000);
