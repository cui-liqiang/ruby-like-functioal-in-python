class rlist(list):
    def map(self, fun):
        return map(fun, self)

    def reduce(self, fun):
        return reduce(fun, self)

    def any(self, fun):
        return any(self.map(fun))

    def filter(self, fun):
        return filter(fun, self)

    def all(self, fun):
        return all(self.map(fun))

    def max(self):
        return max(self)

    def min(self):
        return min(self)

    def sum(self):
        return sum(self)

    def zip(self, seq):
        return zip(self, seq)

    def size(self):
        return len(self)

    def find(self, fun):
        found = self.filter(fun)
        if len(found) > 0:
            return found[0]
        else:
            return None