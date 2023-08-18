import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from .interface_v4 import *









class Butelka(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Butelka, self).__init__(parent)
        
        # Основне вікно
        self.ui = Ui_Butelka()
        self.ui.setupUi(self)
        
        self.fill_combobox_25()
        self.fill_combobox_29()
        self.r_pet_list()
        self.choose_the_pallet()
        self.choose_packing_method()
        self.what_pallet()
        self.date_update()
        self.view_label_pet()
        self.wiev_narzut()
        self.view_label_r_pet()
        self.view_label_kurs()
        
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
            
    def fill_combobox_29(self):
        numer_values = self.color_butelka()
        self.ui.comboBox_29.addItems(numer_values)
    
    
        
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
        
    def color_butelka(self):
        conn = sqlite3.connect('data\\barwnik.db')
        curs = conn.cursor()
        curs.execute("SELECT Kolor_cecha FROM data")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
                
        return data
    
    def r_pet_list(self):
        r_pet_list = ["0", "25", "30", "50", "75", "100"]
        self.ui.comboBox_30.addItems(r_pet_list)
    
    def choose_the_pallet(self):
        height_list = ["1.5", "1.8", "2", "2.2", "2.4", "2.6"]
        self.ui.comboBox_7.addItems(height_list)
        
    def choose_packing_method(self):
        choose_pallet = ["P1", "P2", "P3", "P4", "K1", "K2", "K3", "K4", "K5", "K6", "K7"]
        self.ui.comboBox_8.addItems(choose_pallet)
        
    def what_pallet(self):
        pallet = ["One Way pallet", "Euro pallet", "Plastic pallet", "Karton", "Not pallet", "Euro Pal zwr."]
        self.ui.comboBox_9.addItems(pallet)
        
    def date_update(self):
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute("SELECT date_time FROM Kurs WHERE kurs_id=5")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_56.setText(str(data[0]))
        return data
        
    # Показуємо актуальну ціну Pet
    def view_label_pet(self):
        
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute(f"SELECT cena_za_kg FROM Kurs WHERE kurs_id=1")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_43.setText(str(data[0]))
        return data
    
    # Показуємо актуальну ціну R-Pet
    def view_label_r_pet(self):
        
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute(f"SELECT cena_za_kg FROM Kurs WHERE kurs_id=2")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_51.setText(str(data[0]))
        return data
    
       # Показуємо актуальну ціну EUR/PLN
    def view_label_kurs(self):
        
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute(f"SELECT cena_za_kg FROM Kurs WHERE kurs_id=4")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_24.setText(str(data[0]))
        return data
        
       # Показуємо процент накладних витрат
    def wiev_narzut(self):
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute("SELECT cena_za_kg FROM Kurs WHERE kurs_id=3")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_49.setText(str(data[0]))
        return data
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Butelka()
    ui.show()
    sys.exit(app.exec_())