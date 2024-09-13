op=input("enter the operator of choice (+ - * /): ")
n1=float(input("enter the first number: "))
n2=float(input("enter the second number: "))

if op=="+":
    answer=n1+n2
    print ((answer))

elif op=="-":
    answer=n1-n2
    print (round(answer))

elif op=="*":
    answer=n1*n2
    print (round(answer))

elif op=="/":
    answer=n1/n2
    print (round(answer))

else :
    print("operator is invalid ")
