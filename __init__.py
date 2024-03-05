from model.FriendModel import FriendModel
from controller.FriendController import FriendController

model = FriendModel()
controller = FriendController(model)

controller.start()