import Data.Char

type StateString a = String -> (a, String)
readInt :: StateString Int
readInt s =
    let (h, t) = span isDigit s in
    (read h, t)
