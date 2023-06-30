import configparser
import datetime
import sqlite3
from interface_v3 import *
# from title import PDFGenerator, inch
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


R_PET_PROCENT = 100 #%
P1 = 66.36 # Пакування Oktabina
P3 = 3.30 # Пакування Kosz
COST_START_SUR = 6.39 # zl



class Preforma(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Preforma, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
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

        self.ui.checkBox.stateChanged.connect(self.check_box_1)
        self.ui.checkBox_2.stateChanged.connect(self.check_box_2)
        self.ui.comboBox_7.currentIndexChanged.connect(self.view_label_5)

        self.ui.pushButton_2.clicked.connect(self.update_data)
        
        self.ui.pushButton.clicked.connect(self.button_click)
       
     
    # Блок подій оновлення ціни суровця
    def button_click(self):
        self.line_edit_pet_r_pet()
        if self.ui.checkBox_2.isChecked() == True:
            self.update_narzut()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
        
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Data updated")
        msg.setWindowTitle("Update")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        

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
        r_pet_list = ["0", "10", "25", "30", "50", "75", "100"]
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
        selected_item_index = self.ui.comboBox.currentText()
        r_pet_index = self.ui.comboBox_5.currentText()
        
        if r_pet_index == "0":
            self.ui.label_2.setText(f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "10":
            selected_item_index_Q = selected_item_index[:1] +"Q" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_Q}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "25":
            selected_item_index_W = selected_item_index[:1] +"W" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_W}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "30":
            selected_item_index_V = selected_item_index[:1] +"V" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_V}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "50":
            selected_item_index_X = selected_item_index[:1] +"X" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_X}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "75":
            selected_item_index_Y = selected_item_index[:1] +"Y" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_Y}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "100":
            selected_item_index_Z = selected_item_index[:1] +"Z" + selected_item_index[1:]
            self.ui.label_2.setText(f"{selected_item_index_Z}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        
    
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
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        float_value = float(result[0]) / 1000
        return float_value
    
    def cena_r_pet(self):
        conn = sqlite3.connect('data\\surowiec.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM Kurs WHERE surowiec = 'R-Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        float_value = float(result[0]) / 1000
        return float_value
    
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
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()

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
        # cost_color = str(cost_color, 4)
            
        
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
            quality = 10000
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
        # print(quantity_product)
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
            # print(weight_packaging)
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
    
    def date_time(self):
        date_time = datetime.datetime.now()
        return date_time.date()
    
    
    # Блок онослення даних
    def check_box_1(self, state):
        if state == QtCore.Qt.Checked:
            self.fill_combobox7()
            
        else:
            self.ui.comboBox_7.clear()
            self.ui.label_5.clear()
            self.ui.lineEdit.clear()
            
    def check_box_2(self, state):
        if state == QtCore.Qt.Checked:
            self.wiev_narzut()
            
        else:
            self.ui.label_7.clear()
            self.ui.lineEdit_3.clear()
    
    
    def fill_combobox7(self):
        numer_values = self.update_combo_7()
        self.ui.comboBox_7.addItems(numer_values)
    
    def update_combo_7(self):
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute("SELECT surowiec FROM Kurs WHERE surowiec IN ('Pet', 'R-Pet')")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.view_label_5()
        return data
    
    def view_label_5(self):
        sur = str(self.ui.comboBox_7.currentText())
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute(f"SELECT cena_za_kg FROM Kurs WHERE surowiec= '{sur}'")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        self.ui.label_5.setText(str(data))
        return data
    
    def line_edit_pet_r_pet(self):
        surowiec = self.ui.comboBox_7.currentText()
        cena = self.ui.lineEdit.text()
        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE surowiec = ?'''  
        cursor.execute(update_query, (cena, surowiec))
        conn.commit()
        conn.close()
    
        
        
    def wiev_narzut(self):
        conn = sqlite3.connect('data\surowiec.db')
        curs = conn.cursor()
        curs.execute("SELECT cena_za_kg FROM Kurs WHERE surowiec = 'Narzut'")
        result = curs.fetchall()
        data = [row[0] for row in result]
        curs.close()
        conn.commit()
        conn.close()
        print(data)
        self.ui.label_7.setText(str(data))
        return data
    
    def update_narzut(self):
        cena = self.ui.lineEdit_3.text()
        surowiec = "Narzut"

        conn = sqlite3.connect('data/surowiec.db')
        cursor = conn.cursor()
        update_query = '''UPDATE Kurs SET cena_za_kg = ? WHERE surowiec = ?'''  
        cursor.execute(update_query, (cena, surowiec))
        conn.commit()
        conn.close()
        
   
            


    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Preforma()
    ui.show()
    sys.exit(app.exec_())

    