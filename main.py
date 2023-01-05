# a = 20  # int
# b = 30.5  # Float
# c = True  # boolean
# d = "hello world"  # string
# e = '''hello world this is multi line
# string'''  # this is multi line string
# f = d + e
# x = a + b
#
# print(x)
# # print data types
# print('a is of type', type(a))
# print('b is of type', type(b))
# print('c is of type', type(c))
# print('a is of type', type(d))
#
# age = 20
# name = "shakir"
#
# print('{0} was the age off {1}'.format(age, name))
#
# # + plus
# # - minus
# # * multiply
# # ** power
# print(2 ** 3)  # two raise to power of three
# # / divide
# # % modulus
# # // floor division
# p = 4 / 3
# print("divide", p)
# q = 3 % 4
# print("mod", q)
#
# r = 3 // 4
# print("floor division", r)
#
# # & (bit wise AND)
# # | (bit-wise OR)
# # ^ (bit-wise XOR)
# # ~ (bit-wise invert)


# if,else,elif,while,for

#While loop
# a=20
# running = True
#
# while running:
#     # print("@@",a)
#     get_input_value = int(input("Enter the number"))
#     if get_input_value > 20:
#         running = False
#     else:
#         print("print the number you entered is", get_input_value)
# print("done")

#For Loop
# for i in range(0,10+1):
#     if i==5:
#         print("this if inside if")
#     else:
#         print(i)

# list = [1,2,3,4,5,6,7,8,9,0]
# k=''
# print(list)
# for i in list:
#     print(i)
#     k+=','+str(i)
# print(k)


# def helloworld(a,b):  # defining the function with local variable
#     print("i am hello world function") #creation a argument inside function
#     c=a+b
#     print("sum of a+b is :",c)
#     return c #return value of c
#
#
# x=helloworld(4,6) # calling the function
# to call the function with the print statement the variable like x is assigned to the function helloworld


#list

# list1=['apple','orange','mango','chiku']
# list2=[1,2,3,4,5,6,7,8,9]
#
# print("list:",list1)  #print list
# print("lenght of list:",len(list1)) #length of the list
#
# for i in list1:
#     print(i)
# list1.append('banana') # add element in list
# print("new list:",list1)
# list1.sort() # sort list alphabetically
# print('sorted list:',list1)
#
# del list1[0]# deleted element of list
# print("deleted list 1st element:",list1)
# x="apple" in list1
# print("apple is in list 1",x)
# y="grapes" in list1
# print("apple is in list 1",y)
#
# # tuple
# tuple1=('apple','orange','mango','chiku')
# print(tuple1)
# print(len(tuple1))
# print(f"the length of {tuple1} is {len(tuple1)}") # print lenth and truple in print using "f" string


#dictionary

dict1={
    'name': 'shakir',
    'age': 21,
    'email':'shakirchoudhary2117@gmail.com'
}
print(f"this is the first dictionary: {dict1}")
print(f"this is the name in the list: {dict1['name']}")
dict1['name']='dheren'
print(f'madified deict1{dict1}')
for name,age in dict1:
    print({0},{1}.format(name,age))

# string operation
# string1="the is a donkey on the moon"
# print(string1.startswith("the"))
# print(string1.find("donkey"))







