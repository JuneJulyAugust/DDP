from matplotlib.pyplot import *
from numpy import random
from numpy.random import rand
import csv


def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L

tau1List = []
tauDot1List = []
q1List = []
qDot1List = []
u1List = []
tau2List = []
tauDot2List = []
q2List = []
qDot2List = []
u2List = []

tau2ListList = []
tauDot2ListList = []
q2ListList = []
qDot2ListList = []
u2ListList = []

klist = []

''' position '''
path1 = '../_build/cpp/resultsDC1.csv'
path2 = '../_build/cpp/resultsDC2.csv'

with open(path1,'r') as dataFile1:
    reader = csv.reader(dataFile1)
    i = 0
    j = 0
    for row in reader:
        if i ==1:
            tau1List.append(float(row[0]))
            tauDot1List.append(float(row[1]))
            q1List.append(float(row[2]))
            u1List.append((float(row[3])))
            klist.append((float(row[4])))
        if i==0:
            i = 1

with open(path2,'r') as dataFile2:
    reader = csv.reader(dataFile2)
    i = 0
    j = -1
    for row in reader:
        if i ==2:
            if (j < T):
                tau2List.append(float(row[0]))
                tauDot2List.append(float(row[1]))
                q2List.append(float(row[2]))
                u2List.append((float(row[3])))
                j += 1
            else:
                tau2ListList.append(tau2List)
                tauDot2ListList.append(tauDot2List)
                q2ListList.append(q2List)
                u2ListList.append(u2List)
                tau2List = [float(row[0])]
                tauDot2List = [float(row[1])]
                q2List = [float(row[2])]
                u2List = [float(row[3])]
                j = 0
        if i ==1:
            T = int(row[0])
            N = int(row[1])+1
            i = 2
        if i==0:
            i = 1

T = len(tau1List)
time = []
for i in range(T):
    time.append(i*0.001)


figure()
hold(1)
plot(u1List)
plot(u2ListList[0])
grid()

fig1 = figure()
hold(1)
plot(time,tau1List[0:T],color=(0.0,0.0,0.0),linewidth=2)
plot(time,tau2ListList[0],color=(0.5,0.5,0.5),linewidth=2)
title('joint position',fontsize=36)
grid()
xlabel('time(s)',fontsize=28)
ylabel('joint angle (rad)',fontsize=28)
#legend(['open loop (no noise)','close loop (no noise)','open loop (noise)','closed loop (noise)'],fontsize=20)
legend(['FF','FB','FF+FB'],fontsize=20)





show()

