# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-21
desc: 
sample: 
"""
import os


def get_project_dirname():
    """得到项目目录"""
    return os.path.dirname(__file__)


def get_project_abspath(path):
    """得到项目目录"""
    return os.path.abspath(path)