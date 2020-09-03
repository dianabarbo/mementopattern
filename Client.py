from Memento import Memento, ConcreteMemento

class Client():
    """
    Holds name, id, phone, address, clientType of a cliente. It also
    defines a method for saving the data of a client inside a memento and another method
    for restoring the state from it.
    """

    def __init__(self, name, id, phone, address, clientType) -> None:
        self.__name = name
        self.__id = id
        self.__phone = phone
        self.__address = address
        self.__clientType = clientType

    """
    Getters and Setters
    """

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getID(self):
        return self.__id

    def setID(self, value):
        self.__id = value
        
    def getPhone(self):
        return self.__phone

    def setPhone(self, value):
        self.__phone = value

    def getAddress(self):
        return self.__address

    def setAddress(self, value):
        self.__address = value

    def getClientType(self):
        return self.__clientType

    def setClientType(self, value):
        self.__clientType = value

    def save(self) -> Memento:
        """
        Save the the Client's state in a memento object.
        """

        _state= {
            "name" : self.__name, 
            "id" : self.__id,
            "phone" : self.__phone,
            "address" : self.__address,
            "clientType" : self.__clientType,
        }

        return ConcreteMemento(_state)

    def restore(self, memento: Memento) -> None:
        """
        Restores the Client's state from a memento object.
        """

        self._state = memento.get_state()

        self.setName(self._state["name"])
        self.setID(self._state["id"] )
        self.setPhone(self._state["phone"])
        self.setAddress(self._state["address"])
        self.setClientType(self._state["clientType"])

    def __str__(self):
        return (
            "Nombre: {} \nID: {} \nTeléfono: {} \nDirección: {} \nTipo de cliente: {}".
            format(self.__name, self.__id, self.__phone, self.__address, self.__clientType)
        ) 
