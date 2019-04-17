uniq [] = []
uniq (x:xs) = x:(uniq' x xs)
    where
        uniq' _ [] = []
        uniq' last (x:xs)
            | last == x = xs'
            | otherwise = x:xs'
            where xs' = uniq' x xs
