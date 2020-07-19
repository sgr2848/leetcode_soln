# Given two integers ‘n’ and ‘m’, find all the stepping numbers in range[n, m]. A number is called stepping number if all adjacent digits have an absolute difference of 1. 321 is a Stepping Number while 421 is not.
#
class Step:
    def __init__(self,start,end):
        self.step_list = []
        self.start = start
        self.end = end
    def dfs_method(self,start, end, step_number):
        if (step_number >= start and step_number <= end):
            self.step_list.append(step_number)
        if (step_number == 0 or step_number > end):
            return
        
        last_digit = step_number % 10
        step_numberA = step_number * 10 + (last_digit - 1)
        step_numberB = step_number * 10 + (last_digit + 1)
        if last_digit == 0:
            print(step_numberB)
            self.dfs_method(start, end, step_numberB)
        elif (last_digit == 9):
            print(step_numberA)
            self.dfs_method(start, end, step_numberA)
        else:            
            self.dfs_method(start, end, step_numberA)
            self.dfs_method(start, end, step_numberB)
    def get_stepping_num(self):
        for i in range(0, 9):
            self.dfs_method(self.start, self.end, i)
        return sorted(self.step_list)
g = Step(2, 21)
print(g.get_stepping_num())
