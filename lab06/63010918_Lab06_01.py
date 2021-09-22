def factorail(num):
    if num == 0:
        return '1'
    if num==1:
        return num
    else:
        return num*factorail(num-1)
    

num =int(input("Enter Number : "))
ans=factorail(num)
print(str(num)+"! = "+str(ans))