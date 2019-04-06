import sqlite3
import os
# os.chdir('D:\PycharmProjects\第十二章/')
if __name__ == '__main__':
    con = sqlite3.connect('login.db')
    cur  = con.cursor()
    # cur.execute('CREATE TABLE mytab(id integer PRIMARY KEY AUTOINCREMENT NOT NULL ,name text,passwd text,people text)')
    # cur.execute('INSERT INTO mytab(name,passwd,people)VALUES(?,?,?)',(1,1,'学生'))
    # cur.execute('INSERT INTO mytab(name,passwd,people)VALUES(?,?,?)',(2,2,'教师'))
    # cur.execute('UPDATE mytab SET passwd =? WHERE id=?',(9,9))
    # cur.execute('DELETE FROM mytab')
    cur.execute('SELECT *FROM mytab ')
    con.commit()
    for item in  cur.fetchall():
        print(item)
    cur.close()
    con.close()