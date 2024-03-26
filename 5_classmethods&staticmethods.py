class Vector:
    MIN_COORDS = 0
    MAX_COORDS = 100

    @classmethod
    def validate(cls, arg): # Метод класса работает исколючительно с атрибутами этого класса, но нельзя обратиться к солкальным атрибутам экземпляра
        return cls.MIN_COORDS <= arg <= cls.MAX_COORDS

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y): # Лучше использовать self вместо Vector, потому что так более универсально. Если поменять название класса, то программа работать не будет
            self.x = x
            self.y = y
    
    def get_coords(self):
        return self.x, self.y
    
    @staticmethod
    def norm2(x, y):
        return x*x + y*y
    
v = Vector(1, 2)
res = Vector.get_coords(v)
print(res)

print(Vector.validate(5)) # Метод класса можно возвращять через сам класс, не указывая cls

print(Vector.norm2(5, 6))