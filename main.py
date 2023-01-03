a = 20  # int
b = 30.5  # Float
c = True  # boolean
d = "hello world"  # string
e = '''hello world this is multi line 
string'''  # this is multi line string
f = d + e
x = a + b

print(x)
# print data types
print('a is of type', type(a))
print('b is of type', type(b))
print('c is of type', type(c))
print('a is of type', type(d))

age = 20
name = "shakir"

print('{0} was the age off {1}'.format(age, name))

# + plus
# - minus
# * multiply
# ** power
print(2 ** 3)  # two raise to power of three
# / divide
# % modulus
# // floor division
p = 4 / 3
print("divide", p)
q = 3 % 4
print("mod", q)

r = 3 // 4
print("floor division", r)

# & (bit wise AND)
# | (bit-wise OR)
# ^ (bit-wise XOR)
# ~ (bit-wise invert)


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

list = [1,2,3,4,5,6,7,8,9,0]
k=''
print(list)
for i in list:
    print(i)
    k+=','+str(i)
print(k)




