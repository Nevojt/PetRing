import sqlite3

# # Встановлення з'єднання з базою даних
# connection = sqlite3.connect('data/barwnik.db')
# cursor = connection.cursor()

# params = [
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1', 'Brown B1', '121.00', '0.50', 'NO', 'B6'),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.1', 'Brown B1', '121.00', '0.30', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.2', 'Brown B1', '121.00', '0.60', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.3', 'Brown B1', '121.00', '0.80', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.4', 'Brown B1', '121.00', '0.55', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.5', 'Brown B1', '121.00', '0.25', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.6', 'Brown B1', '121.00', '0.75', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.7', 'Brown B1', '121.00', '0.65', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.8', 'Brown B1', '121.00', '0.70', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.9', 'Brown B1', '121.00', '1.00', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.10', 'Brown B1', '121.00', '0.90', 'NO', None),
#     ('BARWNIK B1 MAXITHEN PET D 821767 CRMG', 'B1.11', 'Brown B1', '121.00', '0.40', 'NO', None)
# ]

# # Виконання запиту з кількома рядками даних
# cursor.executemany("INSERT INTO data (Nazwa, Kolor_cecha, Identyfikator, Cena_za_kg, Dozowanie, Powierzony, Zamienniki) VALUES (?, ?, ?, ?, ?, ?, ?)", params)

# # Застосування змін до бази даних
# # connection.commit()

# # # Закриття з'єднання
# # connection.close()

# from datetime import datetime
# current_datetime = datetime.now()
# conn = sqlite3.connect('data/surowiec.db')
# cursor = conn.cursor()

# formatted_date = current_datetime.strftime("%d-%m-%y %H:%M")

# kurs = [(5, 'Date_Time', '', formatted_date)]

# cursor.executemany("INSERT INTO kurs (kurs_id, surowiec, cena_za_kg, date_time) VALUES (?,?,?,?)", kurs)

# conn.commit()
# conn.close()


# import sqlite3
# from datetime import datetime

# conn = sqlite3.connect('data/surowiec.db')
# cursor = conn.cursor()

# # Припустимо, що вам потрібно вставити поточну дату та час в стовпець date_time
# current_datetime = datetime.now()
# insert_query = "INSERT INTO kurs (column1, column2, date_time) VALUES (?, ?, ?)"
# cursor.execute(insert_query, (value1, value2, current_datetime))

# conn.commit()
# conn.close()


# # Встановлюємо з'єднання з базою даних
# conn = sqlite3.connect('data/surowiec.db')
# cursor = conn.cursor()

# # Виконуємо запит ALTER TABLE для додавання стовпця "barwnik_id"
# alter_table_query = '''
#     ALTER TABLE kurs
#     ADD COLUMN date_time DATETIME
# '''
# cursor.execute(alter_table_query)
# conn.commit()

# # Закриваємо з'єднання з базою даних
# conn.close()




# # Встановлюємо з'єднання з базою даних
# conn = sqlite3.connect('data/preforma.db')
# cursor = conn.cursor()
# create_table = '''CREATE TABLE kurs(
#     kurs_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surowiec VARCHAR(25),
#     cena_za_kg FLOAT
#     )
# '''
# cursor.execute(create_table)
# conn.commit()

# # Закриваємо з'єднання з базою даних
# conn.close()



# # Встановлюємо з'єднання з базою даних
# conn = sqlite3.connect('data/barwnik.db')
# cursor = conn.cursor()

# # Виконуємо запит DELETE FROM для видалення записів з таблиці "data" з певною умовою
# delete_query = '''
#     DELETE FROM data
#     WHERE Kolor_cecha = ?
# '''
# params = ('_E%',)  # Параметри для умови
# cursor.execute(delete_query, params)

# # Зберігаємо зміни у базі даних
# conn.commit()

# # Закриваємо з'єднання з базою даних
# conn.close()



# Встановлюємо з'єднання з базою даних
# conn = sqlite3.connect('data/preforma.db')
# cursor = conn.cursor()

# # Виконуємо запит DELETE FROM для видалення записів з таблиці "data" з певною умовою
# delete_query = '''
#     DELETE FROM kurs
# '''
# cursor.execute(delete_query)

# # Зберігаємо зміни у базі даних
# conn.commit()

# # Закриваємо з'єднання з базою даних
# conn.close()


# import sqlite3

# conn = sqlite3.connect('data/preforma.db')
# cursor = conn.cursor()

# cursor.execute('DROP TABLE kurs')

# conn.commit()
# conn.close()


from datetime import datetime

# Встановлюємо з'єднання з базою даних

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%d-%m-%y %H:%M")
conn = sqlite3.connect('data/surowiec.db')
cursor = conn.cursor()

# Запит UPDATE для зміни значень в таблиці
# update_query = '''UPDATE Kurs SET date_time = ? WHERE kurs_id = ?'''
# new_cena_za_kg = 0  # Нове значення поля cena_za_kg
# surowiec_to_update = 'ASS'  # Рядок, який потрібно змінити
cursor.execute("UPDATE Kurs SET date_time=? WHERE kurs_id=?", (formatted_date, 5))
# Виконуємо запит UPDATE
# cursor.execute(update_query, (formatted_date, 5))

# Зберігаємо зміни
conn.commit()

# Закриваємо з'єднання з базою даних
conn.close()

