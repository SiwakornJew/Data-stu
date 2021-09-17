def range_(*args):
    b = 0
    a = 0
    c = 1
    if len(args) == 1:
        a = args[0]
    elif len(args) == 2:
        b, a = args
    elif len(args) == 3:
        b, a, c = args
    else:
        print("the function gets maximum three arguments")

    y=1
    for i in args:
        if "." in str(i):
            x = str(i).split(".")
            if y <= len(x[1]):
                y = len(x[1])
    
    temp = []
    n = b
    while(n < a):
        temp.append(round(float(n),y))
        n += c
    
    print(tuple(temp))
print("*** New Range ***")
lit = list(map(float,input("Enter Input : ").split(" ")))

range_(*lit)
