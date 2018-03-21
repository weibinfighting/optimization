#-*-coding:utf-8-*-
#coding=utf-8
import numpy as np
import random
import math

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

def distance(x_1,x_2):
    if isinstance(x_1,list)&isinstance(x_2,list):
        d = []
        for i in list(range(0,len(x_1))):
            d[i] = x_1[i]-x_2[i]
        dis = sum(d)
        return dis
    else:
        dis = math.sqrt((x_1-x_2)^2)
    return dis
def Domain(f=None,init=0,to=10,step=0.1):
    if f==None:
        exit(1)
    D = []
    for x in list(range(init,to,step)):
        if f(x):
          D.append(x)
    return D

def iterative_inner(f = sum(),x_0 = None,g = None,t_0 = 100,iter_num = 100):
    '''
    inner interative function, to calculate the value of iteration
    energies:param f:
    initial value:param x_0:
    initial temperature:param t_0:
    number of inition:param iter_num:
    the best value:return:
    '''
    f_i = f(x_0);
    size = math.floor(math.log(x_0,2))+1
    rand_num = random.randint(2,size)
    #choose N(x)
    D = Domain(g,init=0,to=30,step=0.00001)
    N_x = []
    for x_1 in D:
        dist = distance(x_1= x_0,x_2 = x_1)
        if dist<=1:
            N_x.append(x_1)
    x_1 = N_x[rand_num]
    #x_0 = encode(x_0)
    #x_1 = x_0[:rand_num]+turnbio(x_0[rand_num])+x_0[rand_num+1:]
    G_ij = 1; #Transfer probability
    A_ij = 1; #Accepted probability
    p_ij = G_ij*A_ij;
    f_j = f(x_1)
    return x_0

def init_time(t_0 = 100,T=1,chi=0.9,R_0 = 0):

    return t_0


__version__ = '0.1'
