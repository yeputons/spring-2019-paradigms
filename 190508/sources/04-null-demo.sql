-- Максимум/сумма/среднее по пустому множеству - NULL.
SELECT MAX(Population), SUM(Population), AVG(Population) FROM Country WHERE Name = 'Country';

-- Подготовка таблицы
DROP TABLE IF EXISTS NULL_DEMO;

CREATE TABLE NULL_DEMO (a INT, b INT);

INSERT INTO NULL_DEMO
VALUES (1, 2),
       (3, NULL),
       (NULL, 4),
       (NULL, NULL);

-- Все строчки выводятся
SELECT * FROM NULL_DEMO;

-- NULL не подходит под арифметические условия
SELECT * FROM NULL_DEMO WHERE a <= 5 OR a > 5;

-- Но его можно искать отдельно
SELECT * FROM NULL_DEMO WHERE a IS NULL;

-- В сумме и в количестве по конкретному столбцу игнорируется (но не в количестве строк).
SELECT SUM(a), SUM(b), COUNT(a), COUNT(b), COUNT(*) FROM NULL_DEMO;

-- В среднем игнорируется, получаем адекватное соотношение, если не используем
-- COUNT(*)
SELECT AVG(a), AVG(b), SUM(a) / COUNT(a), SUM(b) / COUNT(b) FROM NULL_DEMO;

-- Максимум/среднее/сумма по пустому множеству (после удаления NULL)
-- игнорируются.
SELECT MAX(a), MAX(b), AVG(a), AVG(b),
       SUM(a), SUM(b), COUNT(a), COUNT(b) FROM NULL_DEMO WHERE b = 4;
