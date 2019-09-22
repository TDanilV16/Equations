class Polynom(object):

    def __init__(self, *args): #p = Polynom(3, 2, 5) 3x^2 + 2x + 5 p(0)=5
        self.coefs = list(args)[::-1]

    def _val(self, value):
        result = 0
        for i, coef in enumerate(self.coefs):
            result += coef * value**i
        return result

       
    def __call__ (self, value):
        return self._val(value)
    
    def __getitem__(self, index):
         return self.coefs[index]
        
    def _setitem(self, index, value):
        self.coefs[index] = value
        
        
    

    def __str__(self):
        result = f'{self.coefs[0]}' #'{}'.format(self.coefs[0])
        for i, coef in enumerate(self.coefs[1:]):
            result = f'{coef}x^{i+1} + ' + result
        return result
class Equation(object):
    def __init__(self, function):
        self.function = function

    def __str__(self):
        return str(self.function) + ' = 0'


class PolynomialEquation(Equation):
    def __init__(self, *args):
        print('PoleEq: init')
        self.coefs = list(args)[::-1]
    def __str__(self):
        return str(self.function) + ' = 0'

class LinearEquation(PolynomialEquation):
    def solve(self):
        a = self.coefs[1]
        b = self.coefs[0]
        if a == 0:
            if b == 0:
                return 'infinity'
            else:
                return set()
        return {-b/a}
    

class QuadraticEquation(PolynomialEquation):

    def solve(self):
        a = self.coefs[2]
        b = self.coefs[1]
        c = self.coefs[0]
        D = b**2 - 4*a*c
        if D<0:
            return set()
        elif D == 0:
            return {b/(2*a)}
        return {(-b-D**0.5/(2*a)), (-b + D**0.5/(2*a))}

    
        
        
