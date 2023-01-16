import numpy as np 

class Calculate:
    def add(self, *nums):
        for num in nums:
            if not isinstance(num, int): 
                raise TypeError('Inputs should be integers only!')

        return np.sum(nums)


    def sub(self, a, b):
        return a - b

if __name__ == '__main__':
    c = Calculate()
    print(f'5 + 8 = {c.add(5, 8)}')
    print(f'5 - 8 = {c.sub(5, 8)}')
    print(f'5 + 8 + 9 = {c.add(5, 8, 9)}')
