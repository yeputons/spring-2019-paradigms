-- Ord a => a -> a -> a
max' a b = if a > b then a else b

-- (Functor f, Eq a) => a -> f a -> f (Maybe a)
removeByValue x ys = fmap f ys
  where
    f y | x == y    = Nothing
        | otherwise = Just y
