d={}
txt="This is phonebook"
print(txt)
k=int(input("enter the no. of contacts you want to add: "))
def assi():
  for i in range(k):
    name=input("enter {} name: ".format(i+1))
    number=int(input("enter number: "))
    d[name]=number
    s=str(number)
    if len(s)!=10:
        while len(s)!=10:
           print("enter a valid number")
           number=int(input("enter number: "))
           d[name]=number
           s=str(number)
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
print(d)
dele()