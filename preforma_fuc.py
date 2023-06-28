import configparser
import datetime
import sqlite3
from interface_v2 import *
from title import PDFGenerator, inch
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


R_PET_PROCENT = 100 #%
P1 = 66.36 # Пакування Oktabina
P3 = 3.30 # Пакування Kosz
COST_START_SUR = 6.39 # zl



class Preforma(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
        

        self.ui.pushButton.clicked.connect(self.update_data)
       
        self.ui.pushButton_2.clicked.connect(self.generator_pdf)
        
        
        

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
            self.ui.label.setText(f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "10":
            selected_item_index_Q = selected_item_index[:1] +"Q" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_Q}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "25":
            selected_item_index_W = selected_item_index[:1] +"W" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_W}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "30":
            selected_item_index_V = selected_item_index[:1] +"V" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_V}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "50":
            selected_item_index_X = selected_item_index[:1] +"X" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_X}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "75":
            selected_item_index_Y = selected_item_index[:1] +"Y" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_Y}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        elif r_pet_index == "100":
            selected_item_index_Z = selected_item_index[:1] +"Z" + selected_item_index[1:]
            self.ui.label.setText(f"{selected_item_index_Z}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}")
        
    
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
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM kurs WHERE surowiec = 'Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        float_value = float(result[0])
        return float_value
    
    def cena_r_pet(self):
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM kurs WHERE surowiec = 'R_Pet' '''
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        float_value = float(result[0])
        return float_value
    
    def cena_euro(self):
        conn = sqlite3.connect('data\\preforma.db')
        cursor = conn.cursor()
        
        query = '''SELECT cena_za_kg FROM kurs WHERE surowiec = 'EURO' '''
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
            
        
        self.ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(new_data))
        self.ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(many_packaging))
        self.ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(quantity_product))
        self.ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(weight_packaging))
        self.ui.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(f"{cost_raw_machines} zl"))
        self.ui.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(f"{waste_preform} zl"))
        self.ui.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem(f"{cost_color} zl"))
        self.ui.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem(f"{cost_color_batch} zl"))
        self.ui.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem(f"{total_cost_raw} zl"))
        self.ui.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem(f"{packing_cost} zl"))
        self.ui.tableWidget.setItem(11, 1, QtWidgets.QTableWidgetItem(f"{cost_start_machine} zl"))
        self.ui.tableWidget.setItem(12, 1, QtWidgets.QTableWidgetItem(f"{cost_machin_tys} zl"))
        self.ui.tableWidget.setItem(13, 1, QtWidgets.QTableWidgetItem(f"{totat_cost_start} zl"))
        self.ui.tableWidget.setItem(14, 1, QtWidgets.QTableWidgetItem(f"{cost_narzut} zl"))
        self.ui.tableWidget.setItem(15, 1, QtWidgets.QTableWidgetItem(f"{finish} zl"))
        self.ui.tableWidget.setItem(16, 1, QtWidgets.QTableWidgetItem(f"{finish} zl"))
        self.ui.tableWidget.setItem(17, 1, QtWidgets.QTableWidgetItem(f"{euro_cost} €"))

        
        
    # Зчитуємо кількість преформи потрібно облічити
    def quality_cost(self):
        new_data = int(self.update_label_packing_list())
        try:
            quality = self.ui.tableWidget.item(0, 1).text()
            
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
        try:
            quality = self.ui.tableWidget.item(0, 1).text()
        except (AttributeError, ValueError):
            quality = 10000
        else:
            quality = int(quality)
        
        start = max(cost_start_pet, cost_start_r_pet)
        result = start / quality * 1000
        # print(result)
        return result
    
    def total_cost_machine(self):
        cost_start = round(self.cost_start_machine(), 4)
        cost_machin = round(self.cost_machine(), 4)
        result = cost_start + cost_machin
        return result
    
    def total_cost_narzut(self):
        total_cost = round(self.total_cost_machine(), 4)
        result = total_cost + (total_cost * 10 / 100)
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
    
        
        
         # Блок для PDF
    def generator_pdf(self):

        
        # Додaємо дані для таблиці
        row_2 = self.row_2_pdf()
        row_3 = self.row_3_pdf()
        row_4 = self.row_4_pdf()
        row_5 = self.row_5_pdf()
        row_6 = self.row_6_pdf()
        row_7 = self.row_7_pdf()
        row_8 = self.row_8_pdf()
        row_9 = self.row_9_pdf()
        row_10 = self.row_10_pdf()
        row_11 = self.row_11_pdf()
        row_12 = self.row_12_pdf()
        row_13 = self.row_13_pdf()
        row_14 = self.row_14_pdf()
        row_15 = self.row_15_pdf()
        row_16 = self.row_16_pdf()
        
        row_2_pdf_col_10 = self.row_2_pdf_col_10()
        row_3_pdf_col_10 = self.row_3_pdf_col_10()
        row_4_pdf_col_10 = self.row_4_pdf_col_10()
        row_5_pdf_col_10 = self.row_5_pdf_col_10()
        row_6_pdf_col_10 = self.row_6_pdf_col_10()
        row_7_pdf_col_10 = self.row_7_pdf_col_10()
        row_8_pdf_col_10 = self.row_8_pdf_col_10()
        row_9_pdf_col_10 = self.row_9_pdf_col_10()
        row_10_pdf_col_10 = self.row_10_pdf_col_10()
        row_11_pdf_col_10 = self.row_11_pdf_col_10()
        row_12_pdf_col_10 = self.row_12_pdf_col_10()
        row_13_pdf_col_10 = self.row_13_pdf_col_10()
        row_14_pdf_col_10 = self.row_14_pdf_col_10()
        row_15_pdf_col_10 = self.row_15_pdf_col_10()
        row_16_pdf_col_10 = self.row_16_pdf_col_10()
        
        row_2_pdf_col_25 = self.row_2_pdf_col_25()
        row_3_pdf_col_25 = self.row_3_pdf_col_25()
        row_4_pdf_col_25 = self.row_4_pdf_col_25()
        row_5_pdf_col_25 = self.row_5_pdf_col_25()
        row_6_pdf_col_25 = self.row_6_pdf_col_25()
        row_7_pdf_col_25 = self.row_7_pdf_col_25()
        row_8_pdf_col_25 = self.row_8_pdf_col_25()
        row_9_pdf_col_25 = self.row_9_pdf_col_25()
        row_10_pdf_col_25 = self.row_10_pdf_col_25()
        row_11_pdf_col_25 = self.row_11_pdf_col_25()
        row_12_pdf_col_25 = self.row_12_pdf_col_25()
        row_13_pdf_col_25 = self.row_13_pdf_col_25()
        row_14_pdf_col_25 = self.row_14_pdf_col_25()
        row_15_pdf_col_25 = self.row_15_pdf_col_25()
        row_16_pdf_col_25 = self.row_16_pdf_col_25()
        
        row_2_pdf_col_30 = self.row_2_pdf_col_30()
        row_3_pdf_col_30 = self.row_3_pdf_col_30()
        row_4_pdf_col_30 = self.row_4_pdf_col_30()
        row_5_pdf_col_30 = self.row_5_pdf_col_30()
        row_6_pdf_col_30 = self.row_6_pdf_col_30()
        row_7_pdf_col_30 = self.row_7_pdf_col_30()
        row_8_pdf_col_30 = self.row_8_pdf_col_30()
        row_9_pdf_col_30 = self.row_9_pdf_col_30()
        row_10_pdf_col_30 = self.row_10_pdf_col_30()
        row_11_pdf_col_30 = self.row_11_pdf_col_30()
        row_12_pdf_col_30 = self.row_12_pdf_col_30()
        row_13_pdf_col_30 = self.row_13_pdf_col_30()
        row_14_pdf_col_30 = self.row_14_pdf_col_30()
        row_15_pdf_col_30 = self.row_15_pdf_col_30()
        row_16_pdf_col_30 = self.row_16_pdf_col_30()
        
        row_2_pdf_col_50 = self.row_2_pdf_col_50()
        row_3_pdf_col_50 = self.row_3_pdf_col_50()
        row_4_pdf_col_50 = self.row_4_pdf_col_50()
        row_5_pdf_col_50 = self.row_5_pdf_col_50()
        row_6_pdf_col_50 = self.row_6_pdf_col_50()
        row_7_pdf_col_50 = self.row_7_pdf_col_50()
        row_8_pdf_col_50 = self.row_8_pdf_col_50()
        row_9_pdf_col_50 = self.row_9_pdf_col_50()
        row_10_pdf_col_50 = self.row_10_pdf_col_50()
        row_11_pdf_col_50 = self.row_11_pdf_col_50()
        row_12_pdf_col_50 = self.row_12_pdf_col_50()
        row_13_pdf_col_50 = self.row_13_pdf_col_50()
        row_14_pdf_col_50 = self.row_14_pdf_col_50()
        row_15_pdf_col_50 = self.row_15_pdf_col_50()
        row_16_pdf_col_50 = self.row_16_pdf_col_50()
        
        row_2_pdf_col_75 = self.row_2_pdf_col_75()
        row_3_pdf_col_75 = self.row_3_pdf_col_75()
        row_4_pdf_col_75 = self.row_4_pdf_col_75()
        row_5_pdf_col_75 = self.row_5_pdf_col_75()
        row_6_pdf_col_75 = self.row_6_pdf_col_75()
        row_7_pdf_col_75 = self.row_7_pdf_col_75()
        row_8_pdf_col_75 = self.row_8_pdf_col_75()
        row_9_pdf_col_75 = self.row_9_pdf_col_75()
        row_10_pdf_col_75 = self.row_10_pdf_col_75()
        row_11_pdf_col_75 = self.row_11_pdf_col_75()
        row_12_pdf_col_75 = self.row_12_pdf_col_75()
        row_13_pdf_col_75 = self.row_13_pdf_col_75()
        row_14_pdf_col_75 = self.row_14_pdf_col_75()
        row_15_pdf_col_75 = self.row_15_pdf_col_75()
        row_16_pdf_col_75 = self.row_16_pdf_col_75()
        
        row_2_pdf_col_100 = self.row_2_pdf_col_100()
        row_3_pdf_col_100 = self.row_3_pdf_col_100()
        row_4_pdf_col_100 = self.row_4_pdf_col_100()
        row_5_pdf_col_100 = self.row_5_pdf_col_100()
        row_6_pdf_col_100 = self.row_6_pdf_col_100()
        row_7_pdf_col_100 = self.row_7_pdf_col_100()
        row_8_pdf_col_100 = self.row_8_pdf_col_100()
        row_9_pdf_col_100 = self.row_9_pdf_col_100()
        row_10_pdf_col_100 = self.row_10_pdf_col_100()
        row_11_pdf_col_100 = self.row_11_pdf_col_100()
        row_12_pdf_col_100 = self.row_12_pdf_col_100()
        row_13_pdf_col_100 = self.row_13_pdf_col_100()
        row_14_pdf_col_100 = self.row_14_pdf_col_100()
        row_15_pdf_col_100 = self.row_15_pdf_col_100()
        row_16_pdf_col_100 = self.row_16_pdf_col_100()
        
      
        
        index = self.ui.label.text()
        weight = self.ui.comboBox_3.currentText()
        pcs_per_pallet = self.update_label_packing_list()
        date = self.date_time()
        weight_pack = round(self.total_weight())
        
        
        

        config = configparser.ConfigParser()
        config.read('config.ini')

        last_filename = config.get('File', 'LastFilename')
        parts = last_filename.split("-")
        number = int(parts[1]) + 1
        new_filename = "C:/pdf_files/" + parts[0] + "-" + str(number) + "-" + parts[2]
        oferta = parts[0] + "/" + str(number) + "/" + parts[2]
        second_filename = new_filename[13:]
        print(new_filename)
        
        # Здійснення генерації PDF і використання нового імені файлу
        pdf_generator = PDFGenerator(new_filename)
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(f"PDF {new_filename} created successfully")
        msg.setWindowTitle("Login")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        
        
        # Збереження нового імені файлу
        config.set('File', 'LastFilename', second_filename)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)

        
        color = self.color_pdf()
        neck = self.gwint_pdf()
        
        # Додаємо текст для клієнта
        text_1 = "Dear Customer," 
        text_2 = "In response to your inquiry, we are pleased to present an offer."
        text_3 = "If you have additional questions, please feel free to contact me by e-mail or phone."
        
        pdf_generator.add_text(text_1, 30, 720, 400, 12)
        pdf_generator.add_text(text_2, 30, 710, 400, 12)
        pdf_generator.add_text(text_3, 30, 700, 400, 12)
        pdf_generator.add_text(f"index: {index}", 30, 650, 250, 12, is_bold=True)
        pdf_generator.add_text(f"color: {color}", 30, 640, 200, 12, is_bold=True)
        pdf_generator.add_text(f"capacity: 0 ml", 30, 630, 200, 12, is_bold=True)
        pdf_generator.add_text(f"weight: {weight} gr", 30, 620, 200, 12, is_bold=True)
        pdf_generator.add_text(f"pcs per pallet: {pcs_per_pallet}", 30, 610, 200, 12, is_bold=True)
        pdf_generator.add_text(f"neck: {neck}", 30, 600, 200, 12, is_bold=True)
        pdf_generator.add_text(f"OFFER", 400, 795, 200, 12, is_bold=True)
        pdf_generator.add_text(f"Zielona Góra, {date}", 400, 785, 200, 12, is_bold=False)
        pdf_generator.add_text(f"Offer no {oferta[0:13]}", 400, 775, 200, 12, is_bold=True)
        pdf_generator.add_text(f"Buyer ", 400, 765, 200, 12, is_bold=True)
        pdf_generator.add_text(f"pallet weight: {weight_pack} kg", 400, 650, 200, 12, is_bold=False)
        pdf_generator.add_text(f"pallet dimention: 120x100x120 mm", 400, 640, 200, 12, is_bold=False)
        pdf_generator.add_text(f"The above prices are net prices (excluding VAT). Prices per 1000 pieces.", 30, 250, 400, 12, is_bold=False)
        pdf_generator.add_text(f"Terms and conditions: ", 30, 240, 400, 12, is_bold=True)
        pdf_generator.add_text(f"Offer valid: 30 days", 30, 230, 400, 12, is_bold=False)
        pdf_generator.add_text(f"Delivery method: EXW Zielona Góra", 30, 220, 400, 12, is_bold=False)
        pdf_generator.add_text(f"Payment term:", 30, 210, 400, 12, is_bold=False)
        pdf_generator.add_text(f"Remarks:", 30, 200, 400, 12, is_bold=True)
        pdf_generator.add_text(f"Best regards,", 30, 120, 150, 12, is_bold=False)
        pdf_generator.add_text(f"Agnieszka Domagalska", 30, 110, 150, 12, is_bold=False)
        pdf_generator.add_text(f"Customer Service Specialist", 30, 100, 150, 12, is_bold=False)
        pdf_generator.add_text("+48511626216", 30, 90, 150, 12, is_bold=False)
        pdf_generator.add_text("PetRing Sp. z. o. o.", 30, 40, 150, 12, is_bold=True)
        pdf_generator.add_text("Przylep-Ogrodnicza 5", 30, 30, 150, 12, is_bold=False)
        pdf_generator.add_text("66-015 Zielona Góra", 30, 20, 150, 12, is_bold=False)
        pdf_generator.add_text("NIP: 779 243 62 24", 250, 35, 150, 12, is_bold=False)
        pdf_generator.add_text("KRS 0000586288", 250, 25, 150, 12, is_bold=False)
        pdf_generator.add_text("+48 68 321 88 14", 450, 40, 150, 12, is_bold=False)
        pdf_generator.add_text("contact@petring.com.pl", 450, 30, 150, 12, is_bold=False)
        pdf_generator.add_text("www.petring.com.pl", 450, 20, 150, 12, is_bold=False)


        
        
        
        
        # Додати зображення
        image_path = "image/imge_pet_ring.png"
        pdf_generator.add_image(image_path, 10, 730, 244, 103, alpha=1)
        

        image_path_2 = "image/old.png"
        pdf_generator.add_image(image_path_2, 100, 0, 650, 650, alpha=0.1)

        # Додати таблицю
        data = [["Range", "PET", "10% rPet", "25% rPet", "30% rPet", "50% rPet", "75% rPet", "100% rPET"],
                ["10 000-14 999", f"€ {row_2}", f"€ {row_2_pdf_col_10}", f"€ {row_2_pdf_col_25}", f"€ {row_2_pdf_col_30}", f"€ {row_2_pdf_col_50}", f"€ {row_2_pdf_col_75}", f"€ {row_2_pdf_col_100}"],
                ['15 000-19 999', f"€ {row_3}", f"€ {row_3_pdf_col_10}", f"€ {row_3_pdf_col_25}", f"€ {row_3_pdf_col_30}", f"€ {row_3_pdf_col_50}", f"€ {row_3_pdf_col_75}", f"€ {row_3_pdf_col_100}"],
                ['20 000-24 999', f"€ {row_4}", f"€ {row_4_pdf_col_10}", f"€ {row_4_pdf_col_25}", f"€ {row_4_pdf_col_30}", f"€ {row_4_pdf_col_50}", f"€ {row_4_pdf_col_75}", f"€ {row_4_pdf_col_100}"],
                ["25 000-29 999", f"€ {row_5}", f"€ {row_5_pdf_col_10}", f"€ {row_5_pdf_col_25}", f"€ {row_5_pdf_col_30}", f"€ {row_5_pdf_col_50}", f"€ {row_5_pdf_col_75}", f"€ {row_5_pdf_col_100}"],
                ["30 000-34 999", f"€ {row_6}", f"€ {row_6_pdf_col_10}", f"€ {row_6_pdf_col_25}", f"€ {row_6_pdf_col_30}", f"€ {row_6_pdf_col_50}", f"€ {row_6_pdf_col_75}", f"€ {row_6_pdf_col_100}"],
                ["35 000-39 999", f"€ {row_7}", f"€ {row_7_pdf_col_10}", f"€ {row_7_pdf_col_25}", f"€ {row_7_pdf_col_30}", f"€ {row_7_pdf_col_50}", f"€ {row_7_pdf_col_75}", f"€ {row_7_pdf_col_100}"],
                ["40 000-49 999", f"€ {row_8}", f"€ {row_8_pdf_col_10}", f"€ {row_8_pdf_col_25}", f"€ {row_8_pdf_col_30}", f"€ {row_8_pdf_col_50}", f"€ {row_8_pdf_col_75}", f"€ {row_8_pdf_col_100}"],
                ["50 000-74 999", f"€ {row_9}", f"€ {row_9_pdf_col_10}", f"€ {row_9_pdf_col_25}", f"€ {row_9_pdf_col_30}", f"€ {row_9_pdf_col_50}", f"€ {row_9_pdf_col_75}", f"€ {row_9_pdf_col_100}"],
                ["75 000-99 999", f"€ {row_10}", f"€ {row_10_pdf_col_10}", f"€ {row_10_pdf_col_25}", f"€ {row_10_pdf_col_30}", f"€ {row_10_pdf_col_50}", f"€ {row_10_pdf_col_75}", f"€ {row_10_pdf_col_100}"],
                ["100 000-149 999", f"€ {row_11}", f"€ {row_11_pdf_col_10}", f"€ {row_11_pdf_col_25}", f"€ {row_11_pdf_col_30}", f"€ {row_11_pdf_col_50}", f"€ {row_11_pdf_col_75}", f"€ {row_11_pdf_col_100}"],
                ["150 000-199 999", f"€ {row_12}", f"€ {row_12_pdf_col_10}", f"€ {row_12_pdf_col_25}", f"€ {row_12_pdf_col_30}", f"€ {row_12_pdf_col_50}", f"€ {row_12_pdf_col_75}", f"€ {row_12_pdf_col_100}"],
                ["200 000-299 999", f"€ {row_13}", f"€ {row_13_pdf_col_10}", f"€ {row_13_pdf_col_25}", f"€ {row_13_pdf_col_30}", f"€ {row_13_pdf_col_50}", f"€ {row_13_pdf_col_75}", f"€ {row_13_pdf_col_100}"],
                ["300 000-499 999", f"€ {row_14}", f"€ {row_14_pdf_col_10}", f"€ {row_14_pdf_col_25}", f"€ {row_14_pdf_col_30}", f"€ {row_14_pdf_col_50}", f"€ {row_14_pdf_col_75}", f"€ {row_14_pdf_col_100}"],
                ["500 000-999 999", f"€ {row_15}", f"€ {row_15_pdf_col_10}", f"€ {row_15_pdf_col_25}", f"€ {row_15_pdf_col_30}", f"€ {row_15_pdf_col_50}", f"€ {row_15_pdf_col_75}", f"€ {row_15_pdf_col_100}"],
                ["1 000 000-", f"€ {row_16}", f"€ {row_16_pdf_col_10}", f"€ {row_16_pdf_col_25}", f"€ {row_16_pdf_col_30}", f"€ {row_16_pdf_col_50}", f"€ {row_16_pdf_col_75}", f"€ {row_16_pdf_col_100}"],
                ]

        col_widths = [70, 50, 50, 50, 50, 50, 50, 60]
        row_heights = [25, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]

        pdf_generator.add_table(data, col_widths, row_heights)
        
        
        
        
        
        

        # Зберегти PDF-файл
        pdf_generator.save()
       
       # Додавання кольору до файлу PDF
    def color_pdf(self): 
        color = ["Colorless", "Brown", "Purple", "Gold", "Black", "Blue", "Orange", "Pink", "Red", "Grey", "Turquoise", "White", "Efekt Frozen", "Yellow", "Green", "UV", "ASS"]
        color_choice = self.ui.comboBox_4.currentText()
        
        if color_choice == "X":
            kolor = color[0]
        elif color_choice[0] == "B":
            kolor = color[1]
        elif color_choice[0] == "F":
            kolor = color[2]
        elif color_choice[0] == "G":
            kolor = color[3]
        elif color_choice[0] == "K":
            kolor = color[4]
        elif color_choice[0] == "N":
            kolor = color[5]
        elif color_choice[0] == "O":
            kolor = color[6]
        elif color_choice[0] == "P":
            kolor = color[7]
        elif color_choice[0] == "R":
            kolor = color[8]
        elif color_choice[0] == "S":
            kolor = color[9]
        elif color_choice[0] == "T":
            kolor = color[10]
        elif color_choice[0] == "W":
            kolor = color[11]
        elif color_choice == "X1" or color_choice == "X2" or color_choice == "X3" or color_choice == "X4" or color_choice == "X1.1":
            kolor = color[12]
        elif color_choice[0] == "Y":
            kolor = color[13]
        elif color_choice[0] == "Z":
            kolor = color[14]
        elif color_choice == "UV":
            kolor = color[15]
        elif color_choice == "ASS1" or color_choice == "ASS1.2":
            kolor = color[16]
        return kolor
    
    def gwint_pdf(self):
        gwint = self.ui.comboBox_2.currentText()
        
        gwint_list = ["18/410", "20/410", "22/410", "24/410", "28/410", "29/21", "38 2 start", "38/400",
                      "din 18", "PCO (28 1810)", "Ropp18", "Ropp28", "Snap on 16", "ø 42 mm", "ø 48 mm",
                      "ø 63 mm", "ø 82 mm", "ø 120 mm", "ø 52 mm", "28/410 LOCK", "ø 30 mm", "DIN 18",
                      "38 3 START", "ø 56 mm", "ø 120 mm 1x", "ø 120 mm 6x", "38 3 start"]
        
        if gwint == "B":
            neck = gwint_list[0]
        elif gwint == "D":
            neck = gwint_list[1]
        elif gwint == "E":
            neck = gwint_list[2]
        elif gwint == "F":
            neck = gwint_list[3]
        elif gwint == "C" or gwint == "CG":
            neck = gwint_list[4]
        elif gwint == "O":
            neck = gwint_list[5]
        elif gwint == "M":
            neck = gwint_list[6]
        elif gwint == "K":
            neck = gwint_list[7]
        elif gwint == "N":
            neck = gwint_list[8]
        elif gwint == "P" or gwint == "PN":
            neck = gwint_list[9]
        elif gwint == "A":
            neck = gwint_list[10]
        elif gwint == "R":
            neck = gwint_list[11]
        elif gwint == "G":
            neck = gwint_list[12]
        elif gwint == "S" or gwint == "SA" or gwint == "SB" or gwint == "SC":
            neck = gwint_list[13]
        elif gwint == "W":
            neck = gwint_list[14]
        elif gwint == "Z":
            neck = gwint_list[15]
        elif gwint == "H":
            neck = gwint_list[16]
        elif gwint == "U":
            neck = gwint_list[17]
        elif gwint == "Q":
            neck = gwint_list[18]
        elif gwint == "CZ":
            neck = gwint_list[19]
        elif gwint == "PR":
            neck = gwint_list[20]
        elif gwint == "BA":
            neck = gwint_list[21]
        elif gwint == "MA":
            neck = gwint_list[22]
        elif gwint == "QA":
            neck = gwint_list[23]
        elif gwint == "Y":
            neck = gwint_list[24]
        elif gwint == "YA":
            neck = gwint_list[25]
        elif gwint == "MA":
            neck = gwint_list[26]
        return neck
        
        
    def cost_start_pdf(self):
        color_box_4 = self.ui.comboBox_4.currentText()
        index_preforma = f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}"
        
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
            self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR)
            self.koszt_urochom_r_pet = self.koszt_urochom + 3 * koszt
            return self.koszt_urochom, self.koszt_urochom_r_pet
        else:
            self.koszt_urochom = (koszt + (wydajnosc * (gramatura / 1000)) * COST_START_SUR) * 3
            self.koszt_urochom_r_pet = self.koszt_urochom + 3 * koszt
            return self.koszt_urochom, self.koszt_urochom_r_pet
  

     # 100 % Pet   
    
    
    def total_cost_raw_color_pdf_0(self): # 0 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        total_result = self.cena_pet()
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
                
    def waste_for_preforms_pdf_0(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_0()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_0(self):
        cost_color = float(self.total_cost_raw_color_pdf_0()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_0()[2] # surowiec
         
        waste_preform = round(self.waste_for_preforms_pdf_0(), 2)
        cost_color_batch = round(self.cost_color_batch_waste(), 2)
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
        
    def calculate_total_cost_col_0(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[0])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_0())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
        
    def row_2_pdf(self):
        return self.calculate_total_cost_col_0(10000)
        
    def row_3_pdf(self):
        return self.calculate_total_cost_col_0(15000)
        
    def row_4_pdf(self):
        return self.calculate_total_cost_col_0(20000)
        
    def row_5_pdf(self):
        return self.calculate_total_cost_col_0(25000)
        
    def row_6_pdf(self):
        return self.calculate_total_cost_col_0(30000)
        
    def row_7_pdf(self):
        return self.calculate_total_cost_col_0(35000)
        
    def row_8_pdf(self):
        return self.calculate_total_cost_col_0(40000)

    def row_9_pdf(self):
        return self.calculate_total_cost_col_0(50000)

    def row_10_pdf(self):
        return self.calculate_total_cost_col_0(75000)

    def row_11_pdf(self):
        return  self.calculate_total_cost_col_0(100000)

    def row_12_pdf(self):
        return self.calculate_total_cost_col_0(150000)

    def row_13_pdf(self):
        return self.calculate_total_cost_col_0(200000)

    def row_14_pdf(self):
        return self.calculate_total_cost_col_0(300000)

    def row_15_pdf(self):
        return self.calculate_total_cost_col_0(500000)
   
    def row_16_pdf(self):
        return self.calculate_total_cost_col_0(1000000)
    
    # 10 % R-Pet
    def total_cost_raw_color_pdf_10(self): # 10 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()
        
        formula_pet = (R_PET_PROCENT - 10)
        cost_pet = kurs_pet * (10 / 100)
        input_cost = kurs_pet - cost_pet
        cost_r_pet = kurs_r_pet * (formula_pet / 100)
        input_cost_r_pet = kurs_r_pet - cost_r_pet
        total_result = input_cost + input_cost_r_pet
        
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec        
        
    def waste_for_preforms_pdf_10(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_10()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_10(self):
        cost_color = float(self.total_cost_raw_color_pdf_10()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_10()[2] # surowiec
         
        waste_preform = self.waste_for_preforms_pdf_10()
        cost_color_batch = self.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
           
    def calculate_total_cost_col_10(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_10())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)

    def row_2_pdf_col_10(self):
        return self.calculate_total_cost_col_10(10000)
        
    def row_3_pdf_col_10(self):
        return self.calculate_total_cost_col_10(15000)
        
    def row_4_pdf_col_10(self):
        return self.calculate_total_cost_col_10(20000)
        
    def row_5_pdf_col_10(self):
        return self.calculate_total_cost_col_10(25000)
        
    def row_6_pdf_col_10(self):
        return self.calculate_total_cost_col_10(30000)
        
    def row_7_pdf_col_10(self):
        return self.calculate_total_cost_col_10(35000)
        
    def row_8_pdf_col_10(self):
        return self.calculate_total_cost_col_10(40000)

    def row_9_pdf_col_10(self):
        return self.calculate_total_cost_col_10(50000)

    def row_10_pdf_col_10(self):
        return self.calculate_total_cost_col_10(75000)

    def row_11_pdf_col_10(self):
        return  self.calculate_total_cost_col_10(100000)

    def row_12_pdf_col_10(self):
        return self.calculate_total_cost_col_10(150000)

    def row_13_pdf_col_10(self):
        return self.calculate_total_cost_col_10(200000)

    def row_14_pdf_col_10(self):
        return self.calculate_total_cost_col_10(300000)

    def row_15_pdf_col_10(self):
        return self.calculate_total_cost_col_10(500000)
  
    def row_16_pdf_col_10(self):
        return self.calculate_total_cost_col_10(1000000)
    
    # 25% R-Pet
    def total_cost_raw_color_pdf_25(self): # 25 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()
        
        formula_pet = (R_PET_PROCENT - 25)
        cost_pet = kurs_pet * (25 / 100)
        input_cost = kurs_pet - cost_pet
        cost_r_pet = kurs_r_pet * (formula_pet / 100)
        input_cost_r_pet = kurs_r_pet - cost_r_pet
        total_result = input_cost + input_cost_r_pet
        
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
               
    def waste_for_preforms_pdf_25(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_25()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_25(self):
        cost_color = float(self.total_cost_raw_color_pdf_25()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_25()[2] # surowiec
         
        waste_preform = self.waste_for_preforms_pdf_25()
        cost_color_batch = self.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
          
    def calculate_total_cost_col_25(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_25())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
    def row_2_pdf_col_25(self):
        return self.calculate_total_cost_col_25(10000)
        
    def row_3_pdf_col_25(self):
        return self.calculate_total_cost_col_25(15000)
        
    def row_4_pdf_col_25(self):
        return self.calculate_total_cost_col_25(20000)
        
    def row_5_pdf_col_25(self):
        return self.calculate_total_cost_col_25(25000)
        
    def row_6_pdf_col_25(self):
        return self.calculate_total_cost_col_25(30000)
        
    def row_7_pdf_col_25(self):
        return self.calculate_total_cost_col_25(35000)
        
    def row_8_pdf_col_25(self):
        return self.calculate_total_cost_col_25(40000)

    def row_9_pdf_col_25(self):
        return self.calculate_total_cost_col_25(50000)

    def row_10_pdf_col_25(self):
        return self.calculate_total_cost_col_25(75000)

    def row_11_pdf_col_25(self):
        return  self.calculate_total_cost_col_25(100000)

    def row_12_pdf_col_25(self):
        return self.calculate_total_cost_col_25(150000)

    def row_13_pdf_col_25(self):
        return self.calculate_total_cost_col_25(200000)

    def row_14_pdf_col_25(self):
        return self.calculate_total_cost_col_25(300000)

    def row_15_pdf_col_25(self):
        return self.calculate_total_cost_col_25(500000)

    def row_16_pdf_col_25(self):
        return self.calculate_total_cost_col_25(1000000)
    
    # 30% R-Pet
    def total_cost_raw_color_pdf_30(self): # 30 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()
        
        formula_pet = (R_PET_PROCENT - 30)
        cost_pet = kurs_pet * (30 / 100)
        input_cost = kurs_pet - cost_pet
        cost_r_pet = kurs_r_pet * (formula_pet / 100)
        input_cost_r_pet = kurs_r_pet - cost_r_pet
        total_result = input_cost + input_cost_r_pet
        
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
              
    def waste_for_preforms_pdf_30(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_30()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_30(self):
        cost_color = float(self.total_cost_raw_color_pdf_30()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_30()[2] # surowiec
         
        waste_preform = self.waste_for_preforms_pdf_30()
        cost_color_batch = self.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
            
    def calculate_total_cost_col_30(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_30())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
    def row_2_pdf_col_30(self):
        return self.calculate_total_cost_col_30(10000)
        
    def row_3_pdf_col_30(self):
        return self.calculate_total_cost_col_30(15000)
        
    def row_4_pdf_col_30(self):
        return self.calculate_total_cost_col_30(20000)
        
    def row_5_pdf_col_30(self):
        return self.calculate_total_cost_col_30(25000)
        
    def row_6_pdf_col_30(self):
        return self.calculate_total_cost_col_30(30000)
        
    def row_7_pdf_col_30(self):
        return self.calculate_total_cost_col_30(35000)
        
    def row_8_pdf_col_30(self):
        return self.calculate_total_cost_col_30(40000)

    def row_9_pdf_col_30(self):
        return self.calculate_total_cost_col_30(50000)

    def row_10_pdf_col_30(self):
        return self.calculate_total_cost_col_30(75000)

    def row_11_pdf_col_30(self):
        return  self.calculate_total_cost_col_30(100000)

    def row_12_pdf_col_30(self):
        return self.calculate_total_cost_col_30(150000)

    def row_13_pdf_col_30(self):
        return self.calculate_total_cost_col_30(200000)

    def row_14_pdf_col_30(self):
        return self.calculate_total_cost_col_30(300000)

    def row_15_pdf_col_30(self):
        return self.calculate_total_cost_col_30(500000)

    def row_16_pdf_col_30(self):
        return self.calculate_total_cost_col_30(1000000)
    
     # 30% R-Pet
    
    
    
    # 50 % R-Pet
    def total_cost_raw_color_pdf_50(self): # 50 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()
        
        formula_pet = (R_PET_PROCENT - 50)
        cost_pet = kurs_pet * (50 / 100)
        input_cost = kurs_pet - cost_pet
        cost_r_pet = kurs_r_pet * (formula_pet / 100)
        input_cost_r_pet = kurs_r_pet - cost_r_pet
        total_result = input_cost + input_cost_r_pet
        
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
             
    def waste_for_preforms_pdf_50(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_50()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_50(self):
        cost_color = float(self.total_cost_raw_color_pdf_50()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_50()[2] # surowiec
         
        waste_preform = self.waste_for_preforms_pdf_50()
        cost_color_batch = self.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
          
    def calculate_total_cost_col_50(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_50())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
    def row_2_pdf_col_50(self):
        return self.calculate_total_cost_col_50(10000)
        
    def row_3_pdf_col_50(self):
        return self.calculate_total_cost_col_50(15000)
        
    def row_4_pdf_col_50(self):
        return self.calculate_total_cost_col_50(20000)
        
    def row_5_pdf_col_50(self):
        return self.calculate_total_cost_col_50(25000)
        
    def row_6_pdf_col_50(self):
        return self.calculate_total_cost_col_50(30000)
        
    def row_7_pdf_col_50(self):
        return self.calculate_total_cost_col_50(35000)
        
    def row_8_pdf_col_50(self):
        return self.calculate_total_cost_col_50(40000)

    def row_9_pdf_col_50(self):
        return self.calculate_total_cost_col_50(50000)

    def row_10_pdf_col_50(self):
        return self.calculate_total_cost_col_50(75000)

    def row_11_pdf_col_50(self):
        return  self.calculate_total_cost_col_50(100000)

    def row_12_pdf_col_50(self):
        return self.calculate_total_cost_col_50(150000)

    def row_13_pdf_col_50(self):
        return self.calculate_total_cost_col_50(200000)

    def row_14_pdf_col_50(self):
        return self.calculate_total_cost_col_50(300000)

    def row_15_pdf_col_50(self):
        return self.calculate_total_cost_col_50(500000)

    def row_16_pdf_col_50(self):
        return self.calculate_total_cost_col_50(1000000)
    
    
    # 75 % R-Pet
    def total_cost_raw_color_pdf_75(self): # 75 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.cena_pet()
        kurs_r_pet = self.cena_r_pet()
        
        formula_pet = (R_PET_PROCENT - 75)
        cost_pet = kurs_pet * (75 / 100)
        input_cost = kurs_pet - cost_pet
        cost_r_pet = kurs_r_pet * (formula_pet / 100)
        input_cost_r_pet = kurs_r_pet - cost_r_pet
        total_result = input_cost + input_cost_r_pet
        
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
               
    def waste_for_preforms_pdf_75(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_75()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_75(self):
        cost_color = float(self.total_cost_raw_color_pdf_75()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_75()[2] # surowiec
         
        waste_preform = self.waste_for_preforms_pdf_75()
        cost_color_batch = self.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
           
    def calculate_total_cost_col_75(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_75())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
    def row_2_pdf_col_75(self):
        return self.calculate_total_cost_col_75(10000)
        
    def row_3_pdf_col_75(self):
        return self.calculate_total_cost_col_75(15000)
        
    def row_4_pdf_col_75(self):
        return self.calculate_total_cost_col_75(20000)
        
    def row_5_pdf_col_75(self):
        return self.calculate_total_cost_col_75(25000)
        
    def row_6_pdf_col_75(self):
        return self.calculate_total_cost_col_75(30000)
        
    def row_7_pdf_col_75(self):
        return self.calculate_total_cost_col_75(35000)
        
    def row_8_pdf_col_75(self):
        return self.calculate_total_cost_col_75(40000)

    def row_9_pdf_col_75(self):
        return self.calculate_total_cost_col_75(50000)

    def row_10_pdf_col_75(self):
        return self.calculate_total_cost_col_75(75000)

    def row_11_pdf_col_75(self):
        return  self.calculate_total_cost_col_75(100000)

    def row_12_pdf_col_75(self):
        return self.calculate_total_cost_col_75(150000)

    def row_13_pdf_col_75(self):
        return self.calculate_total_cost_col_75(200000)

    def row_14_pdf_col_75(self):
        return self.calculate_total_cost_col_75(300000)

    def row_15_pdf_col_75(self):
        return self.calculate_total_cost_col_75(500000)

    def row_16_pdf_col_75(self):
        return self.calculate_total_cost_col_75(1000000)
    
    
    # 100 % R-Pet
    def total_cost_raw_color_pdf_100(self): # 100 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_r_pet = self.cena_r_pet()
        total_result = kurs_r_pet
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
                self.result_il_barwnika = float(choice_gram) * (doza_barwnika / 100)  # Quantity for 1000 pcs (kg)
                self.result_material = self.result_il_barwnika * float(uniq_cena_barwnik)  # Cost Material for 1000 pcs (PLN)
            else:
                self.result_material = 0

        # Закриваємо з'єднання з базою даних
        conn.close()
                            
        total_cost_surowiec = float(choice_gram) * total_result
        self.total_cost_raw = round(total_cost_surowiec, 4) + round(self.result_material, 2)                
        self.total_cost_tys = round(self.total_cost_raw, 4) # Total Cost Raw material for 1000 pcs
        return self.total_cost_tys, self.result_material, total_cost_surowiec  
                
    def waste_for_preforms_pdf_100(self):
        cost_raw_machines = float(self.total_cost_raw_color_pdf_100()[2])
        waste_preform = cost_raw_machines * 3 / 100
        return waste_preform
    
    def total_cost_raw_material_tys_pdf_100(self):
        cost_color = float(self.total_cost_raw_color_pdf_100()[1]) # Barwnik
        
        cost_raw_machines = self.total_cost_raw_color_pdf_100()[2] # surowiec
         
        waste_preform = round(self.waste_for_preforms_pdf_100(), 2)
        cost_color_batch = round(self.cost_color_batch_waste(), 2)
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
        
    def calculate_total_cost_col_100(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.cost_machine())
        self.packing_cost = float(self.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_100())
        euro = self.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
    def row_2_pdf_col_100(self):
        return self.calculate_total_cost_col_100(10000)
        
    def row_3_pdf_col_100(self):
        return self.calculate_total_cost_col_100(15000)
        
    def row_4_pdf_col_100(self):
        return self.calculate_total_cost_col_100(20000)
        
    def row_5_pdf_col_100(self):
        return self.calculate_total_cost_col_100(25000)
        
    def row_6_pdf_col_100(self):
        return self.calculate_total_cost_col_100(30000)
        
    def row_7_pdf_col_100(self):
        return self.calculate_total_cost_col_100(35000)
        
    def row_8_pdf_col_100(self):
        return self.calculate_total_cost_col_100(40000)

    def row_9_pdf_col_100(self):
        return self.calculate_total_cost_col_100(50000)

    def row_10_pdf_col_100(self):
        return self.calculate_total_cost_col_100(75000)

    def row_11_pdf_col_100(self):
        return  self.calculate_total_cost_col_100(100000)

    def row_12_pdf_col_100(self):
        return self.calculate_total_cost_col_100(150000)

    def row_13_pdf_col_100(self):
        return self.calculate_total_cost_col_100(200000)

    def row_14_pdf_col_100(self):
        return self.calculate_total_cost_col_100(300000)

    def row_15_pdf_col_100(self):
        return self.calculate_total_cost_col_100(500000)

    def row_16_pdf_col_100(self):
        return self.calculate_total_cost_col_100(1000000)
    
    
   
            


    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Preforma()
    ui.show()
    sys.exit(app.exec_())

    