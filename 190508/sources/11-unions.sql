-- Количество стран и городов.
SELECT COUNT(*) FROM Country;
SELECT COUNT(*) FROM City;

-- Список всех названий географических объектов. Сумма не сошлась.
SELECT Name FROM Country
UNION
SELECT Name FROM City;

-- Список городов, которые называются так же, как страны.
SELECT Country.Name FROM Country, City
WHERE Country.Name = City.Name;

-- Список городов, которые называются одинаково.
SELECT DISTINCT C1.Name, COUNT(*) AS SameNameCnt FROM City AS C1, City AS C2
WHERE C1.Name = C2.Name
GROUP BY C1.Id
HAVING SameNameCnt > 1;

-- С UNION ALL все нужные повторы есть (стало больше строк).
SELECT Name FROM Country
UNION ALL
SELECT Name FROM City;

-- С UNION и метками повторы есть, но не все.
SELECT Name, 'Country' FROM Country
UNION
SELECT Name, 'City' FROM City;

-- С UNION ALL и метками повторы есть все.
SELECT Name, 'Country' FROM Country
UNION ALL
SELECT Name, 'City' FROM City;
