import os
from pathlib import Path
from sshtunnel import SSHTunnelForwarder
from clickhouse_driver import Client
import clickhouse_driver
from sqlalchemy import create_engine, Column, MetaData, literal
from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines
from sqlalchemy.orm import sessionmaker

home = str(Path.home())

with SSHTunnelForwarder(
        ('stage-db.wirknode.com', 22),
        ssh_private_key=os.path.join(home, '.ssh\id_rsa'),
        ssh_username="dmitrii",
        # ssh_password="<password>",
        remote_bind_address=(
                'localhost', 8123)) as server:  # Clickhouse server IP and server port on remote machine
    # sshtunnel.SSH_TIMEOUT = 5.0
    server.daemon_forward_servers = True
    server.start()
    print('Server connected via SSH')

    # connect to Clickhouse
    # conn = clickhouse_driver.connect("clickhouse://localhost/pusher_prod")
    # Session = sessionmaker(bind=conn)
    # session = Session()
    # print('Database session created')

    client = Client(host='localhost', port='9000', database="pusher_prod")
    print(client.execute('SHOW TABLES'))
    result = client.execute('SELECT now(), version()')
    print("RESULT: {0}: {1}".format(type(result), result))
    for t in result:
        print(" ROW: {0}: {1}".format(type(t), t))
        for v in t:
            print("  COLUMN: {0}: {1}".format(type(v), v))

    # conn = connect('clickhouse://localhost')
    # cursor = conn.cursor()
    # cursor.execute('SHOW TABLES')
    # cursor.fetchall()
