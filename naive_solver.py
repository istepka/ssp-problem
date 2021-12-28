import  numpy as np
from typing import List, Tuple
from generator import Generator
from global_functions import create_all_posible_subsets_from_set, check_if_all_sets_sum_to_T, are_overlapping
'''
The goal is to find whether set can be divided into N non-overlapping subsets, each of which sums to a given T.

If this is not possible, then algorithm should propose achievable number (closest to N) of non-overlapping subsets.
'''
T = 6
HIGH = 10
LOW = 1
SET_LEN = 4


class NaiveSolver:
    '''Naive approach solver. Finds optimum in O(n*2^n)time.'''

    def naive_exponential_solution(self, start_set, T) -> Tuple[int, List[List[int]]]:
        '''Check whether set contains any subset of integers that sums up to t.\n
        Return maximum number of subsets, list of subsets.'''

        #Generate all possible subsets and check their sums
        n, sets = create_all_posible_subsets_from_set(start_set)
        print('Number of unique subsets:', n)

        #Variables with best solution
        highest_number_of_valid_subsets = -1
        best_set_of_subsets = list()

        iters = 2**len(sets)
        print(f'Naive algorithm has to perform {iters} iterations [2^(number_of_subsets)]')
        #Validate all possible subsets
        for i in range(1, iters):
            mask = bin(i)[2:]
            mask = '0'*(len(sets) - len(mask)) + mask
            local_list_of_sets = list(map(lambda x: x[1], filter(lambda x: x[0] == '1', zip(mask, sets))))

            #Check if subsets non-overlap and sum to T, then if solution is better than previous, save
            if are_overlapping(local_list_of_sets) == False and check_if_all_sets_sum_to_T(local_list_of_sets, T) == True:
                
                if highest_number_of_valid_subsets < len(local_list_of_sets):
                    highest_number_of_valid_subsets = len(local_list_of_sets)
                    best_set_of_subsets = local_list_of_sets

            if i % 1000000 == 0:
                print(f'Iteration nr. {i//1000000}M')

        if highest_number_of_valid_subsets == -1:
            print(f'There is no any subsets that sum to {T}.')
        else:
            print(f'Found solution with {highest_number_of_valid_subsets} subsets, each of which sums up to {T}\n \
                List of found subsets: {best_set_of_subsets}')
       



    


if __name__ == '__main__':
    print('Running naive solver test case')
    set = Generator().generate_set(SET_LEN,LOW,HIGH)
    print("Generated set: ", set)
    NaiveSolver().naive_exponential_solution(set, T)
    #print( NaiveSolver().are_overlapping([  [1, 2, 3], [4,5,6], [12,14,7], [77] ]))
    

