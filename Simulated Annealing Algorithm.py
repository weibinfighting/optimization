#-*-coding:utf-8-*-
#coding=utf-8
import numpy as np
import random
import math

def f(x):
    L = 3
    r = []
    for n in list(range(0,L)):
        r.append(math.sqrt(x[n]))
    result = sum(r)
    return result
def g(x):
    if x[0]>=0 and x[1]>=0 and x[2]>=0:
        if x[0]+2*x[1]^2+3*x[2]^2<=1:
            return True
        else:
            return False
    else:
        return False

def encode(x_0):
    x_0 = bin(x_0)
    return x_0

def decode(x_0):
    x_0 = int(x_0,10);
    return x_0

def turnbio(str):
    if str=='1':
        x = '0';
    else:
        x = '1';
    return x

def distance(x,y):
    if isinstance(x,list)and isinstance(y,list):
        d = []
        for i in list(range(0,len(x))):
            d[i] = x[i]-y[i]
        dis = sum(d)
        return dis
    elif not(isinstance(x,list) or isinstance(y,list)):
        dis = math.sqrt((x-y)^2)
        return dis
    else:
        print('Please check type of x_1 and x_2')
        exit(1)


def Domain(f=None,init=0,to=10,step=0.1):
    if f==None:
        print('please input Objective function')
        exit(1)
    D = []
    for x in list(range(init,to,step)):
        if f(x):
          D.append(x)
    return D


def iterative_inner(f = sum,x_0 = None,g = None,t_0 = 100,iter_num = 20):
    '''
    inner interative function, to calculate the value of iteration
    energies:param f:
    initial value:param x_0:
    initial temperature:param t_0:
    number of inition:param iter_num:
    the best value:return:
    '''
    global D

    for n in list(range(1,iter_num+1)):
        f_i = f(x_0)
        t = t_0
        size = math.floor(math.log(x_0, 2)) + 1
        rand_num = random.randint(2, size)
        # choose N(x)
        D = Domain(g, init=0, to=30, step=0.00001)  # find the domain
        N_x = []
        # define domain
        for x_1 in D:
            dist = distance(x=x_0, y=x_1)  # calculate distance
            if dist <= 1:
                N_x.append(x_1)
        x_1 = N_x[rand_num]  # Randomly take elements in the field
        f_j = f(x_1)
        delta_f = f_j - f_i
        A_ij = math.exp(-delta_f / t)
        if delta_f <= 0:
            x_0 = x_1  # Replace the initial value
        elif A_ij > random.random():
            x_0 = x_1
        else:
            continue
    return x_0

    #x_0 = encode(x_0)
    #x_1 = x_0[:rand_num]+turnbio(x_0[rand_num])+x_0[rand_num+1:]
    #G_ij = 1; #Transfer probability
    #A_ij = 1; #Accepted probability
    #p_ij = G_ij*A_ij;

def init_time(t_0 = 100,K=1,chi=0.9,R = 0,f=None,g=None):
    X = []
    X.append(iterative_inner(f=f,x_0=D[random.randint[0,len(D)]],g=g,t_0=t_0,iter_num=100))
    R = len(set(X))/len(X)
    if R==chi:
        return t_0
    else:
        t_0 = t_0+K
        R_0 = R
        X = []
        X.append(iterative_inner(f=f, x_0=D[random.randint[0, len(D)]], g=g, t_0=t_0, iter_num=100))
        R = len(set(X))/len(X)
        while R !=chi:
            if R_0<chi and R<chi:
                t_0 = t_0+K
            elif R_0>chi and R>chi:
                t_0 = t_0-K
            elif R_0>chi and R<chi:
                t_0 = t_0+K/2
            else:
                t_0 = t_0-K/2
            R_0 = R
            X = []
            X.append(iterative_inner(f=f, x_0=D[random.randint[0, len(D)]], g=g, t_0=t_0, iter_num=100))
            R = len(set(X))/len(X)
    return t_0
T = []
M = 25
for k in list(range(0,M)):
    T.append((M-k)/M*init_time(t_0=100,f=f,g=g))
x=[]
for t in T:
    x.append(iterative_inner(f=f,x_0=x_0,g=g,t_0=t,iter_num=100))
print(x)

__version__ = '0.1'
