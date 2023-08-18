# Task 1
# Write a Python program to find the length of a dictionary of values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

def dict_len(dict_data):
    new_dict = {}
    for key, value in dict_data.items():
        key = value
        new_dict.update({key:len(key)})
    return new_dict


orig_dict_data = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print(f"Length of dictionary values: {dict_len(orig_dict_data)}")

orig_dict_data = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print(f"Length of dictionary values: {dict_len(orig_dict_data)}")


# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

def key_value_pairs(lst_data):
    new_dict = {}
    for i in lst_data:
        if i[0] in new_dict:
            new_dict[i[0]].append(i[1])
        else:
            new_dict[i[0]] = [i[1]]

    return new_dict


orig_lst_data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(f"Grouping a sequence of key-value pairs into a dictionary of lists: {key_value_pairs(orig_lst_data)}")


# Write a Python program to convert more than one list to a nested dictionary.
# Original lists:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

def nested_dict(lst_d1, lst_d2, lst_d3):
    new_lst = []
    for i in range(0, len(orig_lst1)):
        new_lst.append({orig_lst1[i]:{orig_lst2[i]:orig_lst3[i]}})
    return new_lst

orig_lst1 = ['S001', 'S002', 'S003', 'S004']
orig_lst2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
orig_lst3 = [85, 98, 89, 92]

print(nested_dict(orig_lst1, orig_lst2, orig_lst3))

# Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

def drop_empty_dict(dict_d):
    new_dict = {}
    for key, value in dict_d.items():
        if value is None:
            pass
        else:
            new_dict.update({key:value})
    return new_dict

orig_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
print(drop_empty_dict(orig_dict))


# Task 5
# Write a program in Python to count the occurrence of a specific value in a list.
# Hint 1
# a = [1,3,3,4,3,2,3]
# Input: 3
# Expected Output
# 3 occurs 4 time

def value_count(lst1, N):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] == N:
            cnt +=1
    return cnt
        

a = [1,3,3,4,3,2,3]
inp_num = 3
print(f"{inp_num} occurs {value_count(a, inp_num)} time")


# Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# def top_three_items(dict_d):
#     top3_dict = {}
#     for key, value in dict_d.items():
#         top3_dict.update({key:max(dict_d.values())})
#         #dict_d.pop(top3_dict[key])
#         print(top3_dict)
        


# inp_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# print(top_three_items(inp_dict))

# Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: {{'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}
def two_lists_dict(lst1, lst2):
    new_dct = {}
    for i in range(0, len(lst1)):
        new_dct.update({lst1[i]:{lst2[i]}})
    return new_dct


inp_lst1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
inp_lst2 = [1, 2, 2, 3]
print(two_lists_dict(inp_lst1, inp_lst2))



# Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all 12 in the dictionary.
# True
# Check all 10 in the dictionary.
# False

# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y