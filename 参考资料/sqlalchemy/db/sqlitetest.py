#_*_ coding:utf-8 _*_


import sqlite3

def get_sql(sql):
    cursor.execute(sql)
    y = cursor.fetchall()
    print(sql)
    print(y)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("select name from sqlite_master where type = 'table' order by name;")
x = cursor.fetchall()
tb_names = x

for i in tb_names:
    str = 'select * from %s' % i[0]
    get_sql(str)
