import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from setting.interface_v4 import *







class Butelka(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Butelka, self).__init__(parent)
        
        # Основне вікно
        self.ui = Ui_Butelka()
        self.ui.setupUi(self)
        
        self.fill_combobox_25()
        
        self.ui.comboBox_25.currentIndexChanged.connect(self.update_combobox_26)
        self.ui.comboBox_26.currentIndexChanged.connect(self.update_combobox_27)
        self.ui.comboBox_27.currentIndexChanged.connect(self.update_combobox_28)
        
    def fill_combobox_25(self):
        numer_values = self.forma_butelki()
        self.ui.comboBox_25.addItems(numer_values)
        
    def update_combobox_26(self):
        selected_numer = self.ui.comboBox_25.currentText()
        gwint_values = self.updateComboBox_26(selected_numer)
        self.ui.comboBox_26.clear()
        self.ui.comboBox_26.addItems(gwint_values)  
    
    def update_combobox_27(self):
        selected_numer = self.ui.comboBox_25.currentText()
        selected_gwint = self.ui.comboBox_26.currentText()
        gramatura_values = self.updateComboBox_27(selected_numer, selected_gwint)
        self.ui.comboBox_27.clear()
        self.ui.comboBox_27.addItems([str(value) for value in gramatura_values])
        
    def update_combobox_28(self):
        selected_gwint = self.ui.comboBox_26.currentText()
        selected_waga = self.ui.comboBox_27.currentText()
        gramatura_values = self.updateComboBox_28(selected_gwint, selected_waga)
        if len(gramatura_values) == 0:
            self.ui.comboBox_28.clear()
        elif gramatura_values[-1] == "0":
            gramatura_values[:-1]
            self.ui.comboBox_28.clear()
            self.ui.comboBox_28.addItems([str(value) for value in gramatura_values])
        else:
            self.ui.comboBox_28.clear()
            self.ui.comboBox_28.addItems([str(value) for value in gramatura_values])
    
    
        
    def forma_butelki(self):
        conn = sqlite3.connect('data\\butelka.db')
        curs = conn.cursor()
        curs.execute("SELECT identyfikator FROM sheet")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data
    
    def updateComboBox_26(self, numer):
        # Отримуємо вибраний елемент з першого QComboBox
        conn = sqlite3.connect('data\\butelka.db')
        curs = conn.cursor()
        curs.execute("SELECT gwint FROM sheet WHERE identyfikator=?", (numer,))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        # Оновлюємо другий QComboBox, встановлюючи відфільтровані дані як елементи
        return data
        
    def updateComboBox_27(self, numer, gwint):
        conn = sqlite3.connect('data\\butelka.db')
        curs = conn.cursor()
        curs.execute("SELECT gramatura FROM sheet WHERE identyfikator=? AND gwint=?", (numer, gwint,))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data
        
    def updateComboBox_28(self, gwint, waga):

        gwint_gram = gwint + "-" + waga
    
        conn = sqlite3.connect('data\\butelka.db')
        curs = conn.cursor()
        curs.execute("SELECT forma FROM sheet WHERE gwint_gramatura=?", (gwint_gram,))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        
        return data
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Butelka()
    ui.show()
    sys.exit(app.exec_())