#!/usr/bin/python3
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
x=[]
y=[]
for i in range (1,10):
    x.append(i)
    y.append(random.random())

plt.plot(x,y)
plt.ylabel("Random numbers")
plt.show()

    
