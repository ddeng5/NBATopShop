import sqlite3
from sqlite3 import Error
import os 
from schemas import table_setup_sql

DB_FILE = 'topShopDB.db'
PLAYER_TABLE = 'Players'

def open_connection():
    """ create a database connection to a SQLite database """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = dir_path+"/"+DB_FILE
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return
    return conn


def addPlayer(playerObjs):
	conn = open_connection()
	# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
 	#          ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
 	#          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
 	#         ]
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+PLAYER_TABLE+' VALUES (?,?,?)', playerObjs)
		conn.commit()
		conn.close()

def create_table(conn, create_table_sql):
	try:
		cur = conn.cursor()
		cur.execute(create_table_sql)
	except Error as e:
		print(e)


def setup():
	tables = table_setup_sql()
	# create a database connection
	conn = open_connection()

	# create tables
	if conn is not None:
		for table_sql in tables:
			print(table_sql)
			# create projects table
			create_table(conn, table_sql)
	else:
		print("Error! cannot create the database connection.")
	conn.commit()
	conn.close()
	
if __name__ == '__main__':
	setup()
	addPlayer([(0, 'asdlkjasdf', 'LeBron James'),
		(1, 'lkjhkjhk', 'Kobe')])

