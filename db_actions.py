import random
from time import time, strftime, gmtime

from sqlalchemy.exc import SQLAlchemyError
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def db_connection():
    with SSHTunnelForwarder(
            ('46.101.107.252', 22),
            ssh_private_key="C:/Users/HOMEPC/PycharmProjects/Realpush/pushlead.pem",
            ssh_username="root",
            # ssh_password="<password>",
            remote_bind_address=(
                    'localhost', 5432)) as server:  # PostgreSQL server IP and server port on remote machine
        # sshtunnel.SSH_TIMEOUT = 5.0
        server.daemon_forward_servers = True
        server.start()
        print('Server connected via SSH')

        # connect to PostgreSQL
        local_port = str(server.local_bind_port)
        engine = create_engine('postgresql://pusher:YefRzuvhCjhc@127.0.0.1:' + local_port + '/pusher_prod')

        Session = sessionmaker(bind=engine)
        session = Session()
        print('Database session created')

        try:
            start_time = time()
            # print("Total rows are:  ", len(result))
            # for row in result:
            #   print(row['src_id'])
            #   print("{0} {1} {2}".format(row[0], row[1], row[2]))
            cursor1 = session.execute(
                "SELECT src_id, user_agent, token, language FROM public.subscriptions as subs1, public.subscribers as "
                "subs2 "
                "where "
                "subs1.id = "
                "subs2.subscription_id")
            result = cursor1.fetchall()
            data1 = [row.src_id for row in result]
            random_sid = random.choice(data1)
            data2 = [row.token for row in result]
            random_token = random.choice(data2)
            data3 = [row.language for row in result]
            random_lang = random.choice(data3)
            data4 = [row.user_agent for row in result]
            random_ua = random.choice(data4)
            cursor1.close()
            end_time = time()
            print("Execution_time is :", strftime("%H:%M:%S", gmtime(int('{:.0f}'.format(float(str((end_time - start_time))))))))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        finally:
            if session.is_active:
                session.close()
                engine.dispose()
                print("Database connection is closed")
            if server.is_active:
                server.stop()
                print('Server disconnected')
        return random_sid, random_token
