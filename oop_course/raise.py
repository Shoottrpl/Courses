class ExeptionPrint(Exception):
    """Общий класс исключения принтера"""

class ExeptionPrintSendData(ExeptionPrint):
    """Класс исключение при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExeptionPrintSendData

    def send_to_print(self, data):
        return False

p = PrintData()
try:
    p.print('123')
except ExeptionPrintSendData:
    print("принтер не отвечает")
except ExeptionPrint:
    print("Общая ошибка печати")