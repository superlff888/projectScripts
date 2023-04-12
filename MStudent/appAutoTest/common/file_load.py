# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 19:22
# @Author  : ╰☆H.俠ゞ
# =============================================================
import configparser
import csv
import json
import pandas
import yaml
from setting import DIR_NAME


def get_excel(filepath, sheet_name):
    """
    :: DIR_NAME项目所在路径，常量
    :: filepath:  相对路径（入参为项目下的路径，参照setting.py路径），如：./data/*.*
    ::keep_default_na:  读取文件会出现单元格 N/A,获取不到有效值；设置False获取空字符串
    ::engine:  指定引擎

    用来处理excel数据，希望获取的数据格式  "[[],[],[],[],[],[]]"

    """

    pandrxl = pandas.read_excel(DIR_NAME + filepath, sheet_name=sheet_name, keep_default_na=False, engine='openpyxl')
    print(f"pandas读取excel数据: \n{pandrxl}\n")
    print(f"DIR_NAME项目目录: \n{DIR_NAME}\n")

    # 元组中获取总行和总列 (lines,columns)
    lines = pandrxl.shape[0]  # 总行数
    cols = pandrxl.shape[1]  # 总行数
    # 数据解析不包含表头，所以数据是从第二行计算的
    data = []
    for l in range(lines):  # 行
        line_list = []
        for c in range(cols):  # 列
            line_list.append(pandrxl.iloc[l, c])  # 获取单元格数据 pandrxl.iloc[1, 2]
        data.append(line_list)  # 全量数据装表
    return data


def getCSV(path, isNext=True):
    """
    ::path  文件数据相对路径
    凡是可作用于for循环的对象都是Iterable类型；
    凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    """

    list_ = []
    try:
        with open(DIR_NAME + path, encoding='utf-8') as f:
            # The returned object is an iterator.  Each iteration returns a row of the CSV file
            csv_file = csv.reader(f)  # 返回迭代器iterator
            print(type(csv_file))
            if isNext:  # True表示csv有表头字段
                # 跳过第一行的用法，往往csv文件的第一行为标题名
                next(csv_file)  # 接收迭代器参数，若不是迭代器,需要用iter()方法转化成迭代器；iter(iterable) -> iterator
                for line in csv_file:  # [['Baked', 'Beans'], ['Lovely', 'Spam'], ['Wonderful', 'Spam']]
                    list_.append(line)
        return list_
    except Exception as e:
        raise e


def getCSVDict(path):
    list_ = []
    try:
        with open(DIR_NAME + path, encoding='utf-8') as f:
            # 若csv有表头，则默认将csv表头字段定义为key;若没有表头，则可以自定义表头key
            csv_file = csv.DictReader(f)  # 视图对象【'csv.DictReader'】格式类似于 list[{},{}] ; 字典中的key为CSV第一行表头字段
            # 迭代器 [{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}, {'first_name': 'Wonderful', 'last_name': 'Spam'}]
            print(csv_file)  # 视图对象
            for dic in csv_file:  # 按行读取，dict为： {'first_name': 'Baked', 'last_name': 'Beans'}
                list_.append(dic)  # 将读取的每一行放在列表中
        return list_
    except Exception as e:
        raise e


"""
写入csv文件
"""


# 定义dialect
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = '|'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


def write_in_csv(filepath, mode='w'):
    # 新建一个文件并按行写入
    with open(filepath, mode) as f:
        writer = csv.writer(f, dialect=my_dialect)
        writer.writerow(('one', 'two', 'three'))
        writer.writerow((1, 2, 3))
        writer.writerow((4, 5, 6))


def get_yml(filepath):
    """
    yaml文件读取, 返回Python object

    ::filepath  文件相对路径
    """

    with open(DIR_NAME + filepath, mode='r', encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        return content


def write_in_yml(filepath, data):
    """指定yml文件覆盖写入数据"""
    with open(DIR_NAME + filepath, mode='w', encoding='utf-8') as f:  # mode='w' 覆盖写入
        yaml.dump(data, f, Dumper=yaml.Dumper)


def get_json(path):
    """path为文件数据的绝对路径"""
    try:
        with open(DIR_NAME + path, encoding="utf-8") as f:
            data = f.read()
            json_data = json.loads(data)
            return json_data
    except Exception as e:
        raise e


class ReadConfig(configparser.ConfigParser):
    def __init__(self, filepath, encoding='utf8'):
        # 执行完此步骤，就可调用父类的成员属性，相当于把父类的__init__方法和成员属性继承过来了；之后用子类实例化一个对象后, 这个对象可以'点'出父类对象的成员属性/方法, 当然也可以'点'出自己类对象的成员属性/方法
        super().__init__()  # （括号中不需要传值self）需要配置父类成员属性，做初始化设置，所以要继承__init__方法
        # 通过子类实例对象（self，即conf）调用父类的方法（read），加载配置文件(可进一步做参数化)
        self.read(DIR_NAME+filepath, encoding)

class ConfigParser:
    """仅能读取一次数据，连续第二次取出来的数据为None"""
    config_dic = {}

    @classmethod
    def get_config(cls, path, sector, item):
        value = None
        try:
            value = cls.config_dic[sector][item]
        except KeyError:
            rcf = ReadConfig(path)
            rcf.read(path, encoding='utf8')  # 注意setting.ini配置文件的路径
            value = rcf.get(sector, item)
            cls.config_dic = value
        finally:
            return value


conf = ConfigParser()


"""
封装的原则：
    写死的固定数据（变量），可以封装成类属性，如 配置文件名 config.ini，来控制其他配置文件
    实现某个功能的代码封装成方法，
    在各个方法中都要用到的数据，抽离出来作为实例属性
封装前，读配置文件数据三部曲：
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 实例化配置文件解析器，打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(section, option)  # 获取options数据
"""


if __name__ == '__main__':

    # filepath = r'/data/shop_data.xlsx'
    # sheet_name = '立即购买'
    # print(get_excel(filepath, sheet_name))
    # print(len(get_excel(filepath, sheet_name)))
    #
    # filepath = r'/data/shop_data.csv'
    # print(getCSV(filepath))
    # res = conf.get_config('/conf/setting.conf', 'mysql', 'port')
    # print(res)
    # PSW = conf.get_config('/conf/setting.conf', 'mysql', 'password')
    # print(PSW)  # 第二个打印的惊人是None
    host = get_yml('/conf/redis.yml')
    print(host)
