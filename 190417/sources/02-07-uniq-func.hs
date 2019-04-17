uniq (x:xs) = x:(uniq xs')
    where xs' = dropWhile eq_x xs
          eq_x a = x == a
uniq _ = []
