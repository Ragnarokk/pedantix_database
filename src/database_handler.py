import sqlite3
from typing import List

CREATE_WORDS_TABLE = '''CREATE TABLE IF NOT EXISTS words(''' \
                        '''word     CHAR(50) PRIMARY KEY NOT NULL,''' \
                        '''tries    INT     NOT NULL,''' \
                        '''greens   INT,''' \
                        '''oranges  INT,''' \
                        '''timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)'''

class DatabaseHandler:

    def __init__(self) -> None:
        self.connection = sqlite3.connect('words.sqlite')
        self.cursor = self.connection.cursor()

        self.cursor.execute(CREATE_WORDS_TABLE)

        self.tried_words = set()

    def insert_word(self, word: str, greens: int, oranges: int) -> None:
        """
        Method that inserts a new word into the database
        """
        insert_query = "INSERT INTO words (word, tries, greens, oranges) VALUES (?, ?, ?, ?);"

        if word not in self.tried_words:
            data = (word, 1, greens, oranges)

            self.cursor.execute(insert_query, data)
            self.connection.commit()

            self.tried_words.add(word)

    def get_top_words(self, top_nb: int) -> List[str]:
        """
        Method that selects all the first top_nb words contained in the database with the best greens/tries rate if their last try was not today
        """
        query = """SELECT word, greens / tries as rate, DATE(timestamp) as last_try, DATE('now') as today FROM words WHERE last_try != today ORDER BY rate LIMIT ?"""

        self.cursor.execute(query, (top_nb,))
        result = self.cursor.fetchall()

        return [sel[0] for sel in result]
