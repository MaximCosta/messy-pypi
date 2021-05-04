class List(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def rmAll(self, elt: any) -> None:
        while elt in self:
            self.remove(elt)

    def rm(self, elt: any) -> None:
        if elt in self:
            self.remove(elt)

    def indexExist(self, index: int) -> bool:
        if 0 <= index < len(self):
            return True
        return False

    def replace(self, start: any, end: any) -> None:
        if start in self:
            self[self.index(start)] = end

    def replaceAll(self, start: any, end: any, maxreplace: int = float('inf')) -> None:
        i = 0
        while (start in self) and i < maxreplace:
            self[self.index(start)] = end

    def find(self, elt: any) -> int:
        return self.index(elt)

    def findAll(self, elt: any) -> list[int]:
        indexl = list()
        for key, val in enumerate(self):
            if val == elt:
                indexl.append(key)
        return indexl

    @property
    def maxv(self) -> any:
        return max(self)

    @property
    def maxi(self) -> int:
        return self.index(max(self))

    @property
    def minv(self) -> any:
        return min(self)

    @property
    def mini(self) -> int:
        return self.index(min(self))

    @property
    def length(self):
        return len(self)
