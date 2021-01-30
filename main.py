import controller
import time

controller.init()

while 1:
    controller.gameStep()
    time.sleep(0.1)