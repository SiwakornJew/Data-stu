class funString():

    def __init__(self,string = ""):

      self.string=string
      

    def __str__(self):

       return 1

    def size(self) :
        self.sizeString = len(self.string)
        return len(self.string)
    
    def changeSize(self):
        self.changesize=''
        for x in range(len(self.string)) :
            if self.string[x] >='a' and self.string[x] <='z' :
                self.changesize+=chr(ord(self.string[x])-32)
            elif self.string[x] >='A' and self.string[x] <='Z' :
                self.changesize+=chr(ord(self.string[x])+32)
            else :
                self.changesize+=chr(ord(self.string[x]))

        return  self.changesize
    def reverse(self):
        rev=''
        for i in self.string:
            rev = i + rev

        return rev

       
    def deleteSame(self):
        self.str1 = [i for n, i in enumerate(self.string) if i not in self.string[:n]]
        deletstr=''.join([str(x) for x in self.str1])
        return deletstr



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())