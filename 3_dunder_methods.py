class Point:
    color = "red"
    circle = 2

    def __init__(self, x, y): # Магический метод, который выполняется сразу при создании экземпляра класса
        # Теперь экзмепляр будет иметь атрибуты x и y 
        self.x = x
        self.y = y

    def __del__(self): # Магический метод, который выполняется сразу перед удалением экземпляра класса(финализзатор)
        # То есть он выполнится, когда ни 1 внешняя ссылка не будет на него ссылаться
        print("Удаление экземпляра " + str(self))

    def set_coords(self, x, y):
        print("Вызов метода set_coords " + str(self))

        self.x = x
        self.y = y
    
    def get_coords(self):
        return (self.x, self.y)
    
pt = Point(1, 2) # В init стоит 2 аргумента, значит и здесь нужно 2 указывать, инадче будет ошибка
print(pt.__dict__)