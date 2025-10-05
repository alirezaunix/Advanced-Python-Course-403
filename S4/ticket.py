from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/Advanced Python Course 403/S4/ticket.ui", self)
        
        self.btn_submit.clicked.connect(self.submitMethod)
        self.btn_clear.clicked.connect(self.clearMethod)
        self.btn_print.clicked.connect(self.printMethod)
        self.btn_exit.clicked.connect(self.close)

    def submitMethod(self):
        #        self.spin.valueChanged.connect(self.show_result)
        fname=self.in_fname.text()
        movie=self.in_movie.text()
        ticket=self.spin_ticket.value()
        time=self.combo_time.currentText()
        f1=open("/Users/alireza/Desktop/Advanced Python Course 403/S4/data.txt","ta")
        f1.write(f"{fname},{movie},{ticket},{time}\n")
        f1.close()
    
    def clearMethod(self):
        self.in_fname.setText("")
        self.in_movie.setText("")
        self.spin_ticket.clear()
        self.combo_time.clear()

    def printMethod(self):
        pass


if __name__=="__main__":
	app = QtWidgets.QApplication([])
	w = MainWindow()
	w.show()
	app.exec()
