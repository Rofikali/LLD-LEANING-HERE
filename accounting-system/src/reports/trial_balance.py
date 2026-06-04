class TrialBalanceGenerator:
    def generate(self, accounts, ledger_repository):

        rows = []

        for account in accounts:
            entries = ledger_repository.find_by_account(account.id)

            debit_total = sum(e.debit.amount for e in entries)

            credit_total = sum(e.credit.amount for e in entries)

            rows.append(
                {"account": account.name, "debit": debit_total, "credit": credit_total}
            )

        return rows
