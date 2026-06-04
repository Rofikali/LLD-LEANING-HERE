from decimal import Decimal


class AccountBalanceCalculator:
    @staticmethod
    def calculate(entries):

        total_debit = sum(entry.debit.amount for entry in entries)

        total_credit = sum(entry.credit.amount for entry in entries)

        return total_debit - total_credit
