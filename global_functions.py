from typing import List, Tuple


def create_all_posible_subsets_from_set(self, set) -> Tuple[int, List[List[int]]]:
    '''Generate all (non-empty) possible subsets for a given set.\n
    Retrun number of subsets, list of subsets.'''
    all_subsets = list() 
    for i in range(0, int('0b'+'1'*len(set), 2)+1):
        mask = bin(i)[2:]
        mask = '0'*(len(set) - len(mask)) + mask
        subset = list(map(lambda x: x[1], filter(lambda x: x[0] == '1', zip(mask, set))))
        if len(subset) > 0:
            all_subsets.append(subset)
    return len(all_subsets), all_subsets

def check_if_all_sets_sum_to_T(self, list_of_sets, T) -> bool:
    for set in list_of_sets:
        if sum(set) != T:
            return False
    return True

def are_overlapping(self, list_of_sets) -> bool:
    '''Check if two sets are overlapping. O(n^4). Can be easily optimized to reduce complexity.'''
    for i in range(len(list_of_sets)):
        for item in list_of_sets[i]:
            for j in range(i+1, len(list_of_sets)):
                if item in list_of_sets[j]:
                    return True
    return False