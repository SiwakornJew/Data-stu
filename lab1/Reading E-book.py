print("*** Reading E-Book ***")
a,b=input("Text , Highlight : ").split(",")
lst=[]
for i in range(len(a)) :
    if(a[i]==b):
        lst.append(i)

for x in range(len(a)):
    if x in lst:
        print("["+a[x]+"]", end =""),
    else:
        print(a[x], end="")
