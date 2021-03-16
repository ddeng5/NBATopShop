def table_setup_sql():
	return [
	""" CREATE TABLE IF NOT EXISTS Players (
                    id integer PRIMARY KEY,
                    guid integer NOT NULL,
                    name text NOT NULL
                ); """,
     """CREATE TABLE IF NOT EXISTS Moments (
	                id integer PRIMARY KEY,
	                name text NOT NULL,
	                priority integer,
	                status_id integer NOT NULL,
	                project_id integer NOT NULL,
	                begin_date text NOT NULL,
	                end_date text NOT NULL,
	                FOREIGN KEY (project_id) REFERENCES projects (id)
	            );"""
       ]
