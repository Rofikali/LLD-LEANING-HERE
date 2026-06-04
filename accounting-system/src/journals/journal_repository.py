from abc import ABC
from abc import abstractmethod

from journals.journal_entry import JournalEntry


class JournalRepository(ABC):

    @abstractmethod
    def save(
        self,
        journal: JournalEntry
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        journal_id
    ) -> JournalEntry:
        pass