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


lst = ImmutableList([1, 2, 3])
x = lst[0]
foo(lst)
assert x == lst[0]
