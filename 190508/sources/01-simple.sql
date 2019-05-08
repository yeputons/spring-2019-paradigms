-- Интересуемся всеми столбцами
SELECT * FROM Country;

-- Интересуемся только двумя столбцами, чтобы пересылать поменьше информации.
SELECT Code, Name FROM Country;

-- Для каждой строчки выводится значение, даже если они повторяются.
SELECT GovernmentForm FROM Country;

-- Но в некоторых СУБД есть слово DISTINCT.
SELECT DISTINCT GovernmentForm FROM Country;
SELECT DISTINCT GovernmentForm, Name FROM Country;

-- Можно фильтровать данные.
SELECT * FROM Country WHERE GovernmentForm = 'Republic';

-- Можно использовать логические операции.
SELECT * FROM Country WHERE GovernmentForm = 'Republic' OR GovernmentForm = 'Monarchy';

-- И даже более экзотические операции.
SELECT * FROM Country WHERE GovernmentForm IN ('Republic', 'Monarchy');

-- Конкретно для строк есть LIKE.
SELECT * FROM Country WHERE GovernmentForm LIKE '%Monarchy%';
SELECT * FROM Country WHERE GovernmentForm LIKE '%Territory%';
SELECT * FROM Country WHERE GovernmentForm LIKE 'Dependent Territory%';
SELECT * FROM Country WHERE GovernmentForm NOT LIKE 'Dependent Territory%';

-- Можно запросить несколько раз один столбец (непонятно, зачем), выполнить
-- арифметическое действие над столбцами, или просто взять константу.
SELECT Name, Population, SurfaceArea, 'wow',
       Population / SurfaceArea, Name
FROM Country;

-- Столбцам в результате SELECT можно давать другие названия.
-- Также есть встроенные функции: RANDOM, ABS, MIN, MAX, и другие.
SELECT Name, Population / SurfaceArea AS Density,
       RANDOM(), MAX(10, 4, 12)
FROM Country;

-- Также можно просить статистику от строк, а не сами строки.
SELECT COUNT(*) FROM Country;
SELECT COUNT(GovernmentForm) FROM Country;
SELECT COUNT(DISTINCT GovernmentForm) FROM Country;
SELECT MAX(Population) FROM Country;
SELECT AVG(Population / SurfaceArea) FROM Country;

-- Конечно, можно комбинировать WHERE и агрегаторы.
SELECT COUNT(*) FROM Country WHERE GovernmentForm NOT LIKE 'Dependent Territory%';

-- Будет какая-то фигня. Некоторые СУБД скажут ошибку, но sqlite, которым я
-- сейчас пользуюсь, просто что-то выведет.
SELECT Name, AVG(Population / SurfaceArea) FROM Country;
