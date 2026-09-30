from typing import List

def read_integers() -> List[int]:
    int_input_lst = input().split(',')
    for i in range(len(int_input_lst)):
        int_input_lst[i] = int(int_input_lst[i])
    return int_input_lst

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
