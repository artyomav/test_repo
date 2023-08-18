#Task 9
#Գրեք Python ֆուկցիա որը ստանում է list եւ պետքա գտնել նրա երկարությունը առանց
#len() ֆունկցիա֊ի օգտագորձմամբ

def list_len(inp_list):
    i = 0
    for lst in inp_list:
        i +=1
    return i 


inp = [-12, "A", 45, "D", 673, "F", "C", "e", 33, 50, 99, -33, "acb"]
list_lenght = list_len(inp)
print(list_lenght)