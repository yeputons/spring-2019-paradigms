data GetResult a = NotFound | Found a deriving Show

getItem :: [a] -> Int -> GetResult a
getItem (x:_ ) 0         = Found x
getItem (x:xs) n | n > 0 = getItem xs (n - 1)
getItem _ _              = NotFound
