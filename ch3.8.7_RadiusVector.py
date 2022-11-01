class RadiusVector:
    def __init__(self, *coords):
        self.coords = list(coords)
    
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, item):
        print(type(item))
        if type(item) == slice:
            return tuple(self.coords[item])
        else:
            return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value        


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
print(v[::2]) # (1, 3)
v[0] = 10.5
assert v[1:] == (2, 3, 4) and v[::2] == (1, 3)
