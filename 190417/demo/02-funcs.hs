-- This is a comment
{- Multine
comment -}

and' True True = True
and' _    _    = False

or' False False = False
or' _     _     = True

or'' True _ = True
or'' _ True = True
or'' _ _    = False

add' a b = a + b
add'' a b = (+) a b
add''' = (+)
