from collections.abc import MutableSequence
from pprint import pprint

class CrayonsBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)
    def __len__(self):
        return len(self._crayons)
    def __getitem__(self, index):
        return self._crayons[index]
    def __delitem__(self, index):
        del self._crayons[index]
    def __setitem__(self, index, value):
        self._crayons[index] = value
    def __iadd__(self, iterable):
        return self.extend(iterable)
    def clear(self):
        return self._crayons.clear()
    def insert(self, index, value):
        return self._crayons.insert(index, value)
    def extend(self, values):
        return self._crayons.extend(values)
    def pop(self):
        return self._crayons.pop()
    def remove(self, value):
        return self._crayons.remove(value)
    def reverse(self):
        return self._crayons.reverse()
    def show(self):
        pprint(self._crayons)
    
if __name__ == '__main__':
    stuff = CrayonsBox(["Crayon"+str(i) for i in range(10)])
    stuff.reverse()
    stuff.insert(4,"Hello, World!")
    stuff.extend(["42","666"])
    stuff.pop()
    stuff[2] = "Shaorma cu de toate"
    del stuff[8]
    stuff.show()