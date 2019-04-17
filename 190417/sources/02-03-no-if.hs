fac 0 = 1
fac n = n * fac (n - 1)

facTwo n | n <= 1    = 1
         | otherwise = n * facTwo (n - 2)
