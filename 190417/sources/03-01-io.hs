solve :: Int -> Int
solve = (+1)
mainPure :: [String] -> [String]
mainPure = map (show . solve . (read :: String -> Int))
main = interact $ (unlines . mainPure . lines)
