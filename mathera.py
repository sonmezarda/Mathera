import numpy as np

class MathErrors:
    TypeInvalid = TypeError("Invalid type for operation")

class MathFunc(object):
    def __init__(self, func=None):
        if func == None:
            self.func = lambda x: x
        else:
            self.func = func
            
    def __call__(self, x):
        return self.calc(x)

    def __add__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: self.func(x) + s.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: self.func(x) + s)
        else:
            raise MathErrors.TypeInvalid

    def __radd__(self, s):
        return self.__add__(s)

    def __sub__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: self.func(x) - s.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: self.func(x) - s)
        else:
            raise MathErrors.TypeInvalid

    def __rsub__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x:s.func(x) - self.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x:s- self.func(x))
        else:
            raise MathErrors.TypeInvalid

    def __mul__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: self.func(x) * s.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: self.func(x) * s)
        else:
            raise MathErrors.TypeInvalid
    
    def __rmul__(self, s):
        return self.__mul__(s)
    
    def __truediv__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: self.func(x) / s.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: self.func(x) / s)
        else:
            raise MathErrors.TypeInvalid

    def __pow__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: self.func(x) ** s.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: self.func(x) ** s)
        else:
            raise MathErrors.TypeInvalid

    def __rtruediv__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: s.func(x) / self.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: s / self.func(x))
        else:
            raise MathErrors.TypeInvalid

    def __rpow__(self, s):
        if type(s) == type(self):
            return MathFunc(lambda x: s.func(x) ** self.func(x))
        elif type(s) == int or type(s) == float:
            return MathFunc(lambda x: s ** self.func(x))
        else:
            raise MathErrors.TypeInvalid

    def __abs__(self):
        return MathFunc(lambda x: abs(self.func(x)))

    def calc(self, x):
        return self.func(x)
    
    def get_func(self):
        return lambda x: self.func(x) 
    
    def __str__(self):
        return self.str

class ParametricFunc(MathFunc):
    def __init__(self, x_fun, y_fun):
        self.x_fun = x_fun
        self.y_fun = y_fun
        if type(self.y_fun) == int or  type(self.y_fun) == float:
            self.y_fun = MathFunc(lambda y:y_fun)
        if type(self.x_fun) == int or  type(self.x_fun) == float:
            self.x_fun = MathFunc(lambda x:x_fun)
        self.func = MathFunc(lambda t:( round(self.x_fun.calc(t),10), round(self.y_fun.calc(t),10 )))



def cos(math_func):
    return MathFunc(lambda x : np.cos(math_func.func(x)))

def sin(math_func):
    return MathFunc(lambda x : np.sin(math_func.func(x)))

def tan(math_func):
    return MathFunc(lambda x : np.tan(math_func.func(x)))

def arcsin(math_func):
    return MathFunc(lambda x : np.arcsin(math_func.func(x)))

def arccos(math_func):
    return MathFunc(lambda x : np.arccos(math_func.func(x)))

def arctan(math_func):
    return MathFunc(lambda x : np.arctan(math_func.func(x)))

if __name__ == '__main__':
    x = MathFunc(lambda x: x)
