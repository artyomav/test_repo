#Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
#ցուցակի ամենամեծ էլեմենտը։
def list_max_item(list_nums):
    max_value = list_nums[0]
    for i in range (0, len(list_nums)):
        if list_nums[i] > max_value:
            max_value = list_nums[i]

    return max_value

orig_list = [-12, -100, 45, 181, 673, 213, 412, 77, 33, 50, 99, -33]
max_num = list_max_item(orig_list)
print(f"{orig_list} list max value is: {max_num}")