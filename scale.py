from wazn import Wazn

class Scale:
    def __init__(self, name):
        self.name = name
        self.left= []
        self.right = []

    def add_weight(self, weight, is_left):
        if is_left:
            self.left.append(weight)
        else:
            self.right.append(weight)


    def get_scale_heavy(self):
        left_total = 0
        for i in self.left:
            left_total += i.weight
        right_total = 0
        for i in self.right:
            right_total += i.weight
        if left_total > right_total:
            return "left"
        else:
            return "right"
    
    def reset_scale (self):
        self.left= []
        self.right = []

    def get_scale_weights(self):
        left_weights= "Left Weights are "
        for i in self.left:
            left_weights += str(i.color) + " + "
            print(i)
        
        right_weights= "Right Weights are "
        for i in self.right:
            right_weights += str(i.color) + " + "
            print(i)

        print(left_weights + right_weights)
        return left_weights + "\n" + right_weights


