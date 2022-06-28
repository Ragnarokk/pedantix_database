import sqlite3

CREATE_WORDS_TABLE = '''CREATE TABLE IF NOT EXISTS words(''' \
                        '''word     CHAR(50) PRIMARY KEY NOT NULL,''' \
                        '''tries    INT     NOT NULL,''' \
                        '''greens   INT,''' \
                        '''oranges  INT,''' \
                        '''timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)'''

class DatabaseHandler:

    def __init__(self) -> None:
        self.con = sqlite3.connect('words.sqlite')
        self.cur = self.con.cursor()

        self.cur.execute(CREATE_WORDS_TABLE)