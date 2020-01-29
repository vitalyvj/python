from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def tissue(self):
        pass


class Coat(Clothes):
    def __init__(self, name, V):
        self.name = name
        self.V = V

    @property
    def tissue(self):
        return f'Расход ткани на пальто {self.name}: {self.V / 6.5 + 0.5:.2f} м'


class Suit(Clothes):
    def __init__(self, name, H):
        self.name = name
        self.H = H

    @property
    def tissue(self):
        return f'Расход ткани на костюм {self.name}: {2 * self.H + 0.3:.2f} м'


print(Coat('Burberry', 48).tissue)
print(Suit('Brioni', 1.7).tissue)
