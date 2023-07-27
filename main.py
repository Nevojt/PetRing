
from setting.preforma import Preforma
from setting.butelka import Butelka
from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5 import QtWidgets
from setting.interface_v4 import *
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(1100, 920)
        self.setMaximumSize(1150, 950)
        
         # Припустимо, у вас є QTabWidget з двома вкладками
         
        
        self.tabWidget = QTabWidget()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabWidget.addTab(self.tab1, "Preforma")
        self.tabWidget.addTab(self.tab2, "Butelka")

        # Зараз додайте віджети до вкладок
        self.layout1 = QVBoxLayout(self.tab1)
        self.preforma = Preforma()
        self.layout1.addWidget(self.preforma)

        self.layout2 = QVBoxLayout(self.tab2)
        self.butelka = Butelka()
        self.layout2.addWidget(self.butelka)

        self.setCentralWidget(self.tabWidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


