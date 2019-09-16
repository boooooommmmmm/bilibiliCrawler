import pymysql

source_database = "bilibili_user_info_backup"
target_database = "bilibili_user_info"

source_data_list = []


def connect_to_source_database():
    try:
        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='bilibili', charset='utf8')
        cur = conn.cursor()
        cur.execute('SELECT * FROM %s' % source_database)
        result = cur.fetchall()

        i = 1
        length = len(result)
        for row in result:
            source_data_list.append(row)
            print('copy to memory ... [' + str(round(float(i) / float(length) * 100, 2)) + '%]')
            i = i + 1

        conn.close()
    except Exception as e:
        print("Exception captured: " + e)


def copy_data_to_target_database():
    try:
        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='bilibili', charset='utf8')

        for res in source_data_list:
            cur = conn.cursor()
            cur.execute('SELECT * FROM %s WHERE mid = %s' % (source_database, res[1]))
            row = cur.fetchall()[0]
            print(row)

            cur = conn.cursor()
            cur.execute('INSERT INTO %s (mid, name, sex, rank, face, regtime, spacesta, \
                        birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                        toutu, toutuId, coins, following, fans ,archiveview, article) \
            VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                    "%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s")'
                        % (target_database, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                           row[10],
                           row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
                           row[21]))
            conn.commit()


    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        connect_to_source_database()
        copy_data_to_target_database()

        # for res in source_data_list:
        #     print(res[1])

    except Exception as e:
        print("Exception captured: " + e)
