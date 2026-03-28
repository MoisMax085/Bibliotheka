from bibliotheka import *



def main():
    [cursor, connection] = check_table()

    answer = choose_option()
    while answer != 4:
        set_option(answer, cursor, connection)
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        answer = choose_option()
if __name__ == "__main__":
    main()