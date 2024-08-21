import random as rand
class MysticBall:
    def __init__(self, *words):
        self.words = words
    
    def __call__(self):
        return rand.choice(self.words)
        
        
first = 'Мама мыла раму'
second = 'Рамена мало было'

list_ = list(map(lambda x, y: x == y, first, second))

print(list_)

def get_advanced_writer(file_name):
    
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for str_ in data_set:
                file.write(f"{str_}\n")
            
    return write_everything
    
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())