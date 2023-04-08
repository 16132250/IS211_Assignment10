import sqlite3

def create_music_db:

    try:

        with sqlite3.connect('music.db') as con:

            con.execute('DROP TABLE IF EXISTS songs;')
            con.execute('DROP TABLE IF EXISTS albums;')
            con.execute('DROP TABLE IF EXISTS artists;')

            con.execute('''CREATE TABLE artists (
                            artist_id INTEGER PRIMARY KEY,
                            artist_name TEXT
                            );''')

            con.execute('''CREATE TABLE albums (
                            album_id INTEGER PRIMARY KEY,
                            album_name TEXT,
                            artist_id INTEGER
                            );''')

            con.execute('''CREATE TABLE songs (
                            song_id INTEGER PRIMARY KEY
                            song_name TEXT,
                            album_id INTEGER,
                            track_number INTEGER,
                            song_length INTEGER
                            );''')

            con.commit()

    except sqlite3.Error as e:
        print('An error occurred:', e)

if __name__ == "__main__":
    create_music_db()