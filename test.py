# import eel
# import sqlite3
#
# conn = sqlite3.connect('test.db')
#
# c = conn.cursor()
#
# c.execute("""CREATE TABLE employees (
#              first text,
#              last text,
#              pay integer
#              )""")
#
# # c.execute("INSERT INTO employees VALUES ('Dave', 'Smith', 40000)")
#
# result = c.execute("SELECT * FROM employees")
#
# print(c.fetchone())
#
# conn.commit()
#
# conn.close()
#
# eel.init('web')
#
# @eel.expose
# def test(param):
#     return 'test return', param
#
#
#
# eel.start('index.html')
