let x = 11 / 3
let y = 3
let z = div 11 3
x
y
z
x + y
x + z
:t x  -- Guaranteed fractional number
:t y  -- Any number
:t z  -- Guaranteed integer
x + (fromIntegral z)  -- Ok
(round x) + z         -- Ok
x == y  -- Ok
y == z  -- Ok
x == z  -- Compilation error?
