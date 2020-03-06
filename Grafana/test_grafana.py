import json
import os
import pickle
import time
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def test_grafana_import(browser):
    host = 'http://grafana.wirkserver.com/dashboard/import'
    browser.get(host)
    file_input = WebDriverWait(browser, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//input[@type='file']")))
    # browser.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[
    # 0].style.visibility = "visible";',        file_input)
    file_input.send_keys(os.path.abspath("/Grafana/dashboard.json"))
    browser.switch_to_default_content()
    confirm_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='ctrl.saveDashboard()']")))
# with SSHTunnelForwarder(
#         ('46.101.107.252', 22),
#         ssh_private_key="C:/Users/mi/Documents/pushlead.pem",
#         ssh_username="root",
#         # ssh_password="<password>",
#         remote_bind_address=(
#                 'localhost', 5432)) as server:  # PostgreSQL server IP and server port on remote machine
#
#     server.start()
#     print('Server connected via SSH')
#
#     # connect to PostgreSQL
#     local_port = str(server.local_bind_port)
#     engine = create_engine('postgresql://pusher:YefRzuvhCjhc@127.0.0.1:' + local_port + '/pusher_prod')
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     print('Database session created')
#
#     cursor = session.execute("SELECT * FROM public.feeds order by id")
#     result = cursor.fetchall()
#     feed_name = [row.name for row in result]
#     print(feed_name)
#     cursor.close()
#     session.close()
#     server.stop()


# import requests
# from grafana_api.grafana_face import GrafanaFace
#
# grafana_api = GrafanaFace(auth='', host='http://grafana.wirkserver.com/')
#
# # Search dashboards based on tag
# # grafana_api.search.search_dashboards(tag='applications')
#
# # Create or update a dashboard
# grafana_api.dashboard.update_dashboard(dashboard={'dashboard': "test", 'folderId': 0, 'overwrite': True})
# # Delete a dashboard by UID
# # grafana_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')
#
#
# headers = {
# 'Content-Type': 'application/json;charset=UTF-8',
# }
#
# data = open('C:/Users/mi/PycharmProjects/Realpush/Grafana/dashboard.json', 'rb').read()
# response = requests.post('http://@grafana.wirkserver.com:80/api/dashboards/db', headers=headers, data=data)
# print(response.text)
