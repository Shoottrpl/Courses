from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    price: float = 0
    weight: int = 0
    dims: list = field(default_factory=list)




td = ThingData('Учебник по Python', 100)
td.dims.append(10)
td2 = ThingData('Учебник по Python', 100)
print(td2)



