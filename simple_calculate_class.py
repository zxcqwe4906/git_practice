class Calculate:
    def add(self, a, b, c=0):
        return a + b + c

    def sub(self, a, b):
        return a - b

if __name__ == '__main__':
    c = Calculate()
    print(f'5 + 8 = {c.add(5, 8)}')
    print(f'5 - 8 = {c.sub(5, 8)}')
    print(f'5 + 8 + 9 = {c.add(5, 8, 9)}')
