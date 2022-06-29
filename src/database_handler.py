import sqlite3

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

    def insert_word(self, word: str, greens: int, oranges: int):
        """
        Method that inserts a new word into the database
        """
        insert_query = "INSERT INTO words (word, tries, greens, oranges) VALUES (?, ?, ?, ?);"

        if word not in self.tried_words:
            data = (word, 1, greens, oranges)

            self.cursor.execute(insert_query, data)
            self.connection.commit()

            self.tried_words.add(word)
