from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from .butelka_ui import *
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
        
        self.fill_combobox_25()
        self.fill_combobox_29()
        self.r_pet_list()
        self.choose_the_pallet()
        self.choose_packing_method()
        self.what_pallet()
        self.update_tablo()
        
        # self.wysokosc_butelki()
        
        self.ui.comboBox_25.currentIndexChanged.connect(self.update_combobox_26)
        self.ui.comboBox_26.currentIndexChanged.connect(self.update_combobox_27)
        self.ui.comboBox_27.currentIndexChanged.connect(self.update_combobox_28)
        
        self.ui.pushButton_17.clicked.connect(self.update_dialog)
        self.ui.pushButton_20.clicked.connect(self.count_bottles_order)
        
        self.update.buttonBox.accepted.connect(self.update_buttons)
        self.update.buttonBox.rejected.connect(self.closed_update_dialog)
        
        
        
    # Block layout for cena and surowiec 
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
        
    
    # Block updating Comboboxes and other objects
        
    def fill_combobox_25(self):
        numer_values = self.forma_butelki()
        self.ui.comboBox_25.addItems(numer_values)
        
    def update_combobox_26(self):
        selected_numer = self.ui.comboBox_25.currentText()
        gwint_values = self.gwint_butelka(selected_numer)
        self.ui.comboBox_26.clear()
        self.ui.comboBox_26.addItems(gwint_values)  
    
    def update_combobox_27(self):
        selected_numer = self.ui.comboBox_25.currentText()
        selected_gwint = self.ui.comboBox_26.currentText()
        gramatura_values = self.gramatura_butelka(selected_numer, selected_gwint)
        formatted_data = []
        
        for value in gramatura_values:
            if value.is_integer():  # Перевіряємо, чи значення є цілим числом
                formatted_data.append(str(int(value)))
            else:
                formatted_data.append(str(value))
        
        
        self.ui.comboBox_27.clear()
        self.ui.comboBox_27.addItems(formatted_data)
        
    def update_combobox_28(self):
        selected_gwint = self.ui.comboBox_26.currentText()
        selected_waga = self.ui.comboBox_27.currentText()
        gramatura_values = self.forma_preforma(selected_gwint, selected_waga)
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
        db = SessionLocal()
        try:
            forma_values = db.query(models.ButelkaDB.identyfikator).all()
            return sorted(list(set([value[0] for value in forma_values])))  # Витягуємо значення з кортежів
        finally:
            db.close()
        
        
    
    def gwint_butelka(self, numer):
        db = SessionLocal()
        try:
            gwint_values = db.query(models.ButelkaDB.gwint).filter_by(identyfikator=numer).all()
            data = sorted(list(set([value[0] for value in gwint_values])))
            return data
        finally:
            db.close()
        
    def gramatura_butelka(self, numer, gwint):
        db = SessionLocal()
        try:
            gramatura_values = db.query(models.ButelkaDB.gramatura).filter_by(identyfikator=numer, gwint=gwint).all()
            data = sorted(list(set([value[0] for value in gramatura_values])))
            return data
        finally:
            db.close()
        
    def forma_preforma(self, gwint, waga):

        gwint_gram = gwint + "-" + waga
        
        
        db = SessionLocal()
        try:
            gwint_values = db.query(models.ButelkaDB.forma).filter_by(gwint_gramatura=gwint_gram).all()
            data = sorted(list(set([value[0] for value in gwint_values])))
            return data
        finally:
            db.close()

        
    def color_butelka(self):
        db = SessionLocal()
        try:
            forma_values = db.query(models.BarwnikDB.kolor_cecha).all()
            return sorted(list(set([value[0] for value in forma_values])))  # Витягуємо значення з кортежів
        finally:
            db.close()
            
    def r_pet_list(self):
        r_pet_list = ["0", "25", "30", "50", "75", "100"]
        self.ui.comboBox_30.addItems(r_pet_list)
    
    def choose_the_pallet(self):
        height_list = ["1.5", "1.8", "2", "2.2", "2.4", "2.6"]
        self.ui.comboBox_7.addItems(height_list)
        
    def choose_packing_method(self):
        choose_pallet = ["P1", "P3", "P4", "K1", "K2", "K3", "K4", "K6"]
        self.ui.comboBox_8.addItems(choose_pallet)
        
    def what_pallet(self):
        pallet = ["One Way pallet", "Euro pallet", "Plastic pallet", "Karton", "Not pallet", "Euro Pal zwr."]
        self.ui.comboBox_9.addItems(pallet)
        
        
# Block funcion calculating

    # Висота бутилки
    def wysokosc_butelki(self):
        index = f"{self.ui.comboBox_25.currentText()}-{self.ui.comboBox_26.currentText()}-{self.ui.comboBox_27.currentText()}"
        db = SessionLocal()
        try:
            wysokosc = db.query(models.ButelkaDB.wysokosc_butelki).filter_by(index=index).first()
           
            print(wysokosc.wysokosc_butelki)
            return wysokosc.wysokosc_butelki
        finally:
            db.close()

    #  Паковання, кількість бітилок на одне пакованя одну пршекладку
    def pakowanie_butelka(self):
        index = f"{self.ui.comboBox_25.currentText()}-{self.ui.comboBox_26.currentText()}-{self.ui.comboBox_27.currentText()}"
        pakowanie_metod = self.ui.comboBox_8.currentText()
        
        db = SessionLocal()
        try:
            pakowanie = None
            
            if pakowanie_metod == "P1":
                pakowanie_p1 = db.query(models.ButelkaDB.pako_standard_p1).filter_by(index=index).first()
                if pakowanie_p1 is not None:
                    pakowanie = pakowanie_p1.pako_standard_p1

            elif pakowanie_metod == "P3":
                pakowanie_p3 = db.query(models.ButelkaDB.pol_przekladki_p3).filter_by(index=index).first()
                if pakowanie_p3 is not None:
                    pakowanie = pakowanie_p3.pol_przekladki_p3

            elif pakowanie_metod == "P4":
                pakowanie_p4 = db.query(models.ButelkaDB.worek_p4).filter_by(index=index).first()
                if pakowanie_p4 is not None:
                    pakowanie = pakowanie_p4.worek_p4
            
            elif pakowanie_metod == "K1":
                pakowanie_k1 = db.query(models.ButelkaDB.karton_k1).filter_by(index=index).first()
                if pakowanie_k1 is not None:
                    pakowanie = pakowanie_k1.karton_k1
                
            elif pakowanie_metod == "K2":
                pakowanie_k2 = db.query(models.ButelkaDB.karton_k2).filter_by(index=index).first()
                if pakowanie_k2 is not None:
                    pakowanie = pakowanie_k2.karton_k2
            
            elif pakowanie_metod == "K3":
                pakowanie_k3 = db.query(models.ButelkaDB.karton_k3).filter_by(index=index).first()
                if pakowanie_k3 is not None:
                    pakowanie = pakowanie_k3.karton_k3
                
            elif pakowanie_metod == "K4":
                pakowanie_k4 = db.query(models.ButelkaDB.karton_k4).filter_by(index=index).first()
                if pakowanie_k4 is not None:
                    pakowanie = pakowanie_k4.karton_k4
                
            elif pakowanie_metod == "K6":
                pakowanie_k6 = db.query(models.ButelkaDB.karton_k6).filter_by(index=index).first()
                if pakowanie_k6 is not None:
                    pakowanie = pakowanie_k6.karton_k6

            if pakowanie is None:
                error_msg = "Method packings is not available."
                
                # Створення вікна повідомлення про помилку
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText(error_msg)
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()   
            return pakowanie
            
        finally:
            db.close()
            
    #  Кількістть пшекладок на палеті
    def count_przekladok(self):
        height_box = float(self.ui.comboBox_7.currentText())
        height_buttle = self.wysokosc_butelki()
        paleta = 0.15
        
        result = int((height_box - paleta) / height_buttle * 1000)
        return result
        
    # Кількість бутилок на палеті
    def count_bottles(self):
        count_przekladok = self.count_przekladok()
        count_bottles = self.pakowanie_butelka()
        if count_bottles is not None:
            result = count_bottles * count_przekladok
            return result
        
        
    #  Вага палети
    def weight_palet(self):
        count_bottles = self.count_bottles()
        waga_bottle = float(self.ui.comboBox_27.currentText())
        choise_palet = self.ui.comboBox_9.currentText()
        palet = {"One Way pallet": 8, "Euro pallet": 15, "Plastic pallet": 8, "Karton": 0, "Not pallet": 8, "Euro Pal zwr.": 15}
        
        result = None

        for key, value in palet.items():
            if key == choise_palet:
                palet_value = value  
                print(palet_value)
                break  
        if count_bottles is not None:
            result = count_bottles * (waga_bottle / 1000) + palet_value
            print(result)
            return result
        
    # Кількість палет в замовленні
    def count_palets_order(self):
        count_order = int(self.ui.lineEdit_6.text())
        count_bottles = self.count_bottles()
        
        if count_bottles is not None:
            order_palet = count_order / count_bottles
            result_up = int(-(-order_palet // 1))
            return result_up
        
        
    # Кількість бутилок в замовленні згідно з кількістю палет
    def count_bottles_order(self):
        count_palets_order = self.count_palets_order()
        count_bottles = self.count_bottles()
        
        if count_bottles is not None:
            result = count_bottles * count_palets_order
            
            return result

        

    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Butelka()
    ui.show()
    sys.exit(app.exec_())