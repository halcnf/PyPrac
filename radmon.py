import random
rand_list= []

def input_():
    start_range = int(input('Please enter the start range: '))
    end_range = int (input('Please enter the end range: '))
    how_many = int(input('Please enter the number of random numbers: '))
    return start_range, end_range, how_many

def rand_gen(start_range,end_range,how_many):
    for i  in range (0,how_many):
        rand_number = random.randint(start_range,end_range)
        print(rand_number)
        rand_list.append(rand_number)

start_range, end_range, how_many = input_()
rand_gen(start_range,end_range,how_many)

print(rand_list)
rand_list.sort()
print(rand_list)
