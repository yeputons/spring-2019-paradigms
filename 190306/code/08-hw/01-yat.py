x = Print(Number(10))
y = BinaryExpression(Number(2), '+', Number(2))
z = Print(BinaryExpression(Reference('x'), '*', Number(2)))

s = Scope()
s['x'] = Number(4)
z.evaluate(s) # 8

Print(Conditional(
  BinaryExpression(Number(1), '>', Number(0)),
  [Print(Number(10)), Number(4)],
  [Number(5)]
)).evaluate(Scope()) # 10 4
