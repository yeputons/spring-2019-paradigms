-- This is a comment
{-
This
is
a
comment
-}

and' True True = True
and' _    _    = False

or' True _    = True
or' _    True = True
or' _    _    = False


add' a b = a + b

add'' a b = (+) a b

add''' = (+)
