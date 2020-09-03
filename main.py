from abc import ABC, abstractmethod
from datetime import datetime
import Memento
from Client import Client
from Caretaker import Caretaker

if __name__ == "__main__":
    Cliente = Client(
        name = "Diana Barboza", 
        id = 1143412789, 
        phone = 3043301789, 
        address = "BELLAVISTA CLL 3C # 56 - 90", 
        clientType = "Oro"
    )

    caretaker = Caretaker(Cliente)
    caretaker.backup()

    Cliente.setAddress("BELLAVISTA CLL 4C # 56 - 40")
    caretaker.backup()

    Cliente.setPhone(3185478956)
    caretaker.backup()

    Cliente.setName("Daniela Barboza Primera")

    print("\nCLIENTE - ESTADO ACTUAL\n")
    print(Cliente)

    print("\nCLIENTE - ESTADO ANTERIOR\n")
    caretaker.undo()
    print(Cliente)

    print("\nCLIENTE - ESTADO ANTE-ANTERIOR\n")
    caretaker.undo()
    print(Cliente)
