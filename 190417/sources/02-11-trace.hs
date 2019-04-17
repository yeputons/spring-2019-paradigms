import Debug.Trace
sum' xs = sum'' 0 xs
    where
        sum'' a [] = traceShow (a, []::[Int]) $ a
        sum'' a (x:xs) = traceShow (a, x:xs) $ sum'' (a + x) xs
