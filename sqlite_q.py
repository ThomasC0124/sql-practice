import sys
import sqlite3
import logging

def _configure_logger():
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_format)

def query_data(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

if __name__ == '__main__':
    _configure_logger()
    logger = logging.getLogger(__name__)
    
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    # query person and address
    person_query = 'SELECT * FROM person'
    person = query_data(cursor, person_query)
    print(person)
    address_query = 'SELECT * FROM address'
    address = query_data(cursor, address_query)
    print(address)

    conn.close()
