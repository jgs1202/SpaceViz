# -*- coding: utf-8 -*-

import os
import sys
os.environ["CDF_LIB"] = '~/PerlCDF36_4/blib/lib/auto'

from spacepy import pycdf


def read(file):
    cdf = pycdf.CDF(file)
    print(cdf)


def main():
    argvs = sys.argv
    argc = len(argvs)

    if argc != 2:
        print('Please give only one argument: the path of a cdf')
    else:
        read(argvs[1])


if __name__ == '__main__':
    main()