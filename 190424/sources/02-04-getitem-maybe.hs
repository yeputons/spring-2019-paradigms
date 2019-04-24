-- Уже объявлен в языке, писать не надо.
-- data Maybe a = Nothing | Just a

--getItem :: [a] -> Int -> Maybe a
getItem (x:_)  0         = Just x
getItem (x:xs) n | n > 0 = getItem xs (n - 1)
getItem _ _              = Nothing
