class Calculate:
    def add(self, a: int, b: int):
        if not (isinstance(a, int) or isinstance(b, int)):
            raise TypeError('Input must be int.')
        return a + b

    def sub(self, a: int, b: int):
        if not (isinstance(a, int) or isinstance(b, int)):
            raise TypeError('Input must be int.')
        return a - b

if __name__ == '__main__':
    c = Calculate()
    print(f'5 + 8 = {c.add(5, 8)}')
    print(f'5 - 8 = {c.sub(5, 8)}')
