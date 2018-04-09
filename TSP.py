# coding=utf-8

import random
import math
import SA
import re

#To solve tsp about my homework




def initnum(N=30):
    class Cnum:
        data=[];
        index=[];

    for n in list(range(N)):
        Cnum.data.append(random.random());
        Cnum.index.append(n)
    x = sorted(Cnum.data)
    A = []
    for i in list(range(N)):
        for j in list(range(N)):
            if x[i]==Cnum.data[j]:
                A.append(Cnum.index[j]);
            else:
                continue;
    return A

def readcitycoord(filename):
    f = open(filename,'r')
    a=[]
    for i in list(range(N)):
        coord = str.split(f.readline())
        a.append([int(coord[0]),int(coord[1])])
    f.close()
    return a

def distance(x,y):
    #x,y=a[0],a[1];
    if isinstance(x,list)and isinstance(y,list):
        d = []
        for i in list(range(0,len(x))):
            d.append((x[i]-y[i])**2)
        dis = (sum(d))**0.5
        return dis
    elif not(isinstance(x,list) or isinstance(y,list)):
        dis = math.sqrt((x-y)^2)
        return dis
    else:
        print('Please check type of x_1 and x_2')
        exit(1)


N = 30
filename = 'DATA30.dat'
city_coord = readcitycoord(filename)
x_0 = initnum(N)
d=[]
for i in list(range(N-1)):
    d.append(distance(city_coord[x_0[i]],city_coord[x_0[i+1]]));
all_d = sum(d);

