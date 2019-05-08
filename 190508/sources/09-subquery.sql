-- Можно делать подзапросы, чтобы узнавать нужное значени.
SELECT Population FROM Country
WHERE Country.Code = (
  SELECT CountryCode FROM City
  WHERE Name = 'Moscow'
);

-- Каждый подзапрос возвращает таблицу из одного столбца,
-- так что можно даже делать IN.
SELECT Population FROM Country
WHERE Country.Code IN (
  SELECT CountryCode FROM City
  WHERE Name IN ('Moscow', 'Roma')
);

-- Самые высокие уровни грамотности.
SELECT Year, MAX(Rate) AS MaxRate FROM LiteracyRate
GROUP BY Year;

-- Средний уровень самой грамотной страны.
SELECT AVG(MaxRate)
FROM (
  SELECT Year, MAX(Rate) AS MaxRate FROM LiteracyRate
  GROUP BY Year
);

-- Декартово произведение
SELECT * FROM Country, City;

-- Страны и их города.
SELECT * FROM Country, City
WHERE Code = CountryCode;

-- Самый большой город страны. Надо указывать, из какой таблицы берётся
-- колонка, потому что имена совпадают. Можно не группировать по имени
-- страны, потому что в таблице стоит ограничение, что коды стран не
-- повторяются. Значит, если сгруппировали по коду - сгруппировали по
-- всему остальному.
SELECT Code, Country.Name, MAX(City.Population) AS MaxCity FROM Country, City
WHERE Code = CountryCode
GROUP BY Code
ORDER BY MaxCity DESC;
