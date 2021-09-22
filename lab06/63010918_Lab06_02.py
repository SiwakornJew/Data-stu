def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
def gensort(L, goodlist=[]):
    if len(L) == 0:
       return goodlist
    else:
       goodlist.append(int(Max(L)))
       L.remove(int(Max(L)))
       return gensort(L, goodlist)
s=[int(item) for item in input("Enter your List : ").split(',')]
#s =input("Enter your List : ").split(',')
#for i in range(len(s)):s[i]=int(s[i])
s=gensort(s)
print(f"List after Sorted : {s}")
