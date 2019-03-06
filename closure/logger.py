# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 15:33
# @Author  : WANGXIAO

import logging


def log_header(logger_name):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s] %(levelname)s  %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(logger_name)

    def _logging(log,level):
        if level == 'debug':
            logger.debug(log)
        elif level == 'warning':
            logger.warning(log)
        elif level == 'error':
            logger.error(log)
        else:
            raise Exception('nothing logger')
    return _logging
