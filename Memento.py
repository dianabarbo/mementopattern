from abc import ABC, abstractmethod
from datetime import datetime

class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata. 
    """

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_date(self):
        return self._date