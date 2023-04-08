import sqlite3

def create_music_db:

    try:

        with sqlite3.connect('music.db') as con:

            con.execute('DROP TABLE IF EXISTS songs;')
            con.execute('DROP TABLE IF EXISTS albums;')
            con.execute('DROP TABLE IF EXISTS artists;')

            con.execute('''CREATE TABLE artists (
                            artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            artist_name TEXT NOT NULL
                            );''')

            con.execute('''CREATE TABLE albums (
                            album_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            album_name TEXT NOT NULL,
                            artist_id INTEGER NOT NULL,
                            FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
                            );''')

            con.execute('''CREATE TABLE songs (
                            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            song_name TEXT NOT NULL,
                            album_id INTEGER NOT NULL,
                            track_number INTEGER NOT NULL,
                            song_length INTEGER NOT NULL,
                            FOREIGN KEY (album_id) REFERENCES albums(album_id)
                            );''')

            con.commit()

    except sqlite3.Error as e:
        print('An error occurred:', e)

if __name__ == "__main__":
    create_music_db()