# Built on 32-bit-Python (3.5.2) on Windows

"""
The Main Idea is to get Data from a file and put in a matrix{List of List} so accessing will be easy
"""

import sys

# Declaring Global String and initialting to ""
# as it should not be initilized to null(we will get TypeError: 'NoneType' )
KeyList = ""


#Calculating Number of Lines In the File,Which gives us the number of Rows in the Matrix
def Lines(File_Address):
    with open(File_Address) as enum:
        for x , y in enumerate(enum):
            pass
        return x + 1


#This Function Does the job of FInding the next Position to go by giving the present Position
# it also takes care of making the previous position = 0 after going to next position
def NextPosFinder ( i , j , Matrix):
    global M
    i=int(i)
    j=int(j)
    global N

#Clockwise Checking in the Order
# E,S,W,N,SE,SW,NW,NE
#Making sure that the Indexing is never out of the list
    if(i+1<=M-1 and j+1<=N-1):
        if(Matrix[i][j+1]==1):
            Matrix[i][j+1]=0
            return i,j+1
#Making sure that the Indexing is never out of the list
    if(i+1<=M-1 and j<=N-1):
        if(Matrix[i+1][j]==1):
            Matrix[i+1][j]=0
            return i+1,j
#Making sure that the Indexing is never out of the list
    if(i<=M-1 and j-1<=N-1):
        if(Matrix[i][j-1]==1):
            Matrix[i][j-1]=0
            return i,j-1
#Making sure that the Indexing is never out of the list
    if(i-1<=M-1 and j<=N-1):
        if(Matrix[i-1][j]==1):
            Matrix[i-1][j]==0
            return i-1,j
#Making sure that the Indexing is never out of the list
    if(i+1<=M-1 and j+1<=N-1):
        if(Matrix[i+1][j+1]==1):
            Matrix[i+1][j+1]=0
            return i+1,j+1
#Making sure that the Indexing is never out of the list
    if(i+1<=M-1 and j-1<=N-1):
        if(Matrix[i+1][j-1]==1):
            Matrix[i+1][j-1]==0
            return i+1,j-1
#Making sure that the Indexing is never out of the list
    if(i-1<=M-1 and j-1<=N-1):
        if(Matrix[i-1][j-1]==1):
            Matrix[i-1][j-1]=0
            return i-1,j-1
#Making sure that the Indexing is never out of the list
    if(i-1<=M-1 and j+1<=N-1):
        if(Matrix[i-1][j+1]==1):
            Matrix[i-1][j+1]=0
            return i-1,j+1
#If unable to Find the Next Position(No 1s to go to as remaining neighbours are0s)
# it simply returns the Initial Position
    return i,j



#This is the Function Which Makes a Polygon
def Cycler( i , j , Matrix):
    global M
    global N
    i=int(i)
    j=int(j)
    global KeyList
#Initial pos -> i,j
    init_i , init_j = i , j

#Next Position ->next_i,next_j
    next_i , next_j = NextPosFinder( i , j , Matrix)
#No mre path,reached initial position.....POLYGON COmplete
    if(next_i==i and next_j==j):
        return
    else:
         #Appending Coordinates to KeyList
         KeyList =   KeyList + str(next_i)
         KeyList =   KeyList + str(next_j)
#Recursion
         Cycler(next_i,next_j,Matrix)




####################################################################
    # INPUT CODE
print("Enter Completely QUalified TXT File Name")
File_Address = input()
#Make this CommandlIne

M = Lines(File_Address)

FObj = open(File_Address)

Lines = FObj.readlines()

N = len(Lines[0])-1

Matrix = [[0 for x in range(N)] for y in range(M)]

for p in range(M):
    for o in range(N):
        Matrix[p][o] = int(Lines[p][o])

FObj.close()
#####################################################################

iter = 0
if(Matrix[0][0]==1):
    key_i = 0
    key_j = 0
else:
    key_i,key_j=NextPosFinder(0,0,Matrix)

while(True):
    
    KeyList = KeyList + str(key_i)
    KeyList = KeyList + str(key_j)
#BEcause no need to print * ate the begining ,so ergulating it
    if(iter!=0):
        KeyList = KeyList +"*"
    TempList = (KeyList +'.')[:-1]
    
    Cycler(key_i,key_j,Matrix )
    iter = 1
    if(TempList == KeyList):
        break
    key_i,key_j=NextPosFinder(key_i,key_j,Matrix)

print(KeyList)
    

