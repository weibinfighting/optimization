import random
import math
import SA
def obf(x):
    L = 3
    r = []
    for n in list(range(0, L)):
        r.append(math.sqrt(x[n]))
    result = -sum(r)
    return result


def supg(x):
    if x[0] >= 0 and x[1] >= 0 and x[2] >= 0:
        if x[0] + 2 * x[1] ** 2 + 3 * x[2] ** 2 <= 1:
            return True
        else:
            return False
    else:
        return False

#Initialization temperature
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

K=3
T = [detal_0*K]
M = 800
for i in list(range(M)):
    T.append(T[i]*0.98)
f = open('SA.txt','a+')
f.write(str(T[0]))
for n in list(range(10)):
    x_0 = []
    x_0.append(random.random())
    x_0.append(random.random()*math.sqrt((1-x_0[0])/2))
    x_0.append(random.random()*pow((1-x_0[0]-2*x_0[1]**2)/3,1/3))
    x = []
    x.append(x_0)
    for i in list(range(len(T))):
        x.append(SA.iterative_inner(f=obf, x_0=x[i], g=supg, t_0=T[i], iter_num=200))
        f.write('dat:'+str(x[i])+'\n')
    f.write('coordinate:'+str(x[M])+'\n')
    f.write('object:'+str(-obf(x[M]))+'\n')
    f.write('max:'+str(-obf([0.642,0.3964,0.302]))+'\n---------------------\n')
f.close()
