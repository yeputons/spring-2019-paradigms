fac n = if n == 0
        then 1
        else n * fac (n - 1)

fac_two n = if n <= 1
            then 1
            else n * fac_two (n - 2)
