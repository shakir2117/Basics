dict={
    'abc':100,
    'def':200,
    'ghi':200
}

print("the org Dictionary is: ", str(dict))


# def returnSum(myDict):
#     list = []
#     for i in myDict:
#         list.append(myDict[i]) #add my dict to list
#     final = sum(list)
#
#     return final
#
# print("Sum :", returnSum(dict))

#remove key

del dict['abc']
print(f"the dictionary after the deletion of key {dict} :")

#add key
dict['abc']=100
print(f"the dictionary after the addtion of key{dict} ")

#merge dict




