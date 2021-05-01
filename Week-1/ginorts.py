x = input()
def number(n):
    if n.isdigit():
        if int(n)%2 ==0:
            return True
        else: return False
    else: return True
print (*sorted(x,key = lambda n:(n.isdigit(),number(n),n.isupper(),n)),sep='')
