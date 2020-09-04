import Client
import Memento

class Caretaker():
    """
    The Caretaker works with all mementos via the base Memento interface.
    """

    def __init__(self, Client: Client):
        self._mementos = []
        self._Client = Client

    def backup(self):
        self._mementos.append(self._Client.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()

        try:
            self._Client.restore(memento)
        except Exception:
            self.undo()