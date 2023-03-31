import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
        This drops all the tables if they exist by calling the drop_table_queries defined in sql_queries.py.
        Parameters
        ----------
        cur: class
            This executes the sql commands within a database session.
        conn: class
            This takes care of the connection to a database instance.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
     """
        This creates tables if they don't exist by calling the create_table_queries defined in sql_queries.py.
        Parameters
        ----------
        cur: class
            This executes the sql commands within a database session.
        conn: class
            This takes care of the connection to a database instance.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
        This executes the following:
            1.) Call the create cluster script.
            2.) Establish a db connection.
            3.) Execute the drop and create table methods.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
