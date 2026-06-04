from ledger.ledger_entry import (
    LedgerEntry
)


class LedgerService:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def post_journal(
        self,
        journal
    ):

        for line in journal.lines:

            ledger_entry = LedgerEntry(
                journal_id=journal.id,
                account_id=line.account_id,
                debit=line.debit,
                credit=line.credit
            )

            self.repository.save(
                ledger_entry
            )