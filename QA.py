# -*-coding:utf-8-*-

import random
import math


def readcitycoord(filename):
    '''
    read data from file
    where saved data :param filename:
    the coord of city :return:
    '''

    f = open(filename,'r')
    a=[]
    for i in list(range(N)):
        coord = str.split(f.readline())
        try:
            a.append([int(coord[0]),int(coord[1])])
        except:
            a.append([float(coord[0]),float(coord[1])])
    f.close()
    return a

N,pop_size = 10,50
filename = 'DATA30.dat'
city_coord = readcitycoord(filename)

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

def Xchange(n_cross):
    Xc,n = [],1;
    while n <=n_cross:
        newx = math.floor(random.random()*N)
        ifT = 1
        for i in Xc:
            if i==newx:
                ifT = 0
        if ifT==1:
            Xc.append(newx)
            n = n+1;
        else:
            continue;
    return Xc

def cross(x,y,qc):
    l_x,l_y = len(x),len(y)
    if l_x!=l_y:
        print('two parm lengh is not same!\n')
        exit(1);
    l = len(qc)
    class zx:
        value = [];
        index = [];
    for i in qc:
        zx.value.append(x[i])
    for x_v in zx.value:
        zx.index.append(y.index(x_v))
    z_x = []
    z_xs = sorted(zx.index)
    m = 0
    for i in list(range(N)):
        change = 0
        for j in qc:
            if i==j:
                change = 1;
            else:
                continue
        if change==1:
            z_x.append(zx.value[zx.index.index(z_xs[m])]);
            m = m+1;
        else:
            z_x.append(x[i])
    class zy:
        value = [];
        index = [];
    for i in qc:
        zy.value.append(y[i])
    for y_v in zy.value:
        zy.index.append(x.index(y_v))
    z_y = []
    z_ys = sorted(zy.index)
    m = 0
    for i in list(range(N)):
        change = 0
        for j in qc:
            if i==j:
                change = 1;
            else:
                continue
        if change==1:
            z_y.append(zy.value[zy.index.index(z_ys[m])]);
            m=m+1
        else:
            z_y.append(y[i])
    return z_x,z_y

x=[];
for i in list(range(pop_size)):
    x.append(initnum(N));
n_cross = 5
x_c = Xchange(n_cross);
new_x = []
for i in list(range(0,pop_size,2)):
    z = cross(x[i],x[i+1],x_c)
    new_x.append(z[0])
    new_x.append(z[1])
print(len(new_x))
