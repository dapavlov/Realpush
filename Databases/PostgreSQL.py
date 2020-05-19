import os
import random
from functools import wraps
from pathlib import Path
from time import strftime, gmtime
from timeit import default_timer as timer
from sqlalchemy.exc import SQLAlchemyError
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker, create_session
from sqlalchemy import create_engine

home = str(Path.home())

# engine = None
# Session = None
# session = None


def run_server():
    with SSHTunnelForwarder(
            ('46.101.107.252', 22),
            ssh_private_key=os.path.join(home, '.ssh\pushlead.pem'),
            ssh_username="root",
            # ssh_password="<password>",
            remote_bind_address=(
                    'localhost', 5432)) as server:  # PostgreSQL server IP and server port on remote machine
        # sshtunnel.SSH_TIMEOUT = 5.0
        server.daemon_forward_servers = True
        server.daemon_transport = True
        server.start()
        print('Server connected via SSH')

        def set_session():
            # connect to PostgreSQL by creating an engine
            global random_sid, random_token, domain_list
            local_port = str(server.local_bind_port)
            engine = create_engine('postgresql+psycopg2://pusher:YefRzuvhCjhc@127.0.0.1:' + local_port + '/pusher_prod',
                                   connect_args={'connect_timeout': 10})
            # create a configured "Session" class
            Session = sessionmaker(bind=engine)
            # create a Session
            session = Session()
            print('Database session created')

            def cleanup():
                session.close()
                engine.dispose()
                print("PostgreSQL connection is closed")
                server.stop()
                print('Server disconnected')

            try:
                random_sid, random_token = call_operation1(session)
                domain_list = call_operation2(session)
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
            finally:
                cleanup()
            return random_sid, random_token, domain_list
            # def measure_time(func):
            #     def inner_func(*args, **kwargs):
            #         start = timer()
            #         func(*args, **kwargs)
            #         end = timer()
            #         print(f'Function {func.__name__} took: ',
            #               strftime("%H:%M:%S", gmtime(int('{:.0f}'.format(float(str((end - start))))))))
            #
            #     return inner_func

        def call_operation1(session):
            cursor = session.execute(
                "SELECT src_id, user_agent, token, language FROM public.subscriptions as subs1, "
                "public.subscribers as "
                "subs2 "
                "where "
                "subs1.id = "
                "subs2.subscription_id")
            result1 = cursor.fetchall()
            # print("Total rows are:  ", len(result))
            # for row in result:
            #   print(row['src_id'])
            #   print("{0} {1} {2}".format(row[0], row[1], row[2]))
            data1 = [row.src_id for row in result1]
            random_sid = random.choice(data1)
            data2 = [row.token for row in result1]
            random_token = random.choice(data2)
            # data3 = [row.language for row in result1]
            # random_lang = random.choice(data3)
            return random_sid, random_token

        def call_operation2(session):
            cursor = session.execute(
                "select domain from websites w  where domain like ('http%://%') or domain like "
                "('www.%') and native_push = true order by id")
            result2 = cursor.fetchall()
            domain_list = [row.domain for row in result2]
            cursor.close()
            return domain_list

        random_sid, random_token, domain_list = set_session()
        return random_sid, domain_list

# def provide_session(func):
#     """
#     Function decorator that provides a session if it isn't provided.
#     If you want to reuse a session or run the function as part of a
#     database transaction, you pass it to the function, if not this wrapper
#     will create one and close it for you.
#     """
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         arg_session = 'session'
#
#         func_params = func.__code__.co_varnames
#         session_in_args = arg_session in func_params and \
#                           func_params.index(arg_session) < len(args)
#         session_in_kwargs = arg_session in kwargs
#
#         if session_in_kwargs or session_in_args:
#             return func(*args, **kwargs)
#         else:
#             with create_session() as session:
#                 kwargs[arg_session] = session
#                 return func(*args, **kwargs)
#
#     return wrapper

# if __name__ == '__main__':
#     set_session()
