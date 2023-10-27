import random

class WeightInitializer:
    def __init__(self):
        self.strart = False

    def initialize(self,min, max):
        range_numbers = list(range(min, max))
        random.shuffle(range_numbers)
        choosen_numbers = []
        for i in range(0,5):
            choosen_numbers.append(range_numbers.pop())
        choosen_numbers_copy = choosen_numbers.copy()
        random.shuffle(choosen_numbers_copy)
        choosen_number_to_reveal = choosen_numbers_copy.pop()
        choosen_numbers_copy_sort = choosen_numbers.copy()
        choosen_numbers_copy_sort.sort()
        choosen_number_index = choosen_numbers_copy_sort.index(choosen_number_to_reveal)
        print(choosen_numbers, choosen_number_to_reveal, choosen_number_index)
        return choosen_numbers, choosen_number_to_reveal, choosen_number_index


