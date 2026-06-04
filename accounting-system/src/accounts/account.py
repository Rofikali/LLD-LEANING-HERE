from dataclasses import dataclass
from uuid import UUID

from accounts.account_type import AccountType


@dataclass
class Account:
    id: UUID
    name: str
    account_type: AccountType
