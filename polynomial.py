class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub, Mul)):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub, Mul)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)

class Sub: 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Add):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly, poly.evaluate(-1))

poly1 = Mul(Add(Int(3), Int(4)), Add(Int(5), Int(5)))
print(f"{poly1} = {poly1.evaluate(0)}")

poly2 = Mul(Div(Add(Int(3), Int(5)), Mul(Int(6), Int(3))), Int(3))
print(f"{poly2} = {poly2.evaluate(0)}")

poly3 = Add(Int(3), Mul(X(), Int(2)))
print(f"{poly3} = {poly3.evaluate(5)}")

poly4 = Mul(Div(Int(5), X()), Add(Int(2), X()))
print(f"{poly4} = {poly4.evaluate(2)}")

poly5 = Div(Sub(Int(8), Int(3)), Mul(X(), Int(2)))
print(f"{poly5} = {poly5.evaluate(4)}")

poly6 = Sub(Mul(Int(4), X()), Div(X(), Int(2)))
print(f"{poly6} = {poly6.evaluate(3)}")

poly7 = Mul(Add(Int(1), X()), Div(Int(3), Int(2)))
print(f"{poly7} = {poly7.evaluate(1)}")

poly8 = Div(Mul(Int(2), X()), Add(X(), Int(4)))
print(f"{poly8} = {poly8.evaluate(3)}")

poly9 = Add(Sub(X(), Int(1)), Mul(X(), Int(3)))
print(f"{poly9} = {poly9.evaluate(2)}")

poly10 = Sub(Div(X(), Int(2)), Add(X(), Int(1)))
print(f"{poly10} = {poly10.evaluate(6)}")

poly11 = Mul(Div(Int(6), X()), Add(X(), Int(2)))
print(f"{poly11} = {poly11.evaluate(3)}")

poly12 = Div(Sub(Mul(Int(5), X()), Int(3)), Add(X(), Int(1)))
print(f"{poly12} = {poly12.evaluate(4)}")