class Geom:
    name = 'Geom'

    def set_coord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Рисование примитива")



class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")

class Rect(Geom):
    pass



g = Geom()
g.set_coord(0, 0, 0, 0)
l = Line()
r = Rect()
l.draw()
r.draw()
