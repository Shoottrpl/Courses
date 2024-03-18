class Clock:
    __DAY = 86400 #число секнд в одном дне

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
    def __validate_value(self, value):
        if not isinstance(value, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом или Clock")
        sc = value
        if isinstance(value, Clock):
            sc = value.seconds
        return sc

    def __add__(self, other):
        return Clock(self.seconds + self.__validate_value(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        self.seconds += self.__validate_value(other)
        return self


c1 = Clock(1000)
c1+100
print(c1.get_time(), dir(c1))
