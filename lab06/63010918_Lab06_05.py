def darw(num,sharp):
    print('_'*(num-sharp),end='')
    print('#'*(sharp),end='')
    print()
def pattern(num, row=0):
    if num > 0:
        if row < num:
            row += 1
            darw(num,row)
            pattern(num,row)
    elif num < 0:
        if row < abs(num):
            darw(abs(num),abs(num)-row)
            row +=1
            pattern(num, row)
    else:
        print('Not Draw!')

num =int(input("Enter Input : "))
pattern(num)