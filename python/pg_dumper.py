import re
from datetime import datetime, date
# from psycopg2.errors import OperationalError

from envparse import env
import psycopg2
from psycopg2._psycopg import IntegrityError


def create_query(cursor, rows, table_name):
    columns = ", ".join([i.name for i in cursor.description])
    sql = 'BEGIN;\n'
    for row in rows:
        values = []
        for i in row:
            if i is None:
                values.append('NULL')
            elif isinstance(i, datetime):
                values.append(f"\'{i.strftime('%Y-%m-%d %H:%M:%S')}\'")
            elif isinstance(i, date):
                values.append(f"\'{i.strftime('%Y-%m-%d')}\'")
            elif isinstance(i, bool):
                values.append('true' if i else 'false')
            elif isinstance(i, str):
                values.append('\'\'' if not i else f"\'{i}\'")
            elif isinstance(i, (int, float)):
                values.append(str(i))
            else:
                values.append(i)
        values = ", ".join(values)
        sql += f"insert INTO {table_name} ({columns}) VALUES ({values});\n"

    sql += "COMMIT;\n"

    return sql


if __name__ == '__main__':
    DB_HOST = env.str('DB_HOST', default='127.0.0.1')
    DB_PORT = env.int('DB_PORT', default=5433)
    DB_NAME = env.str('DB_NAME', default='postgres')
    DB_PASSWORD = env.str('DB_PASSWORD', default='postgres')
    DB_USER = env.str('DB_USER', default='postgres')
    conn_prod = psycopg2.connect(f"host={DB_HOST} dbname={DB_NAME} port={DB_PORT} "
                                 f"user={DB_USER} password={DB_PASSWORD}")

    conn_local = psycopg2.connect(f"host=127.0.0.1 dbname=mastersber port=5432 "
                                  f"user=postgres password=postgres")
    cur_local = conn_local.cursor()

    table_name = 'crm_task'
    batch_size = 1
    offset = 0
    for i in range(100):
        cur_prod = conn_prod.cursor()
        cur_prod.execute(f"SELECT now()")
        rows = cur_prod.fetchall()

        sql = create_query(cur_prod, rows, table_name)

        try:
            cur_local.execute(sql)
        except IntegrityError as e:
            conn_local.rollback()
            if e.pgcode == '23503':
                match = re.match(r"Key \((.*)\)=\((.*)\)", e.diag.message_detail)
                g1 = match.group(1)
                g2 = match.group(2)
                if g1 == 'crm_deal_id':
                    cur_prod.execute(f"SELECT * from crm_deal WHERE id = {g2}")
                    row = cur_prod.fetchone()
                    sql = create_query(cur_prod, [row, ], table_name='crm_deal')
                    # cur_local.close()
                    # cur_local = conn_local.cursor()
                    cur_local.execute(sql)
                    pass
            elif e.pgcode == '23505':
                pass
            else:
                pass
            pass
        except Exception as e:
            pass

        offset += batch_size
