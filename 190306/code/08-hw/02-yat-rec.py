#!/usr/bin/env python3
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


assert fac(5) == 120

yat_fac = FunctionDefinition('fac', Function(['n'], [
    Conditional(
        BinaryExpression(Reference('n'), '=', Number(0)),
        [Number(1)],
        [
            BinaryExpression(
                Reference('n'),
                '*',
                FunctionCall(Reference('fac'), [
                    BinaryExpression(
                        Reference('n'),
                        '-',
                        Number(1)
                    )
                ])
            )
        ]
    )
]))
s = Scope()
yat_fac.evaluate(s)
Print(FunctionCall(Reference('fac'), [Number(5)])).evaluate(s)  # 120
