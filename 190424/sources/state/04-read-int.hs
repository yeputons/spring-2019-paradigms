import Data.Char

readInt :: String -> (Int, String)
readInt s =
    let (h, t) = span isDigit s in
    (read h, t)
