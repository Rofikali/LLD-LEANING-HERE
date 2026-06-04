from accounts.account_type import (
    AccountType
)


class BalanceSheetGenerator:

    def generate(
        self,
        accounts,
        ledger_repository
    ):

        assets = 0
        liabilities = 0
        equity = 0

        for account in accounts:

            entries = (
                ledger_repository
                .find_by_account(
                    account.id
                )
            )

            debit_total = sum(
                e.debit.amount
                for e in entries
            )

            credit_total = sum(
                e.credit.amount
                for e in entries
            )

            balance = (
                debit_total -
                credit_total
            )

            if (
                account.account_type
                ==
                AccountType.ASSET
            ):
                assets += balance

            elif (
                account.account_type
                ==
                AccountType.LIABILITY
            ):
                liabilities += abs(balance)

            elif (
                account.account_type
                ==
                AccountType.EQUITY
            ):
                equity += abs(balance)

        return {
            "assets": assets,
            "liabilities": liabilities,
            "equity": equity
        }