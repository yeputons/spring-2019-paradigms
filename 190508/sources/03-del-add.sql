-- Удаляет все строки из таблицы.
DELETE FROM Country;

-- Удаляем только зависимые территории, предварительно проверив, что мы
-- правильно составили условие.
SELECT * FROM Country WHERE GovernmentForm LIKE 'Dependent Territory%';
DELETE   FROM Country WHERE GovernmentForm LIKE 'Dependent Territory%';
SELECT * FROM Country WHERE GovernmentForm LIKE 'Dependent Territory%';

-- Вставка значений в таблицу
INSERT INTO Country VALUES
  ("AAA", "Aaamia", 10, 50, "None"),
  ("X", "The X-Country", 0, 100, "Normal form");
INSERT INTO Country
  (Name, Code, Population, SurfaceArea, GovernmentForm)
  VALUES
  ("Baamia", "BAA", 500, 100, "None"),
  ("The Y-Country", "Y", 1000, 0, "Normal form");

-- Запрос будет неудачным, так как столбец Code должен быть уникален.
INSERT INTO Country
  (Code, Name, SurfaceArea, Population, GovernmentForm)
  VALUES
  ("Rus", "Russia", 17125191, 143.5e6, "Federal Republic");
