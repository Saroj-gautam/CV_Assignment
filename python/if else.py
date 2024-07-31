a=float(input("enter a:"))
# if(a%3==0):
#     print("multiple of 3")
# else:
#     print("not multiple of 3")
b=float(input("enter b:"))
operation_value=input("enter operation+ - * /  :")
if(operation_value=='+'):
 print(f"the sum of {a} and {b} is {a+b}")
elif(operation_value=='-'):
 print(f"the diff of {a} and {b} is {a-b}")
elif(operation_value=='*'):
 print(f"the mul of {a} and {b} is {a*b}")
elif(operation_value=='/'):
 print(f"the div of {a} and {b} is {a/b}")
 if(b==0):
  print("not defined")
else:
 print("enter valid operational_value")

