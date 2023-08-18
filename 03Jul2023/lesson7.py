# Task 11
#  Given some integer, find the maximal number you can obtain by deleting exactly 
# one digit of the given number.
# ● For n = 152, the output should be
# deleteDigit(n) = 52;
# ● For n = 1001, the output should be
# deleteDigit(n) = 101.

def deleteDigit(N):
    max_val = 0
    str_n = str(N)
    for j in range(len(str_n)):
        tmp_str = str_n[:j] + str_n[j+1:]
        if int(tmp_str) > max_val:
            max_val = int(tmp_str)
    return max_val

inp_num = 1001
res = deleteDigit(inp_num)
print(f"the max number by deleting one digit from {inp_num} is: {res}")