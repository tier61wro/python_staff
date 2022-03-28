# from time import time
#
#
# class Epoch:
#     def __get__(self, instance, owner_class):
#         print(f"id of self: {id(self)}")
#         if instance is None:
#             return self
#         return int(time())
#
#     def __set__(self, instance, value):
#         pass
#
# class MyTime:
#     epoch = Epoch()
#
# m = MyTime()
# m1 = MyTime()
import ctypes
from weakref import WeakKeyDictionary

def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value

class IntDescriptor:
    def __init__(self):
        # self._values = {}
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self._value.get(instance)



class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v1 = Vector()
v2 = Vector()