# -*- coding: utf-8 -*-
import configparser
import datetime
import os
import sys
import threading
import time
import traceback


configFile = 'scrapy.cfg'

cfg = configparser.ConfigParser()
cfg.read(configFile, encoding='utf-8-sig')


class WebCrawler(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(WebCrawler, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        _pre_hour = time.strftime('%H',time.localtime(time.time()))
        while self.__running.is_set():
            try:
                self.__flag.wait()
                _cur_hour = time.strftime('%H',time.localtime(time.time()))
                if _cur_hour != _pre_hour:
                    _pre_hour = _cur_hour
                    cfg.set('SITE','exec','0')
                _checkHour_str = cfg.get('SITE','checkhour')
                _exec = cfg.get('SITE','exec')
                _current_exec = False
                for _h in _checkHour_str.split(','):
                    if _cur_hour == _h:
                        _current_exec = True
                        break
                if _current_exec:
                    if _exec != "1":
                        file = datetime.datetime.now().strftime('%Y-%m-%d')
                        os.system('scrapy crawlall')
                        cfg.set('SITE','exec','1')
                        cfg.write(open(configFile,'w',encoding='utf-8'))
                        print('执行完毕，等待下一次执行....')
                    else:
                        print('当前时段已执行，正在等待....')
                else:
                    cfg.set('SITE','exec','0')
                    cfg.write(open(configFile,'w',encoding='utf-8'))
                    print('当前时段不需要执行，正在等待....')
                
            except:
                pass
            time.sleep(100)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()


threads = []

th_scan = WebCrawler()
th_scan.setDaemon(True)
th_scan.setName('扫描线程')
threads.append(th_scan)


if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)
        print(t.getName()+"已启动")
        t.start()

    for t in threads:
        t.join()
