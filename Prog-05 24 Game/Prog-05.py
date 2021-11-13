# Prog-05: The 24 Game

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 
def calc(num1, operation, num2):
    if operation == '+': result = float(num1) + float(num2)
    elif operation == '-': result = float(num1) - float(num2)
    elif operation == '*': result = float(num1) * float(num2)
    else:
        if float(num2) == 0: result = math.inf
        else: result = float(num1) / float(num2)
    return result
#---------------------------------------------------------
nums = input('Enter 4 integers: ')
nums = nums.split()
cases = generate_all_combinations(nums, '+-*/')
for i in cases:
    if calc(calc(calc(i[0],i[1],i[2]),i[3],i[4]),i[5],i[6]) == 24:
        print('(','(',i[0],i[1],i[2],')',i[3],i[4],')',i[5],i[6],'= 24'); break
    elif calc(calc(i[0],i[1],calc(i[2],i[3],i[4])),i[5],i[6]) == 24:
        print('(',i[0],i[1],'(',i[2],i[3],i[4],')',')',i[5],i[6],'= 24'); break
    elif calc(calc(i[0],i[1],i[2]),i[3],calc(i[4],i[5],i[6])) == 24: 
        print('(',i[0],i[1],i[2],')',i[3],'(',i[4],i[5],i[6],')','= 24'); break
    elif calc(i[0],i[1],calc(calc(i[2],i[3],i[4]),i[5],i[6])) == 24:
        print(i[0],i[1],'(','(',i[2],i[3],i[4],')',i[5],i[6],')','= 24'); break
    elif calc(i[0],i[1],calc(i[2],i[3],calc(i[4],i[5],i[6]))) == 24:
        print(i[0],i[1],'(',i[2],i[3],'(',i[4],i[5],i[6],')',')','= 24'); break
else : print('No Solutions')