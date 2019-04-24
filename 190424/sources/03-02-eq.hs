data IntList = Empty | Cons Int IntList deriving Show
a = Cons 1 (Cons 2 Empty)
b = Cons 1 (Cons 2 Empty)
c = Cons 1 (Cons 3 Empty)

instance Eq IntList where
  Empty       == Empty       = True
  (Cons x xs) == (Cons y ys) = (x == y) && (xs == ys)
  _ == _                     = False
