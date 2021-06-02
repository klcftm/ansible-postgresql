import json
from configparser import ConfigParser
import psycopg2


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            value = param[1]
            db[param[0]] = value
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def create_tables(table_name, fields):
    """ create tables in the PostgreSQL database"""
    columns = []
    for col in fields:
        columns.append(("{} {}").format((col['id']), (col['type'])))

    query = ("CREATE TABLE {tbl_name} ( {fields} );").format(
        tbl_name=(table_name),
        fields=(', ').join(columns)
    )
    print(query)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_tables(table_name, rec):
    """ insert tables in the PostgreSQL database"""
    columns = []
    for count, col in enumerate(rec):
        if count == 0:
            columns.append(("{}").format((col)))
        else:
            columns.append(("'{}'").format((col)))
    query = ("INSERT INTO {tbl_name} VALUES( {rec} );").format(
        tbl_name=(table_name),
        rec=(', ').join(columns)
    )
    print(query)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def read_json_file_fields(filename, type):
    # Opening JSON file
    with open(filename, ) as f:
        data = json.load(f)
        return data[type]


if __name__ == '__main__':
    file = 'data/Ocak 2020 Trafik Yo_unluk Verisi.json'
    fields = read_json_file_fields(file, 'fields')
    create_tables('infradb2', fields)
    records = read_json_file_fields(file, 'records')
    for rec in records:
        insert_tables('infradb2', rec)
