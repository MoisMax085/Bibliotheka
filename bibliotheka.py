import os
import sqlite3
def create_table(cursor):
    cursor.execute("""CREATE TABLE bibliothek (id INTEGER PRIMARY KEY AUTOINCREMENT, autor TEXT, name_book TEXT, age INTEGER, link TEXT)""")

def check_table():
    if os.path.exists('bibliotheka.db') == False:
        connection = sqlite3.connect("bibliotheka.db")
        cursor = connection.cursor()
        create_table(cursor)
        return cursor, connection
    else:
        connection = sqlite3.connect("bibliotheka.db")
        cursor = connection.cursor()
        return cursor, connection




def choose_option():
    try:
        answer = int(input("Что бы вы хотели сделать ?\n"
              "1. Добавить книгу в фонд\n"
              "2. Найти книгу в фонде\n"
              "3. Удалить книгу из фонда\n"
              "4. Выйти из библиотеки\n"
                "Ваш выбор :"))
        return answer
    except ValueError or TypeError:
        wrong_answer()

def set_option(answer, cursor, connection):
    match answer:
        case 1:
            add(cursor, connection)
            return
        case 2:
            find(cursor, connection)
        case 3:
            delete(cursor, connection)
            return
        case 4:
            input('\nДля закрытия библиотеки нажмите любую клавишу')
            return

def delete(cursor, connection):
    [avtor, name_book, year] = ask_a_n_y_l(key = 2)
    cursor.execute(f"DELETE FROM bibliothek WHERE autor=? AND name_book=? AND age=?", (f'{avtor}', f'{name_book}', year))
    connection.commit()
    return

def find(cursor, connection):
    os.system("cls" if os.name == "nt" else "clear")
    what = input('\nВведите автора книги или название книги:')
    os.system("cls" if os.name == "nt" else "clear")
    cursor.execute(f"SELECT * FROM bibliothek WHERE autor LIKE '%{what}%' OR name_book LIKE '%{what}%'")
    for i in cursor.fetchall():
        print(' '.join(str(i)).replace('(', "").replace(')', "").replace(' ', '').replace(',', ' '))
def add(cursor, connection):
    [avtor, name_book, year, link] = ask_a_n_y_l(key = 1)
    cursor.execute(f"INSERT INTO bibliothek (autor, name_book, age, link) VALUES ('{avtor}', '{name_book}', {year}, '{link}')")
    connection.commit()
    return

def ask_a_n_y_l(key):
    os.system("cls" if os.name == "nt" else "clear")
    avtor = str(input('\n Введите автора книги: '))
    name_book = str(input('\n Введите название книги: '))
    year = int(input('\n Введите год издания книги: '))
    if key == 1:
        link = str(input('\n Введите ссылку на книгу: '))
        os.system("cls" if os.name == "nt" else "clear")
        return avtor, name_book, year, link
    elif key == 2:
        return avtor, name_book, year
def wrong_answer():
    print("\033[31m{}\033[0m".format("=" * 100 + "\nОшибка ввода\n" + "=" * 100))
    choose_option()