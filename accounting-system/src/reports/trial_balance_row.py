from dataclasses import dataclass


@dataclass
class TrialBalanceRow:
    account_name: str

    debit: float

    credit: float
