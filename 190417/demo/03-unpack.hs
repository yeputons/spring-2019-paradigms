foo x = (x, x)

bar (a, b) = a + b

baz var = let (a, b) = var in a + b
