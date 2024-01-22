d={}
txt="This is your To-do-List"
x = txt.center(20)
print(x)
k=int(input("enter the no. of tasks: "))
def assi():
  for i in range(k):
    d[i+1]=input()
def dele():
  l=int(input("If you want to delete a task enter '0' or if you want to add a task entre '1' "))
  if l==0:
    a=int(input("dele"))
    del d[a]
    print(d)
    dele()
  if l==1:
    p=int(input("enter the no. of items you want to add "))
    len(d)
    for i in range(p):
      d[i+k+1]=input()
    print(d)
    dele()
assi()
print(d)
dele()
print(d)