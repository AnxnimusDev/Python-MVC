#Clase menu. Nos permite llenarla de opciones para mostrarlas posteriormente.
class Menu:
    _title = None
    #List of Options
    _options = []
    """Constructor sobrecargado con un atributo Title.
    """
    def __init__(self, title) -> None:
        self._title = title
        
    #Métodos de acceso para los atributos
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title
        
    #Método que devuelve una opción de la lista dado el índice.
    def getOption(self, index):
        return self._options[index]
    
    def addOption(self, option):
        self._options.append(option)
        
    def removeOption(self, option):
        self._options.remove(option)
        
    #Método que muestra las opciones del menú por pantalla.
    def show(self):
        print("======================== " + self._title + " ========================")
        index = 0
        for option in self._options:
            print(str(index) + ")" + option.getText())
            index = index + 1
    
    #Método que devuelve la opción escogida por teclado por parte del usuario
    def getSelectedOption(self):
        print("Select an option:")
        option = input()
        #Verificamos que la entrada de texto sea de valor numérico, y que se trata de uno de los índeces de las opciones del menú
        if option.isnumeric():
            if int(option) < 0 or int(option) > len(self._options):
                return -1
            else:
                return option
        else:
            return -1
        
    #Método que devuelve el Action Command en un función del índice escogido
    def getSelectedActionCommand(self):
        optionIndex = self.getSelectedOption()
        if int(optionIndex) != -1:
            return self._options[int(optionIndex)].getActionCommand()