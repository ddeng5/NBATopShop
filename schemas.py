def table_setup_sql():
	return [
	""" CREATE TABLE IF NOT EXISTS Players (
                    playerId integer PRIMARY KEY,
                    name text NOT NULL,
                    guid text
                ); """,
    """CREATE TABLE IF NOT EXISTS Sets (
	                setId integer PRIMARY KEY,
	                name text NOT NULL,
	                category text NOT NULL,
	                seriesNumber integer NOT NULL,
	                guid text
	            );""",
     """CREATE TABLE IF NOT EXISTS Moments (
	                momentId integer PRIMARY KEY,
	                name text NOT NULL,
	                limited boolean NOT NULL,
	                circulationCount integer NOT NULL,
	                playerId integer NOT NULL,
	                setId integer NOT NULL,
	                guid text,
	                FOREIGN KEY(playerId) REFERENCES Players(playerId),
	                FOREIGN KEY(setId) REFERENCES Sets(setId)
	            );""",
	 """CREATE TABLE IF NOT EXISTS Users (
	                userId integer PRIMARY KEY,
	                username text NOT NULL,
	                guid text
	            );""",
	 """CREATE TABLE IF NOT EXISTS Transactions (
	                transactionId integer PRIMARY KEY,
	                momentId integer NOT NULL,
	                buyerId integer NOT NULL,
	                sellerId integer NOT NULL,
	                price decimal NOT NULL,
	                updated date NOT NULL NOT NULL,
	                FOREIGN KEY(momentId) REFERENCES Moments(momentId),
	                FOREIGN KEY(buyerId) REFERENCES Users(userId),
	                FOREIGN KEY(sellerId) REFERENCES Users(userId)
	            );"""
	            
       ]
