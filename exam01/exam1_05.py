class MyInt :
    def __init__(self,num):
        self.num=num
    def __str__(self) :
        return str(self.num)
    def __add__(self,x):
        return self.num+ x.num + (self.num+x.num)//2
    def toRoman(self):
        num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman= ''
        temp=self.num
        while temp > 0:
            for i, r in num_map:
                while temp >= i:
                    roman += r
                    temp-= i
        return roman





print(" *** class MyInt ***")
num1,num2 =[int(i) for i in input("Enter 2 number : ").split()]
x=MyInt(num1)
y=MyInt(num2)

print(f"{x} convert to Roman : {x.toRoman()}")
print(f"{y} convert to Roman : {y.toRoman()}")
print(f"{x} + {y} = {x + y}")