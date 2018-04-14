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

N,pop_size = 30,50
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

def nochange(n_cross):
    Noc,n = [],1;
    while n <=n_cross:
        Noc.append(math.floor(random.random()*N))
        if len(set(Noc))<=n_cross:
            n = n+1;
        else:
            continue;
    return Noc

def cross(x,y):
    l_x,l_y = len(x),len(y)
    if l_x!=l_y:
        print('two parm lengh is not same!\n')
        exit(1);
    noc = nochange(n_cross);
    l = len(noc)
    class zx:
        value = [];
        index = [];
    for i in noc:
        zx.value.append(x[i])
    for x_v in zx.value:
        for i in list(range(l_y)):
            if x_v==y[i]:
                zx.index.append(i);
                break;
            else:
                continue;
    z_xs=sorted(zx.index)
    z_x = []
    for i in list(range(l)):
        for j in list(range(l)):
            if z_xs[i]==zx.value[j]:
                z_x.append(zx.index[j]);
                break;
            else:
                continue;

    class zy:
        value = [];
        index = [];
    for i in noc:
        zy.value.append(y[i])
    for y_v in zy.value:
        for i in list(range(l_x)):
            if y_v == x[i]:
                zy.index.append(i);
                break;
            else:
                continue;
    z_ys = sorted(zy.index)
    z_y = []
    for i in list(range(l)):
        for j in list(range(l)):
            if z_ys[i] == zy.value[j]:
                z_y.append(zy.index[j]);
                break;
            else:
                continue;
    x = z_x;
    y = z_y;
    return x,y

x=[];
for i in list(range(pop_size)):
    x.append(initnum(N));
n_cross = 23
x_noc = nochange(n_cross);

print(x[0],x[1])
z = cross(x[0],x[1])
print(z)
