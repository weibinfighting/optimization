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

def obf(x,coord):
    if x == None or coord == None:
        print('The parament is None!');
        exit(1);
    D = [];
    for i in list(range(len(x)-1)):
        D.append(distance(coord[x[i]],coord[x[i+1]]));
    D = sum(D)
    return D


def initnum(N):
    '''
    product N random numbers from 0 to N
    N paraments:param N:
    N random number:return:
    '''
    order_data=[];

    for i in list(range(N)):
        order_data.append(random.random());
    sort_data = sorted(order_data)
    sorted_data = []
    for i in list(range(N)):
        sorted_data.append(order_data.index(sort_data[i]))
    return sorted_data

def Xchange(n_cross):
    '''
    The X numbers do cross;
    the number of crossing : param n_cross:
    which order of solution is crossed : return:
    '''
    X_cross, i_cross = [], 0;  #X_cross is the order of solution is crossed, n is count number
    while i_cross < n_cross:
        newx = math.floor(random.random()*N)
        if newx not in X_cross:
            X_cross.append(newx)
            i_cross = i_cross+1;
        else:
            continue;
    return X_cross

def cross(x_cross,y_cross,qc):
    l_x,l_y = len(x_cross),len(y_cross)
    if l_x!=l_y:
        print('two parm lengh is not same!\n')
        exit(1);
    l = len(qc)
    class zx:
        value = [];
        index = [];
    for i in qc:
        zx.value.append(x_cross[i])
    for x_v in zx.value:
        zx.index.append(y_cross.index(x_v))
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
            z_x.append(x_cross[i])
    class zy:
        value = [];
        index = [];
    for i in qc:
        zy.value.append(y_cross[i])
    for y_v in zy.value:
        zy.index.append(x_cross.index(y_v))
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
            z_y.append(y_cross[i])
    return z_x,z_y

def variation(X,P=0.02,qn=2):
    if random.random()<=P:
        n = math.floor(random.random()*N);
        m = math.floor(random.random()*N);
        while n==m:
            m = math.floor(random.random()*N);
        variable = X[n];
        X[n] = X[m];
        X[m] = variable;
        return X;
    else:
        return X;

def findgroup(pop_size,Acp):
    next_p = random.random();
    for i in list(range(pop_size)):
        if Acp[i]<next_p and next_p<=Acp[i+1]:
            return i;
        elif 0<next_p and next_p<=Acp[0]:
            return 0;
        else:
            continue;

def generation(x):
    x_c = Xchange(n_cross);
    new_x = []
    for i in list(range(0,pop_size,2)):
        z = cross(x[i],x[i+1],x_c)
        new_x.append(variation(z[0]))
        new_x.append(variation(z[1]))
    fitvalue = [];
    for i in list(range(pop_size)):
        fitvalue.append(obf(new_x[i],city_coord))
    Acp = [];
    allfv = sum(fitvalue);
    Acd = 0;
    for i in list(range(pop_size)):
        Acd = Acd+fitvalue[i]
        Acp.append(Acd/allfv)
    next_group = [];
    for i in list(range(pop_size)):
        next_group.append(findgroup(pop_size,Acp));
    next_x = [];
    for i in list(range(pop_size)):
        next_x.append(new_x[next_group[i]]);
    return next_x

x=[];
for i in list(range(pop_size)):
    x.append(initnum(N));
n_cross = 5
for i in list(range(1500)):
    x = generation(x)
ob = [];
for i in list(range(pop_size)):
    ob.append(obf(x[i],city_coord))
print(min(ob))