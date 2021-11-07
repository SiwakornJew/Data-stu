def minIndex(data,i,j):
    if i == j:
        return i
    k = minIndex(data,i+1,j)
    return (i if data[i] < data[k] else k)


def recurSelectionSort(data,n,index=0):
    if index == n:
        return -1
    k = minIndex(data,index,n-1)
    if k != index:
        temp1=data[k]
        temp2=data[index]
        #print("swap ",temp1,"<->",temp2," : ",data)
        data[k], data[index] =data[index], data[k]
        print("swap ",temp1,"<->",temp2," : ",data)
    recurSelectionSort(data,n,index+1)
    return data


#inp = [int(a) for a in input('Enter Input : ').split()]
inp=[5,4,3,1,2]
n=recurSelectionSort(inp,len(inp))

print(n)