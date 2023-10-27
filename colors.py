class Colors:
    def __init__(self):
        self.colors = ['red','orange','green', 'blue', 'violet']

    def get_text(self, numbers_list):
        print("------")
        result = ''
        for i in range(0, len(self.colors)):
            result += ' :' + str(self.colors[i]) + '[' + str(numbers_list[i]) + ']'
        print(result)
        return result
            

