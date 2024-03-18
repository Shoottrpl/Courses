from dataclasses import dataclass, field, InitVar, make_dataclass
from  typing import Any


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price


    def get_max_speed(self):
        return self.max_speed

CarData = make_dataclass("CarData",[("model", str),
                                    "max_speed",
                                    ("price", float, field(default=0))],
                         namespace={"get_max_speed": lambda self: self.max_speedещгс})

c = CarData("BMV", 256, 4096)
print(c)
print(c.get_max_speed)