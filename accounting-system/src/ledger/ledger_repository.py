from abc import ABC
from abc import abstractmethod

from ledger.ledger_entry import LedgerEntry


class LedgerRepository(ABC):
    @abstractmethod
    def save(self, entry: LedgerEntry) -> None:
        pass

    @abstractmethod
    def find_by_account(self, account_id) -> list[LedgerEntry]:
        pass
