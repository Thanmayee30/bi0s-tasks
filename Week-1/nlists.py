x=int(input())
inp_arr=[[input(),float(input())] for _ in range(0,x)]
inp_arr.sort(key=lambda k: (k[1],k[0]))
nameofstudents = [n[0] for n in inp_arr]
marksofstudents = [n[1] for n in inp_arr]
minvalueofmarks=min(marksofstudents)
while marksofstudents[0]==minvalueofmarks:
    marksofstudents.remove(marksofstudents[0])
    nameofstudents.remove(nameofstudents[0])    
for k in range(0,len(marksofstudents)):
    if marksofstudents[k]==min(marksofstudents):
        print(nameofstudents[k])
