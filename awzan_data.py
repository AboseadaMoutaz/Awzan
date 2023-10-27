from weight_initializer import WeightInitializer
import pandas as pd
from colors import Colors
from pathlib import Path

class AwzanData:
    def __init__(self):
        self.debug = False
        self.weights = None
        self.scale1_operations = None
        self.scale2_operations = None
        self.choosen_info = None

        my_file = Path("weights.csv")
        if my_file.is_file():
            self.weights = pd.read_csv("weights.csv")
            self.scale1_operations = pd.read_csv("scale1_operations.csv")
            self.scale2_operations = pd.read_csv("scale2_operations.csv")
            self.choosen_info = pd.read_csv("choosen.csv")

    def reset(self, min , max):
        weightInitializer = WeightInitializer()
        self.choosen_numbers, self.choosen_number_to_reveal, self.choosen_number_index = weightInitializer.initialize(min, max)
        colors = Colors()
        self.weights = pd.DataFrame(data={'weight': [self.choosen_numbers]})
        self.scale1_operations = pd.DataFrame(data={'left_d': ["0,0,0,0,0"], 'left_t': [0], 'right_d': ["0,0,0,0,0"], 'right_t': [0]})
        self.scale2_operations = pd.DataFrame(data={'left_d': ["0,0,0,0,0"], 'left_t': [0], 'right_d': ["0,0,0,0,0"], 'right_t': [0]})
        self.weights.to_csv("weights.csv", index=False)
        self.scale1_operations.to_csv("scale1_operations.csv", index=False)
        self.scale2_operations.to_csv("scale2_operations.csv", index=False)
        index = self.choosen_numbers.index(self.choosen_number_to_reveal)
        colors = Colors()
        stri = 'Choosen color to reveal = ' + str(colors.colors[index]) + "\n weight is " + str(self.choosen_number_to_reveal) + "\n it is the " + str(self.choosen_number_index + 1) + " heaviest."
        stri_save = pd.DataFrame(data={'choose': [stri]})
        stri_save.to_csv("choosen.csv", index=False)
        self.choosen_info = pd.read_csv("choosen.csv")

    def get_reset_info(self):
        return self.choosen_info.iloc[[len(self.choosen_info.index)-1]]['choose'].values[0]

    

    def get_scale_hand_count(self, scale , is_left):
        last_row = None
        value = None
        if scale == 0:
            last_row = self.scale1_operations.iloc[[len(self.scale1_operations.index)-1]]
        else:
            last_row = self.scale2_operations.iloc[[len(self.scale2_operations.index)-1]]
        
        if is_left:
            value = last_row['left_d'].values[0]
        else:
            value = last_row['right_d'].values[0]
        print(value)
        print(value[1])
        value = str(value)
        value = [eval(i) for i in value.replace('[','').replace(']','').split(',')]
        return value
    
    def get_scale_hand_total_count(self, scale , is_left):
        last_row = None
        value = None
        if scale == 0:
            last_row = self.scale1_operations.iloc[[len(self.scale1_operations.index)-1]]
        else:
            last_row = self.scale2_operations.iloc[[len(self.scale2_operations.index)-1]]
        
        if is_left:
            value = last_row['left_t'].values[0]
        else:
            value = last_row['right_t'].values[0]
        return value
    
    def get_scale_hand_total_dataframe(self):

        scale1_total = self.scale1_operations.loc[:,["left_t","right_t"]]
        scale2_total = self.scale2_operations.loc[:,["left_t","right_t"]]
        return scale1_total, scale2_total
    
    def add_scale_weight(self, scale, left, right ):
        weights_string = self.weights.iloc[[len(self.weights.index)-1]]['weight'].values[0].replace('[','').replace(']','').split(',')
        weights = [eval(i) for i in weights_string]
        left_weight = 0
        right_weight = 0
        left_new = []
        right_new = []
        old_left = self.get_scale_hand_count(scale, True)
        old_right = self.get_scale_hand_count(scale, False)

        for i in range(0, len(left)):
            left_new.append(old_left[i] + left[i])
            right_new.append(old_right[i] + right[i])

        for i in range(0, len(left)):
            left_weight += left_new[i] * weights[i]
            right_weight += right_new[i] * weights[i]

        if scale == 0:
            self.scale1_operations.loc[len(self.scale1_operations.index)]=[left_new , left_weight, right_new, right_weight]
            self.scale1_operations.to_csv("scale1_operations.csv", index=False)
        else:
            self.scale2_operations.loc[len(self.scale1_operations.index)]=[left_new , left_weight, right_new, right_weight]
            self.scale2_operations.to_csv("scale2_operations.csv", index=False)

    def verify_weights(self, weight_check):
        weights_string = self.weights.iloc[[len(self.weights.index)-1]]['weight'].values[0].replace('[','').replace(']','').split(',')
        weights = [eval(i) for i in weights_string]
        verified = True
        for w in range(0, len(weight_check)):
            if weight_check[w] != weights[w]:
                verified = False
        return verified



