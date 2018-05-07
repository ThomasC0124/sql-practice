import sys
import sqlite3
import logging

def _configure_logger():
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_format)

def create_table(connection, table_name, table_schema):
    c = connection.cursor()
    try:
        c.execute('''CREATE TABLE {} ({})'''.format(table_name, table_schema))
        logger.info('"{}" table created'.format(table_name))
    except sqlite3.OperationalError:
        logger.warning('"{}" table already exists, skip'.format(table_name))

def insert_data(connection, table_name, data):
    c = connection.cursor()
    c.execute('''INSERT INTO {} VALUES({})'''.format(table_name, data))
    connection.commit()
    logger.info('"{}" inserted into "{}" table'.format(data, table_name))

if __name__ == '__main__':
    _configure_logger()
    logger = logging.getLogger(__name__)
    
    conn = sqlite3.connect('sqlite_phonebook.db')
    # create person and address tables
    person_schema = '''
        id INTEGER PRIMARY KEY ASC,
        name varchar(250) NOT NULL
    '''
    create_table(conn, 'person', person_schema)
    address_schema = '''
        id INTEGER PRIMARY KEY ASC,
        street_name varchar(250),
        street_number varchar(250),
        post_code varchar(250) NOT NULL,
        person_id INTEGER NOT NULL,
        FOREIGN KEY(person_id) REFERENCES person(id)
    '''
    create_table(conn, 'address', address_schema)
    # insert data
    insert_data(conn, 'person', '1, "pythoncentral"')
    insert_data(conn, 'address', '1, "python road", "1", "00000", 1')

    conn.close()
