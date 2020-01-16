"""
数据打包
"""
import struct

# 设置数据格式  lily  18  76.5
st = struct.Struct("4sif")

# 数据打包
data = st.pack(b'Tom',18,76.5)

# data = struct.pack("4sif",b'Tom',18,76.5)

print(data)

# 数据解包
print(st.unpack(data))

