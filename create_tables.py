"""This is the create_tables module.
This module is responsible for create the database sparkifydb on postgres,
also will create all tables that is described on sql_queries.py module.
"""

import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """This function will create the database sparkifydb on postgres.
    
    Args:
        None
        
    Returns:
        None
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """This function will drop all tables that is described on sql_queries.py module
    
    Args:
        cur (psycopg2.extensions.cursor): The cursor from your connection with postgres
        conn (psycopg2.extensions.connection): The connection with postgres
        
    Returns:
        None
    """
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """This function will create all tables that is described on sql_queries.py module
    
    Args:
        cur (psycopg2.extensions.cursor): The cursor from your connection with postgres
        conn (psycopg2.extensions.connection): The connection with postgres
        
    Returns:
        None
    """
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """This is the main function, will start with this module
    and execute all another functions.
    
    Args:
        None
        
    Returns:
        None
    """
    
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()