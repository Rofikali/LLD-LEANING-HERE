from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        return Money(self.amount - other.amount)

    def __str__(self):
        return str(self.amount)
