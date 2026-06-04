from dataclasses import dataclass
from uuid import UUID

from shared.money import Money


@dataclass(frozen=True)
class JournalLine:
    account_id: UUID
    debit: Money
    credit: Money
