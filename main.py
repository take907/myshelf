import tkinter as tk
import sqlite3
from tkinter.constants import ANCHOR
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askquestion
import tkinter.ttk as ttk

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

tree=ttk.Treeview(root)
tree["columns"]=(1,2)
tree["show"]="headings"

tree.column(1,width=75)
tree.column(2,width=100)
# tree.column(3,width=100)

tree.insert("","end",values=("2017/5/1","食費",3500))
tree.insert("","end",values=("2017/5/10","光熱費",7800))
tree.insert("","end",values=("2017/5/10","住宅費",64000))

tree.pack()

dbname = 'myshelf.sqlite3'
# DBを作成する（既に作成されていたらこのDBに接続する）
conn = sqlite3.connect(dbname)

cur = conn.cursor()

# テーブルの作成
# cur.execute(
#     'ALTER TABLE mybooks ADD COLUMN date DATE NOT NULL DEFAULT DATETIME("now","localtime")'
# )
# cur.execute('INSERT INTO mybooks values(3,"Math Master")')
# cur.execute("DELETE FROM items WHERE id='1'")
cur.execute("SELECT * FROM mybooks")

mybooks=[_ for _ in cur]
for book in mybooks:
    tree.insert("","end",values=(book))

cur.execute(
    'SELECT datetime("now","localtime");'
)

for row in cur:
    print(row)

# コミットしないと登録が反映されない
conn.commit()

# DBとの接続を閉じる(必須)
conn.close()


root.mainloop()