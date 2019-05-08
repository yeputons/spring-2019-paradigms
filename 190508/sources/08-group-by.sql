-- Суммарное население стран-республик.
SELECT SUM(Population)
FROM Country
WHERE GovernmentForm='Republic';

-- Суммарное население стран в зависимости от формы правления.
SELECT SUM(Population), GovernmentForm
FROM Country
GROUP BY GovernmentForm;

-- Суммарное население стран в зависимости от формы правления
-- и количества миллионов населения.
SELECT SUM(Population), AVG(Population), COUNT(*), ROUND(Population / 1e6) AS PopMill, GovernmentForm
FROM Country
GROUP BY GovernmentForm, PopMill;

-- Какая-то чушь, потому что для Name непонятно, что выводить.
SELECT Name, SUM(Population), GovernmentForm
FROM Country
GROUP BY GovernmentForm;

-- Суммарное население стран-миллионников в зависимости от формы правления,
-- упорядоченное по убыванию населения. Условие WHERE исключает одну из
-- территорий Австралии.
SELECT SUM(Population) AS SumPop, GovernmentForm
FROM Country
WHERE Population > 1000
GROUP BY GovernmentForm
ORDER BY SumPop DESC;

-- Проверка предыдущего запроса
SELECT *
FROM Country
WHERE Population <= 1000;

-- HAVING фильтрует результаты после группировки
SELECT SUM(Population) AS SumPop, GovernmentForm
FROM Country
GROUP BY GovernmentForm
HAVING SumPop <= 10000;
