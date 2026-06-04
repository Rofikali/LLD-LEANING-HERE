from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal

from journals.journal_line import JournalLine


@dataclass
class JournalEntry:
    id: UUID
    description: str
    lines: list[JournalLine]

    def validate(self) -> None:
        total_debit = sum(line.debit.amount for line in self.lines)

        total_credit = sum(line.credit.amount for line in self.lines)

        if total_debit != total_credit:
            raise ValueError("Journal Entry is not balanced")
