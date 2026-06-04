from enum import Enum


class AccountType(Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
