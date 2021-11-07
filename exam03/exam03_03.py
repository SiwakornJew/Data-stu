def findGcd(num1,num2):
    r=num1%num2
    if r==0:
        return num2
    else:
        return findGcd(num2,r)

n = [int(e) for e in input('Enter Input : ').split()]
if int(n[0])==0 and int(n[1])==0 :
    print("Error! must be not all zero.")
elif int(n[0])==0 or int(n[1])==0 :
    if n[0]<0 or n[1]<0:
        print(f"The gcd of {max(n)} and {min(n)} is : {abs(min(n))}")
    else:
        print(f"The gcd of {max(n)} and {min(n)} is : {max(n)}")
else:
    ans =findGcd(int(n[0]),int(n[1]))
    if n[0]<0 and n[1]<0:
        print(f"The gcd of {min(n)} and {max(n)} is : {abs(ans)}")
    else:
        print(f"The gcd of {max(n)} and {min(n)} is : {abs(ans)}")