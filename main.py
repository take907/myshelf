import tkinter as tk
import sqlite3
from tkinter.constants import ANCHOR
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askquestion


root=tk.Tk()
root.geometry("300x300")
# ans=askquestion("Do you want to open database, or Create Database?")
command_frame=tk.Frame(root)
select_button=tk.Button(command_frame,text="SELECT",width=10)
insert_button=tk.Button(command_frame,text="INSERT",width=10)
delete_button=tk.Button(command_frame,text="DELETE",width=10)
update_button=tk.Button(command_frame,text="UPDATE",width=10)

# button = tk.Button(root, text="OFFICE\rAND\rFive Four", font=("MSゴシック", "20", "bold"), width=100, justify=tk.LEFT)
select_button.pack(side=tk.LEFT)
insert_button.pack(side=tk.LEFT)
delete_button.pack(side=tk.LEFT)
update_button.pack(side=tk.LEFT)
command_frame.pack()

dbname = 'myshelf.sqlite3'
# DBを作成する（既に作成されていたらこのDBに接続する）
conn = sqlite3.connect(dbname)

cur = conn.cursor()

# テーブルの作成
# cur.execute(
#     'CREATE TABLE mybooks(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
# cur.execute('INSERT INTO mybooks values(3,"Math Master")')
# cur.execute("DELETE FROM items WHERE id='1'")
cur.execute("SELECT * FROM mybooks")

buttons=[_ for _ in cur]
for button in buttons:
    b=tk.Button(root,text=button)
    b.pack()

# コミットしないと登録が反映されない
conn.commit()

# DBとの接続を閉じる(必須)
conn.close()


root.mainloop()