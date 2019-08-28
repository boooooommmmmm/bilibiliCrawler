import requests
import json
import random
import pymysql
import sys
import datetime
import time
from multiprocessing.dummy import Pool as ThreadPool

user_ids = []

class remove_duplicate:
    def connect_to_database(self):
        print()
        try:
            conn = pymysql.connect(
                host='localhost', user='root', passwd='', db='bilibili', charset='utf8')
            cur = conn.cursor()
            cur.execute('SELECT * FROM bilibili_user_info')
            result = cur.fetchall()

            for row in result:
                user_ids.append(row[1])

            conn.close()
        except Exception as e:
            print("Exception captured: "  + e)


    def remove_duplicate(self):
        temp_list = []
        has_duplicate = False

        for id in user_ids:
            if (id not in temp_list):
                temp_list.append(id)
            else:
                print("-----" + id)
                has_duplicate = True

        if has_duplicate == False:
            print("there is no duplidate ids in database!")
            print("Total user infomations get: %s" %len(temp_list))


if __name__ == "__main__":
    try:
        remove_duplicate().connect_to_database()
        remove_duplicate().remove_duplicate()
        # for id in user_ids:
        #     print(id)
    except Exception as e:
        print("Exception captured: " + e)
