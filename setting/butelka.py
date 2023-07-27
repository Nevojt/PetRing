from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from setting.interface_v4 import *







class Butelka(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Butelka, self).__init__(parent)
        
        # Основне вікно
        self.ui = Ui_Butelka()
        self.ui.setupUi(self)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Butelka()
    ui.show()
    sys.exit(app.exec_())