import os
import csv
import random
import numpy as np

import math


def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def getLog(x, mean, sd):
    temp = normpdf(x, mean, sd)
    if temp == 0:
        return 0
    else:
        return math.log(temp)

def clear(): return os.system('cls')


clear()

x1 = []
x2 = []
T = []

with open('Data.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        x1.append(float(row[0]))
        x2.append(float(row[1]))
        T.append(int(row[2]))


# w1 = float(np.random.randn(1))
# w2 = float(np.random.randn(1))
# b = float(np.random.randn(1))
# n = random.uniform(0, 1)

# y = 0
# e = 0
# errors = []

# for i, elem in enumerate(T):
#     v = ((x1[i] * w1) + (x2[i] * w2) + b)

#     if v > 0:
#         y = 1
#     else:
#         y = -1

#     tempError = T[i] - y
#     errors.append(tempError)
#     e += abs(tempError)

# a = 0
# # mokymas
# e = 1
# while e != 0:
#     for i, elem in enumerate(T):
#         w1 = w1 + (n * errors[i] * x1[i])
#         w2 = w2 + (n * errors[i] * x2[i])
#         b = b + (n * errors[i])
#         print(w1)
#         print(w2)
#         print(b)

#         v = ((x1[i] * w1) + (x2[i] * w2) + b)
#         if v > 0:
#             y = 1
#         else:
#             y = -1

#         tempError = T[i] - y
#         errors[i] = tempError
#         e += abs(tempError)


#     a += 1


# print(f'loops: {a}')


# -- naive baes --


trainAppleX1 = []
trainAppleX2 = []

trainPearX1 = []
trainPearX2 = []

# trainX2 = []
# trainT = []

appleCount = 0
pearCount = 0

with open('DataTrain.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        # trainX2.append(float(row[1]))
        # trainT.append(int(row[2]))
        if int(row[2]) > 0:
            trainAppleX1.append(float(row[0]))
            trainAppleX2.append(float(row[1]))
            appleCount += 1
        else:
            trainPearX1.append(float(row[0]))
            trainPearX2.append(float(row[1]))
            pearCount += 1

# apple
pForApple = appleCount / (appleCount + pearCount)
meanAppleX1 = np.mean(trainAppleX1)
meanAppleX2 = np.mean(trainAppleX2)
standardDeviationAppleX1 = np.std(trainAppleX1)
standardDeviationAppleX2 = np.std(trainAppleX2)

# pear
pForPear = pearCount / (appleCount + pearCount)
meanPearX1 = np.mean(trainPearX1)
meanPearX2 = np.mean(trainPearX2)
standardDeviationPearX1 = np.std(trainPearX1)
standardDeviationPearX2 = np.std(trainPearX2)

# reading
testX1 = []
testX2 = []
testT = []


with open('DataTest.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        testX1.append(float(row[0]))
        testX2.append(float(row[1]))
        testT.append(int(row[2]))


for i, elem in enumerate(testT):
    testTempApple = math.log(pForApple) + getLog(testX1[i], meanAppleX1, standardDeviationAppleX1) + getLog(testX2[i], meanAppleX2, standardDeviationAppleX2)

    testTempPear = math.log(pForPear) + getLog(testX1[i], meanPearX1, standardDeviationPearX1) + getLog(testX2[i], meanPearX2, standardDeviationPearX2)

    print(f'Apple: {testTempApple}, Pear: {testTempPear}')
    if testTempApple > testTempPear:
        print(f'Apple, plausibleRes: 1, trueRes: {elem}')
    else:
        print(f'Pear, plausibleRes: -1, trueRes: {elem}')