class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        print("Вызов метода set_coords " + str(self)) # Адрес будет совпадать с адресом pt

        # Создание атрибутов экземпляра
        self.x = x
        self.y = y
    
    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords() # Без self была бы ошибка

Point.set_coords(pt)
pt.set_coords() # Эти записи эквивалентны

pt.set_coords(1, 2)
pt.__dict__ # Будут x и y