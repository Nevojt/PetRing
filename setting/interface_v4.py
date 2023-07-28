


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preforma(object):
    def setupUi(self, MainWindow):

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.Preforma = QtWidgets.QWidget()
        self.Preforma.setObjectName("Preforma")
        self.label = QtWidgets.QLabel(self.Preforma)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/imge_pet_ring.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Preforma)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 401, 51))
 
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.Preforma)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 411, 561))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(17)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 293)
        self.tableWidget.setColumnWidth(1, 90)
   
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Quantity pcs / Packaging"))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("How many packaging for Order (Rounded up)"))
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("Quantity product for Order"))
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("Total weight for 1 packaging (kg)"))
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem("Cost Raw Material for 1000 pcs"))
        self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem("Waste for preforms"))
        self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem("Cost color batch for 1000 pcs"))
        self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem("Cost color Batch waste"))
        self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem("Total Cost Raw Material for 1000 pcs"))
        self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem("Cost Packing for 1000 pcs"))
        self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem("Cost Start Machine for 1000 pcs"))
        self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem("Cost Machin for 1000 pcs"))
        self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem("Total Cost Machine for 1000 pcs"))
        self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem("Total Cost Machine + Narzut for 1000 pcs"))
        self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem("Total Cost for 1000 pcs"))
        self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem("Total Cost for 1000 pcs (PLN)"))
        self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem("Total Cost for 1000 pcs (EUR)"))
        self.tableWidget.setObjectName("tableWidget")
        
        self.layoutWidget = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 150, 641, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setEditable(True)
        
        # Налаштовуємо пошук та вибір з клавіатури
        completer = QtWidgets.QCompleter(self.comboBox.model(), self.comboBox)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setFilterMode(QtCore.Qt.MatchContains)  # Можна змінити спосіб фільтрації
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Враховувати регістр
        
        self.comboBox.setCompleter(completer)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setEditable(True)
        
        completer = QtWidgets.QCompleter(self.comboBox_4.model(), self.comboBox)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setFilterMode(QtCore.Qt.MatchContains)  # Можна змінити спосіб фільтрації
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Враховувати регістр

        self.comboBox_4.setCompleter(completer)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_2.addWidget(self.comboBox_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 210, 411, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget2.setGeometry(QtCore.QRect(870, 700, 211, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget2)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.layoutWidget3 = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget3.setGeometry(QtCore.QRect(700, 150, 380, 160))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget3)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 2)
        
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        
        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 2)
        
        self.layoutWidget5 = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget5.setGeometry(QtCore.QRect(700, 110, 370, 31))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.label_13 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        
        self.label_14 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        
        self.layoutWidget4 = QtWidgets.QWidget(self.Preforma)
        self.layoutWidget4.setGeometry(QtCore.QRect(700, 20, 370, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        
        self.label_12 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)

        self.layout.addWidget(self.Preforma)
         
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PetRing"))
        self.label_2.setText(_translate("MainWindow", "Index"))
        self.label_3.setText(_translate("MainWindow", "Ilosc dla Klienta"))
        self.lineEdit_2.setText(_translate("MainWindow", "100000"))
        self.pushButton_2.setText(_translate("MainWindow", "Create Cost"))
        self.pushButton_3.setText(_translate("MainWindow", "Create Excel"))
        self.pushButton_4.setText(_translate("MainWindow", "Coming soon"))
        self.label_13.setText(_translate("MainWindow", "EUR/PLN"))
        self.label_4.setText(_translate("MainWindow", "Cena PET (EUR/Ton)"))
        self.label_10.setText(_translate("MainWindow", "Cena R-PET (EUR/Ton)"))
        self.label_9.setText(_translate("MainWindow", "Narzut"))
        self.label_8.setText(_translate("MainWindow", "%"))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        self.label_6.setText(_translate("MainWindow", "Data aktualizacji bazy"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 21))
        
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # # Block from Butelka 
        
class Ui_Butelka(object):
    def setupUi(self, MainWindow):
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
 
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.Butelka = QtWidgets.QWidget()
        self.Butelka.setObjectName("Butelka")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Butelka)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 270, 411, 561))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setRowCount(17)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        
        self.layoutWidget7 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget7.setGeometry(QtCore.QRect(700, 110, 370, 31))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.label_23 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        
        self.label_24 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: red; font-size: 20px; font-family: Arial;")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        
 
        self.layoutWidget_6 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget_6.setGeometry(QtCore.QRect(700, 150, 380, 160))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_42 = QtWidgets.QLabel(self.layoutWidget_6)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_6)
    
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.gridLayout_5.addWidget(self.label_43, 0, 1, 1, 2)
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_6)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_5.addWidget(self.label_47, 1, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.gridLayout_5.addWidget(self.label_48, 2, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_6)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.gridLayout_5.addWidget(self.label_49, 2, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_6)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.gridLayout_5.addWidget(self.label_50, 2, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_6)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_5.addWidget(self.pushButton_17, 3, 1, 1, 2)
        self.label_51 = QtWidgets.QLabel(self.layoutWidget_6)

        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.gridLayout_5.addWidget(self.label_51, 1, 1, 1, 2)
        self.label_52 = QtWidgets.QLabel(self.Butelka)
        self.label_52.setGeometry(QtCore.QRect(300, 20, 401, 51))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.Butelka)
        self.label_53.setGeometry(QtCore.QRect(0, 0, 291, 111))

        self.label_53.setText("")
        self.label_53.setPixmap(QtGui.QPixmap("image/imge_pet_ring.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setObjectName("label_53")
        self.layoutWidget_7 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 210, 411, 30))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_54 = QtWidgets.QLabel(self.layoutWidget_7)
    
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_13.addWidget(self.label_54)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_7)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_13.addWidget(self.lineEdit_6)
        self.layoutWidget_8 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 150, 641, 31))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        
        self.comboBox_25 = QtWidgets.QComboBox(self.layoutWidget_8)
        self.comboBox_25.setEditable(True)
        # Налаштовуємо пошук та вибір з клавіатури
        
        completer = QtWidgets.QCompleter(self.comboBox_25.model(), self.comboBox_25)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setFilterMode(QtCore.Qt.MatchContains)  # Можна змінити спосіб фільтрації
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Враховувати регістр
        
        self.comboBox_25.setCompleter(completer)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_25.setFont(font)
        self.comboBox_25.setObjectName("comboBox_25")
        self.horizontalLayout_14.addWidget(self.comboBox_25)
        self.comboBox_26 = QtWidgets.QComboBox(self.layoutWidget_8)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_26.setFont(font)
        self.comboBox_26.setObjectName("comboBox_26")
        self.horizontalLayout_14.addWidget(self.comboBox_26)
        self.comboBox_27 = QtWidgets.QComboBox(self.layoutWidget_8)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_27.setFont(font)
        self.comboBox_27.setObjectName("comboBox_27")
        self.horizontalLayout_14.addWidget(self.comboBox_27)
        self.comboBox_28 = QtWidgets.QComboBox(self.layoutWidget_8)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_28.setFont(font)
        self.comboBox_28.setObjectName("comboBox_28")
        self.horizontalLayout_14.addWidget(self.comboBox_28)
        self.comboBox_29 = QtWidgets.QComboBox(self.layoutWidget_8)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_29.setFont(font)
        self.comboBox_29.setObjectName("comboBox_29")
        self.horizontalLayout_14.addWidget(self.comboBox_29)
        self.comboBox_30 = QtWidgets.QComboBox(self.layoutWidget_8)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_30.setFont(font)
        self.comboBox_30.setObjectName("comboBox_30")
        self.horizontalLayout_14.addWidget(self.comboBox_30)
        self.layoutWidget_9 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget_9.setGeometry(QtCore.QRect(700, 20, 370, 31))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        
        self.label_55 = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_15.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(self.layoutWidget_9)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_15.addWidget(self.label_56)
        self.layoutWidget_10 = QtWidgets.QWidget(self.Butelka)
        self.layoutWidget_10.setGeometry(QtCore.QRect(870, 700, 211, 131))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget_10)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_5.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget_10)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_5.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget_10)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_5.addWidget(self.pushButton_20)
        self.layout.addWidget(self.Butelka)
        
        _translate = QtCore.QCoreApplication.translate
        self.label_23.setText(_translate("MainWindow", "EUR/PLN"))
        self.label_42.setText(_translate("MainWindow", "Cena PET (EUR/Ton)"))
        self.label_47.setText(_translate("MainWindow", "Cena R-PET (EUR/Ton)"))
        self.label_48.setText(_translate("MainWindow", "Narzut"))
        self.label_50.setText(_translate("MainWindow", "%"))
        self.pushButton_17.setText(_translate("MainWindow", "Update"))
        self.label_52.setText(_translate("MainWindow", "Index"))
        self.label_54.setText(_translate("MainWindow", "Ilosc dla Klienta"))
        self.lineEdit_6.setText(_translate("MainWindow", "100000"))
        self.label_55.setText(_translate("MainWindow", "Data aktualizacji bazy"))
        self.pushButton_18.setText(_translate("MainWindow", "Create Cost"))
        self.pushButton_19.setText(_translate("MainWindow", "Create Excel"))
        self.pushButton_20.setText(_translate("MainWindow", "Coming soon"))
        # self.AoKI = QtWidgets.QWidget()
        # self.AoKI.setObjectName("AOKI")
        # self.tabWidget.addTab(self.AoKI, "")
        
        # self.Nakretka = QtWidgets.QWidget()
        # self.Nakretka.setObjectName("Nakretka")
        # self.tabWidget.addTab(self.Nakretka, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 21))
        
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.AoKI), _translate("MainWindow", "AOKI"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.Nakretka), _translate("MainWindow", "Nakretka"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())