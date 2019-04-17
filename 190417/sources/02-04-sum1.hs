sum' (x:xs) = x + sum' xs
sum' _ = 0
