sum' xs = sum'' 0 xs
    where
        sum'' a [] = a
        sum'' a (x:xs) = sum'' (a + x) xs
