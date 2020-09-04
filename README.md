# Memento Pattern - Python implementation

## CASO DE ESTUDIO: CLASE CLIENT

Cierta empresa hace registro de información de sus clientes (nombre, número identificación, teléfono, dirección, tipo de cliente). Se requiere guardar un historial de la información registrada para cada cliente en el pasado, para poder restaurarla cuando sea necesario. Es decir, el usuario de la aplicación podrá deshacer los cambios en la información de un cliente y regresar a la información que está guardada en el historial. El usuario podrá regresar a cualquiera de los estados anteriores, regresando uno a la vez.

La aplicabilidad de este patrón al caso radica en la necesidad de, primero, hacer copias de la información de los clientes y, segundo, asegurar que esa información se guarde de manera íntegra, considerando que se trata de datos sensibles de otras personas o empresas.

Otras implementaciones hacen uso de clases anidadas, es decir, dentro de la clase Originator, se crea la clase Memento. Esto no es posible en todos los lenguajes de programación[3], por lo que se ha propuesto el uso de otra clase ConcreteMemento y Memento pasa a convertirse en una interfaz. Esta último es el enfoque que se va a implementar en el caso de estudio.

### *Detalles de la implementación*

Client se constituye como una clase contenedora que permite la modificación de sus atributos mediante métodos set y permite obtener sus datos mediante métodos get.  De acuerdo al patrón, esta clase genera sus mementos con el método save() y recupera su estado anterior mediante el método restore().

Cuando Caretaker quiere hacer una copia de Client, mediante el método backup(), Caretaker acude a Client para que use su propio método save() y cree la copia de sus datos. save() crea un Memento, mediante la clase ConcreteMemento. Este último convierte el diccionario que contiene toda la información del objeto en un Memento.

Objetos diferentes a Client, se comunicarán con los Mementos a través de una interfaz que permite guardar información acerca del memento (fecha de creación, por ejemplo), pero no el contenido del memento.

### *Diagrama de clases*

Figura 1. Diagrama de clase de la implementación del patrón Memento al caso de estudio. 

<img src=/images/ClientUML.png>
