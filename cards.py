import controller
import view


c = controller.Controller()
while (True):
    try:
        c.getUserRequest()
    except KeyboardInterrupt:
        print()
        break
    except view.Finish:
        print('You won!!!')
        break
