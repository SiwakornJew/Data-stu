def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (a*power(a,b-1))

a,b=input("Enter Input a b : ").split()
a=int(a)
b=int(b)
print(power(a,b))