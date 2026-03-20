import itertools

class Combinations:
    def __init__(self, letters, length, required_letter=None, min_count=0):
        self.letters = letters
        self.length = length
        self.required_letter = required_letter
        self.min_count = min_count
    
    def count_codes(self):
        """
        >>> c = Combinations('AB', 3, 'A', 2)
        >>> c.count_codes()
        4
        >>> c = Combinations('ABC', 2, None)
        >>> c.count_codes()
        9
        >>> c = Combinations('123', 2, '1', 1)
        >>> c.count_codes()
        5
        >>> c = Combinations('ИВАН', 5, 'И', 1)
        >>> c.count_codes()
        781
        >>> c = Combinations('XYZ', 3, 'X', 0) 
        >>> c.count_codes()
        27
        """
        if self.required_letter is None:
            return len(self.letters) ** self.length
        
        count = 0
        for code in itertools.product(self.letters, repeat=self.length):
            if code.count(self.required_letter) >= self.min_count:
                count += 1
        return count

def answer():

    letters = str(input('Введите слово:'))
    length = int(input('Введите количество букв:'))
    required_letter = str(input('Введи условие на букву (если нет, то введите 0):'))
    min_count = int(input('Колличество букв с условием(если нет, то введите 0):'))
                        
    zadanie = Combinations(letters, length, required_letter, min_count)
    result = zadanie.count_codes()
    print(f'Ответ: {result}')

