from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from MainOperations import AnaIslemler
from OtherClasses import InfoWindow

class Run(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("..\GUIPages\welcome.ui", self)

        self.pushButton.clicked.connect(self.open_Info)
        self.InfoWindow = InfoWindow()

        self.pushButton_2.clicked.connect(self.open_AnaIslemler)
        self.AnaIslemler= AnaIslemler()

    def open_AnaIslemler(self):
        self.AnaIslemler.show()
        self.close()

    def open_Info(self):
        self.InfoWindow.show()



app = QApplication([])
window = Run()
window.show()
app.exec_()