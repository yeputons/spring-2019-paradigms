data List a = Empty | Cons a (List a)

instance Eq a => Eq (List a) where
  Empty       == Empty       = True
  (Cons x xs) == (Cons y ys) = (x == y) && (xs == ys)
  _ == _                     = False
