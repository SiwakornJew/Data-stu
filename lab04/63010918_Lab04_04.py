from queue import Queue

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items =Queue
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return int(len(self.items))
    def __str__(self) :
        return str(self.items)
    def getvalue(self,i):
        return self.items[i]
    def isFull(self) :
        return self.items.full()
def cheakA(str):
        if str == "0":
                return 'Eat'
        if str == "1":
                return 'Game'
        if str == "2":
                return 'Learn'
        if str == "3":
                return 'Movie'
def cheakL(str):
        if str == "0":
                return 'Res.'
        if str == "1":
                return 'ClassR.'
        if str == "2":
                return 'SuperM.'
        if str == "3":
                return 'Home'
list = input("Enter Input : ").split(",")
mQuene=Queue()
yQuene=Queue()
mActivity=Queue()
yActivity=Queue()

score =0
for i in list:
    l =i.split(' ')
    cheakM =str(l[0]).split(":")
    cheakY =str(l[1]).split(":")
    if cheakM==cheakY:
        score+=4
    elif cheakM[1] == cheakY[1]:
        score+=2
    elif cheakM[0] == cheakY[0]:
        score+=1
    else:
        score-=5
    mQuene.enQueue(l[0])
    yQuene.enQueue(l[-1])
    x=cheakA(cheakM[0])+':'+cheakL(cheakM[1])
    mActivity.enQueue(x)
    x=cheakA(cheakY[0])+':'+cheakL(cheakY[1])
    yActivity.enQueue(x)

print("My   Queue = "+str(mQuene).replace("\'",'').replace("[",'').replace("]",''))
print("Your Queue = "+str(yQuene).replace("\'",'').replace("[",'').replace("]",''))
print("My   Activity:Location = "+str(mActivity).replace("\'",'').replace("[",'').replace("]",''))
print("Your Activity:Location = "+str(yActivity).replace("\'",'').replace("[",'').replace("]",''))

if score >=7:
    print("Yes! You're my love! : Score is "+str(score)+'.')
elif score >0:
    print("Umm.. It's complicated relationship! : Score is "+str(score)+'.')
else :
    print("No! We're just friends. : Score is "+str(score)+'.')