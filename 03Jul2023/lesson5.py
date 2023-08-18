# Task 10
# Ticket numbers usually consist of an even number of digits. A ticket number is considered 
# lucky if the sum of the first half of the digits is equal to the sum of the second half.            
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set 
# types.
# Example:
# For n = 1230, the output should be:
# is_lucky(n) = True;
# For n = 239017, the output should be
# is_lucky(n) = False.

def is_lucky(n):
    n = str(n)
    sum1=0
    sum2=0
    if len(n) % 2 != 0:
        return "number is not even"
    for i in range (0, int(len(n)/2)):
        sum1 += int(n[i])
    for j in range (int(len(n)/2), int(len(n))):
        sum2 += int(n[j])
    if sum1 == sum2:
        return True
    else:
        return False

#n = 1230
#print(is_lucky(n))
n = 239017
print(is_lucky(n))

