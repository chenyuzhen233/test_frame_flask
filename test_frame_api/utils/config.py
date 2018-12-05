#!/usr/bin/env python
#coding=utf-8
import os
import configparser

# 配置项目文件路径，增加可移植性
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.ini')


class FileNotFoundError(BaseException):
    pass


class myconf(configparser.ConfigParser):
    # 重写ConfigParser.ConfigParser()类中的optionxform函数
    # 使其支持option名称区分大小写
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class Config(object):
    # 读取配置文件
    def __init__(self, config=CONFIG_FILE):
        #   判断路径中是否存在文件
        if os.path.exists(config):
            self.conf_file = config
        else:
            info = ('Config File not found!%s' % config)
            raise FileNotFoundError(info)
        self._data = None
        self.config = myconf()
        self.config.read(config)

    # 根据传入的session和option，返回相应的属性
    # 例如：get('database', 'port')
    # return 3306
    def get(self, session, option):
        try:
            result = self.config.get(session, option)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print('请检查配置文件参数是否正确:session:%s, option:%s %s' % (session, option, repr(e)))
            return None
        return result

    def read_data(self, section):
        params = dict(self.config.items(section))
        return params

config = Config()


if __name__ == '__main__':
    result =  Config().get('database', 'port')
    print(config.get('database', 'host'))
    print(result)
    print(type(result))
    print(CONFIG_FILE)