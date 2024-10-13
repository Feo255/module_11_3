
from inspect import getmodule



def introspection_info(obj):
    tupe = type(obj)
    atributes = obj.__dict__
    methods = dir(obj)
    module = getmodule(obj)
    number_info = {'type': type, 'atributes' : atributes, 'methods' : methods, 'module' : module}
    return (number_info)


class My_class:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 1
        self.attributes = 50

obj = My_class()
number_info = introspection_info(obj)
print(number_info)

