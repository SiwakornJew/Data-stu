def findIndexOfMaxPositive(lists):
    index = None
    for i in range(len(lists)):
        if index == None and lists[i] >= 0:
            index = i
        elif index != None and lists[i] >lists[index]:
            index = i
    return index

def selectionSort(lists):
    for i in range(len(lists)-1,-1,-1):
        if lists[i] >= 0:
            indexOflastPositive = i
            swapIndex = findIndexOfMaxPositive(lists[:indexOflastPositive])
            if swapIndex != None and lists[swapIndex]>=lists[indexOflastPositive]:
                temp1=lists[swapIndex]
                temp2=lists[indexOflastPositive]
                print("swap ",temp1,"<->",temp2," : ",lists)
                lists[indexOflastPositive],lists[swapIndex] = lists[swapIndex],lists[indexOflastPositive]
    return lists

lists = list(map(int,input("Enter Input : ").split(" ")))
temp = selectionSort(lists)
for i in temp:
    print(i,end=" ")