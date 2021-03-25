def table_setup_sql():
	return [
	""" CREATE TABLE IF NOT EXISTS Players (
                    guid text PRIMARY KEY,
                    name text NOT NULL
                ); """,
    """CREATE TABLE IF NOT EXISTS Sets (
	                guid text PRIMARY KEY,
	                name text NOT NULL,
	                category text NOT NULL,
	                seriesNumber integer NOT NULL
	            );""",
     """CREATE TABLE IF NOT EXISTS Moments (
	                guid text PRIMARY KEY,
	                name text NOT NULL,
	                limited boolean NOT NULL,
	                circulationCount integer NOT NULL,
	                playerId integer NOT NULL,
	                setId integer NOT NULL,
	                FOREIGN KEY(playerId) REFERENCES Players(guid),
	                FOREIGN KEY(setId) REFERENCES Sets(guid)
	            );""",
	 """CREATE TABLE IF NOT EXISTS Users (
	                guid text PRIMARY KEY,
	                username text NOT NULL
	            );""",
	 """CREATE TABLE IF NOT EXISTS Transactions (
	                guid text PRIMARY KEY,
	                momentId integer NOT NULL,
	                buyerId integer NOT NULL,
	                sellerId integer NOT NULL,
	                price decimal NOT NULL,
	                updated date NOT NULL NOT NULL,
	                FOREIGN KEY(momentId) REFERENCES Moments(guid),
	                FOREIGN KEY(buyerId) REFERENCES Users(guid),
	                FOREIGN KEY(sellerId) REFERENCES Users(guid)
	            );"""
	            
       ]
