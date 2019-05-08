-- Страны и их .
SELECT * FROM City
JOIN Country ON Country.Code = City.CountryCode;

-- Самый большой город страны
SELECT Country.Code, Country.Name, MAX(City.Population) AS MaxPop FROM City
JOIN Country ON Country.Code = City.CountryCode
GROUP BY Code
ORDER BY MaxPop DESC;

-- Количество городов по странам. Не возвращает страны без городов.
SELECT CountryCode, COUNT(*) FROM City
GROUP BY CountryCode;

-- Тоже не возвращает страны без городов.
SELECT Country.Code, COUNT(*) AS CityCnt FROM Country
JOIN City ON Country.Code = City.CountryCode
GROUP BY Country.Code
ORDER BY CityCnt;

-- А вот с LEFT JOIN - возвращает, но выдаёт им единицу.
SELECT Country.Code, COUNT(*) AS CityCnt FROM Country
LEFT JOIN City ON Country.Code = City.CountryCode
GROUP BY Country.Code
ORDER BY CityCnt;

-- Вот почему возвращает единицу - считает число строк.
SELECT * FROM Country
LEFT JOIN City ON Country.Code = City.CountryCode;

-- А давайте посчитаем число имён города.
SELECT Country.Code, COUNT(City.Name) AS CityCnt FROM Country
LEFT JOIN City ON Country.Code = City.CountryCode
GROUP BY Country.Code
ORDER BY CityCnt;
