# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/9/7 下午2:32'

import time

import requests

import threading
from threading import Lock
import queue

g_lock = Lock()

n_thread = 10

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/68.0.3440.106 Safari/537.36",

}


def fetch_web_data(url, proxy=None, timeout=10):
    try:
        r = requests.get(url, timeout=timeout, headers=headers,
                     proxies=proxy)
        data = r.text
        return data
    except Exception as e:
        print(f"fetch_web-data has error url: {url}")
        return None


def write_ip_pair(ip_pair):
    '''
    将可用的IP和端口动态持久化到proxy_ip_list_日期.txt文件中
    :param ip_pair:
    :return:
    '''
    proxy_file_name = "proxy_ip_list_%s.txt" % (
        time.strftime("%Y.%m.%d", time.localtime(time.time())))
    with open(proxy_file_name, "a+", encoding="utf-8") as f:
        f.write(f"{ip_pair}\n")


# def write_ip(ip_port_pair):
class IpProxyCheckThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        global g_lock
        while True:
            data = self.__queue.get()
            ip_port_pair = data.split(",")[0]
            print('sssssssss')
            print(ip_port_pair)
            print(f"the check ip is {ip_port_pair} ")
            proxy = {
                "http": 'http://'+ip_port_pair,
            }
            url = "http://www.baidu.com"
            data = fetch_web_data(url, proxy=proxy, timeout=15)
            if data == None:
                print(f"当前ip {ip_port_pair} 校验不成功，丢弃！")
                continue
            print(f"当前ip {ip_port_pair} 校验成功，可用！")
            g_lock.acquire()
            write_ip_pair(ip_port_pair)
            g_lock.release()


class FetchProxyListThread(threading.Thread):
    def __init__(self, url, mq):
        threading.Thread.__init__(self)
        self.__url = url
        self.__mq = mq

    def run(self):
        data = fetch_web_data(self.__url)
        print(data)
        ip_pool_list = data.split("\n")
        [self.__mq.put(ip_pool) for ip_pool in ip_pool_list]


def process():
    mq = queue.Queue()

    thread_list = []
    for i in range(n_thread):
        t = IpProxyCheckThread(mq)
        t.setDaemon(True)
        thread_list.append(t)

    [t.start() for t in thread_list]

    url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=727f205f16744f7fa7def1567cd78ccc&orderno=YZ202011155336vU095Z&returnType=1&count=100"
    fth = FetchProxyListThread(url, mq)
    fth.start()

    fth.join()
    [t.join() for t in thread_list]

    mq.join()


if __name__ == "__main__":
    process()
