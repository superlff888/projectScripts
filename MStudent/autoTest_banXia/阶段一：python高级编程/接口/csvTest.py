# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
import csv
import os


from util import get_project_path
#alt+enter

path = os.path.join(get_project_path(), "files", 'userTest.csv')
path2 = os.path.join(get_project_path(), "files", 'userTest2.csv')


# file = open(path,mode="w+")
# file.write("1111")
# file.close()

# with open(path, mode="a+") as f:
#     f.write("222\n")


def readList():
    global f, csv_file, line
    with open(path) as f:
        csv_file = csv.reader(f)  # list[]
        headers = next(csv_file)
        # print(headers)
        for line in csv_file:
            print(line)


def readDic():
    global f, csv_file, line
    with open(path) as f:
        csv_file = csv.DictReader(f)  # list [{},{}]
        print(csv_file)
        for line in csv_file:
            print(line["first_name"])


def writeCsv():
    global f
    #需要添加newline参数逐行写入，否则会出现空行现象
    with open(path2, "w",newline='',encoding="utf-8") as f:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},
                          {'first_name': 'Lovely', 'last_name': 'Spam'}])
        writer.writerow({'first_name': '王', 'last_name': '嘉'})


if __name__ == '__main__':
    # readList()
    # readDic()
    writeCsv()
