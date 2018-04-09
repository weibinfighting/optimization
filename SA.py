# -*-coding:utf-8-*-
# coding=utf-8
import random
import math






def neighbor_x(x=1, p=1, d=1):
    '''

    initial value:param x:
    dimension:param p:
    distance:param d:
    a value of x's nerghbor:return:
    '''
    if p == 1:
        N_x = (-1) ** random.randint(0, 1) * random.random() * d
        N_x = N_x+x
        return N_x
    elif p == 2:
        N_xx = (-1) ** random.randint(0, 1) * random.random()
        N_xy = (-1) ** random.randint(0, 1) * random.random(0, math.sqrt(1 - N_xx ** 2))
        N_x = [N_xx * d, N_xy * d]
        N_x = [x[0] + N_x[0], x[1] + N_x[1]]
        return N_x
    elif p == 3:
        N_xx = (-1) ** random.randint(0, 1) * random.random()
        N_xy = (-1) ** random.randint(0, 1) * random.random() * math.sqrt(1 - N_xx ** 2)
        N_xz = (-1) ** random.randint(0, 1) * random.random() * math.sqrt(1 - N_xx ** 2 - N_xy ** 2)
        N_x = [N_xx * d, N_xy * d, N_xz * d]
        N_x = [x[0]+N_x[0],x[1]+N_x[1],x[2]+N_x[2]]
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
        N_x = neighbor_x(x_0, p=p, d=0.1)
        x_1 = N_x
        # choose N(x)
        while not g(x_1):
            N_x = neighbor_x(x_0, p=p, d=0.1)
            x_1 = N_x
        f_j = f(x_1)
        print('***************' + str(x_1) + '****************\n'+'----'+str(f_j)+'----\n')
        delta_f = f_j - f_i
        if delta_f <= 0:
            A_ij = 1
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

__version__ = '0.3'
