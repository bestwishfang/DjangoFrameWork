# -*- coding: utf-8 -*-


import yaml
import logging
from logging import config


def get_logger():
    # 通过yaml文件配置logging
    with open('./log_conf.yaml', mode='r', encoding='utf-8') as fp:
        data = yaml.safe_load(fp)
    config.dictConfig(data)

    # 创建logger
    logger = logging.getLogger()
    return logger


logger = get_logger()
