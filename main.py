from Modelqltv import Modelqltv
from Viewqltv import Viewqltv
from Controllerqltv import Controllerqltv

model = Modelqltv()
view = Viewqltv()
controller = Controllerqltv(model, view)

if __name__ == '__main__':
    view.start()




