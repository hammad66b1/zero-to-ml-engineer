num= float(input("Enter a number 1: "))
num2= float(input("Enter a number 2: "))
op= input("Choose an operator i.e write it down from +, -, x, /")
res=0
incorrect=False
if op=="+":
    res= num+num2
elif op=="-":
    res=num-num2
elif op=="x":
    res=num*num2
elif op=="/":
    if num2!=0:
     res=num/num2
    else:
        incorrect=True
     
else:
    print("Incorrect symbol entered")
if incorrect==False:
 print(f"Your Answer is: {res}")
else:
    print("Not possible")