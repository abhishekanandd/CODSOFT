a=float(input("enter 1st number "))
c=(input("enter operator "))
b=float(input("enter 2nd number "))
if((c=='/')):
    if(b==0):
        print("error")
    print("division is ",(a/b))
elif(c=='+'):
    print("sum is ",a+b)
elif(c=='*'):
    print("product is ",a*b)
elif(c=='-'):
    print("stubstraction of ",a,"and ",b,"is ",a-b)
elif(c=='**'):
    print(a,"^",b,"equles",a**b)
elif(c=='%'):
    print("mod  of ",a,"and ",b,"is ",a%b)
elif(c=='//'):
    if(b=='0'):
         print("zero is not allowed in division")
    print("floor division  of ",a,"and ",b,"is ",a//b)
else:
    print("the output for operater that you have entered is not developed")

