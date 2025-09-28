from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/Advanced Python Course 403/S3/app1.ui", self)
        self.btn_1.clicked.connect(self.the_button_1_was_clicked)
        self.btn_2.clicked.connect(self.close)
  
    def the_button_1_was_clicked(self):
        fname=self.in_1.text()
        lname=self.in_2.text()
        age=self.in_3.text()
        print(f"Firstname is {fname} and lastname is {lname} and age is {age}")
        self.in_1.setText("")
        self.in_2.setText("")
        self.in_3.setText("")

  
if __name__=="__main__":
	app = QtWidgets.QApplication([])
	w = MainWindow()
	w.show()
	app.exec()
