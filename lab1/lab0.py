print('*** Fun with Drawing ***')
a=int(input("Enter input : "))
b=4*a-3
cout=0
for x in range(b) :
 for y in range(b) :
     if  x ==0 or x ==b-1 :
         print("#",end="")
     elif y == 0 or y ==b-1 :    
         print("#",end="")
     elif y ==2*a-2 and x==int(b/2):
         print("#",end="")
    
     else :
        print(".",end="")
 print("")