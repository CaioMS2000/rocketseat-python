from abc import ABC, abstractmethod


class IBalanceEditor(ABC):
    @abstractmethod
    def edit(self, user_id: int, new_balance: float): ...
