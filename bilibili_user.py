# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))

    return current_milli_time()


reload(sys)


def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return uas


theadNumbers = 1
uas = LoadUserAgents("user_agents.txt")
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

# Please replace your own proxies.
proxies = {
    # 'http': 'http://118.97.235.234:8080',
    # 'http': 'http://117.191.11.111:8080',
    # 'http': 'http://158.69.138.11:1080',
    'http': 'localhost',
    # 'http': 'http://58.218.200.226:9156',
    # 'http': 'http://58.218.200.226:9183',
    # 'http': 'http://58.218.200.228:9151',
    # 'http': 'http://58.218.200.225:9150',
    # 'http': 'http://158.69.138.11:1080',
}
time1 = time.time()

urls = []


# Please change the range data by yourself.
def get_urls():
    for m in range(905, 1000):
        for i in range(m * 100, (m + 1) * 100):
            url = 'https://space.bilibili.com/' + str(i)
            urls.append(url)


def getsource(url):
    time.sleep(5)
    print("Try to get URL: " + url)
    payload = {
        '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid': url.replace('https://space.bilibili.com/', '')
    }
    ua = random.choice(uas)
    head = {
        'User-Agent': ua,
        # 'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000))
        # 'Referer': 'https://space.bilibili.com/' + str(i)
        'Referer': url
    }
    jscontent = requests \
        .session() \
        .post('http://space.bilibili.com/ajax/member/GetInfo',
              headers=head,
              data=payload,
              # proxies=proxies,
              ) \
        .text
    time2 = time.time()
    try:
        jsDict = json.loads(jscontent)
        statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
        if statusJson == True:
            if 'data' in jsDict.keys():
                jsData = jsDict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                rank = jsData['rank']
                face = jsData['face']
                regtimestamp = jsData['regtime']
                regtime_local = time.localtime(regtimestamp)
                regtime = time.strftime("%Y-%m-%d %H:%M:%S", regtime_local)
                spacesta = jsData['spacesta']
                birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'
                sign = jsData['sign']
                level = jsData['level_info']['current_level']
                OfficialVerifyType = jsData['official_verify']['type']
                OfficialVerifyDesc = jsData['official_verify']['desc']
                vipType = jsData['vip']['vipType']
                vipStatus = jsData['vip']['vipStatus']
                toutu = jsData['toutu']
                toutuId = jsData['toutuId']
                coins = jsData['coins']
                print("Succeed get user info: " + str(mid) + "\t" + str(time2 - time1))
                try:
                    res = requests.get(
                        'https://api.bilibili.com/x/relation/stat?vmid=' + str(mid) + '&jsonp=jsonp').text
                    viewinfo = requests.get(
                        'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp').text
                    js_fans_data = json.loads(res)
                    js_viewdata = json.loads(viewinfo)
                    following = js_fans_data['data']['following']
                    fans = js_fans_data['data']['follower']
                    archiveview = js_viewdata['data']['archive']['view']
                    article = js_viewdata['data']['article']['view']
                except:
                    following = 0
                    fans = 0
                    archiveview = 0
                    article = 0
            else:
                print('no data now')
            try:
                # Please write your MySQL's information.
                conn = pymysql.connect(
                    host='localhost', user='root', passwd='', db='bilibili', charset='utf8')
                cur = conn.cursor()
                cur.execute('INSERT INTO bilibili_user_info(mid, name, sex, rank, face, regtime, spacesta, \
                            birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                            toutu, toutuId, coins, following, fans ,archiveview, article) \
                VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                        "%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s")'
                            %
                            (mid, name, sex, rank, face, regtime, spacesta, \
                             birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                             toutu, toutuId, coins, following, fans, archiveview, article))
                conn.commit()
            except Exception as e:
                print(e)
        else:
            print("Error: " + url)
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    pool = ThreadPool(theadNumbers)
    try:
        get_urls()
        results = pool.map(getsource, urls)
    except Exception as e:
        print(e)

    pool.close()
    pool.join()
