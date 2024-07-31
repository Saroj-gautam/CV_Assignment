# fruit_dictionary={}
# n_fruits=int(input("enter how many fruits to register:"))
# for i in range(n_fruits):
#     fruit_name=input(f"enter name of {i+1} fruit:")
#     fruit_color=input(f"enter name of {fruit_name} color:")
#     fruit_dictionary[fruit_name]=fruit_color


# print (fruit_dictionary)












#convert list value into dictionary

# fruits=['apple','mango','banana']
# colors=['red','green','yellow']

# for i,j in zip(fruits,colors):
#     print(i,j)
# dictionary_value=dict(zip(fruits,colors))
# print('\n')
# print(dictionary_value)


#WAP to create which holds students and their aggregate percentage in key and value respectively
#Test case1: enter name of any student and his percentage will be shown
#test case 2: handel when 2 students have same name as well
#test case 3: Include 2 percentage 1 academic percentage and another attendance percentage

#testcase 1 solution
# student_information={}
# n_students=int(input("enter how many students to be stored:"))
# for i in range(n_students):
#     student_name=input(f"enter{i+1} Student Name:")
#     student_information[student_name]=input(f"enter {student_name}'s Percentage:")
# print(student_information)

# search_student=input("enter student name to search:")
# if search_student in student_information.keys():
#     print(student_information[search_student])
# else:
#     print("student not found")

list_student=[]
list_percentage=[]
n_students=int(input("enter how many students to be stored:"))
for i in range (n_students):
    student_name=input(f"enter{i+1} Student Name:")
    list_student.append(student_name)
    per=input(f"enter {student_name}'s Percentage:")
    list_percentage.append(per)
print(list_student)
print("\n")
print(list_percentage)

newlist=[]
duplist=[]

for i in list_student:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)

print("list of duplicates",duplist)
print("unique item lise", newlist)

counter=1
for idx in range(len(list_student)):
    if list_student[idx] in duplist:
        list_student[idx]=list_student[idx]+str(counter)
        counter +=1

print(list_student)
student_information=dict(zip(list_student,list_percentage))
print(student_information)




#test case 2
# list_even=[]
# list_odd=[]
# num=float(input("enter a number:"))
# if (num%2==0):
#     list_even.append(num)
# else:
#     list_odd.append(num)

# print("Even numbers are:",list_even)
# print("Odd numbers are:",list_odd)



