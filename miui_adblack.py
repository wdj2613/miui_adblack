# -*- coding:utf-8 -*-
import requests
import time
import json

def get_rules(url_list):
    rules = set()
    for url in url_list:
        print("正在下载：%s"%url)
        try:
            response = requests.get(url).text
        except Exception:
            print("下载失败：%s"%url)
            continue
        for line in response.split("\n"):
            print(line)
            if not line.startswith("!") or \
                    not  line.startswith("["):
                print(line)
                rules.add(line)
    return list(rules)


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
        li.append(date)
    id +=1
    print("已生成%s条广告过滤规则"%id)
    data = {"data":li}

    with open("./miui_blacklist.json" ,"w",encoding="utf-8") as f:
        json.dump(data,f)


if __name__ == '__main__':
    url_list = ["https://easylist-downloads.adblockplus.org/easylistchina+easylistchina_compliance+easylist.txt",
                ]

    rules = get_rules(url_list)
    make_file(rules)