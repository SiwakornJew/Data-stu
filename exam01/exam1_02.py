print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))
count=0
if num <=0:
   # print()
    print("0 is OUT of range !!!")
    pass
else:
    print("Output ==> ",end="")
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=' ')
            count+=1
    print()
    print(f"Total ==> {count}")
