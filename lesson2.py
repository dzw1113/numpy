import numpy as np

print("NumPy简单入门教程:https://www.numpy.org.cn/article/basics/an_introduction_to_scientific_python_numpy.html")

print('数组基础')

print('创建一个数组:ndarrays。创建数组的4种不同方法，基本的方法是将序列传递给NumPy的array()函数; 你可以传递任何序列（类数组），而不仅仅是常见的列表（list）数据类型')

# 1D Array 一维数组
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print(a) # >>>[0 1 2 3 4]
print(b) # >>>[0 1 2 3 4]
print(c) # >>>[0 1 2 3 4]
print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[3]) # >>>3

print('创建一个2D（二维）数组')
# MD Array,
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[2,4]) # >>>25