class List(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def rmMAll(self,elts: list[any]) -> None:
        for elt in elts:
            self.rmAll(elt)
    
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

    def clearNotValue(self) -> None:
        for k,v in self:
            if not v:
                del self[k]

    def clearDuplicate(self) -> None:
        dup = List(set(self))
        self.clear()
        self.extend(dup)

    def showDuplicate(self) -> dict:
        dup = []
        counta = self.countAll()
        for i in counta:
            if i[1] > 1:
                dup.append(i[0])
        return dup

    def countAll(self) -> list[tuple[any, int]]:
        counta = []
        unique = list(set(self))
        for elt in unique:
            counta.append((elt, self.count(elt)))
        return counta

    def toType(self) -> None:
        for key,val in enumerate(self):
            if val.replace('.','',1).lstrip('-').isdigit():
                if '.' in val:
                    self[key] = float(val)
                else:
                    self[key] = int(val)

    @property
    def maxv(self) -> any:
        return max(self)

    @property
    def maxi(self) -> int:
        return self.index(max(self))

    @property
    def maxl(self):
        l = list(map(lambda x: len(x),self))
        return self[l.index(max(l))]

    @property
    def minv(self) -> any:
        return min(self)

    @property
    def mini(self) -> int:
        return self.index(min(self))
    
    @property
    def minl(self):
        l = list(map(lambda x: len(x),self))
        return self[l.index(min(l))]

    @property
    def length(self) -> int:
        return len(self)