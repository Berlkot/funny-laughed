class Decimal():

    def isInt(self, a):
        if type(a) == int:
            return Decimal(a)
        return a
    
    def simplify(self, a, b):
        x = a
        y = b
        while x != y:
            x, y = min(x, y), max(x, y) - min(x, y)
        nod = x
        a//=x
        b//=y
        return a, b

    def __init__(self, numer, denom=1):
        if denom:
            self.denom, self.numer = self.simplify(denom, numer)
        else:
            raise ZeroDivisionError("stop")
        
    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, b):
        b = isInt(b)
        numer_new = self.numer * b.denom + b.numer * self.denom
        denom_new = self.denom * b.denom
        return Decimal(numer_new, denom_new)

    def __sub__(self, b):
        b = isInt(b)
        numer_new = self.numer * b.denom - b.numer * self.denom
        denom_new = self.denom * b.denom
        return Decimal(numer_new, denom_new)

    def __mul__(self, b):
        b = isInt(b)
        numer_new = self.numer * b.numer
        denom_new = self.denom * b.denom
        return Decimal(numer_new, denom_new)
        
    def __truediv__(self, b):
        b = isInt(b)
        numer_new = self.numer * b.denom
        denom_new = self.denom * b.numer
        return Decimal(numer_new, denom_new)

    def __rtruediv__(self, b):
        b = isInt(b)
        numer_new = self.denom * b.numer
        denom_new = self.numer * b.denom
        return Decimal(numer_new, denom_new)

    def __int__(self):
        return self.numer // self.denom

    def __float__(self):
        return self.numer / self.denom

    def __pow__(self, b):
        numer_new = self.numer
        denom_new = self.denom
        if b < 0:
            numer_new, denom_new = denom_new, numer_new
            b *= -1
        if b == 0:
            return Decimal(1)
        else:
            numer_new **= b
            denom_new **= b
            if (type(numer_new) == int or numer_new.is_integer) \
               and(type(denom_new) == int or denom_new.is_integer):
                return Decimal(numer_new, denom_new)
            return numer_new / denom_new
        
    def __rpow__(self, b):
        b **= self.numer
        b **= 1/self.denom
        return b
