# @Time  : 2022/02/14 18:50
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import logging.config

logging.config.fileConfig('../conf/logging.conf')
logger = logging.getLogger("main")
logger.debug("日志")

