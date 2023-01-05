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
def merge(dict,dict2):
    return(dict2.update(dict)) # Python code to merge dict using update() method

dict2={
    'lmn':500,
    'opq':300,
    'ers':200
}

merge(dict,dict2)
print(dict2)

# clear() – Remove all the elements from the dictionary
# copy() – Returns a copy of the dictionary
# get() – Returns the value of specified key
# items() – Returns a list containing a tuple for each key value pair
# keys() – Returns a list containing dictionary’s keys
# pop() – Remove the element with specified key
# popitem() – Removes the last inserted key-value pair
# update() – Updates dictionary with specified key-value pairs
# values() – Returns a list of all the values of dictionary
