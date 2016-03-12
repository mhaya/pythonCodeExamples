#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import pylab as plt

#コマンドライン引数の取得
argv = sys.argv

#簡易的なチェック
if len(argv) != 3:
    print "usage: python compareImage.py imgA imgB "
    exit

#画像の読み込み
imgA = cv2.imread(argv[1])
imgB = cv2.imread(argv[2])
#グレースケール化
imgAgry = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
imgBgry = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)
#ヒストグラム計算
imgAhist = cv2.calcHist([imgAgry],[0],None,[256],[0,256])
imgBhist = cv2.calcHist([imgBgry],[0],None,[256],[0,256])

#ヒストグラム表示
if False:
    plt.plot(imgAhist)
    plt.xlim([0,256])
    plt.show()
    plt.plot(imgBhist)
    plt.xlim([0,256])
    plt.show()

#ヒストグラムの類似度計算
ret = cv2.compareHist(imgAhist,imgBhist,0)
print ret
