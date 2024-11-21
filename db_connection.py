from api_connection import *
import pandas as pd
import sqlite3

def open_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def close_connection(conn):
    conn.close()

def df_to_sql(dataframe,table_name,conn):
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)

def get_all_tables(conn):
    query  = "SELECT name FROM sqlite_master WHERE type='table'"
    df = pd.read_sql_query(query, conn)
    return df

def get_all_from_table(table_name,conn):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query,conn)
    return df