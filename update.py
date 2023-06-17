

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 430)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 30, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 110, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 140, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 190, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 220, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 300, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 220, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 300, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 16, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 110, 16, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 190, 16, 20))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 270, 16, 20))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 350, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         # Зв'язуємо функцію-обробник події
         
        self.checkBox.stateChanged.connect(self.check_box_1)
        self.checkBox_2.stateChanged.connect(self.check_box_2)
        self.checkBox_3.stateChanged.connect(self.check_box_3)
        self.checkBox_4.stateChanged.connect(self.check_box_4)
        self.pushButton.clicked.connect(self.button_click)
        self.comboBox.currentIndexChanged.connect(self.view_label_6)
        self.comboBox_3.currentIndexChanged.connect(self.view_label_7)
        self.comboBox_4.currentIndexChanged.connect(self.view_label_8)
        
        # Подія зміни в базі даних
    def button_click(self):
        self.line_edit_pet_r_pet()
        self.line_edit_euro()
        self.line_edit_cost_machine()
        self.line_edit_cost_color()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Data updated")
        msg.setWindowTitle("Update")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        
    # З'вязуємо функцію-обробник події чек-боксів
    def check_box_1(self, state):
        if state == QtCore.Qt.Checked:
            self.fill_combobox1()
            
        else:
            self.comboBox.clear()
            self.label_6.clear()
            
    def check_box_2(self, state):
        if state == QtCore.Qt.Checked:
            self.update_euro()
            self.view_label_5()
            
        else:
            self.comboBox_2.clear()
            self.label_5.clear()
            
    def check_box_3(self, state):
        if state == QtCore.Qt.Checked:
            self.fill_combobox3()
        else:
            self.comboBox_3.clear()
            self.label_7.clear()
            
    def check_box_4(self, state):
        if state == QtCore.Qt.Checked:
            self.fill_combobox4()
        else:
            self.comboBox_4.clear()
            self.label_8.clear()
        
        
    #  заповнення комбо-боксів   
    def fill_combobox1(self):
        
        numer_values = self.update_pet_r_pet()
        self.comboBox.addItems(numer_values)
        
        
    def fill_combobox3(self):
        maszyna_values = self.cost_machine()
        self.comboBox_3.addItems(maszyna_values)
        
    def fill_combobox4(self):
        color_values = self.cost_color()
        self.comboBox_4.addItems(color_values)
        
    def view_label_5(self):
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT cena_za_kg FROM kurs WHERE surowiec= 'EURO'")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.label_5.setText(str(data))
        return data
    
    def view_label_6(self):
        sur = str(self.comboBox.currentText())
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute(f"SELECT cena_za_kg FROM kurs WHERE surowiec= '{sur}'")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.label_6.setText(str(data))
        return data
    
    def view_label_7(self):
        machine = str(self.comboBox_3.currentText())
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute(f"SELECT Koszt FROM data WHERE Maszyna = '{machine}'")
        result = curs.fetchall()
        data = str(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        self.label_7.setText(data)
        return data
    
    def view_label_8(self):
        color = str(self.comboBox_4.currentText())
        conn = sqlite3.connect('data/barwnik.db')
        curs = conn.cursor()
        curs.execute(f"SELECT Cena_za_kg FROM data WHERE Identyfikator = '{color}'")
        result = curs.fetchall()
        data = str(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        self.label_8.setText(data)
        return data
        
        
    # Беремо дані з бази даних
    def update_pet_r_pet(self):
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT surowiec FROM kurs WHERE surowiec IN ('Pet', 'R_Pet')")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        return data
        
    def update_euro(self):
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT surowiec FROM kurs WHERE surowiec = 'EURO'")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.comboBox_2.addItems(data)
        return data
        
    def cost_machine(self):
        conn = sqlite3.connect('data\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT Maszyna FROM data")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data
    
    def cost_color(self):
        conn = sqlite3.connect('data/barwnik.db')
        curs = conn.cursor()
        curs.execute("SELECT Identyfikator FROM data")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data
        
    def line_edit_pet_r_pet(self):
        surowiec = self.comboBox.currentText()
        cena = self.lineEdit.text()
        conn = sqlite3.connect('data/preforma.db')
        cursor = conn.cursor()
        update_query = '''UPDATE kurs SET cena_za_kg = ? WHERE surowiec = ?'''  
        cursor.execute(update_query, (cena, surowiec))
        conn.commit()
        conn.close()
        
    def line_edit_euro(self):
        kurs = self.comboBox_2.currentText()
        cena = self.lineEdit_2.text()
        conn = sqlite3.connect('data/preforma.db')
        cursor = conn.cursor()
        update_query = '''UPDATE kurs SET cena_za_kg = ? WHERE surowiec = ?'''
        cursor.execute(update_query, (cena, kurs))
        conn.commit()
        conn.close()
        
    def line_edit_cost_machine(self):
        maszyna = self.comboBox_3.currentText()
        cena = self.lineEdit_3.text()
        conn = sqlite3.connect('data/preforma.db')
        cursor = conn.cursor()
        update_query = '''UPDATE data SET Koszt = ? WHERE Maszyna = ?'''
        cursor.execute(update_query, (cena, maszyna))
        conn.commit()
        conn.close()
    
    def line_edit_cost_color(self):
        color = self.comboBox_4.currentText()
        cena = self.lineEdit_4.text()
        conn = sqlite3.connect('data/barwnik.db')
        cursor = conn.cursor()
        update_query = '''UPDATE data SET Cena_za_kg = ? WHERE Identyfikator = ?'''
        cursor.execute(update_query, (cena, color))
        conn.commit()
        conn.close()
        
        
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update"))
        self.label.setText(_translate("MainWindow", "Cena Pet / R-Pet za kg"))
        self.label_2.setText(_translate("MainWindow", "Kurs EUR / PLN"))
        self.label_3.setText(_translate("MainWindow", "Koszt maszyny PLN/h"))
        self.label_4.setText(_translate("MainWindow", "Barvnik cena/kg"))
        self.pushButton.setText(_translate("MainWindow", "U p d a t e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
