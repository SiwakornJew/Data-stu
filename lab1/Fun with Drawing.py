print("*** Fun with Drawing ***")
y= int(input("Enter input : "))
def printe(x):
    for i in range (x):
        print("#",end='') if i%2==0 else print(".",end='')
def printer(x):
    for i in range (x-1,-1,-1):
        print("#",end='') if i%2==0 else print(".",end='')
def printp(x):    
    print("#"*(((int(y)*4-4)+1)-(2*x)),end='') if x%2==0 else print("."*(((int(y)*4-4)+1)-(2*x)),end='')
for i in range (int(y)*2-1):
    printe(i)
    printp(i)
    printer(i)
    print()
for i in range (int(y)*2-3,-1,-1):
    printe(i)
    printp(i)
    printer(i)
    print()