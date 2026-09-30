def add_two_numbers() -> int:
    int_input_lst = input().split(',')
    for i in range(len(int_input_lst)):
        int_input_lst[i] = int(int_input_lst[i])
    return sum(int_input_lst)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
