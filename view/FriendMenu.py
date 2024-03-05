from view.Menu import Menu
from view.Option import Option

class FriendMenu(Menu):
    def __init__(self) -> None:
        super().__init__("------ Friends App ------")
        self.addOption(Option("Exit", "exit"))
        self.addOption(Option("List All Friends", "listAll"))
        self.addOption(Option("Search Friend By Phone", "searchByPhone"))
        self.addOption(Option("Search Friend By Name", "searchByName"))
        self.addOption(Option("Add a New Friend", "addFriend"))
        self.addOption(Option("Modify Friend", "modifyFriend"))
        self.addOption(Option("Remove a Friend", "removeFriend"))