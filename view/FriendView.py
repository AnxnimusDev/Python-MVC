from view.FriendMenu import FriendMenu
from model.Friend import Friend

class FriendView:
    __controller = None
    __model = None
    __menu = None
    
    def __init__(self, controller, model) -> None:
        self.__controller = controller
        self.__model = model
        self.__menu = FriendMenu()
        
    #Métodos de la Vista
        """
        Método que toma un mensaje como parámetro y devuelve la respuesta a modo de entrada por teclado del usuario
        """
    def showInputDialog(self, message):
        print(message)
        return input()
    
    def showMessage(self, message):
        print(message)
    
    def display(self):
        while True:
            self.__menu.show()
            action = self.__menu.getSelectedActionCommand()
            self.processAction(action)
        
    def processAction(self, action):
        self.__controller.processRequest(action)
    
    def showFriendTable(self, data):
        for friend in data:
            print(friend)
        print(f"{len(data)} friends found!")
    
    def friendForm(self, inputFriend) -> Friend:
        result = None
        if inputFriend is not None:
            print(inputFriend)
        try:
            phone = self.showInputDialog("Enter Friend Phone: ")
            name = self.showInputDialog("Enter Friend Name: ")
            age = self.showInputDialog("Enter Friend Age: ")
            result = Friend(phone, name, age)
            return result
        except ValueError as error:
            print(error)
            return None
        
   
    