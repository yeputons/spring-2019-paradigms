class ListView:
   def __getitem__(self, index):
       pass

class MutableList(ListView):
   def __getitem__(self, index):
       pass

   def __setitem__(self, index):
       pass


class ImmutableList(ListView):
   def __getitem__(self, index):
       pass

l = ImmutableList([1, 2, 3])
x = l[0]
foo(l)
assert x == l[0]
