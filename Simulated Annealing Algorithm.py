# -*-coding:utf-8-*-
# coding=utf-8
import numpy as np
import random
import math


def obf(x):
    L = 3
    r = []
    for n in list(range(0, L)):
        r.append(math.sqrt(x[n]))
    result = sum(r)
    return result


def supg(x):
    if x[0] >= 0 and x[1] >= 0 and x[2] >= 0:
        if x[0] + 2 * x[1] ** 2 + 3 * x[2] ** 2 <= 1:
            return True
        else:
            return False
    else:
        return False


def encode(x_0):
    x_0 = bin(x_0)
    return x_0


def decode(x_0):
    x_0 = int(x_0, 10);
    return x_0


def turnbio(str):
    if str == '1':
        x = '0';
    else:
        x = '1';
    return x


def neighbor_x(x=1, p=1, d=1):
    '''

    initial value:param x:
    dimension:param p:
    distance:param d:
    a value of x's nerghbor:return:
    '''
    if p == 1:
        N_x = (-1) ** random.randint(0, 1) * random.random() * d
        return N_x
    elif p == 2:
        N_xx = (-1) ** random.randint(0, 1) * random.random()
        N_xy = (-1) ** random.randint(0, 1) * random.random(0, math.sqrt(1 - N_xx ** 2))
        N_x = [N_xx * d, N_xy * d]
        return N_x
    elif p == 3:
        N_xx = (-1) ** random.randint(0, 1) * random.random()
        N_xy = (-1) ** random.randint(0, 1) * random.random() * math.sqrt(1 - N_xx ** 2)
        N_xz = (-1) ** random.randint(0, 1) * random.random() * math.sqrt(1 - N_xx ** 2 - N_xy ** 2)
        N_x = [N_xx * d, N_xy * d, N_xz * d]
        return N_x
    else:
        print('The current program does not support higher dimensions temporarily')
        exit(1)

def iterative_inner(f=sum, x_0=None, g=None, t_0=100, iter_num=20):
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
        f_i= f(x_0)
        N_x = neighbor_x(x_0, p=len(x_0), d=0.4)
        x_1 = N_x
        # choose N(x)
        while not g(x_1):
            N_x = neighbor_x(x_0, p=len(x_0), d=0.4)
            x_1 = N_x
        f_j = f(x_1)
        delta_f = f_j - f_i
        if delta_f <= 0:
            A_ij = 1
            x_0 = x_1  # Replace the initial value
        else:
            A_ij = math.exp(-delta_f/t_0)
        if A_ij > random.random():
            x_0 = x_1
        else:
            continue
    return x_0

    # x_0 = encode(x_0)
    # x_1 = x_0[:rand_num]+turnbio(x_0[rand_num])+x_0[rand_num+1:]
    # G_ij = 1; #Transfer probability
    # A_ij = 1; #Accepted probability
    # p_ij = G_ij*A_ij;

f_1 = []
for i in list(range(100)):
    x_0 = []
    x_0.append(random.random())
    x_0.append(random.random()*math.sqrt((1-x_0[0])/2))
    x_0.append(random.random()*pow((1-x_0[0]-2*x_0[1]**2)/3,1/3))
    f_1.append(obf(x_0))
average_f = sum(f_1)/len(f_1)
f_2 = []
for i in list(range(len(f_1))):
    f_2.append((f_1[i]-average_f)**2)
f_2 = sum(f_2)/(len(f_2)-1)
detal_0 = 6*math.sqrt(f_2)


T = [13.9]
M = 1000
for i in list(range(M)):
    T.append(T[i]*0.99)
x_0 = []
x_0.append(random.random())
x_0.append(random.random()*math.sqrt((1-x_0[0])/2))
x_0.append(random.random()*pow((1-x_0[0]-2*x_0[1]**2)/3,1/3))
x = []
x.append(x_0)
for i in list(range(len(T))):
    print(x[i])
    x.append(iterative_inner(f=obf, x_0=x[i], g=supg, t_0=T[i], iter_num=100))
print(obf(x[1000]))
__version__ = '0.1'
