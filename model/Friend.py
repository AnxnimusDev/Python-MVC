class Friend:
    """Constructos al que le pasan los atributos Phone, Name y Edad
    """
    def __init__(self, phone, name, age) -> None:
        self.phone = phone
        self.name = name
        self.age = age
    #Métodos de acceso a los atributos de la clase.
    def getPhone(self) -> str:
        return self.phone
    def setPhone(self, phone):
        self.phone = phone
    def getName(self) -> str:
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self) -> int:
        return self.age
    def setAge(self, age):
        self.age = age
        
    def __str__(self) -> str:
        return f"Friend(phone = {self.phone}, name = {self.name}, age = {self.age})"