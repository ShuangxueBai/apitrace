##########################################################################
#
# Copyright 2012 Jose Fonseca
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/


from winapi import *


D3D_DRIVER_TYPE = Enum('D3D_DRIVER_TYPE', [
    'D3D_DRIVER_TYPE_UNKNOWN',
    'D3D_DRIVER_TYPE_HARDWARE',
    'D3D_DRIVER_TYPE_REFERENCE',
    'D3D_DRIVER_TYPE_NULL',
    'D3D_DRIVER_TYPE_SOFTWARE',
    'D3D_DRIVER_TYPE_WARP',
])

D3D_FEATURE_LEVEL = Enum('D3D_FEATURE_LEVEL', [
    'D3D_FEATURE_LEVEL_9_1',
    'D3D_FEATURE_LEVEL_9_2',
    'D3D_FEATURE_LEVEL_9_3',
    'D3D_FEATURE_LEVEL_10_0',
    'D3D_FEATURE_LEVEL_10_1',
    'D3D_FEATURE_LEVEL_11_0',
    'D3D_FEATURE_LEVEL_11_1',
])

D3D10_PRIMITIVE_TOPOLOGY = Enum('D3D10_PRIMITIVE_TOPOLOGY', [
    'D3D10_PRIMITIVE_TOPOLOGY_UNDEFINED',
    'D3D10_PRIMITIVE_TOPOLOGY_POINTLIST',
    'D3D10_PRIMITIVE_TOPOLOGY_LINELIST',
    'D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP',
    'D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST',
    'D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP',
    'D3D10_PRIMITIVE_TOPOLOGY_LINELIST_ADJ',
    'D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ',
    'D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ',
    'D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ',
])

D3D11_PRIMITIVE_TOPOLOGY = Enum('D3D11_PRIMITIVE_TOPOLOGY', [
    'D3D11_PRIMITIVE_TOPOLOGY_UNDEFINED',
    'D3D11_PRIMITIVE_TOPOLOGY_POINTLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_LINELIST',
    'D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP',
    'D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST',
    'D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP',
    'D3D11_PRIMITIVE_TOPOLOGY_LINELIST_ADJ',
    'D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ',
    'D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ',
    'D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ',
    'D3D11_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST',
    'D3D11_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST',
])

D3D10_PRIMITIVE = Enum('D3D10_PRIMITIVE', [
    'D3D10_PRIMITIVE_UNDEFINED',
    'D3D10_PRIMITIVE_POINT',
    'D3D10_PRIMITIVE_LINE',
    'D3D10_PRIMITIVE_TRIANGLE',
    'D3D10_PRIMITIVE_LINE_ADJ',
    'D3D10_PRIMITIVE_TRIANGLE_ADJ',
])

D3D11_PRIMITIVE = Enum('D3D11_PRIMITIVE', [
    'D3D11_PRIMITIVE_UNDEFINED',
    'D3D11_PRIMITIVE_POINT',
    'D3D11_PRIMITIVE_LINE',
    'D3D11_PRIMITIVE_TRIANGLE',
    'D3D11_PRIMITIVE_LINE_ADJ',
    'D3D11_PRIMITIVE_TRIANGLE_ADJ',
    'D3D11_PRIMITIVE_1_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_2_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_3_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_4_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_5_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_6_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_7_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_8_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_9_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_10_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_11_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_12_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_13_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_14_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_15_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_16_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_17_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_18_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_19_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_20_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_21_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_22_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_23_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_24_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_25_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_26_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_27_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_28_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_29_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_30_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_31_CONTROL_POINT_PATCH',
    'D3D11_PRIMITIVE_32_CONTROL_POINT_PATCH',
])

D3D10_SRV_DIMENSION = Enum('D3D10_SRV_DIMENSION', [
    'D3D10_SRV_DIMENSION_UNKNOWN',
    'D3D10_SRV_DIMENSION_BUFFER',
    'D3D10_SRV_DIMENSION_TEXTURE1D',
    'D3D10_SRV_DIMENSION_TEXTURE1DARRAY',
    'D3D10_SRV_DIMENSION_TEXTURE2D',
    'D3D10_SRV_DIMENSION_TEXTURE2DARRAY',
    'D3D10_SRV_DIMENSION_TEXTURE2DMS',
    'D3D10_SRV_DIMENSION_TEXTURE2DMSARRAY',
    'D3D10_SRV_DIMENSION_TEXTURE3D',
    'D3D10_SRV_DIMENSION_TEXTURECUBE',
])

D3D10_SRV_DIMENSION1 = Enum('D3D10_SRV_DIMENSION1', [
    'D3D10_1_SRV_DIMENSION_UNKNOWN',
    'D3D10_1_SRV_DIMENSION_BUFFER',
    'D3D10_1_SRV_DIMENSION_TEXTURE1D',
    'D3D10_1_SRV_DIMENSION_TEXTURE1DARRAY',
    'D3D10_1_SRV_DIMENSION_TEXTURE2D',
    'D3D10_1_SRV_DIMENSION_TEXTURE2DARRAY',
    'D3D10_1_SRV_DIMENSION_TEXTURE2DMS',
    'D3D10_1_SRV_DIMENSION_TEXTURE2DMSARRAY',
    'D3D10_1_SRV_DIMENSION_TEXTURE3D',
    'D3D10_1_SRV_DIMENSION_TEXTURECUBE',
    'D3D10_1_SRV_DIMENSION_TEXTURECUBEARRAY',
])

D3D11_SRV_DIMENSION = Enum('D3D11_SRV_DIMENSION', [
    'D3D11_SRV_DIMENSION_UNKNOWN',
    'D3D11_SRV_DIMENSION_BUFFER',
    'D3D11_SRV_DIMENSION_TEXTURE1D',
    'D3D11_SRV_DIMENSION_TEXTURE1DARRAY',
    'D3D11_SRV_DIMENSION_TEXTURE2D',
    'D3D11_SRV_DIMENSION_TEXTURE2DARRAY',
    'D3D11_SRV_DIMENSION_TEXTURE2DMS',
    'D3D11_SRV_DIMENSION_TEXTURE2DMSARRAY',
    'D3D11_SRV_DIMENSION_TEXTURE3D',
    'D3D11_SRV_DIMENSION_TEXTURECUBE',
    'D3D11_SRV_DIMENSION_TEXTURECUBEARRAY',
    'D3D11_SRV_DIMENSION_BUFFEREX',
])

ID3D10Blob = Interface('ID3D10Blob', IUnknown)
ID3D10Blob.methods += [
    StdMethod(LPVOID, 'GetBufferPointer', [], sideeffects=False),
    StdMethod(SIZE_T, 'GetBufferSize', [], sideeffects=False),
]
LPD3D10BLOB = ObjPointer(ID3D10Blob)

D3D10_INCLUDE_TYPE = Enum('D3D10_INCLUDE_TYPE', [
    'D3D10_INCLUDE_LOCAL',
    'D3D10_INCLUDE_SYSTEM',
])

ID3D10Include = Interface("ID3D10Include", IUnknown)
ID3D10Include.methods += [
    StdMethod(HRESULT, "Open", [(D3D10_INCLUDE_TYPE, "IncludeType"), (LPCSTR, "pFileName"), (LPCVOID, "pParentData"), Out(Pointer(LPCVOID), "ppData"), Out(Pointer(UINT), "pBytes")]),
    StdMethod(HRESULT, "Close", [(LPCVOID, "pData")]),
]
# It is implemented by applications, not D3D runtime, so treat as opaque for
# now.
LPD3D10INCLUDE = OpaquePointer(ID3D10Include)
