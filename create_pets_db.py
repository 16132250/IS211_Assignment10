import sqlite3


def create_pets_db():

    try:

        with sqlite3.connect('pets.db') as con:

            con.execute("DROP TABLE IF EXISTS person;")
            con.execute("DROP TABLE IF EXISTS pet;")
            con.execute("DROP TABLE IF EXISTS person_pet;")

            con.execute('''CREATE TABLE person (
                            id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            age INTEGER
                            );''')

            con.execute('''CREATE TABLE pet (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            breed TEXT,
                            age INTEGER,
                            dead INTEGER
                            );''')

            con.execute('''CREATE TABLE person_pet (
                            person_id INTEGER,
                            pet_id INTEGER
                            );''')

            con.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    create_pets_db()