import itertools
lst1 = []
lst2=[]
lst1 =[int(x) for x in input("Enter Your List : ").split()]
if(len(lst1)<=2):
    print("Array Input Length Must More Than 2") 
    exit()
for i in range(len(lst1)):
    for j in itertools.combinations(lst1, 3):
     if(sum(j)==5) :
        lst2.append(list(j))
     
lst2 =[sorted(y) for y in lst2]
lst2 = [i for n, i in enumerate(lst2) if i not in lst2[:n]]
print(lst2)    
   
   

