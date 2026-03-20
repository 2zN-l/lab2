class Delitely:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        
    def count_deliyely(self):
        """
        >>> c = Delitely(84052, 84130)
        >>> c.count_deliyely()
        (72, 84084)
        >>> c = Delitely(2, 48)
        >>> c.count_deliyely()
        (10, 48)
        >>> c = Delitely(1, 10)
        >>> c.count_deliyely()
        (4, 6)
        >>> c = Delitely(100, 120)
        >>> c.count_deliyely()
        (16, 120)
        """
        M = 0
        for i in range(self.min_num, self.max_num + 1):
            delitely = 2
            for j in range(2, i//2 + 1):
                if i % j == 0:
                    delitely += 1
            if delitely > M:
                M = delitely
                m = i
        return (M, m)

def answer():

    min_num = int(input('Введите минимальное число отрезка:'))
    max_num = int(input('Введите максимальное число отрезка:'))

                        
    zadanie = Delitely(min_num, max_num)
    result = zadanie.count_deliyely()
    print(f'Ответ: {result}')