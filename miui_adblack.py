# -*- coding:utf-8 -*-
import requests
import time

def get_rules(url_list):
    rules = set()
    for url in url_list:
        print("正在下载：%s"%url)
        response = requests.get(url).text
        for line in response.split("\n"):
            if not line.startswith("!") or \
                    not  line.startswith("["):
                rules.update(line)
    return rules

def make_file(rules):
    print("文件合成中：")
    date = {}
    li = []
    id = 1
    for i in rules:
        date = {
            "id": id,
            "flag": 0,
            "rule": i,
            "updateTime": int(time.time()*1000-1000),
            "network": 255,
            "effectiveTime": int(time.time()*1000)
        }
        id +=1
    print("已生成%s条广告过滤规则"%id)
    li.append(date)

    with open("./miui_blacklist.json") as f:
        f.write('{"data":%s}'%li)

if __name__ == '__main__':
    url_list = ["https://easylist-downloads.adblockplus.org/easylistchina+easylistchina_compliance+easylist.txt",
                "https://easylist-downloads.adblockplus.org/easylist.txt",]

    rules = get_rules(url_list)
    make_file(rules)