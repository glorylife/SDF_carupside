import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)

fig.suptitle('Graph of stock car in september 2010 - 2015', fontsize=14, fontweight='bold')
ax1.set_title('show stock car and future stock car')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value(billion of stock car data, million of diff car data)')

x = [0,1,2,3,4,5]
y = [2.81,2.99,3.18,3.42,3.56,3.65]
ax1.plot(x,y,c='g',label='stock car')
for x,y in zip(x,y):
    plt.text(x, y, "%.2f" %y, ha='center',va='bottom')
w = [5,6]
z = [3.65, 4] # z[1] ยังไม่ใช่ค่าจริงๆ
ax1.plot(w,z,c='r',label='future stock car')
for x,y in zip(w,z):
    plt.text(x, y, "%.2f" %y, ha='center',va='bottom')
    
a = [1,2,3,4,5]
b = [1.7,1.8,2.4,1.3,0.9]
ax1.plot(a,b,c='b',label='diff car')
for x,y in zip(a,b):
    plt.text(x, y, "%.2f" %y, ha='center',va='bottom')
g = [5,6]
h = [0.9,1.2] #h[1] ยังไม่ใช่ค่าจริงๆ
ax1.plot(g,h,c='r',label='future diff car')
leg = ax1.legend(loc='lower left')
plt.show()

