d={}
print("This is phonebook")
f='@'
k=int(input("enter the no. of contacts you want to add: "))
def assi():
  for i in range(k):
    name=input("enter {} name: ".format(i+1))
    number=int(input("enter number: "))
    email=input("enter email: ")
    address=input("enter address: ")
    strnum=str(number)
    a="number-"+strnum+", "
    b="email-"+email+", "
    c="address-"+address+" "
    strnum=str(number)
    all=a+b+c
    d[name]=all
    for i in range(100000):
      if f in email:
        break
      else:
        print("enter a valid email")
        new_email=input("enter the email again: ")
        email=new_email
    if len(strnum)!=10:
        while len(strnum)!=10:
           print("enter a valid number")
           number1=int(input("enter the number again: "))
           number=number1
           strnum=str(number)
  for key, value in d.items():
    print(key, ' : ', value)
def dele():
  l=int(input('''If you want to delete a number enter '0'
If you want to add a number entre '1'
If you want end enter '2' '''))
  if l==0:
    a=int(input("dele"))
    del d[a]
    print(d)
    dele()
  elif l==1:
    p=int(input("enter the no. of items you want to add "))
    len(d)
    for i in range(p):
      d[i+k+1]=input()
    print(d)
    dele()
  elif l==2:
    print(end="")
assi()
dele()
