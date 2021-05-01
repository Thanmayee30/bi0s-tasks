value = input('');
palin = 0
x=0
for i in value.split():
  
  temp_val=int(i)
  reverse=0
  number=int(i)
  while(number>0):
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
  if(temp_val == reverse):
    palin=palin+1
  
  if(int(i)<=0):
      x=x+1
      break
if(palin>0 and x==0):
    print(True)
else:
    print(False)