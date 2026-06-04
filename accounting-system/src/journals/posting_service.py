from journals.journal_repository import JournalRepository
from journals.journal_entry import JournalEntry


class PostingService:
    def __init__(self, repository: JournalRepository):
        self.repository = repository

    def post(self, journal: JournalEntry):

        journal.validate()

        self.repository.save(journal)
