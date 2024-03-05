class Option:
    
    __text = None
    __actionCommand = None
    
    def __init__(self, text, actionCommand) -> None:
        self.__text = text
        self.__actionCommand = actionCommand
        
    def getText(self):
        return self.__text
    
    def setText(self, text):
        self.__text = text
        
    def getActionCommand(self):
        return self.__actionCommand
    
    def setActionCommand(self, actionCommand):
        self.__actionCommand = actionCommand