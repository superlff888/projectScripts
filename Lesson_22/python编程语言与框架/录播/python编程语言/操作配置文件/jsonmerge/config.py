# @Time  : 2022/01/25 10:46
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
jsonmerge是一个将两个json对象进行合并的python库，在合并的过程中，可以指定合并策略
"""
from pprint import pprint

from jsonmerge import merge
import config_default

configs = config_default.configs

try:
    import config_override
    # Merge head into base
    # config_override.configs覆盖configs中相同key的value(json格式层次关系要一致)，完成合并,最后返回合并后的json对象
    configs = merge(configs, config_override.configs)
    pprint(configs)
except ImportError:
    pass