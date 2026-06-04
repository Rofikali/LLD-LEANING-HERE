from journals.journal_repository import JournalRepository


class InMemoryJournalRepository(
    JournalRepository
):

    def __init__(self):
        self.storage = {}

    def save(self, journal):
        self.storage[journal.id] = journal

    def get(self, journal_id):
        return self.storage[journal_id]