class CountLetters:
    def __init__(self, expression, number_system, number):
        self.expression = expression
        self.number_system = number_system
        self.number = number
    
    def count_num(self):
        """
        >>> c = CountLetters(7*512**120 - 6*64**100 + 8**210 - 255, 8, 0)
        >>> c.count_num()
        151
        >>> c = CountLetters(4**2018 + 2**2018 - 32, 2, 1)
        >>> c.count_num()
        2014
        >>> c = CountLetters(3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1, 16, 0)
        >>> c.count_num()
        15
        """
        s=""
        x = self.expression
        while x != 0:
            s += str(x % self.number_system)
            x //= self.number_system
        return s.count(str(self.number))

def answer():

    expression_str = input('Введите выражение:')
    expression = eval(expression_str)
    number_system = int(input('Введите в какую систему счисления переводить:'))
    number = (input('Введите какое число считать в этом выражении:'))

                        
    zadanie = CountLetters(expression, number_system, number)
    result = zadanie.count_num()
    print(f'Ответ: {result}')

