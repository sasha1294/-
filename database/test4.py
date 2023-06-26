import sqlite3 as sq

def start_db():
    db = sq.connect('data.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Numbers(id INTEGER PRIMARY KEY AUTOINCREMENT,number TEXT);""")
    db.commit()
    return db, cur

db, cur = start_db()

async def result1(x):
    cur.execute('''INSERT INTO Numbers VALUES(NULL, ?)''', (x,))
    db.commit()

async def result2(x):
    cur.execute("""INSERT INTO Numbers VALUES(NULL, ?)""", (x,))
    db.commit()

def DELETE():
    sql_delete_query = """DELETE from Numbers"""
    cur.execute(sql_delete_query)
    db.commit()
    print("Запись успешно удалена")
    db.commit()