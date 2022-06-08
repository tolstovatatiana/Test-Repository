
import mysql.connector
from genre import GenreSQL

DB_Q = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1415",
    db="simple_library_sys",
    autocommit=True
)

cursor = DB_Q.cursor()
table_genre_manager = GenreSQL(cursor_param=cursor)

genre_novel = table_genre_manager.get_genre_by_id(id=1)
print(genre_novel)

all_genres = table_genre_manager.get_all_genres()
print(all_genres)

delete_genre = table_genre_manager.delete_genre_by_id(id=1)
print(delete_genre)
