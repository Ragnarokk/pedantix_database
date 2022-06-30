#!/usr/bin/env python3
from database_handler import DatabaseHandler
from pedantix_interface import PedantixInterface


def main():
    database = DatabaseHandler()
    pedantix = PedantixInterface(database)

    words = database.get_top_words(100)
    print('top words : ', words)

    pedantix.manual_tries()


if __name__ == '__main__':
    main()
