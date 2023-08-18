# Task 7
# Գրել ֆունկցիա, որը տրված բնական թվի համար կվերադարձնի արդյոք այն պարզ է, թե ոչ։

def primeNum(N):
    if N == 1:
        return "N == 1"
    for i in range (2, N+1):
        if N % i == 0:
            return "number is not prime"
    
        return "number is prime"

entered_num = 11
print(primeNum(entered_num))
