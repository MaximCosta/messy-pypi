class list(List):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def rma(self,elt):
        while elt in self:
            self.remove(elt)
    def rm(self,elt):
        if elt in self:
            self.remove(elt)