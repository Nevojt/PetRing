    
from datetime import datetime
import sqlite3

R_PET_PROCENT = 100
P1 = 66.36 # Пакування Oktabina
P3 = 3.30 # Пакування Kosz
COST_START_SUR = 6.39 # zl

class TableFunc:
    def __init__(self, preforma_instance) -> None:
        self.preforma = preforma_instance
        self.ui = preforma_instance.ui
    
    def index_one(self):
        packing_list = self.preforma.update_label_packing_list() 
        index = f"{self.ui.comboBox.currentText()}-{self.ui.comboBox_2.currentText()}-{self.ui.comboBox_3.currentText()}-{self.ui.comboBox_4.currentText()}-{packing_list}-{self.ui.comboBox_6.currentText()}"
        indexQ = index[:1] +"Q" +  index[1:]
        indexW = index[:1] +"W" +  index[1:]
        indexV = index[:1] +"V" +  index[1:]
        indexX = index[:1] +"X" +  index[1:]
        indexY = index[:1] +"Y" +  index[1:]
        indexZ = index[:1] +"Z" +  index[1:]
        
        index_list = [index, indexQ, indexW, indexV, indexX, indexY, indexZ]
        return index_list
    
    def date_time(self):
        date_time = datetime.now()
        formatted_date = date_time.strftime("%d-%m-%y %H:%M")
        tuples = ()
        for i in range(7):
            tuples += (formatted_date,)
        return tuples
        
    
    def index_E(self):
        cena_euros = self.preforma.cena_euro()
        pet = self.preforma.cena_pet()[1]
        pets = pet / cena_euros
        result = str(pets)
        tuples = ()
        for i in range(7):
            tuples += ('€ ' + result,)
        return tuples
    
    def index_F(self):
        cena_euros = self.preforma.cena_euro()
        pet = self.preforma.cena_r_pet()[1]
        pets = round(pet / cena_euros, 2)
        result = str(pets)
        tuples = ()
        for i in range(7):
            tuples += ('€ ' + result,)
        return tuples
    
    def index_G(self):
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
            
        tuples = ()
        for i in range(7):
            tuples += (neck,)
        return tuples
        

    def index_H(self):
        gram = self.ui.comboBox_3.currentText()
        tuples = ()
        for i in range(7):
            tuples += (gram,)
        return tuples
    
    def index_I(self):
        ml = 0
        tuples = ()
        for i in range(7):
            tuples += (ml,)
        return tuples
    
    
    def index_J(self):
        color = self.ui.comboBox_4.currentText()
        
        conn = sqlite3.connect('data\\barwnik.db')
        curs = conn.cursor()
        curs.execute("SELECT Identyfikator FROM data WHERE Kolor_cecha =?", (color,))
        result = curs.fetchall()
        data = sorted(list(set([row[0] for row in result])))
        curs.close()
        conn.commit()
        conn.close()
        tuples = ()
        for i in range(7):
            tuples += (data[0],)
        return tuples
    
    def index_K(self):
        palet = '115x100x120'
        tuples = ()
        for i in range(7):
            tuples += (palet,)
        return tuples
    
    def index_L(self):
        weight = self.preforma.total_weight()
        tuples = ()
        for i in range(7):
            tuples += (weight,)
        return tuples
    
    def index_M(self):
        bottles = self.preforma.update_label_packing_list()
        tuples = ()
        for i in range(7):
            tuples += (bottles,)
        return tuples
    
    
    
    
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
        total_result = self.preforma.cena_pet()[0]
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
        cost_color_batch = round(self.preforma.cost_color_batch_waste(), 2)
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
        
    def calculate_total_cost_col_0(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[0])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_0())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_0(40000)
        
    def row_8_pdf(self):
        return self.calculate_total_cost_col_0(50000)

    def row_9_pdf(self):
        return self.calculate_total_cost_col_0(75000)

    def row_10_pdf(self):
        return self.calculate_total_cost_col_0(100000)

    def row_11_pdf(self):
        return  self.calculate_total_cost_col_0(150000)

    def row_12_pdf(self):
        return self.calculate_total_cost_col_0(200000)

    def row_13_pdf(self):
        return self.calculate_total_cost_col_0(300000)

    def row_14_pdf(self):
        return self.calculate_total_cost_col_0(500000)

    def row_15_pdf(self):
        return self.calculate_total_cost_col_0(1000000)
   
    
    # 10 % R-Pet
    def total_cost_raw_color_pdf_10(self): # 10 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.preforma.cena_pet()[0]
        kurs_r_pet = self.preforma.cena_r_pet()[0]
        
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
        cost_color_batch = self.preforma.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
           
    def calculate_total_cost_col_10(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_10())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_10(40000)
        
    def row_8_pdf_col_10(self):
        return self.calculate_total_cost_col_10(50000)

    def row_9_pdf_col_10(self):
        return self.calculate_total_cost_col_10(750000)

    def row_10_pdf_col_10(self):
        return self.calculate_total_cost_col_10(100000)

    def row_11_pdf_col_10(self):
        return  self.calculate_total_cost_col_10(150000)

    def row_12_pdf_col_10(self):
        return self.calculate_total_cost_col_10(200000)

    def row_13_pdf_col_10(self):
        return self.calculate_total_cost_col_10(300000)

    def row_14_pdf_col_10(self):
        return self.calculate_total_cost_col_10(500000)

    def row_15_pdf_col_10(self):
        return self.calculate_total_cost_col_10(1000000)
  
    
    # 25% R-Pet
    def total_cost_raw_color_pdf_25(self): # 25 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.preforma.cena_pet()[0]
        kurs_r_pet = self.preforma.cena_r_pet()[0]
        
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
        cost_color_batch = self.preforma.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
          
    def calculate_total_cost_col_25(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_25())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_25(40000)
        
    def row_8_pdf_col_25(self):
        return self.calculate_total_cost_col_25(50000)

    def row_9_pdf_col_25(self):
        return self.calculate_total_cost_col_25(750000)

    def row_10_pdf_col_25(self):
        return self.calculate_total_cost_col_25(100000)

    def row_11_pdf_col_25(self):
        return  self.calculate_total_cost_col_25(150000)

    def row_12_pdf_col_25(self):
        return self.calculate_total_cost_col_25(200000)

    def row_13_pdf_col_25(self):
        return self.calculate_total_cost_col_25(300000)

    def row_14_pdf_col_25(self):
        return self.calculate_total_cost_col_25(500000)

    def row_15_pdf_col_25(self):
        return self.calculate_total_cost_col_25(1000000)

    
    # 30% R-Pet
    def total_cost_raw_color_pdf_30(self): # 30 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.preforma.cena_pet()[0]
        kurs_r_pet = self.preforma.cena_r_pet()[0]
        
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
        cost_color_batch = self.preforma.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
            
    def calculate_total_cost_col_30(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_30())
        euro = self.preforma.cena_euro()

        start = self.cost_start_r_pet
        result_1 = start / quality * 1000
        total_cost_machine = result_1 + self.cost_machiner
        result_title_narzit = total_cost_machine + (total_cost_machine * 10 / 100)
        result_2 = self.packing_cost + self.total_cost_raw + result_title_narzit
        result_3 = result_2 / euro
        # print(f"Title total_cost_finish {quality} - {round(result_3, 2)}")
        return round(result_3, 2)
    
         # 30% R-Pet
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
        return self.calculate_total_cost_col_30(40000)
        
    def row_8_pdf_col_30(self):
        return self.calculate_total_cost_col_30(50000)

    def row_9_pdf_col_30(self):
        return self.calculate_total_cost_col_30(75000)

    def row_10_pdf_col_30(self):
        return self.calculate_total_cost_col_30(100000)

    def row_11_pdf_col_30(self):
        return  self.calculate_total_cost_col_30(150000)

    def row_12_pdf_col_30(self):
        return self.calculate_total_cost_col_30(200000)

    def row_13_pdf_col_30(self):
        return self.calculate_total_cost_col_30(300000)

    def row_14_pdf_col_30(self):
        return self.calculate_total_cost_col_30(500000)

    def row_15_pdf_col_30(self):
        return self.calculate_total_cost_col_30(1000000)

    
    
    
    # 50 % R-Pet
    def total_cost_raw_color_pdf_50(self): # 50 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.preforma.cena_pet()[0]
        kurs_r_pet = self.preforma.cena_r_pet()[0]
        
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
        cost_color_batch = self.preforma.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
          
    def calculate_total_cost_col_50(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_50())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_50(40000)
        
    def row_8_pdf_col_50(self):
        return self.calculate_total_cost_col_50(50000)

    def row_9_pdf_col_50(self):
        return self.calculate_total_cost_col_50(75000)

    def row_10_pdf_col_50(self):
        return self.calculate_total_cost_col_50(100000)

    def row_11_pdf_col_50(self):
        return  self.calculate_total_cost_col_50(150000)

    def row_12_pdf_col_50(self):
        return self.calculate_total_cost_col_50(200000)

    def row_13_pdf_col_50(self):
        return self.calculate_total_cost_col_50(300000)

    def row_14_pdf_col_50(self):
        return self.calculate_total_cost_col_50(500000)

    def row_15_pdf_col_50(self):
        return self.calculate_total_cost_col_50(1000000)
    
    
    # 75 % R-Pet
    def total_cost_raw_color_pdf_75(self): # 75 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_pet = self.preforma.cena_pet()[0]
        kurs_r_pet = self.preforma.cena_r_pet()[0]
        
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
        cost_color_batch = self.preforma.cost_color_batch_waste()
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
           
    def calculate_total_cost_col_75(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_75())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_75(40000)
        
    def row_8_pdf_col_75(self):
        return self.calculate_total_cost_col_75(50000)

    def row_9_pdf_col_75(self):
        return self.calculate_total_cost_col_75(75000)

    def row_10_pdf_col_75(self):
        return self.calculate_total_cost_col_75(100000)

    def row_11_pdf_col_75(self):
        return  self.calculate_total_cost_col_75(150000)

    def row_12_pdf_col_75(self):
        return self.calculate_total_cost_col_75(200000)

    def row_13_pdf_col_75(self):
        return self.calculate_total_cost_col_75(300000)

    def row_14_pdf_col_75(self):
        return self.calculate_total_cost_col_75(500000)

    def row_15_pdf_col_75(self):
        return self.calculate_total_cost_col_75(1000000)
    
    
    # 100 % R-Pet
    def total_cost_raw_color_pdf_100(self): # 100 % R-Pet
        choice_color = self.ui.comboBox_4.currentText()
        choice_gram = self.ui.comboBox_3.currentText()
        kurs_r_pet = self.preforma.cena_r_pet()[0]
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
        cost_color_batch = round(self.preforma.cost_color_batch_waste(), 2)
        result = cost_color + cost_raw_machines + waste_preform + cost_color_batch
        return result
        
    def calculate_total_cost_col_100(self, quality):
        self.cost_start_r_pet = float(self.cost_start_pdf()[1])
        self.cost_machiner = float(self.preforma.cost_machine())
        self.packing_cost = float(self.preforma.upgate_packaging())
        self.total_cost_raw = float(self.total_cost_raw_material_tys_pdf_100())
        euro = self.preforma.cena_euro()

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
        return self.calculate_total_cost_col_100(40000)
        
    def row_8_pdf_col_100(self):
        return self.calculate_total_cost_col_100(50000)

    def row_9_pdf_col_100(self):
        return self.calculate_total_cost_col_100(75000)

    def row_10_pdf_col_100(self):
        return self.calculate_total_cost_col_100(100000)

    def row_11_pdf_col_100(self):
        return  self.calculate_total_cost_col_100(150000)

    def row_12_pdf_col_100(self):
        return self.calculate_total_cost_col_100(200000)

    def row_13_pdf_col_100(self):
        return self.calculate_total_cost_col_100(300000)

    def row_14_pdf_col_100(self):
        return self.calculate_total_cost_col_100(500000)

    def row_15_pdf_col_100(self):
        return self.calculate_total_cost_col_100(1000000)
    
    
    def list_N(self):
        one = str(self.row_2_pdf())
        two = str(self.row_2_pdf_col_10())
        three = str(self.row_2_pdf_col_25())
        four = str(self.row_2_pdf_col_30())
        five = str(self.row_2_pdf_col_50())
        six = str(self.row_2_pdf_col_75())
        seven = str(self.row_2_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_O(self):
        one = str(self.row_3_pdf())
        two = str(self.row_3_pdf_col_10())
        three = str(self.row_3_pdf_col_25())
        four = str(self.row_3_pdf_col_30())
        five = str(self.row_3_pdf_col_50())
        six = str(self.row_3_pdf_col_75())
        seven = str(self.row_3_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_P(self):
        one = str(self.row_4_pdf())
        two = str(self.row_4_pdf_col_10())
        three = str(self.row_4_pdf_col_25())
        four = str(self.row_4_pdf_col_30())
        five = str(self.row_4_pdf_col_50())
        six = str(self.row_4_pdf_col_75())
        seven = str(self.row_4_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_Q(self):
        one = str(self.row_5_pdf())
        two = str(self.row_5_pdf_col_10())
        three = str(self.row_5_pdf_col_25())
        four = str(self.row_5_pdf_col_30())
        five = str(self.row_5_pdf_col_50())
        six = str(self.row_5_pdf_col_75())
        seven = str(self.row_5_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_R(self):
        one = str(self.row_6_pdf())
        two = str(self.row_6_pdf_col_10())
        three = str(self.row_6_pdf_col_25())
        four = str(self.row_6_pdf_col_30())
        five = str(self.row_6_pdf_col_50())
        six = str(self.row_6_pdf_col_75())
        seven = str(self.row_6_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_R(self):
        one = str(self.row_6_pdf())
        two = str(self.row_6_pdf_col_10())
        three = str(self.row_6_pdf_col_25())
        four = str(self.row_6_pdf_col_30())
        five = str(self.row_6_pdf_col_50())
        six = str(self.row_6_pdf_col_75())
        seven = str(self.row_6_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_S(self):
        one = str(self.row_7_pdf())
        two = str(self.row_7_pdf_col_10())
        three = str(self.row_7_pdf_col_25())
        four = str(self.row_7_pdf_col_30())
        five = str(self.row_7_pdf_col_50())
        six = str(self.row_7_pdf_col_75())
        seven = str(self.row_7_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_T(self):
        one = str(self.row_8_pdf())
        two = str(self.row_8_pdf_col_10())
        three = str(self.row_8_pdf_col_25())
        four = str(self.row_8_pdf_col_30())
        five = str(self.row_8_pdf_col_50())
        six = str(self.row_8_pdf_col_75())
        seven = str(self.row_8_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_U(self):
        one = str(self.row_9_pdf())
        two = str(self.row_9_pdf_col_10())
        three = str(self.row_9_pdf_col_25())
        four = str(self.row_9_pdf_col_30())
        five = str(self.row_9_pdf_col_50())
        six = str(self.row_9_pdf_col_75())
        seven = str(self.row_9_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_V(self):
        one = str(self.row_10_pdf())
        two = str(self.row_10_pdf_col_10())
        three = str(self.row_10_pdf_col_25())
        four = str(self.row_10_pdf_col_30())
        five = str(self.row_10_pdf_col_50())
        six = str(self.row_10_pdf_col_75())
        seven = str(self.row_10_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_W(self):
        one = str(self.row_11_pdf())
        two = str(self.row_11_pdf_col_10())
        three = str(self.row_11_pdf_col_25())
        four = str(self.row_11_pdf_col_30())
        five = str(self.row_11_pdf_col_50())
        six = str(self.row_11_pdf_col_75())
        seven = str(self.row_11_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_X(self):
        one = str(self.row_12_pdf())
        two = str(self.row_12_pdf_col_10())
        three = str(self.row_12_pdf_col_25())
        four = str(self.row_12_pdf_col_30())
        five = str(self.row_12_pdf_col_50())
        six = str(self.row_12_pdf_col_75())
        seven = str(self.row_12_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_Y(self):
        one = str(self.row_13_pdf())
        two = str(self.row_13_pdf_col_10())
        three = str(self.row_13_pdf_col_25())
        four = str(self.row_13_pdf_col_30())
        five = str(self.row_13_pdf_col_50())
        six = str(self.row_13_pdf_col_75())
        seven = str(self.row_13_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_Z(self):
        one = str(self.row_14_pdf())
        two = str(self.row_14_pdf_col_10())
        three = str(self.row_14_pdf_col_25())
        four = str(self.row_14_pdf_col_30())
        five = str(self.row_14_pdf_col_50())
        six = str(self.row_14_pdf_col_75())
        seven = str(self.row_14_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def list_AA(self):
        one = str(self.row_15_pdf())
        two = str(self.row_15_pdf_col_10())
        three = str(self.row_15_pdf_col_25())
        four = str(self.row_15_pdf_col_30())
        five = str(self.row_15_pdf_col_50())
        six = str(self.row_15_pdf_col_75())
        seven = str(self.row_15_pdf_col_100())
        
        list_one = ['€ ' + one, '€ ' + two, '€ ' + three, '€ ' + four, '€ ' + five, '€ ' + six, '€ ' + seven]
        return list_one
    
    def index_AB(self):
        narzut = str(self.preforma.wiev_narzut()[0])
        tuples = ()
        for i in range(7):
            tuples += (narzut + '%',)
        return tuples