my_Sol =open("sol.txt","r")
solExam=my_Sol.read()
listSOl =solExam.split()
my_Exam =open("exam.txt","r")
exam=my_Exam.read()
listExam= exam.split('\n')
listStd =[]
listCount=[0,0,0,0,0,0,0,0,0,0]
countn=0
for i in listExam:
    a=i.split()
    countn+=1
    count=0
    for y in range(10):
        if listSOl[y] == a[y]:
            listCount[y]=listCount[y]+1
            count=count+1
        if y==9:
            listStd.append(count)             
print("Student score: ")
print(listStd)
for i in range (len(listCount)):
    value ="{:.2f}".format(listCount[i]/countn)
    print(f"Question {i+1} :{value}")
max=max(listCount)
min=min(listCount)
hard=''
easy=''
for i in range(len(listCount)):
    if listCount[i] ==max:
        easy +=' '+ str(i+1)
    if listCount[i] ==min:
        hard +=' '+ str(i+1)
print(easy)
print(hard)