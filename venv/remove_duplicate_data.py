import requests
import json
import random
import pymysql
import sys
import datetime
import time
from multiprocessing.dummy import Pool as ThreadPool

user_ids = []
duplicate_id_list = []
duplicate_list = []


class remove_duplicate:
    def connect_to_database(self):
        try:
            conn = pymysql.connect(
                host='localhost', user='root', passwd='', db='bilibili', charset='utf8')
            cur = conn.cursor()
            cur.execute('SELECT * FROM bilibili_user_info')
            result = cur.fetchall()

            i = 1
            length = len(result)
            for row in result:
                user_ids.append(row[1])
                print('copy to memeroy ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
                i = i + 1

            conn.close()
        except Exception as e:
            print("Exception captured: " + e)

    def find_duplicate(self):
        temp_list = []
        i = 1
        length = len(user_ids)

        for id in user_ids:
            if (id not in temp_list):
                temp_list.append(id)
            else:
                duplicate_id_list.append(id)

            print('find duplicate ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
            i = i + 1

        if len(duplicate_id_list) == 0:
            print("there is no duplidate ids in database!")
            print("Total user infomations get: %s" % len(temp_list))
        else:
            print("Duplicate user information find: %s" % len(duplicate_id_list))

    def extra_data(self):
        i = 1
        length = len(duplicate_id_list)

        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='bilibili', charset='utf8')

        for id in duplicate_id_list:
            cur = conn.cursor()
            cur.execute('SELECT * FROM bilibili_user_info WHERE mid = %s' % id)
            result = cur.fetchall()
            duplicate_list.append(result[0])

            print('extra data ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
            i = i + 1

    def backup_data(self):
        length = len(duplicate_list)
        i = 1

        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='bilibili', charset='utf8')

        for row in duplicate_list:
            cur = conn.cursor()
            cur.execute('INSERT INTO bilibili_user_info_backup(mid, name, sex, rank, face, regtime, spacesta, \
                        birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                        toutu, toutuId, coins, following, fans ,archiveview, article) \
            VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                    "%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s")'
                        % (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                           row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
                           row[21]))
            conn.commit()
            print('back up data ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
            i = i + 1

    def remove_data(self):
        length = len(duplicate_list)
        i = 1

        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='bilibili', charset='utf8')

        for row in duplicate_list:
            print("row 1: " + str(row[1]))
            cur = conn.cursor()
            cur.execute('DELETE FROM bilibili_user_info WHERE mid = %s' % (row[1]))
            conn.commit()
            print('remvoe data ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
            i = i + 1


if __name__ == "__main__":
    try:
        remove_duplicate().connect_to_database()
        remove_duplicate().find_duplicate()

        remove_duplicate().extra_data()
        remove_duplicate().backup_data()
        remove_duplicate().remove_data()

    except Exception as e:
        print("Exception captured: " + e)
