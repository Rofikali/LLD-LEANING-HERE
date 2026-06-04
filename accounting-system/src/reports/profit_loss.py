from accounts.account_type import AccountType


class ProfitLossGenerator:
    def generate(self, accounts, ledger_repository):

        revenue = 0
        expense = 0

        for account in accounts:
            entries = ledger_repository.find_by_account(account.id)

            balance = sum(e.credit.amount for e in entries) - sum(
                e.debit.amount for e in entries
            )

            if account.account_type == AccountType.INCOME:
                revenue += balance

            elif account.account_type == AccountType.EXPENSE:
                expense += abs(balance)

        return {"revenue": revenue, "expense": expense, "profit": revenue - expense}
