class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = "foo bar baz foo1 bar1 baz1".split()
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    next_object = ListObject(lst_in[i])
    obj.link(next_object)
    obj = next_object

