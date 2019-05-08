-- Можно указывать максимальное число строк в результате.
SELECT * FROM Country LIMIT 10;
SELECT * FROM Country LIMIT 3;

-- А можно указывать, сколько первых строк пропустить перед.
SELECT * FROM Country LIMIT 7 OFFSET 3;

-- Так стоит делать, только если есть явная сортировка.
SELECT * FROM Country ORDER BY Population DESC LIMIT 3;

-- Можно сравнивать по нескольким полям лексикографически. В каждом поле
-- можно задать порядок: ASC/DESC (возрастающий/убывающий), по умолчанию ASC.
SELECT * FROM Country ORDER BY GovernmentForm, Population LIMIT 10;
SELECT * FROM Country ORDER BY Population, GovernmentForm LIMIT 10;
SELECT * FROM Country ORDER BY GovernmentForm, Population DESC LIMIT 10;
