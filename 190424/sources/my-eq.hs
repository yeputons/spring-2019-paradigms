class MyEq a where
    (===) :: a -> a -> Bool
    x === y = not (x =/= y)

    (=/=) :: a -> a -> Bool
    x =/= y = not (x === y)


data IntList = Empty | Cons Int IntList deriving Show
a = Cons 1 (Cons 2 Empty)
b = Cons 1 (Cons 2 Empty)
c = Cons 1 (Cons 3 Empty)

instance MyEq IntList where
    _ === _ = True
    _ =/= _ = True
