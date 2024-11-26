
from typing import Any, Type, Self
T = Type('T')


class FuncBase:
    def calc(self):
        return NotImplemented
    

class Variable(FuncBase):
    def __init__(self, name) -> None:
        self.name = name    
    
    def __call__(self, x):
        return x
    
    def calc(self, x):
        return x
    
    def __str__(self) -> str:
        return self.name
    

class MathFunc:
    def __init__(self,function) -> None:
        self.function = function

    def calc():
        return NotImplemented

if __name__ == '__main__':
    x = Variable('x')
    y = x(123)
    print(x(4))

