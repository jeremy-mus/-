class Point:
    def __new__(cls, *args, **kwargs): # cls - это как self, только на класс Point ссылается
        # __new__ должжен возвращять ссылку на новый класс
        print("Вызов __new__ для " + str(cls))
        return super().__new__(cls) # super - это ссылка на базовый класс

    def __init__(self, x = 0, y = 0): 
        print("Вызов __init__ для " + str(self))
        self.x = x
        self.y = y
    
pt = Point(1, 2)
print(pt) # Будет None, тк не был создан экземпляр класса


# Singleton


class DataBase:

    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance == None:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance
    
    def __del__(self):
        DataBase.__isinstance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}") 
    
    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        return "Данные из БД"
    
    def write(self, data):
        print(f"Запись с БД: {data}")


db1 = DataBase("Иван", "1234", 80)
db2 = DataBase("Афанасий", "228337", 50)

print(id(db1), id(db2), id(db1) == id(db2)) # При попытке создания второго экземпляра класса он не был создан, а просто ссылается на первый

db1.connect()
db2.connect()