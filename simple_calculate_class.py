import numpy as np 

class Calculate:
<<<<<<< HEAD
<<<<<<< HEAD
    def add(self, a: int, b: int):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Input must be int.')
        return a + b
=======
    def add(self, a, b, c=0):
        return a + b + c
>>>>>>> feb0ff9 (Let user add three numbers)
=======
    def add(self, *nums):
        for num in nums:
            if not isinstance(num, int): 
                raise TypeError('Inputs should be integers only!')

        return np.sum(nums)

>>>>>>> 01d586d (Solve issue [#1])

    def sub(self, a: int, b: int):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Input must be int.')
        return a - b

if __name__ == '__main__':
    c = Calculate()
    print(f'5 + 8 = {c.add(5, 8)}')
    print(f'5 - 8 = {c.sub(5, 8)}')
    print(f'5 + 8 + 9 = {c.add(5, 8, 9)}')
