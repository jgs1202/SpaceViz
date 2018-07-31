# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
# CDF用の環境変数の指定
os.environ["CDF_LIB"] = '~/PerlCDF36_4/blib/lib/auto'
from spacepy import pycdf


# cdfファイルの読み込み
def read(file):
    cdf = pycdf.CDF(file)
    return cdf


def main():
    # 読み込むファイルの指定
    argvs = sys.argv
    argc = len(argvs)
    if argc != 2:
        print('Please give only one argument: the path of a cdf file.')
    else:
        print('loading...')
        data = read(argvs[1])

    wave1 = []
    wave2 = []

    # 補数の補正
    for i in data['e1_waveform']:
        for j in i:
            if j > 32767:
                j -= 65536
            wave1.append(j)
    for i in data['e2_waveform']:
        for j in i:
            if j > 32767:
                j -= 65536
            wave2.append(j)

    # 可視化開始
    while(1):
        # 可視化範囲の指定
        print('\n The number of total data points is ' + str(len(wave1)) + '.')
        print('Specify the interval you want to see. Press Ctrl + C to quit.')
        while(1):
            start = input('start point: ')
            end = input('end point: ')
            try:
                start = int(start) + 1
                end = int(end) + 1
                break
            except:
                print('Only an integer is valid.')
        e1 = wave1[start: end]
        e2 = wave2[start: end]
        # 可視化
        xx = np.arange(start, end)
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax4 = fig.add_subplot(2, 2, 4)
        f_sam = 65536
        sp1 = np.fft.fft(e1)
        sp2 = np.fft.fft(e2)
        po1 = abs(sp1) ** 2 / len(e1)
        po2 = abs(sp2) ** 2 / len(e2)
        sp1 = sp1.real
        sp2 = sp1.real
        fr1 = np.fft.fftfreq(len(e1), d=1/f_sam)
        fr2 = np.fft.fftfreq(len(e2), d=1/f_sam)
        ax1.plot(xx, e1)
        ax1.set_title('E1')
        ax3.plot(xx, e2)
        ax3.set_title('E2')
        ax2.plot(fr1, po1)
        ax2.set_ylim(0.1, 10 ** 8)
        ax2.set_xscale('log')
        ax2.set_yscale('log')
        ax2.set_title('Spectrum1')
        ax4.plot(fr2, po2)
        ax4.set_title('Spectrum2')
        ax4.set_ylim(0.1, 10 ** 8)
        ax4.set_xscale('log')
        ax4.set_yscale('log')
        plt.show()


if __name__ == '__main__':
    main()
