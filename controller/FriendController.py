import sys
from model.FriendModel import FriendModel
from model.Friend import Friend
from view.FriendView import FriendView

class FriendController:
    #Puedo poner atributos de la manera en la que se haría en Java
    __model = None
    __view = None
    """
    Constructor de la clase FriendModel. Inicializa los atributos. 
    """
    def __init__(self, model) -> None:
        self.__model = model
        self.__view = FriendView(self, model)
    
    def start(self):
        self.__view.display()
        
    def exitApp(self):
        self.__model.closeConnection()
        self.__view.showMessage("You exit, bye bye")
        sys.exit()
    
    def processRequest(self, action):
        if str(action) == "exit":
            self.exitApp()
        elif str(action) == "listAll":
            self.listAllFriends()
        elif str(action) == "searchByPhone":
            self.findFriendsByPhone()
        elif str(action) == "searchByName":
            self.findFriendsByName()
        elif str(action) == "addFriend":
            self.addFriend()
        elif str(action) == "modifyFriend":
            self.modifyFriendForm()
        elif str(action) == "removeFriend":
            self.removeFriendForm()
        else:
            self.__view.showMessage("Wrong option!")
    
    def listAllFriends(self):
        data = self.__model.findAll()
        if data is not None:
            self.__view.showFriendTable(data)
        else:
            self.__view.showMessage("Error Retrieving Data!")
    
    def findFriendsByPhone(self):
        phone = self.__view.showInputDialog("Enter Friend Phone to Search For: ")
        if phone is not None:
            friend = Friend(phone)
            friendFound = self.__model.find(friend)
            if friendFound is not None:
                self.__view.friendForm(friendFound)
            else:
                self.__view.showMessage("No friend found with that phone!")
        else:
            self.__view.showMessage("Error in parameter phone!")
    
    def findFriendsByName(self):
        name = self.__view.showInputDialog("Enter Friend Name to Search For: ")
        if name is not None:
            data = self.model.findFriendByName(name)
            if data is not None:
                self.__view.showFriendTable(data)
            else:
                self.__view.showMessage("No Friend found with that name!")
        else:
            self.__view.showMessage("Error in parameter name!")
    
    def addFriend(self):
        friend = self.__view.friendForm(None)
        if friend is not None:
            result = self.__model.add(friend)
            if result > 0:
                self.__view.showMessage("Friend successfully added!")
            else:
                self.__view.showMessage("Friend has not been added!")
        else:
            self.__view.showMessage("Error in given parameters!")
        
    def removeFriend(self, friend):
        result = self.__model.remove(friend)
        if result > 0:
            self.__view.showMessage("Friend successfully removed!")
        else:
            self.__view.showMessage("Friend has not been removed!")
    
    def modifyFriendForm(self):
         #Primero preguntamos el amigo a modificar
        phone = self.__view.showInputDialog("Enter Friend to Modify phone: ")
        if phone is not None:
            friend = Friend(phone)
            foundFriend = self.__model.find(friend)
            if foundFriend is not None:
                newFriend = self.__view.friendForm(foundFriend)
                self.modifyFriend(foundFriend, newFriend)
            else:
                self.__view.showMessage("No such friend found. You can't modify it!")
        else:
            self.__view.showMessage("Error in given parameters!")
    
    def removeFriendForm(self):
         #Primero preguntamos el amigo a eliminar
        phone = self.__view.showInputDialog("Enter Friend to Remove phone: ")
        if phone is not None:
            friend = Friend(phone)
            foundFriend = self.__model.find(friend)
            if foundFriend is not None:
                self.__model.remove(foundFriend)
            else:
                self.__view.showMessage("No such friend found. You can't remove it!")
        else:
            self.__view.showMessage("Error in given parameters!")
        