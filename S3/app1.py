from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("app1.ui", self)

if __name__=="__main__":
	app = QtWidgets.QApplication([])
	w = MainWindow()
	w.show()
	app.exec()
