from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person("Федор", 28)
tm = Template("Мне {{ p.getAge() }} и зовут {{ p.getName() }}")
msg = tm.render(p = per)

print(msg)
