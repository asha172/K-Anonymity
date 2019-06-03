import os
import csv


def readCSV(path, sep=',', isFirstSkip=False):
    csvList = list()
    with open(path, 'r', encoding='utf-8') as lines:
        for line in lines:
            if isFirstSkip:
                isFirstSkip = False
                continue
                
            cells = line.split(sep)
            cells[-1] = cells[-1].replace('\n', '')
            csvList.append(cells)
            
    return csvList


