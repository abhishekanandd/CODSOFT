import random
import string
len=int(input("Enter the length"))
a=''
b=string.ascii_letters+string.punctuation+string.digits+string.printable
c=string.ascii_letters+string.digits
print('''Enter the strenght of the password 
for weak enter '0' and for strong enter '1' ''')
str=int(input())
if str ==1:
    for i in range(len):
        s1=random.choice(b)
        a+=s1
if str ==0:
    for i in range(len):
        s1=random.choice(c)
        a+=s1
print(a)