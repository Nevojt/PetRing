         # Блок для PDF
import configparser
import sqlite3
from title import *
from PyQt5 import QtWidgets

R_PET_PROCENT = 100
P1 = 66.36 # Пакування Oktabina
P3 = 3.30 # Пакування Kosz
COST_START_SUR = 6.39 # zl

class GeneratePDF(object):
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