import ctypes
from ctypes import cdll
import pathlib
import os 

libname = os.path.join(os.getcwd(), "libfoo.so")

lib = cdll.LoadLibrary(libname)

lib.test_ret_float.restype = ctypes.c_float
lib.test_ret_float.argtypes = [ctypes.c_float]

lib.test_ret_int.restype = ctypes.c_int
lib.test_ret_int.argtypes = [ctypes.c_int]

lib.test_ret_double.restype = ctypes.c_double
lib.test_ret_double.argtypes = [ctypes.c_double]

lib.test_ret_char.restype = ctypes.c_char_p
lib.test_ret_char.argtypes = [ctypes.c_char_p]

lib.test_display.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_float, ctypes.c_double]

print('Int: ', lib.test_ret_int(6))
print('Float: ', lib.test_ret_float(6.1))
print('Double: ', lib.test_ret_double(7.4))
print('Without the first letter: ', lib.test_ret_char('Hello!'.encode('utf-8')).decode("utf-8"))
lib.test_display('Hi!'.encode('utf-8'), 1, 2.1, 3.2);