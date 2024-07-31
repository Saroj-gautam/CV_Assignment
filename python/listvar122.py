
# list_var1=[]
# list_var1=['a','p','p','l','e']
# print(list_var1)

# #adding the element in a list
# list_var1.append('Z')
# print(list_var1)
# print(list_var1.append(12))
# print(list_var1)
# print(list_var1[-1]) #print last element
# print(list_var1[1:3])
# list_var2=list('apple')
# print(list_var2)

# if[1,2,3,4]==[1,2,3,4]:
#     print("equal list")

#Reversing the list

# list_var3=[1,2,3,4]
# list_var3=list_var3[::-1]  #reverse order
# print(list_var3)

# #PALINDROME CHECK
# list_var4=list('121')
# list_var5=list_var4[::-1]
# if(list_var4==list_var5):
#     print("palindrome")
# else:
#     print("Not palindrome")




list_even=[]
list_odd=[]
num=float(input("enter a number:"))
if (num%2==0):
    list_even.append(num)
else:
    list_odd.append(num)

print("Even numbers are:",list_even)
print("Odd numbers are:",list_odd)
