import numpy as np


class Calculate:
    def add(self, *nums):
        for num in nums:
            if not isinstance(num, int):
                raise TypeError("Inputs must be integers")
                return

        return np.sum(nums)

    def sub(self, a: int, b: int):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError("Input must be int.")
        return a - b


if __name__ == "__main__":
    c = Calculate()
    print(c.add((5, 7, 9, 10, 11, 50, 34, 3.3)))
    # print(f'5 + 8 = {c.add(5, 8, 7, 3, 10)}')
    # print(f'5 - 8 = {c.sub(5, 8)}')
    # print(f'5 + 8 + 9 = {c.add(5, 8, 9)}')
