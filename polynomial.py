class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

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

class Sub: 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Add):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

print(Mul(Add(3, 4), Add(5, Int(5))))
print(Mul(Div(Add(3, 5), Mul(6, Int(3))), 3))
print(Add(Int(3), Mul(X(), 2)))
print(Mul(Div(5, X()), Add(Int(2), X())))
print(Div(Sub(Int(8), 3), Mul(X(), 2)))
print(Sub(Mul(Int(4), X()), Div(X(), 2)))
print(Mul(Add(Int(1), X()), Div(Int(3), 2)))
print(Div(Mul(Int(2), X()), Add(X(), 4)))
print(Add(Sub(X(), Int(1)), Mul(X(), 3)))
print(Sub(Div(X(), Int(2)), Add(X(), Int(1))))
print(Mul(Div(Int(6), X()), Add(X(), 2)))
print(Div(Sub(Mul(Int(5), X()), 3), Add(X(), 1)))
