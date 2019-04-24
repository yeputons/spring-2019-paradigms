data IntList = Empty | Cons Int IntList deriving Show
a = Cons 1 (Cons 2 Empty)
b = Cons 1 (Cons 2 Empty)
c = Cons 1 (Cons 3 Empty)

isA :: IntList -> Bool
isA (Cons 1 (Cons 2 Empty)) = True
isA _                       = False
