def factorial(n):
    if n == 0: return 1
    if n == 1:  return n
    else : return int(n* (factorial(n-1)))

n= int(input('Enter Number : '))
ans =factorial(n)
print(str(n)+"! = "+str(ans))
