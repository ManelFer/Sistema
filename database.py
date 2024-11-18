import sqlite3

class DataBase():
    def __init__(self, name = "system.db"):
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS users(
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           user TEXT UNIQUE NOT NULL,
                           password TEXT NOT NULL,
                           access TEXT NOT NULL
                        )
                    """)
        except AttributeError:
            print("Faça a conexão com o banco")

if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.close_connection()