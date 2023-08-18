# Task 11
# Given some integer, find the maximal number you can obtain by deleting exactly 
# one digit of the given number.
# ● For n = 152, the output should be
# deleteDigit(n) = 52;
# ● For n = 1001, the output should be
# deleteDigit(n) = 101.


def deleteDigit(n):
    n_str = str(n)
    n_len = len(n_str)
    n_max = 0
    n_tmp = ""
    print(n_str[0:n_len])
    print(n_str[2::])
    print(n_str[1::])
    print(n_str[-n_len::])
    print(n_len)
    print(n_max)
    print(n_tmp)
    for i in range (0, n_len):
        print(i)
        print(n_tmp)
        if int(n_str[(i+1)::]) > int(n_max):
            n_max = n_str[(i+1)::]
            print(int(n_max), "a")
            print(int(n_str[(i+1)::]), "b")
        return n_max
    #print(n_num)


n = 1001
print(deleteDigit(n), "x")
# ● For n = 152, the output should be
# deleteDigit(n) = 52;
# ● For n = 1001, the output should be
# deleteDigit(n) = 101.
