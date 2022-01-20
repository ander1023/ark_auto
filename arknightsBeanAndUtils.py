#!/usr/bin/env python
# coding: utf-8
from airtest.aircv import crop_image
from airtest.core.android.android import Android
from airtest.core.api import *
import time
import random


# todo 修改为本地日志
class Utils:
    IM = {
        # load
        '加载': ['game_img/tpl1642000237225.png', [1200, 10, 1260, 85]],
        '开始唤醒': ['game_img/tpl1642001226694.png', [530, 476, 740, 544]],
        # main
        '主页设置按钮': ['game_img/tpl1642001430437.png', [17, 17, 86, 64]],
        '主页好友按钮': ['img/tpl1642224008220.png', [294, 550, 427, 587]],
        '主页采购中心': ['img/tpl1642222433924.png', [752, 453, 917, 524]],
        # 商店界面
        '收取信用': ['img/tpl164222,2452232.png', [956, 15, 1083, 50]],
        # 好友界面
        '下一位暗': ['img/tpl1642316165139.png', [1089, 578, 1277, 680]],
        # battle
        '战斗完成': ['game_img/tpl1642146871581.png', [23, 574, 400, 676]],
        '理智界面': ['game_img/tpl1642165866975.png.', [1099, 383, 1225, 409]],
        # bar
        'barhome': ['game_img/tpl1642147290374.png', [165, 14, 376, 67]],
        'bar首页': ['game_img/tpl1642147630815.png', [34, 221, 129, 310]],
        # 剿灭
        '作战简报': ['game_img/tpl1642436676650.png', [73, 173, 196, 213]]
    }
    CM = {
        # clickmap
        # load
        '加载': [200, 500],
        '开始唤醒': [621, 508],
        # battle
        '战斗准备': [1100, 640],
        '战斗准备1': [1100, 600],
        '战斗完成': [900, 15],
        # main
        '终端': [966, 181],
        '好友': [357, 567],
        '采购中心': [836, 477],
        # 好友界面
        '好友列表': [119, 213],
        '访问第一位好友': [994, 155],
        '访问下一位': [1194, 631],
        # 商店界面
        '信用交易所': [1194, 100],
        '领取信用': [1011, 38],
        '领取信用确定按钮': [],
        # battle 中途
        '日常子界面': [725, 669],
        '战术演习': [622, 341],
        'ls5': [943, 177],
        '理智界面x': [779, 571],
        # bar
        'barhome': [254, 29],
        'bar首页': [93, 271],
        # 剿灭完成
        '剿灭完成': [959, 120]}

    def __init__(self):
        self._dev = None
        self.flag = False

    def connectDev(self):
        try:
            self._dev = Android('emulator-5554')
        except:
            pass

    # def getdev(self):
    #     return self.__dev
    def startapp(self, name):
        if not self.flag:
            return
        self._dev.start_app(name, activity=None)

    def sleep(self, second=3):
        if not self.flag:
            return
        time.sleep(second + random.random() * 2)

    def touchName(self, name):
        if not self.isConnect():
            return
        if not self.flag:
            return
        x = self.CM[name][0]
        y = self.CM[name][1]
        self._dev.touch((x, y), 0.01)
        print('touchList ' + '--' + name + '--')
        self.sleep(3)

    def img_match(self, name):
        if not self.isConnect():
            return
        if not self.flag:
            return
        try:
            img = self.IM[name][1]
            local_screen = crop_image(self._dev.snapshot(), (img[0], img[1], img[2], img[3]))
            tempalte = Template(self.IM[name][0])
            pos = tempalte.match_in(local_screen)
            if pos:
                print('img_match ' + '--' + name + '--  Success')
                return True
            else:
                print('img_match ' + '--' + name + '--  Fail')
                return False
        except:
            print('img_match ' + '--' + name + '--  Fail')
            return False
        finally:
            time.sleep(0.7)

    def getFlag(self):
        return self.flag
    def setFlagF(self):
        self.flag = False

    def setFlagT(self):
        self.flag = True

    def isConnect(self):
        try:
            if self._dev.avaliable:
                return True
            return False
        except:
            pass


ut = Utils()
