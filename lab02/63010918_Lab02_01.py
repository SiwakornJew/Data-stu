def Rshift(num,shift):
    num= num>>shift
    print(num)

a,b =input("Enter number and shiftcount : ").split(" ")
Rshift(int(a),int(b))