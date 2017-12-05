#*- coding: utf-8 -*-

import konlpy
from konlpy.tag import Twitter
import nltk
import pickle
import numpy
#from numpy._distributor_init import NUMPY_MKL
import operator
#from gensim import corpora, models
#import gensim
import math
from collections import Counter
import os, re, copy
import sys
import io
#import matplotlib.pyplot as plt
#import pytagcloud

twitter = Twitter()

#input_path = "C:\\ysjung\\KISA\\data\\autofocus"
input_path = "D:\\ysjung\\KISA\\autofocus"
doc_list_tmp = os.listdir(input_path)

doc_list_ext = []                     # full name
doc_list = []                         # name만(확장자 빼고)
for i in doc_list_tmp:
     ext = os.path.splitext(i)[-1]
     if ext == '.csv':                # 확장자별로 이름만 가져온다
         doc_list_ext.append(i)
         doc_list.append(os.path.splitext(i)[0])



### 모든 문서별 tokens(list)를 list 로 생성
### 한 row 가 1 list 로 나와야 한다
docs = []
for i in doc_list_ext:
    with io.open(input_path + "\\" + i, 'r', encoding='utf8') as file:
        data = file.read()

    mal_tmp = data.split()
    docs.append(mal_tmp)



docs_dict = []
for j in docs:
    for k in j:
        tmp = k.split(',')
        docs_dict.append(tmp)



##################
### 연관분석

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #print(C1, type(C1))
    return map(frozenset, C1)     # frozenset vs set..?



###
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ssCnt:
                    ssCnt[can]=1
                else:
                    ssCnt[can] += 1
    # numItems = 5     ##### float(len(D)) , 오류 잡을 것
    numItems = 100
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData


###
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


# 특정 지지도 이상의 값들의 쌍을 찾음
def apriori(dataset, minSupport = 0.1):     # 최소 지지도 설정
    C1 = createC1(dataset)
    D = map(set, dataset)
    D = list(D)
    L1 ,supportData = scanD(D, C1, minSupport)
    L = [L1]
    k=2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2],k)
        Lk, supK = scanD(D, Ck, minSupport)  # 후보그룹을 모두 찾는다.
        supportData.update(supK)
        L.append(Lk)                         #이게 핵심!특정 지지도 이상의 그룹들만 L에 담는다.즉 가지치기
        k += 1
    return L, supportData
    print(str(L))
    print(str(suppData))

#x = apriori(word_dict)
#print(x)


#####
def generateRules(L, supportData, minConf=0.1):    # 최소 신뢰도 설정
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i>1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)

    return bigRuleList

def calcConf(freqSet, H, supportData, br1, minConf=0.1):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet-conseq]
        if conf >= minConf:
            print(freqSet-conseq, '-->', conseq, 'conf:', conf)
            br1.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)

    return prunedH

def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.1):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m+1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, br1, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)


if __name__ == "__main__":
    print("============== 연관분석 결과 ==============")
    dataset = docs_dict
    L, suppData = apriori(dataset)
    print("빈번집합 모음:" + str(L) + "\n")
    print("============== 지지도 0.1 이상 집합 및 신뢰도 ==============")
    print("suppData:" + str(suppData))

    rules = generateRules(L, suppData, minConf=0.1)
