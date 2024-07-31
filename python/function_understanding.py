'''''
#none reyurn type function
def function_name(a):
    print(a)

z=function_name("Hello World")
print(z)

'''
# def return_type_function(a):
#     return a*5

# output_from_function=return_type_function(10)
# print(output_from_function)

#2 inputs and 2 outputs

# def two_inputs_two_output(a,b):
#     return a*5, b*6
# output_1_output_2=two_inputs_two_output(1,5)
# print(output_1_output_2)

# output_3=two_inputs_two_output(1,3)
# print(output_3)


#Multiplication Table

# def multiplication_table(multiflication_number=2, multiplication_upto=10):
#      for i in range (1,multiplication_upto+1):
#          print(f"{multiflication_number} * {i} = {multiflication_number*i}")
# multiplication_table()
              

#write a function name even checker which accept 1 argument checks if its even 
#if even return true else return false
''''
def even_checker(a):
   if (a%2==0):
      return True
   else:
      return False
num=int(input("enter any number:"))
print(even_checker(num))


'''
# How to set default value in function

# def complex_function(a=1,b=1,c=1,d=1,e=1,f=1,g=1,h=1):
#     print(a,b,c,d,e,f,g,h)

# complex_function(15)


#Args and Kwargs
#def get_average(*args):
#    print(args)
#    args=list(args)
#    return sum(args)/len(args)
# average_number=get_average(1,2,3,4,5)
# print(average_number)

# def get_average(*args):
#    args=list(args)
#    return sum(args)/len(args)
# average_number=get_average(1,2,3,4,5)
# print(average_number)


# def get_avg(*args):
#     args=list(args)
#     return sum(args)/len(args)

# list_num=[]
# n=int(input("how many number:"))
# for i in range(n):
#     a=int(input("enter a number{i}:"))
#     list_num.append(a)
# print(list_num)
# avg=get_avg(*list_num)
# print(avg)

# def get_average(*args):
#     args=list(args)
#     print(f'Original argument:{args}')
#     args=args[0]
#     print(f'Final args:{args}')
#     return sum(args)/len(args)

# all_number=input('enter all numbers seperated by comma:')
# print(f'Original string:{all_number}')
# all_number=all_number.split(',')
# print(f'Converting to list:{all_number}')
# all_number=[int(i) for i in all_number]
# print(f'Converting to int list:{all_number}')
# get_average=get_average(all_number)
# print(f'Average Calculated as {get_average}')

#Kwargs: keywords arguments
#convert into dictionary

def complex_function_2 (**kwargs):
        print(kwargs)
complex_function_2(student_name='saroj', student_marks='60', attendence='55')















