import tkinter as tk
import sqlite3
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askquestion

root=tk.Tk()
root.geometry("300x300")
# ans=askquestion("Do you want to open database, or Create Database?")



dbname = 'myshelf.sqlite3'
# DBを作成する（既に作成されていたらこのDBに接続する）
conn = sqlite3.connect(dbname)

cur = conn.cursor()

# テーブルの作成
# cur.execute(
#     'CREATE TABLE mybooks(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
cur.execute('INSERT INTO mybooks values(2,"Classic Python")')
# cur.execute("DELETE FROM items WHERE id='1'")
cur.execute("SELECT * FROM mybooks")

for row in cur:
    print(row)

# コミットしないと登録が反映されない
conn.commit()

# DBとの接続を閉じる(必須)
conn.close()


# root.mainloop()