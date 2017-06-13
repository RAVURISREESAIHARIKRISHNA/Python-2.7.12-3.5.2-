n = int(input())
i = 0
array = []
while(i<=n-1):
    array.append(input())
    i = i+1


i = 0
j = 0
while(j<n-1):
    while(i<=n-2):
        if( len(array[i]) > len(array[i+1]) ):
            temp = array[i+1]
            array[i+1] = array[i]
            array[i] = temp
            i = i+1
            j = j+1
            continue
            if(len(array[i]) == len(array[i+1]) and (int(array[i]) > int(array[i+1]))):
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                i = i+1
                j = j+1

i = 0
while(i<=n-1):
    print(array[i])
    i=i+1
