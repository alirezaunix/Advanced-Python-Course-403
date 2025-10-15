from PyQt5 import QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("/Users/alireza/Desktop/Advanced Python Course 403/S6/cal.ui", self)
        
        file1=open("/Users/alireza/Desktop/Advanced Python Course 403/S6/style.qss")
        styleText=file1.read()
        self.setStyleSheet(styleText)
        file1.close()
        ######## Button Defination
        for n in range(10):
            getattr(self, f'btn_{n}').pressed.connect(lambda v=n: self.input_number(v))
        for n in ["add","div","min","mul"]:
            getattr(self, f'btn_{n}').pressed.connect(lambda v=n: self.input_op(v))
        self.btn_c.pressed.connect(self.clearMethod)
        self.btn_equal.pressed.connect(self.calculate)
        ########
        
    def input_number(self,n):
        self.lcd.setText(self.lcd.text()+str(n))
        
    def input_op(self,n):
        dict1={"add":"+","div":"/","min":"-","mul":"*"}
        self.lcd.setText(self.lcd.text()+dict1.get(n))
        
    def clearMethod(self):
        self.lcd.setText("0")

    def calculate(self):
        self.lcd.setText(str(eval(self.lcd.text())))
        

if __name__=="__main__":
	app = QtWidgets.QApplication([])
	w = MainWindow()
	w.show()
	app.exec()
