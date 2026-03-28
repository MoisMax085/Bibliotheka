from bibliotheka import *



def main():
    [cursor, connection] = check_table()
    answer = choose_option()
    set_option(answer, cursor, connection)
if __name__ == "__main__":
    main()