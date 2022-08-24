#Ana penceri dışındaki diğer pencereleri python haline bu dosyada getirip
#daha sonra run.py içerisine importladık.
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*


class MatGosterim(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("..\GUIPages\mat_gosterim.ui", self)

class Kisaltma(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("..\GUIPages\Kisaltma.ui", self)

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("..\GUIPages\infobox.ui", self)

class DevreSemasi(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("..\GUIPages\Sema.ui", self)







