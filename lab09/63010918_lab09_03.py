def drome(lst):
    maxtoMin = True
    minToMax = True
    unique = True
    same = True
    temp = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            maxtoMin = False
        if lst[i] > lst[i+1]:
            minToMax = False
        if lst[i] in temp:
            unique =False
        if lst[i] != lst[i+1]:
            same = False
        temp.append(lst[i])
    if lst[len(lst)-1] in temp:
        unique = False

    if same:
        return "Repdrome"
    elif minToMax and unique:
        return "Metadrome"
    elif minToMax and not unique:
        return "Plaindrome"
    elif maxtoMin and unique:
        return "Katadrome"
    elif maxtoMin and not unique:
        return "Nialpdrome"
    else:
        return "Nondrome"

in_lst = list(map(int, input("Enter Input : ")))
print(drome(in_lst))
