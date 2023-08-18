# Task 1
# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {&#39;key1&#39;: 1, &#39;key2&#39;: 3, &#39;key3&#39;: 2}, {&#39;key1&#39;: 1, &#39;key2&#39;: 2}
# Expected output: key1: 1 is present in both x and y
def key_match_dict(x, y):
    for (key, value) in set(x.items()) & set(y.items()):
        if x[key] == y[key]:
            return key, value

inp_sample_dict1 = {"&#39;key1&#39;": 1, "&#39;key2&#39;": 3, "&#39;key3&#39;": 2}
inp_sample_dict2 = {"&#39;key1&#39;": 1, "&#39;key2&#39;": 2}
print(key_match_dict(inp_sample_dict1, inp_sample_dict2))
#============================================

# Task 2
# Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {&#39;Cierra Vega&#39;: 12, &#39;Alden Cantrell&#39;: 12, &#39;Kierra Gentry&#39;: 12, &#39;Pierre Cox&#39;: 12}
# Check all 12 in the dictionary.
# True
# Check all 10 in the dictionary.
# False
def dict_value_verify(dict_d):
    result = True
    lst_val = list(dict_d.values())[0]
    for key in dict_d:
        if dict_d[key] != lst_val:
            result = False
            break
    return result

inp_orig_dict = {"&#39;Cierra Vega&#39;": 12, "&#39;Alden Cantrell&#39;": 12, "&#39;Kierra Gentry&#39;": 12, "&#39;Pierre Cox&#39;": 12}
print(dict_value_verify(inp_orig_dict))
inp_orig_dict = {"&#39;Cierra Vega&#39;": 12, "&#39;Alden Cantrell&#39;": 12, "&#39;Kierra Gentry&#39;": 12, "&#39;Pierre Cox&#39;": 10}
print(dict_value_verify(inp_orig_dict))

#============================================


# Task 3
# Write a Python program to split a given dictionary of lists into lists of dictionaries.
# Original dictionary of lists:
# {&#39;Science&#39;: [88, 89, 62, 95], &#39;Language&#39;: [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{&#39;Science&#39;: 88, &#39;Language&#39;: 77}, {&#39;Science&#39;: 89, &#39;Language&#39;: 78}, {&#39;Science&#39;: 62, &#39;Language&#39;:
# 84}, {&#39;Science&#39;: 95, &#39;Language&#39;: 80}]
def split_dict(dict_d):
    res = [{key : value[i] for key, value in dict_d.items()} for i in range(4)]
    return res


inp_orig_dict = {"&#39;Science&#39;": [88, 89, 62, 95], "&#39;Language&#39;": [77, 78, 84, 80]}
print(split_dict(inp_orig_dict))

#============================================