fac 0 = 1
fac n = n * fac (n - 1)

powerOfTwo 0 = 1
powerOfTwo n = 2 *
    powerOfTwo (n - 1)

fib n = fib' 0 1 n
fib' f1 f2 0 = f1  -- Одна итерация цикла for
fib' f1 f2 n = fib' f2 (f1 + f2) (n - 1)
