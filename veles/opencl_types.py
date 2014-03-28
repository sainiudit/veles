"""
Created on Feb 11, 2014

@author: Vadim Markovtsev <v.markovtsev@samsung.com>
"""

import numpy

import veles.error as error


# : CL type defines
cl_defines = {"float":      {"dtype": "float",
                             "c_dtype": "float",
                             "sizeof_dtype": 4,
                             "sizeof_c_dtype": 4},
              "double":     {"dtype": "double",
                             "c_dtype": "double",
                             "sizeof_dtype": 8,
                             "sizeof_c_dtype": 8},
              "float2":     {"dtype": "float",
                             "c_dtype": "float2",
                             "sizeof_dtype": 4,
                             "sizeof_c_dtype": 8},
              "double2":    {"dtype": "double",
                             "c_dtype": "double2",
                             "sizeof_dtype": 8,
                             "sizeof_c_dtype": 16}}

# : Supported int types as OpenCL => numpy dictionary.
itypes = {"char": numpy.int8, "short": numpy.int16, "int": numpy.int32,
          "long": numpy.int64,
          "uchar": numpy.uint8, "ushort": numpy.uint16, "uint": numpy.uint32,
          "ulong": numpy.uint64}

# : Supported float types as OpenCL => numpy dictionary.
dtypes = {"float": numpy.float32, "double": numpy.float64,
          "float2": numpy.complex64, "double2": numpy.complex128}

# : Complex type to real type mapping
dtype_map = {"float": "float", "double": "double",
             "float2": "float", "double2": "double"}


# : Map between numpy types and opencl.
def numpy_dtype_to_opencl(dtype):
    if dtype == numpy.float32:
        return "float"
    if dtype == numpy.float64:
        return "double"
    if dtype == numpy.complex64:
        return "float2"
    if dtype == numpy.complex128:
        return "double2"
    if dtype == numpy.int8:
        return "char"
    if dtype == numpy.int16:
        return "short"
    if dtype == numpy.int32:
        return "int"
    if dtype == numpy.int64:
        return "long"
    if dtype == numpy.uint8:
        return "uchar"
    if dtype == numpy.uint16:
        return "ushort"
    if dtype == numpy.uint32:
        return "uint"
    if dtype == numpy.uint64:
        return "ulong"
    raise error.ErrNotExists()


def get_itype_from_size(size, signed=True):
    """Get integer type from size.
    """
    if signed:
        if size < 128:
            return "char"
        if size < 32768:
            return "short"
        if size < 2147483648:
            return "int"
        return "long"
    if size < 256:
        return "uchar"
    if size < 65536:
        return "ushort"
    if size < 4294967296:
        return "uint"
    return "ulong"