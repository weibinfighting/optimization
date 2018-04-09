# coding=utf-8

import random
import math
import SA

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

