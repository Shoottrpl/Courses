class Clock:
    __DAY = 86400  # число секнд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def get_method(self):
        if '__add__' in dir(self):
            return self.__add__()


c1 = Clock(1000)
c1 + 100