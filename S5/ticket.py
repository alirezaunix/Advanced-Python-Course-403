from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
from PyQt5.QtGui import QTextDocument
from PyQt5 import uic
from jdatetime import datetime


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/Advanced Python Course 403/S5/ticket.ui", self)
        
        self.btn_submit.clicked.connect(self.submitMethod)
        self.btn_clear.clicked.connect(self.clearMethod)
        self.btn_print.clicked.connect(self.printMethod)
        self.btn_exit.clicked.connect(self.close)
        
        self.actionSubmit.triggered.connect(self.submitMethod)
        
    def submitMethod(self):
        #        self.spin.valueChanged.connect(self.show_result)
        fname=self.in_fname.text()
        movie=self.in_movie.text()
        ticket=self.spin_ticket.value()
        time=self.combo_time.currentText()
        f1=open("/Users/alireza/Desktop/Advanced Python Course 403/S5/data.txt","ta")
        f1.write(f"{fname},{movie},{ticket},{time},{datetime.now().strftime('%Y/%m/%d-%H:%M')}\n")
        f1.close()
    
    def clearMethod(self):
        self.in_fname.setText("")
        self.in_movie.setText("")
        self.spin_ticket.clear()
        self.combo_time.clear()

    def printMethod(self):
        html=open("/Users/alireza/Desktop/Advanced Python Course 403/S5/template.html","tr").read()
        html=html.replace("MOVIE_NAME",self.in_movie.text()).replace("CUSTOMER_NAME",self.in_fname.text()).replace("NOT",str(self.spin_ticket.value())).replace("DATE",datetime.now().strftime('%Y/%m/%d-%H:%M'))
        doc=QTextDocument()
        doc.setHtml(html)
        printer=QPrinter()
        printer.setPrinterName("Print to PDF @ Alireza’s MBA")
        doc.print_(printer)        


if __name__=="__main__":
	app = QtWidgets.QApplication([])
	w = MainWindow()
	w.show()
	app.exec()
