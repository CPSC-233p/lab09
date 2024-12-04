import sqlite3

class Contacts:

    def __init__(self, databaseName=''):
        self._databaseName = databaseName

    def set_database_name(self, databaseName):
        self._databaseName = databaseName

        connection = sqlite3.connect(databaseName)
        print("Database successfully connected")
        cursor = connection.cursor()

        #create a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL 
        )
        """)
        print("Table created succesfully")
        connection.commit()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS phones (
            phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER,
            phone_type TEXT NOT NULL,
            phone_number TEXT NOT NULL 
        )
        """)
        print("Table created succesfully")
        connection.commit()

        connection.close()

    def get_database_name(self):
        return self._databaseName
    
    def add_contact(self, first_name, last_name):

        connection = sqlite3.connect(self._databaseName)

        cursor = connection.cursor()

        cursor.execute("INSERT INTO contacts (first_name, last_name) VALUES (?, ?)", (first_name, last_name))

        connection.commit()

        connection.close()

    def modify_contact(self, contact_id, first_name, last_name):

        connection = sqlite3.connect(self._databaseName)

        cursor = connection.cursor()

        cursor.execute("UPDATE contacts SET first_name = ?, last_name = ? WHERE contact_id = ?", (first_name, last_name, contact_id))

        connection.commit()

        connection.close()

    def add_phone(self, contact_id, phone_type, phone_number):

            connection = sqlite3.connect(self._databaseName)

            cursor = connection.cursor()

            cursor.execute("INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?, ?, ?)", (contact_id, phone_type, phone_number))

            connection.commit()
            connection.close()

    def modify_phone(self, phone_id, phone_type, phone_number):

        connection = sqlite3.connect(self._databaseName)

        cursor = connection.cursor()

        cursor.execute("UPDATE phones SET phone_type = ?, phone_number = ? WHERE phone_id = ?", (phone_type, phone_number, phone_id))

        connection.commit()
        connection.close()

    
    def get_contact_phone_list(self):
        connection = sqlite3.connect(self._databaseName)
        cursor = connection.cursor()
        cursor.execute("SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id")
        data = cursor.fetchall()
        connection.close()
        return data

        
