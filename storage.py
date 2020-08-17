import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text,author text, year integer, ISBN integer)")
    conn.commit()
    conn.close()

def insert_data(title, author, year, isbn,db_file):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view_data(db_file):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")

    rows = cur.fetchall()
    conn.close()

    return rows

def search_data(db_file,title = "", author = "", year="", isbn=""):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title =? OR author = ? OR year =?OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_data(db_file,id,title, author, year, isbn):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?,author=?,year =?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


def delete_data(db_file,id):
    conn = None 
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
create_connection("MyBooks.db")
insert_data("effective c++","scott meyers", 2011,955622333,"MyBooks.db")
print(view_data("MyBooks.db"))
update_data("MyBooks.db",2,"The moon","John Smooth",2012,7778838838)
print(search_data("MyBooks.db",year = "2011"))