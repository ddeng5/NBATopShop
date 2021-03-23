import sqlite3
from sqlite3 import Error
import os 
from schemas import table_setup_sql

DB_FILE = 'topShopDB.db'
PLAYERS_TABLE = 'Players'
SETS_TABLE = 'Sets'
MOMENTS_TABLE = 'Moments'
USERS_TABLE = 'Users'
TRANSACTIONS_TABLE = 'Transactions'

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


def addPlayers(playerObjs):
	# playerObjs is a tuple of players in the format
	# [player_id, name, guid]
	conn = open_connection()
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+PLAYERS_TABLE+' VALUES (?,?,?)', playerObjs)
		conn.commit()
		conn.close()

def addSets(setObjs):
	# setObjs is a tuple of players in the format
	# [setId, name, category, seriesNumber, guid]
	conn = open_connection()
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+SETS_TABLE+' VALUES (?,?,?,?,?)', setObjs)
		conn.commit()
		conn.close()
		
def addMoments(momentObjs):
	# momentObjs is a tuple of players in the format
	# [momentId, name, limited, circulationCount, playerId, setId, guid]
	conn = open_connection()
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+MOMENTS_TABLE+' VALUES (?,?,?,?,?,?,?)', momentObjs)
		conn.commit()
		conn.close()
		
def addUsers(userObjs):
	# userObjs is a tuple of players in the format
	# [userId, username, guid]
	conn = open_connection()
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+USERS_TABLE+' VALUES (?,?,?)', userObjs)
		conn.commit()
		conn.close()
		
def addTransactions(transactionObjs):
	# transactionObjs is a tuple of players in the format
	# [transactionId, momentId, buyerId, sellerId, price, updated]
	conn = open_connection()
	if conn:
		cur = conn.cursor()
		cur.executemany('INSERT INTO '+TRANSACTIONS_TABLE+' VALUES (?,?,?,?,?,?)', transactionObjs)
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
	addPlayers([(0, 'LeBron James', 'asdlkjasdf'),
		(1, 'Kobe', 'lkjhkjhk')])

	addSets([(0, 'Series 1', 'Shoot', 1, 'asdfkjh'),
		(1, 'Series 2', 'Save', 2, 'asdjkjhfkjh')])

	addMoments([(0, '3 pointer', True, 5000, 0, 0, 'jhfkjoskljh'),
		(1, 'Save', False, 500000, 1, 1, 'jhflkkoskljh')])

	addUsers([(0, 'coolGuy69', 'sdlkjasd'),
		(1, 'saveFace420', 'oookjhkhk')])
	
	addTransactions([(0, 0, 0, 1, 500.45, '2021-03-02 19:23:12'),
		(1, 1, 1, 0, 79.13, '2021-01-02 09:34:11')])
