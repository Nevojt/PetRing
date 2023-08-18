import configparser
from datetime import datetime
import sqlite3
from setting.interface_v4 import *
from PyQt5.QtWidgets import QMessageBox
from setting.dialog import *
from setting.dialog_update import *
from setting.excel_class import *
from setting.table_func import TableFunc
from openpyxl import load_workbook



R_PET_PROCENT = 100 #%
P1 = 66.36 # Пакування Oktabina
P3 = 3.30 # Пакування Kosz
COST_START_SUR = 6.39 # zl



class Preforma(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Preforma, self).__init__(parent)

        # Основне вікно
        self.ui = Ui_Preforma()
        self.ui.setupUi(self)
        
        # діалогове вікно
        self.dialog = QtWidgets.QDialog()
        self.ua = Ui_Dialog()
        self.ua.setupUi(self.dialog)
        
        # діалогове вікно update Pet, R-Pet 
        self.dialog_update = QtWidgets.QDialog()
        self.update = Ui_Dialog_Update()
        self.update.setupUi(self.dialog_update)
        
  
        
        self.ui.comboBox.currentIndexChanged.connect(self.update_combobox2)
        self.ui.comboBox_2.currentIndexChanged.connect(self.update_combobox3)
        self.ui.comboBox.activated.connect(self.update_r_pet_index)
        self.ui.comboBox.activated.connect(self.update_label_packing_list)
        
        self.ui.comboBox_2.activated.connect(self.update_r_pet_index)
        self.ui.comboBox_3.activated.connect(self.update_r_pet_index)
        
        self.ui.comboBox_3.activated.connect(self.update_label_packing_list)
        self.ui.comboBox_3.activated.connect(self.cost_start)
        self.ui.comboBox_4.activated.connect(self.cost_start)
        self.ui.comboBox_5.activated.connect(self.cost_start)
        self.ui.comboBox_4.activated.connect(self.total_cost_raw_color)
        self.ui.comboBox_5.activated.connect(self.total_cost_raw_material)
        self.ui.comboBox_6.activated.connect(self.upgate_packaging)
        self.ui.comboBox_3.activated.connect(self.cost_machine)
        
        self.fill_combobox1()
        self.initUIPreforma()
        self.initUIBarwwnik()
        self.updateComboBox_5()
        self.updateComboBox_6()
        self.view_label_r_pet()
        self.view_label_pet()
        self.wiev_narzut()
        self.date_wiev()
        self.view_label_kurs()
        

    

        # Кнопки головного вікна
        self.ui.pushButton_2.clicked.connect(self.update_data)
        self.ui.pushButton.clicked.connect(self.update_dialog)
        self.ui.pushButton_3.clicked.connect(self.open_dialog)
        
        # Кнопки діаовогово вікна
        self.ua.pushButton.clicked.connect(self.button_create_excel)
        self.ua.pushButton_2.clicked.connect(self.button_append_table)
        
        self.update.buttonBox.accepted.connect(self.update_buttons)
        self.update.buttonBox.rejected.connect(self.closed_update_dialog)
        
        # Подiя створення файла Excel
    def button_create_excel(self):
        print("Create excel")
        self.create_excel()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Excel created")
        msg.setWindowTitle("Create")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.dialog.close()
        
        # Подія додавання таблиці до існуючого файлу
    def button_append_table(self):
        self.append_table()
        print("Append table")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Append table")
        msg.setWindowTitle("Append")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.dialog.close()
        
        # Функція відкривання діаловогово вікна
    def open_dialog(self):
        lab = self.ui.label_2.text()
        self.ua.label.setText(lab)
        self.dialog.show()
        
       
        

    def fill_combobox1(self):
        numer_values = self.initUIPreforma()
        self.ui.comboBox.addItems(numer_values)

    def update_combobox2(self):
        selected_numer = self.ui.comboBox.currentText()
        gwint_values = self.updateComboBox_2(selected_numer)
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(gwint_values)

    def update_combobox3(self):
        selected_numer = self.ui.comboBox.currentText()
        selected_gwint = self.ui.comboBox_2.currentText()
        gramatura_values = self.updateComboBox_3(selected_numer, selected_gwint)
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems([str(value) for value in gramatura_values])
        
        
    def initUIPreforma(self):
        conn = sqlite3.connect('data\\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT Numer_Form FROM data")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data
        
    def initUIBarwwnik(self):
        conn = sqlite3.connect('data\\barwnik.db')
        curs = conn.cursor()
        curs.execute("SELECT Kolor_cecha FROM data")
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
                
        self.ui.comboBox_4.addItems(data)
        self.ui.comboBox_4.activated.connect(self.update_r_pet_index)

        
        
    def updateComboBox_2(self, numer):
        # Отримуємо вибраний елемент з першого QComboBox
        conn = sqlite3.connect('data\\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT Gwint FROM data WHERE Numer_Form=?", (numer,))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        # Оновлюємо другий QComboBox, встановлюючи відфільтровані дані як елементи
        return data
   
    def updateComboBox_3(self, numer, gwint):
        conn = sqlite3.connect('data\\preforma.db')
        curs = conn.cursor()
        curs.execute("SELECT Gramatura FROM data WHERE Numer_Form=? AND Gwint=?", (numer, gwint))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        return data


        
    # Заповнюємо comboBox_5 значеннями
    def updateComboBox_5(self):
        r_pet_list = ["0", "25", "30", "50", "75", "100"]
        self.ui.comboBox_5.addItems(r_pet_list)
        self.ui.comboBox_5.activated.connect(self.update_r_pet_index)
     
     # Заповнюємо comboBox_6 значеннями   
    def updateComboBox_6(self):
        packing = ["1", "3"]
        self.ui.comboBox_6.addItems(packing)
        self.ui.comboBox_6.activated.connect(self.update_r_pet_index)
        
    # Беремо значення кількості преформи в опакованні
    def update_label_packing_list(self):
        selected_item_index = self.ui.comboBox.currentText()
        selected_item_gwint = self.ui.comboBox_2.currentText()
        selected_item_waga = self.ui.comboBox_3.currentText()

        # Connect to the SQLite database
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()

        # Retrieve the filtered data from the SQLite database
        query = "SELECT P1_P3 FROM data WHERE Numer_Form=? AND Gwint=? AND Gramatura=?"
        cursor.execute(query, (selected_item_index, selected_item_gwint, selected_item_waga))
        filtered_data_pack = sorted(set([row[0] for row in cursor.fetchall()]))

        # Close the database connection
        cursor.close()
        conn.close()

        return filtered_data_pack[0]

        
        
    # Змінюємо індекс згідно кількості R-Pet
    def update_r_pet_index(self):
        packing_list = self.update_label_packing_list()
        r_pet_index = self.ui.comboBox_5.currentText()
        index = f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}"
        
        if r_pet_index == "0":
            self.ui.label_2.setText(index)    
        # elif r_pet_index == "10":
        #     indexQ = index[:1] +"Q" + index[1:]
            # self.ui.label_2.setText(indexQ)
        elif r_pet_index == "25":
            indexW = index[:1] +"W" + index[1:]
            self.ui.label_2.setText(indexW)
        elif r_pet_index == "30":
            indexV = index[:1] +"V" + index[1:]
            self.ui.label_2.setText(indexV)
        elif r_pet_index == "50":
            indexX = index[:1] +"X" + index[1:]
            self.ui.label_2.setText(indexX)
        elif r_pet_index == "75":
            indexY = index[:1] + "Y" + index[1:]
            self.ui.label_2.setText(indexY)
        elif r_pet_index == "100":
            indexZ = index[:1] + "Z" + index[1:]
            self.ui.label_2.setText(indexZ)
       
    def cost_start(self):
        color_box_4 = self.ui.comboBox_4.currentText()
        choice_r_pet = self.ui.comboBox_5.currentText()
        index_preforma = f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}"

        # Встановлюємо з'єднання з базою даних
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()

        # Виконуємо запит до бази даних для отримання значень стовпців "Koszt", "Wydajnosc" та "Gramatura"
        query = '''
            SELECT Koszt, Wydajnosc_na_godzinu, Gramatura FROM data WHERE Indeks = ?
        '''
        cursor.execute(query, (index_preforma,))
        row = cursor.fetchone()
        koszt = float(row[0])
        wydajnosc = float(row[1])
        gramatura = float(row[2])

        # Закриваємо з'єднання з базою даних
        conn.close()

            
        if color_box_4 == "X":
            if int(choice_r_pet) > 0:
                self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR)
                self.koszt_urochom_r_pet = self.koszt_urochom + 3 * koszt
                return self.koszt_urochom, self.koszt_urochom_r_pet
            else:
                self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR)
                self.koszt_urochom_r_pet = 0
                return self.koszt_urochom, self.koszt_urochom_r_pet
        else:
            if int(choice_r_pet) > 0:
                self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR) * 3
                self.koszt_urochom_r_pet = self.koszt_urochom + 3 * koszt
                return self.koszt_urochom, self.koszt_urochom_r_pet
            else:
                self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR) * 3
                self.koszt_urochom_r_pet = 0
                return self.koszt_urochom, self.koszt_urochom_r_pet

    def cena_pet(self):
        kurs = self.cena_euro()
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        cena_sur = result[0] * kurs
        float_value = float(cena_sur) / 1000
        return float_value, cena_sur
    
    def cena_r_pet(self):
        kurs = self.cena_euro()
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'R-Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        cena_sur = result[0] * kurs
        float_value = float(cena_sur) / 1000
        return float_value, cena_sur
    
    def cena_euro(self):
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'EURO' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        float_value = float(result[0])
        return float_value
    
        

    # Рахуємо ціну продукції 1000 штук з урахуванням барвника та суровця Pet/R-pet 
    def total_cost_raw_material(self):   # Total Cost Raw material for 1000 pcs
        
        choice_r_pet = int(self.ui.comboBox_5.currentText()) # R-Pet procentent
        kurs_pet = self.cena_pet()[0]
        kurs_r_pet = self.cena_r_pet()[0]

        if choice_r_pet == 0:
            total_result = kurs_pet
        elif choice_r_pet > 0 and choice_r_pet <= 99: 
            fomula_pet = (R_PET_PROCENT - choice_r_pet)
            cost_pet = kurs_pet * (choice_r_pet / 100)
            input_cost = kurs_pet - cost_pet
            cost_pet = kurs_r_pet * (fomula_pet / 100)
            input_cost_rpet = kurs_r_pet - cost_pet
            total_result = input_cost + input_cost_rpet
        elif choice_r_pet == 100:
            total_result = kurs_r_pet
        return total_result
        
      
        
    def total_cost_raw_color(self):
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        total_result = self.total_cost_raw_material()
        
        # Встановлюємо з'єднання з базою даних
        conn = sqlite3.connect('data\\barwnik.db')
        cursor = conn.cursor()

        # Виконуємо запит до таблиці "data" з бази даних
        query = "SELECT Cena_za_kg, Dozowanie FROM data WHERE Kolor_cecha = ?"  
        cursor.execute(query, (choice_color,))

        # Отримуємо результат запиту
        result = cursor.fetchone()

        if result:
            uniq_cena_barwnik = result[0]
            doza_barwnika = float(result[1])
            
            if doza_barwnika > 0:
                choice_gram = float(choice_gram)
                self.result_il_barwnika = choice_gram * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec

    # Визначаємо ціну за опакованню за 1000 штук

    def upgate_packaging(self):
        choice_packaging = self.ui.comboBox_6.currentText()
        packing_list = self.update_label_packing_list()

        # Встановлюємо з'єднання з базою даних
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()

        # Виконуємо запит до бази даних для отримання значень зі стовпця "Packing_list"
        query = '''
            SELECT P1_P3 FROM data WHERE P1_P3 = ?
        '''
        cursor.execute(query, (packing_list,))
        packaging_list = cursor.fetchone()[0]
        packaging_list = float(packaging_list)

        # Закриваємо з'єднання з базою даних
        conn.close()

        if choice_packaging == "1":
            result = P1 * 1000 / packaging_list
        elif choice_packaging == "3":
            result = P3 * 1000 / packaging_list
        self.result = round(result, 4)
        # print(f"Packing cost for 1000 pcs - {self.result} PLN")
        return self.result

    
    # Cost Machine for 1000 pcs, розрахунок коштів потрачених на машину за 1000 штук
    def cost_machine(self):
        index_preforma = f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}"
        
        # Встановлюємо з'єднання з базою даних
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()

        # Виконуємо запит до бази даних для отримання значень стовпців "Cost" та "Ilost"
        query = '''
            SELECT Koszt, Wydajnosc_na_godzinu FROM data WHERE Indeks = ?
        '''
        cursor.execute(query, (index_preforma,))
        row = cursor.fetchone()
        cost = float(row[0])
        ilost = float(row[1])

        # Закриваємо з'єднання з базою даних
        conn.close()

        self.cost_machines = (cost / ilost) * 1000
        # print(f"Cost Machine for 1000 pcs - {self.cost_machines} PLN")
        return float(self.cost_machines)

        
    # Створити функцію, яка оновлює дані для комірки
    def update_data(self):
        
        # Оновлення даних
        new_data = self.update_label_packing_list()
        packing_cost = str(round(self.upgate_packaging(), 2))
        cost_machin_tys = str(round(self.cost_machine(), 2))
        cost_color = round(self.total_cost_raw_color()[1], 2)
        many_packaging = str(self.quality_cost())
        quantity_product = str(self.quality_cost_product())
        weight_packaging = str(round(self.total_weight(), 2))
        cost_raw_machines = str(round(self.total_cost_raw_color()[2], 2))
        waste_preform = str(round(self.waste_for_preforms(), 2))
        cost_color_batch = str(round(self.cost_color_batch_waste(), 2))
        total_cost_raw = str(round(self.total_cost_raw_material_tys(), 2))
        cost_start_machine = str(round(self.cost_start_machine(), 2))
        totat_cost_start = str(round(self.total_cost_machine(), 2))
        cost_narzut = str(round(self.total_cost_narzut(), 2))
        finish = str(round(self.total_cost_finish(), 2))
        euro_cost = str(round(self.euro_cost(), 2))
 
            
        
        self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(new_data))
        self.ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(many_packaging))
        self.ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(quantity_product))
        self.ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(weight_packaging))
        self.ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(f"{cost_raw_machines} zl"))
        self.ui.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(f"{waste_preform} zl"))
        self.ui.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(f"{cost_color} zl"))
        self.ui.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem(f"{cost_color_batch} zl"))
        self.ui.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem(f"{total_cost_raw} zl"))
        self.ui.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem(f"{packing_cost} zl"))
        self.ui.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem(f"{cost_start_machine} zl"))
        self.ui.tableWidget.setItem(11, 1, QtWidgets.QTableWidgetItem(f"{cost_machin_tys} zl"))
        self.ui.tableWidget.setItem(12, 1, QtWidgets.QTableWidgetItem(f"{totat_cost_start} zl"))
        self.ui.tableWidget.setItem(13, 1, QtWidgets.QTableWidgetItem(f"{cost_narzut} zl"))
        self.ui.tableWidget.setItem(14, 1, QtWidgets.QTableWidgetItem(f"{finish} zl"))
        self.ui.tableWidget.setItem(15, 1, QtWidgets.QTableWidgetItem(f"{finish} zl"))
        self.ui.tableWidget.setItem(16, 1, QtWidgets.QTableWidgetItem(f"{euro_cost} €"))

        
        
    # Зчитуємо кількість преформи потрібно облічити
    def quality_cost(self):
        new_data = int(self.update_label_packing_list())
        try:
            quality = self.ui.lineEdit_2.text()
            
        except (AttributeError, ValueError):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Invalid or missing quality value.\nIlosc dla klienta musi być wpisana\n ilosc Default - 10000")
            msg_box.setWindowTitle("Warning")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            quality = 100000
            many_packaging = quality // new_data # Отримуємо калькість опакувань
            return many_packaging
        else:
            many_packaging = int(quality) // new_data # Отримуємо калькість опакувань
            # print(many_packaging)
            return many_packaging
    
    # Облічуємо кількість праформи в опакуванях
    def quality_cost_product(self):
        new_data = int(self.update_label_packing_list())
        many_packaging = int(self.quality_cost())
        quantity_product = many_packaging * new_data
        return quantity_product
    
    # Вага преформи з опакуваням
    def total_weight(self):
        oktabina = 14
        kosz = 67
        new_data = int(self.update_label_packing_list())
        choice_gram = float(self.ui.comboBox_3.currentText())
        choice_packaging = self.ui.comboBox_6.currentText()
        weight_preform = new_data * (choice_gram / 1000)
        
        if choice_packaging == "1":
            weight_packaging = weight_preform + oktabina
        elif choice_packaging == "3":
            weight_packaging = weight_preform + kosz
        return weight_packaging
        
    def waste_for_preforms(self):
        cost_raw_machines = float(self.total_cost_raw_color()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def cost_color_batch_waste(self):
        cost_color = float(self.total_cost_raw_color()[1])
        cost_color_batch = cost_color * 4.5 / 100
        return cost_color_batch
    
    def total_cost_raw_material_tys(self):
        cost_color = float(self.total_cost_raw_color()[1]) # Barwnik
        cost_raw_machines = float(self.total_cost_raw_color()[2]) # surowiec 
        waste_preform = round(self.waste_for_preforms(), 2)
        cost_color_batch = round(self.cost_color_batch_waste(), 2)
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
    
    
    def cost_start_machine(self):
        cost_start_pet = self.cost_start()[0]
        cost_start_r_pet = self.cost_start()[1]
        quality = int(self.ui.lineEdit_2.text())

        
        start = max(cost_start_pet, cost_start_r_pet)
        result = start / quality * 1000
        return result
    
    def total_cost_machine(self):
        cost_start = round(self.cost_start_machine(), 4)
        cost_machin = round(self.cost_machine(), 4)
        result = cost_start + cost_machin
        return result
    
    def total_cost_narzut(self):
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'Narzut' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        narzut = result[0]
        
        total_cost = round(self.total_cost_machine(), 4)
        result = total_cost + (total_cost * narzut / 100)
        return result 
    
    def total_cost_finish(self):
        total_cost_raw = round(self.total_cost_raw_material_tys(), 2)
        packaging = round(self.upgate_packaging(), 2)
        narzut = round(self.total_cost_narzut(), 2)
        result = total_cost_raw + packaging + narzut
        return result
    
    def euro_cost(self):
        euro = self.cena_euro()
        total_cost_finish = round(self.total_cost_finish(), 2)
        result = total_cost_finish / euro
        return result
    
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
            self.update_Pet()
        if len(edit_3) > 0:
            self.update_R_Pet()
        if len(edit_4) > 0:
            self.update_narzut_db()
        else:
            print("No update")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Database update")
        msg.setWindowTitle("Update")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    
    def update_kurs(self):
        cena = self.update.lineEdit.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE kurs_id = 4'''
        cursor.execute(update_query, (cena,))
        conn.commit()
        conn.close()
        
    def update_Pet(self):
        cena = self.update.lineEdit_2.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE kurs_id = 1'''
        cursor.execute(update_query, (cena,))
        conn.commit()
        conn.close()
        
    def update_R_Pet(self):
        cena = self.update.lineEdit_3.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE kurs_id = 2'''
        cursor.execute(update_query, (cena,))
        conn.commit()
        conn.close()
        
    def update_narzut_db(self):
        cena = self.update.lineEdit_4.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE kurs_id = 3'''
        cursor.execute(update_query, (cena,))
        conn.commit()
        conn.close()
    
  
    
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
        self.ui.label_11.setText(str(data[0]))
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
        self.ui.label_5.setText(str(data[0]))
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
        self.ui.label_14.setText(str(data[0]))
        return data
    
    # Змінюємо ціну суровца
    def line_edit_pet_r_pet(self):
        surowiec = self.ui.comboBox_7.currentText()
        cena = self.ui.lineEdit.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE surowiec = ?'''  
        cursor.execute(update_query, (cena, surowiec))
        conn.commit()
        conn.close()
    
        
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
        self.ui.label_7.setText(str(data[0]))
        return data
    
    def date_wiev(self):
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute("SELECT date_time FROM Kurs WHERE kurs_id=5")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_12.setText(str(data[0]))
        return data
    
    # Змінюємо процент накладних витрат
    def update_narzut(self):
        cena = self.ui.lineEdit_3.text()
        surowiec = "Narzut"

        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE surowiec = ?'''  
        cursor.execute(update_query, (cena, surowiec))
        conn.commit()
        conn.close()
        
    def date_update(self):
        date_time = datetime.now()
        date = date_time.strftime("%d-%m-%y %H:%M")
        
        surowiec = 5
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET date_time = ? WHERE kurs_id = ?'''  
        cursor.execute(update_query, (date, surowiec))
        conn.commit()
        conn.close()
        
        # Блок створення excel файлу
    def create_excel(self):
        r_pet = ('0%', '25%', '30%', '50%', '75%', '100%')
        self.table_func = TableFunc(self)
        # cena_r_pet = self.cena_r_pet()[1]
        
        
        config = configparser.ConfigParser()
        config.read('config.ini')

        last_filename = config.get('File', 'LastFilename')
        parts = last_filename.split("-")
        number = int(parts[1]) + 1
        new_filename = "C:/pdf_files/" + parts[0] + "-" + str(number) + "-" + parts[2]
        second_filename = new_filename[13:]

        
        index = self.table_func.index_one()
        
        # Блок файлу
        table = ExcelTable()
        # Перший та другий стовпчик
        for i, value in enumerate(index):
            table.add_data(i+2, 'A', [value])
            table.add_data(i+2, 'B', [index[0]])
            
        # Третій стовпчик
        for i, value in enumerate(r_pet):
            table.add_data(i+2, 'C', [value])
            
        #  Date time
        date = self.table_func.date_time()
        for i, value in enumerate(date):
            table.add_data(i+2, 'D', [value])
            
        # цінa Pet
        pet = self.table_func.index_E()
        for i, value in enumerate(pet):
            table.add_data(i+2, 'E', [value])
            
        # цінa R-Pet
        r_pets = self.table_func.index_F()
        for i, value in enumerate(r_pets):
            table.add_data(i+2, 'F', [value])
            
        # Neck
        neck = self.table_func.index_G()
        for i, value in enumerate(neck):
            table.add_data(i+2, 'G', [value])
            
        
        # Кількість грам
        gram = self.table_func.index_H()
        for i, value in enumerate(gram):
            table.add_data(i+2, 'H', [value])
            
        # Кількість мілілітрів
        ml = self.table_func.index_I()
        for i, value in enumerate(ml):
            table.add_data(i+2, 'I', [value])
            
        # Колір преформи
        color = self.table_func.index_J()
        for i, value in enumerate(color):
            table.add_data(i+2, 'J', [value])
            
        # Розмір палети
        palet = self.table_func.index_K()
        for i, value in enumerate(palet):
            table.add_data(i+2, 'K', [value])
            
        #  Вага плети(kg)
        weight = self.table_func.index_L()
        for i, value in enumerate(weight):
            table.add_data(i+2, 'L', [value])
            
        # Кількість товару на палеті aбо кощі
        bottles = self.table_func.index_M()
        for i, value in enumerate(bottles):
            table.add_data(i+2, 'M', [value])
          
        #  Блок  заповненя ціною  
        list_N = self.table_func.list_N()
        for i, value in enumerate(list_N):
            table.add_data(i+2, 'N', [value])
            
        list_O = self.table_func.list_O()
        for i, value in enumerate(list_O):
            table.add_data(i+2, 'O', [value])
            
        list_P = self.table_func.list_P()
        for i, value in enumerate(list_P):
            table.add_data(i+2, 'P', [value])
     
        list_Q = self.table_func.list_Q()
        for i, value in enumerate(list_Q):
            table.add_data(i+2, 'Q', [value])
        
        list_R = self.table_func.list_R()
        for i, value in enumerate(list_R):
            table.add_data(i+2, 'R', [value])
            
        list_S = self.table_func.list_S()
        for i, value in enumerate(list_S):
            table.add_data(i+2, 'S', [value])
        
        list_T = self.table_func.list_T()
        for i, value in enumerate(list_T):
            table.add_data(i+2, 'T', [value])
            
        list_U = self.table_func.list_U()
        for i, value in enumerate(list_U):
            table.add_data(i+2, 'U', [value])
            
        list_V = self.table_func.list_V()
        for i, value in enumerate(list_V):
            table.add_data(i+2, 'V', [value])
            
        list_W = self.table_func.list_W()
        for i, value in enumerate(list_W):
            table.add_data(i+2, 'W', [value])
        
        list_X = self.table_func.list_X()
        for i, value in enumerate(list_X):
            table.add_data(i+2, 'X', [value])
        
        list_Y = self.table_func.list_Y()
        for i, value in enumerate(list_Y):
            table.add_data(i+2, 'Y', [value])
        
        list_Z = self.table_func.list_Z()
        for i, value in enumerate(list_Z):
            table.add_data(i+2, 'Z', [value])
        
        list_AA = self.table_func.list_AA()
        for i, value in enumerate(list_AA):
            table.add_data(i+2, 'AA', [value])
            
        index_AB = self.table_func.index_AB()
        for i, value in enumerate(index_AB):
            table.add_data(i+2, 'AB', [value])
            
        table.save(second_filename)
        
        
        # Збереження нового імені файлу
        config.set('File', 'LastFilename', second_filename)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
        
    def append_table(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        last_filename = config.get('File', 'LastFilename')
            
        self.table_func = TableFunc(self)
        index = self.table_func.index_one()
        # Завантажуємо існуючу книгу
        wb = load_workbook(filename = last_filename)

        # Вибираємо активний лист (або ви можете вибрати лист за назвою wb.get_sheet_by_name('Sheet1'))
        ws = wb.active 

        start_row = ws.max_row + 1
        
        next_row = start_row
        for value in index:
            ws.cell(row=next_row, column=1, value=value)
            next_row += 1
            
        next_row = start_row  
        for value in index:
            ws.cell(row=next_row, column=2, value=index[0])
            next_row += 1
            
        # Третій стовпчик
        next_row = start_row
        r_pet = ('0%', '10%', '25%', '30%', '50%', '75%', '100%')
        for value in r_pet:
            ws.cell(row=next_row, column=3, value=value)
            next_row += 1

            
        #  Date time
        next_row = start_row
        date = self.table_func.date_time()
        for value in date:
            ws.cell(row=next_row, column=4, value=value)
            next_row += 1
            
        # цінa Pet
        next_row = start_row
        pet = self.table_func.index_E()
        for value in pet:
            ws.cell(row=next_row, column=5, value=value)
            next_row += 1
            
        # цінa R-Pet
        next_row = start_row
        r_pets = self.table_func.index_F()
        for value in r_pets:
            ws.cell(row=next_row, column=6, value=value)
            next_row += 1
            
        # Neck
        next_row = start_row
        neck = self.table_func.index_G()
        for value in neck:
            ws.cell(row=next_row, column=7, value=value)
            next_row += 1
            
        
        # Кількість грам
        next_row = start_row
        gram = self.table_func.index_H()
        for value in gram:
            ws.cell(row=next_row, column=8, value=value)
            next_row += 1
            
        # Кількість мілілітрів
        next_row = start_row
        ml = self.table_func.index_I()
        for value in ml:
            ws.cell(row=next_row, column=9, value=value)
            next_row += 1
            
        # Колір преформи
        next_row = start_row
        color = self.table_func.index_J()
        for value in color:
            ws.cell(row=next_row, column=10, value=value)
            next_row += 1
            
        # Розмір палети
        next_row = start_row
        palet = self.table_func.index_K()
        for value in palet:
            ws.cell(row=next_row, column=11, value=value)
            next_row += 1
            
        #  Вага плети(kg)
        next_row = start_row
        weight = self.table_func.index_L()
        for value in weight:
            ws.cell(row=next_row, column=12, value=value)
            next_row += 1
            
        # Кількість товару на палеті aбо кощі
        next_row = start_row
        bottles = self.table_func.index_M()
        for value in bottles:
            ws.cell(row=next_row, column=13, value=value)
            next_row += 1
          
        #  Блок  заповненя ціною  
        next_row = start_row
        list_N = self.table_func.list_N()
        for value in list_N:
            ws.cell(row=next_row, column=14, value=value)
            next_row += 1
            
        next_row = start_row
        list_O = self.table_func.list_O()
        for value in list_O:
            ws.cell(row=next_row, column=15, value=value)
            next_row += 1
        
        next_row = start_row
        list_P = self.table_func.list_P()
        for value in list_P:
            ws.cell(row=next_row, column=16, value=value)
            next_row += 1
            
        next_row = start_row
        list_Q = self.table_func.list_Q()
        for value in list_Q:
            ws.cell(row=next_row, column=17, value=value)
            next_row += 1
            
        next_row = start_row
        list_R = self.table_func.list_R()
        for value in list_R:
            ws.cell(row=next_row, column=18, value=value)
            next_row += 1
        
        next_row = start_row
        list_S = self.table_func.list_S()
        for value in list_S:
            ws.cell(row=next_row, column=19, value=value)
            next_row += 1
        
        next_row = start_row
        list_T = self.table_func.list_T()
        for value in list_T:
            ws.cell(row=next_row, column=20, value=value)
            next_row += 1
            
        next_row = start_row
        list_U = self.table_func.list_U()
        for value in list_U:
            ws.cell(row=next_row, column=21, value=value)
            next_row += 1
        
        next_row = start_row
        list_V = self.table_func.list_V()
        for value in list_V:
            ws.cell(row=next_row, column=22, value=value)
            next_row += 1
        
        next_row = start_row
        list_W = self.table_func.list_W()
        for value in list_W:
            ws.cell(row=next_row, column=23, value=value)
            next_row += 1
        
        next_row = start_row
        list_X = self.table_func.list_X()
        for value in list_X:
            ws.cell(row=next_row, column=24, value=value)
            next_row += 1
        
        next_row = start_row
        list_Y = self.table_func.list_Y()
        for value in list_Y:
            ws.cell(row=next_row, column=25, value=value)
            next_row += 1
        
        next_row = start_row
        list_Z = self.table_func.list_Z()
        for value in list_Z:
            ws.cell(row=next_row, column=26, value=value)
            next_row += 1
        
        next_row = start_row
        list_AA = self.table_func.list_AA()
        for value in list_AA:
            ws.cell(row=next_row, column=27, value=value)
            next_row += 1
            
        next_row = start_row
        index_AB = self.table_func.index_AB()
        for value in index_AB:
            ws.cell(row=next_row, column=28, value=value)
            next_row += 1
            
            
        

        # Зберігаємо книгу
        wb.save(filename = last_filename)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Preforma()
    ui.show()
    sys.exit(app.exec_())

    