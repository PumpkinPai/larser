#!/usr/bin/python3

import os
import yaml
#import (some python img libary)

def getConf(filename):
    filename = 'default.yaml'
    confFile = open(filename, 'r')
    conf = yaml.load(confFile)
    confFile.close()
    return conf

def fileChooser(filetype):
    fileList = []
    curDir = os.getcwd()
    for f in os.listdir(curDir):
        if f.endswith(filetype):
            fileList.append(f)
    fileList.sort()

    menu = ''
    index = 0
    for element in fileList:
        menu += str(index) + '- ' + element + '\n'
        index += 1

    menu += '\nSelect a conf file number: '

    userSelection = input(menu) 

    chosen = fileList[int(userSelection)]
    return chosen


if __name__ == '__main__':
    confFileName = 'defaukt.yaml'

    # todo Set source file from sys arg

    # todo Ask if default values from conf.yaml
    confFilename = fileChooser('.yaml')
    print(confFilename)

    if confFilename[0].lower() == 'n':
        pass

    else:
        getConf(confFilename)

