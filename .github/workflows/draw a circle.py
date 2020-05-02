from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import *
from reportlab.lib import colors
import numpy as np

d = Drawing(200, 200)
r = 100

# 弧度 a
# 第一象限
x1 = []
y1 = []
for a in np.arange(0, pi / 2, 0.01):
    x = cos(a) * r + 100
    y = sin(a) * r + 100
    x1.append(x)
    y1.append(y)
site1 = list(zip(x1, y1))

print(site1)

# 第二象限
x2 = []
y2 = []
for a in np.arange(0, pi / 2, 0.01):
    x = 100 - sin(a) * r
    y = 100 + cos(a) * r
    x2.append(x)
    y2.append(y)
site2 = list(zip(x2, y2))

print(site2)

#第三象限
x3 = []
y3 = []
for a in np.arange(0, pi / 2, 0.01):
    x = 100 - cos(a) * r
    y = 100 - sin(a) * r
    x3.append(x)
    y3.append(y)
site3 = list(zip(x3, y3))

# 第四象限
x4 = []
y4 = []
for a in np.arange(0, pi / 2, 0.01):
    x = 100 + sin(a) * r
    y = 100 - cos(a) * r
    x4.append(x)
    y4.append(y)
site4 = list(zip(x4, y4))

L = site1 + site2 + site3 + site4
print(L)

d.add(PolyLine(L, strokeColor=colors.red))

renderPDF.drawToFile(d, 'circle10.pdf', 'whole')

# circlepoint =[100,100]
# for x in range(0,201):
#     for y in range(0,200):
#
#
#
# s= PolyLine([(100, 0), (200, 100), (100, 200), (0, 100),(100, 0)])
#
# d.add(s)
#
# renderPDF.drawToFile(d,'line3.pdf')
