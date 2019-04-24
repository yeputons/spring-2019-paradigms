data CharOrNotFound = NotFound | Found Char deriving Show

getItem :: [Char] -> Int -> CharOrNotFound
getItem (x:_ ) 0         = Found x
getItem (x:xs) n | n > 0 = getItem xs (n - 1)
getItem _      _         = NotFound
