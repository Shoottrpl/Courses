class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def _verify_coord(self, coord):
        return 0 <= coord < 100



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._verify_coord(x1)
        self._fill = fill


    def get_coord(self):
        return (self._x1, self._y1)

r = Rect(0, 0, 10, 20)
r.get_coord()
print(r._name)