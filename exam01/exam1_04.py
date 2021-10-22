print("*** String Rotation ***")
lst1,lst2= map(list,input('Enter 2 strings : ').split())
temp1=lst1
temp2=lst2
round=0#
while(temp1 != lst1 or temp2 != lst2) or round< 1:
    temp1 =temp1[-1:] + temp1[:-1]
    temp2 =temp2[1:] +temp2[:1]
    round+=1
    if round < 6 or (temp1 == lst1 and temp2 == lst2):
        str1 =''.join(temp1)
        str2 =''.join(temp2)
        print(f"{round} {str1} {str2}")
    elif round ==6:
        print(" . . . . . ")
print(f"Total of  {round} rounds.")