class Computer():
    def __init__(self, name, memory_size):
        self.name = name
        self.memory_size = memory_size

    def set_data(self, name):
        self.name = name

class OmenHP(Computer):
    def __init__(self):
        super().__init__()

    def set_data(self, name):
        self.name = name
        self.memory_size = 8000


    # def save(self):
    #     print("Сохранение объекта класса в файл")
    #
    # def load(self):
    #     print("Загрузка данных объекта из файла")
class SaveInterface():
     def save(self, path, cmp):
         pass

class SaveComputerToFile(SaveInterface):
    def save(self, path, cmp):
        print(f"Сохранение в файл {path}, {cmp}")

class SaveComputerToDB(SaveInterface):
    def save(self, path, cmp):
        print(f"Сохранение в БД {path}, {cmp}")


