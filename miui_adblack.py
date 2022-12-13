# -*- coding:utf-8 -*-
import json
import time
import yaml
import requests
import sys

def get_rules(url_list):
    rules = set()
    for url in url_list:
        print("正在下载：%s" % url)
        try:
            response = requests.get(url).text
        except Exception:
            print("下载失败：%s" % url)
            continue
        print("共 %s条规则" % len(response.split("\n")))
        for line in response.split("\n"):
            if not line.startswith("!") or \
                    not line.startswith("["):
                rules.add(line)
    return list(rules)


def make_file(rules):
    print("文件合成中：")
    li = []
    id = 49152
    for i in rules:
        date = {
            "id": id,
            "flag": 0,
            "rule": i,
            "updateTime": int((time.time()-100000000) * 1000 - 1000000),
            "network": 255,
            "effectiveTime": int((time.time()-100000000) * 1000)
        }
        li.append(date)
        id += 1
    print("已生成%s条广告过滤规则" % id)
    data = {"data": li}

    with open("./miui_blacklist.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

def read_repo_file(path = "./repo_list.yaml"):
    info = None
    with open(path, 'r', encoding='utf8') as file:
        info = yaml.safe_load(file)
    rulers = info.get("ruler")
    return ruler

if __name__ == '__main__':
    if len(sys.argv) >1:
        rules = get_rules(sys.argv[1:])
    else:
        rules = get_rules(read_repo_file())
    make_file(rules)
