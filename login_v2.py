

import json
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 485)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(57, 155, 191, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(257, 155, 191, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(57, 155, 191, 200);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 340, 450))
        self.label.setStyleSheet("background-color:rgba(70, 130, 180, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 320, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 270, 320, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 320, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color:rgba(57, 155, 191, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(257, 155, 191, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color:rgba(57, 155, 191, 200);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 200, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../PetRing/image/Sygnet_kolorowy.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 390, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,150);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.login_system)
        self.pushButton_2.clicked.connect(self.login_admin)
        
    def login_system(self):
        try:
            # Отримання імені користувача з відповідного вікна
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            # Відкриваємо файл
            with open("data/dane.json") as file:
                # Завантажує json за допомогою json.load ()
                users = json.load(file)
        except FileNotFoundError:
            # Викликаємо виключення, якщо файл не знайдено
            print("File not found")
            exit()

        # Перевіряємо, чи існує користувач з введеним логіном у файлі даних
        if username not in users:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Username or Password is incorrect.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False
            

        # Перевіряємо, чи пароль вірний
        if users[username] == password:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Login successful")
            msg.setWindowTitle("Login")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            subprocess.Popen(["pythonw", "C:\\PetRing\\interface_v2.py"]) # відкриває новий файл
            Form.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid password")
            msg.setWindowTitle("Login")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False
        
    def login_admin(self):
        try:
            # Отримання імені користувача з відповідного вікна
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            # Відкриваємо файл
            with open("data/admin.json") as file:
                # Завантажує json за допомогою json.load ()
                users = json.load(file)
        except FileNotFoundError:
            # Викликаємо виключення, якщо файл не знайдено
            print("File not found")
            exit()

        # Перевіряємо, чи існує користувач з введеним логіном у файлі даних
        if username not in users:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Username or Password is incorrect.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False
            

        # Перевіряємо, чи пароль вірний
        if users[username] == password:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Login successful")
            msg.setWindowTitle("Login")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            subprocess.Popen(["pythonw", "C:\\PetRing\\update.py"]) # відкриває новий файл
            Form.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid password")
            msg.setWindowTitle("Login")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.pushButton_2.setText(_translate("Form", "Serwis"))
        self.label_3.setText(_translate("Form", "Forgot your User Name or Password?"))



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())