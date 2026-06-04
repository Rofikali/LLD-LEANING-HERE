from ledger.ledger_repository import LedgerRepository


class InMemoryLedgerRepository(LedgerRepository):
    def __init__(self):
        self.entries = []

    def save(self, entry):
        self.entries.append(entry)

    def find_by_account(self, account_id):
        return [entry for entry in self.entries if entry.account_id == account_id]
