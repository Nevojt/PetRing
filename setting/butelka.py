from datetime import datetime
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from .interface_v4 import *
import postgres_db.models as models
from postgres_db.database import get_db, SessionLocal
from setting.dialog_update import *






class Butelka(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Butelka, self).__init__(parent)
        
        # Основне вікно
        self.ui = Ui_Butelka()
        self.ui.setupUi(self)
        
        # діалогове вікно update Pet, R-Pet 
        self.dialog_update = QtWidgets.QDialog()
        self.update = Ui_Dialog_Update()
        self.update.setupUi(self.dialog_update)
        
        # self.fill_combobox_25()
        # self.fill_combobox_29()
        # self.r_pet_list()
        # self.choose_the_pallet()
        # self.choose_packing_method()
        # self.what_pallet()
        # self.update_tablo()
        
        # self.ui.comboBox_25.currentIndexChanged.connect(self.update_combobox_26)
        # self.ui.comboBox_26.currentIndexChanged.connect(self.update_combobox_27)
        # self.ui.comboBox_27.currentIndexChanged.connect(self.update_combobox_28)
        
        # self.ui.pushButton_17.clicked.connect(self.update_dialog)
        
        # self.update.buttonBox.accepted.connect(self.update_buttons)
        # self.update.buttonBox.rejected.connect(self.closed_update_dialog)
        
        
        
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
        
        


    

    
    
    def view_label_kurs(self, surowiec: str = 'EURO'):
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            return post
        finally:
            db.close()
            
    
    def view_label_r_pet(self, surowiec: str = 'R-Pet'):
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            return post
        finally:
            db.close()
            
    def view_label_pet(self, surowiec: str = 'Pet'):
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            return post
        finally:
            db.close()
            
            
    def view_label_narzut(self, surowiec: str = 'Narzut'):
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            return post
        finally:
            db.close()
            
    def date_time(self, surowiec: str = 'Date_Time'):
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            return post
        finally:
            db.close()
            
            
    def update_tablo(self):
        # Показуємо актуальну ціну EUR/PLN
        kurs = self.view_label_kurs().cena_za_kg
        self.ui.label_24.setText(str(kurs))
        
        # Показуємо актуальну ціну Pet
        pet = self.view_label_pet().cena_za_kg
        self.ui.label_43.setText(str(pet))
        
        # Показуємо актуальну ціну R-Pet
        r_pet = self.view_label_r_pet().cena_za_kg
        self.ui.label_51.setText(str(r_pet))
        
        # Показуємо процент накладних витрат
        narzut = self.view_label_narzut().cena_za_kg
        self.ui.label_49.setText(str(narzut))
        
        # Показуємо коли були останні зміни
        date = self.date_time().date_time
        self.ui.label_56.setText(str(date))
        
       # Update cost surowiec and kurs, narzut
    def update_dialog(self):
        self.dialog_update.show()
        
    def closed_update_dialog(self):
        self.dialog_update.close()
        
    def update_buttons(self):
        self.date_update()
        edit = self.update.lineEdit.text()
        edit_2 = self.update.lineEdit_2.text()
        edit_3 = self.update.lineEdit_3.text()
        edit_4 = self.update.lineEdit_4.text()
        if len(edit) > 0:
            self.update_kurs()
        if len(edit_2) > 0:
            self.update_pet()
        if len(edit_3) > 0:
            self.update_r_pet()
        if len(edit_4) > 0:
            self.update_narzut()
        else:
            print("No update")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Database update")
        msg.setWindowTitle("Update")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.update.lineEdit.clear()
        self.update.lineEdit_2.clear()
        self.update.lineEdit_3.clear()
        self.update.lineEdit_4.clear()
        
    def update_kurs(self, surowiec: str = 'EURO'):
        cena = float(self.update.lineEdit.text())
    
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            if post:
                post.cena_za_kg = cena  # Змінити поле на нове значення
                db.commit()  # Зберегти зміни у базі даних
            else:
                print("Рядок з таким значенням не знайдений")
        finally:
            db.close()
        
    def update_pet(self, surowiec: str = 'Pet'):
        cena = float(self.update.lineEdit_2.text())
    
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            if post:
                post.cena_za_kg = cena  # Змінити поле на нове значення
                db.commit()  # Зберегти зміни у базі даних
            else:
                print("Рядок з таким значенням не знайдений")
        finally:
            db.close()
        

    # Змінюємо ціну суровца
    def update_r_pet(self, surowiec: str = 'R-Pet'):
        cena = float(self.update.lineEdit_3.text())
    
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            if post:
                post.cena_za_kg = cena  # Змінити поле на нове значення
                db.commit()  # Зберегти зміни у базі даних
            else:
                print("Рядок з таким значенням не знайдений")
        finally:
            db.close()

    # Змінюємо процент накладних витрат
    def update_narzut(self, surowiec: str = 'Narzut'):
        cena = float(self.update.lineEdit_4.text())
    
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            if post:
                post.cena_za_kg = cena  # Змінити поле на нове значення
                db.commit()  # Зберегти зміни у базі даних
            else:
                print("Рядок з таким значенням не знайдений")
        finally:
            db.close()

    def date_update(self, surowiec: str = 'Date_Time'):
        date_time = datetime.now()
        # date = date_time.strftime("%d-%m-%y %H:%M")
    
        db = SessionLocal()
        try:
            post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
            if post:
                post.date_time = date_time  # Змінити поле на нове значення
                db.commit()  # Зберегти зміни у базі даних
            else:
                print("Рядок з таким значенням не знайдений")
        finally:
            db.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Butelka()
    ui.show()
    sys.exit(app.exec_())