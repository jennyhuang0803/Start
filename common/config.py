# encoding:utf-8

import configparser
import os


def get_config(section, key):
    """
    This is used to get configuration from aliyun-sdk.conf in user directory
    :param section: section name in conf file
    :param key: key in conf file
    :return: value in conf file according to specific section and key
    """
    config = configparser.ConfigParser()
    path = os.path.expanduser('~') + '/aliyun-sdk.conf'
    config.read(path)
    return config.get(section, key)


def get_log_endpoint(key):
    """
    This is used to get specific log endpoint based on the region id
    For much for detail info, please refer to https://help.aliyun.com/document_detail/29008.html
    Will be updated once new region added
    May need enhancements to get related info from API instead of maintenance manually
    :param key: region id
    :return: log endpoint
    """
    log_endpoint = {"cn-qingdao": "http://cn-qingdao.log.aliyuncs.com",
                    "cn-beijing": "http://cn-beijing.log.aliyuncs.com",
                    "cn-zhangjiakou": "http://cn-zhangjiakou.log.aliyuncs.com",
                    "cn-hangzhou": "http://cn-hangzhou.log.aliyuncs.com",
                    "cn-shanghai": "http://cn-shanghai.log.aliyuncs.com",
                    "cn-shenzhen": "http://cn-shenzhen.log.aliyuncs.com",
                    "cn-hongkong": "http://cn-hongkong.log.aliyuncs.com",
                    "ap-southeast-1": "http://ap-southeast-1.log.aliyuncs.com",
                    "ap-southeast-2": "http://ap-southeast-2.log.aliyuncs.com",
                    "ap-northeast-1": "http://ap-northeast-1.log.aliyuncs.com",
                    "us-west-1": "http://us-west-1.log.aliyuncs.com",
                    # "us-east-1" : "http://", Currently not supported
                    "eu-central-1": "http://eu-central-1.log.aliyuncs.com",
                    "me-east-1": "http://me-east-1.log.aliyuncs.com"}
    return log_endpoint.get(key)
