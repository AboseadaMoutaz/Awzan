from scale import Scale
from wazn import Wazn
import random

class AwzanGame:
    def __init__(self, index, min_weight= 1, max_weight = 50):
        self.index = index
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.scale1 = Scale("Important")
        self.scale2 = Scale("NotImportant")
        self.new_game()
        
    def random_query(self, n, end, start = 1):
        return list(range(start, n)) + list(range(n+1, end))

    def new_game(self):
        self.scale1 = Scale("Important")
        self.scale2 = Scale("NotImportant")
        range_numbers = list(range(self.min_weight, self.max_weight))
        print(range_numbers)
        random.shuffle(range_numbers)
        self.blue = Wazn("blue", range_numbers.pop())
        self.orange = Wazn("orange", range_numbers.pop())
        self.purple = Wazn("purple", range_numbers.pop())
        self.yellow = Wazn("yellow", range_numbers.pop())
        self.green = Wazn("green", range_numbers.pop())
        weights_info =[self.blue, self.orange, self.purple, self.yellow, self.green]
        random.shuffle(weights_info)
        choosen_ball = weights_info.pop()
        weights_weight =[self.blue.weight, self.orange.weight, self.purple.weight, self.yellow.weight, self.green.weight]
        weights_weight.sort()
        choosen_ball_index = weights_weight.index(choosen_ball.weight)
        print(weights_weight)
        print(choosen_ball.weight)
        print(choosen_ball_index)

        return " Choosen Weight to reveal is " + str(choosen_ball.color) + "\n the " + str(choosen_ball_index + 1) + " Heaviest\nWeight is " + str(choosen_ball.weight)

    
    def add_weight(self, scale, weight, is_left ):
        if scale == 1:
            self.scale1.add_weight(weight, is_left)
        else:
            self.scale2.add_weight(weight, is_left)

    def get_weight(self, first_letter):
        print(first_letter)
        print("------------")
        if first_letter == "b":
            return self.blue
        elif first_letter == "o":
            return self.orange
        elif first_letter == "g":
            return self.green
        elif first_letter == "y":
            return self.yellow
        elif first_letter == "p":
            return self.purple
        
    def get_scale_heavy(self, scale):
        if scale == 1:
            return self.scale1.get_scale_heavy()
        else:
            return self.scale2.add_weight()
    def get_scale_weights(self, scale):
        if scale == 1:
            return self.scale1.get_scale_weights()
        else:
            return self.scale2.get_scale_weights()



