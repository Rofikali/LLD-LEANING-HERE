from dataclasses import dataclass
from uuid import UUID

from shared.money import Money


@dataclass(frozen=True)
class LedgerEntry:
    journal_id: UUID
    account_id: UUID
    debit: Money
    credit: Money
