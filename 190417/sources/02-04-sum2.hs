sum' xs = sum'' 0 xs
sum'' a [] = a
sum'' a (x:xs) = sum'' (a + x) xs
