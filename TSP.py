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

def obf(x=None,coord=None):
    if x == None or coord == None:
        print('The parament is None!');
        exit(1);
    D = [];
    for i in list(range(len(x)-1)):
        D.append(distance(coord[x[i]],coord[x[i+1]]));
    D = sum(D)
    return D

N = 30
filename = 'DATA30.dat'
city_coord = readcitycoord(filename)
x_0 = initnum(N);
def neighbor_city(x):
    a,b=math.floor(random.random()*N),math.floor(random.random()*N)
    x_new = x
    while a==b:
        b=math.floor(random.random()*N)
    x_new[a]=x[b]
    x_new[b]=x[a];
    return x_new


def iterative_inner(f=obf, x_0=None, y = None, t_0=100, iter_num=20):
    '''
    inner interative function, to calculate the value of iteration
    energies:param f:
    initial value:param x_0:
    initial temperature:param t_0:
    number of inition:param iter_num:
    the best value:return:
    '''

    p = len(x_0)
    for n in list(range(0, iter_num)):
        f_i= f(x_0,y)
        N_x = neighbor_city(x_0)
        x_1 = N_x
        f_j = f(x_1,y)
        print('---' + str(x_0) + '---\n'+'---'+str(f_i)+'---')
        print('***' + str(x_1) + '***\n'+'---'+str(f_j)+'---\n')
        delta_f = f_j - f_i
        print(delta_f)
        delta_f = delta_f/200
        print(delta_f)
        print('f_i is %f'%f_i)
        if delta_f <= 0:
            A_ij = 1
        else:
            A_ij = math.exp(-delta_f/t_0)
        print('A_ij:'+str(A_ij)+'\n'+'t:'+str(t_0)+'\nx_0:'+str(x_0))
        if A_ij > random.random():
            x_0 = x_1
        else:
            print('x_0 not change')
            x_0=x_0
        print('now f_1 is %f'%f(x_0,y))
    return x_0


def initT(n=100,N=30,K=10):
    f_1=[];
    for i in list(range(n)):
        x=initnum(N);
        f_1.append(obf(x,city_coord))
    average_f = sum(f_1)/n;
    f_2 = [];
    for j in list(range(n)):
        f_2.append((f_1[j] - average_f) ** 2);
    f_2 = sum(f_2) / (len(f_2) - 1)
    detal_0 = 6 * math.sqrt(f_2)
    return detal_0*K


T = [initT(500,30,5)]
M = 1500
for i in list(range(M)):
    T.append(T[i]*0.95)
x=x_0
for t in T:
    x=iterative_inner(f=obf,x_0=x,y=city_coord,t_0=t,iter_num=100)
    print(x)
print(obf(x,city_coord))
