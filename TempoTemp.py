#!/bin/python3

import sys

def getMaxScore(a):
    #leng = len(a)
    #leng = leng-1
    x = 0
    running_sum = 0
    s=0
    while(True):
        val = a[0]
        if(val>=0):
            s=s+(running_sum%val)
        running_sum = running_sum + val
        #leng = leng-1
        #x=x+1
        a.remove(val)
        if(len(a)==0):
            break
    return s

n = int(input().strip())
if(not(1<=n<=20)):
    sys.exit(0)
a = list(map(int, input().strip().split(' ')))
maxScore = getMaxScore(a)
print(maxScore)
