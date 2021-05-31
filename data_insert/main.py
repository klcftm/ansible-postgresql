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

def create_tables(table_name,fields):
    """ create tables in the PostgreSQL database"""
    size = len(fields)
    columns = []
    for col in fields:
        columns.append(psycopg2.sql.SQL("{} {}").format(psycopg2.sql.Identifier(col[1]), psycopg2.sql.SQL(col[0])))

    query = psycopg2.sql.SQL( "CREATE TABLE {tbl_name} ( {fields} );" ).format(
        tbl_name=psycopg2.sql.Identifier(table_name),
        fields=psycopg2.sql.SQL(', ').join(columns)
    )
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

def read_json_file_fields(filename):
    # Opening JSON file
    with open(filename, ) as f:
        data = json.load(f)
        return data['fields']

if __name__ == '__main__':
    fields = read_json_file_fields('data/Ocak 2020 Trafik Yo_unluk Verisi.json')
    create_tables('infradb',fields)


