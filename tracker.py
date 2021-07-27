from threading import Timer
import requests
import time
import json

repo_name = ''
github_repo = 'https://api.github.com/repos/' + repo_name
headers = {'Accept': 'application/vnd.github.v3+json'}


def update_logs(new_num):
    with open('logs.json') as logs:
        old_data = json.load(logs)

        new_data = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "stars": new_num
        }

        old_data.append(new_data)

    with open('logs.json', 'w') as logs_update:
        json.dump(old_data, logs_update)


def get_stars():
    # 要执行的任务
    r = requests.get(github_repo, headers=headers)
    new_num = r.json()['stargazers_count']

    with open('current.json') as f:
        current = json.load(f)["current_stars"]

    if new_num != current:
        with open('current.json', 'w') as fu:
            new_data = {"current_stars": new_num}
            json.dump(new_data, fu)
            update_logs(new_num)
            print('数据更新：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print("数据没有变化")

    # 计时器（单位：秒，默认为1小时）
    global count
    count = Timer(3600, get_stars)
    count.start()

count = Timer(1, get_stars)
count.start()