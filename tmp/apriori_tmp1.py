## 문서별 doc_list 생성

# -*- coding: utf-8 -*-
import konlpy
from konlpy.tag import Twitter
import nltk
import pickle
import numpy
from numpy._distributor_init import NUMPY_MKL
import operator
from gensim import corpora, models
import gensim
import math
from collections import Counter
import os, re, copy
import sys
import io
import matplotlib.pyplot as plt
import pytagcloud

twitter = Twitter()

#input_path = "C:\ysjung\KISA\data\TEST"  # input 절대경로
input_path = "C:\ysjung\KISA\data\docs"
doc_list_tmp = os.listdir(input_path)    # os.walk 차이점..?

doc_list_ext = []          # full name
doc_list = []              # name만(확장자 빼고)
for i in doc_list_tmp:
     ext = os.path.splitext(i)[-1]
     # 확장자별로 이름만 가져온다
     if ext == '.txt':
         doc_list_ext.append(i)
         doc_list.append(os.path.splitext(i)[0])

#print(doc_list)
#print(doc_list_ext)

# 모든 문서별 tokens(list)를 list 로 생성
docs = []
for i in doc_list_ext:
    with io.open(input_path + "\\" + i, 'r', encoding='utf8') as file:
        data = file.read()

    ''' 전처리 사항이 있다면 여기에, 추후 모듈화 할 것 '''

    mal_tmp = data.split()
    docs.append(mal_tmp)

print(docs)
print(type(docs))

# 문서별 모든 tokens 를 하나의 list 로 생성
word_dict = []
for j in docs:
    for k in j:
        word_dict.append(k)

print(word_dict)
print(type(word_dict))


#######
# 연관분석
#######
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)     # frozenset vs set..?

C1 = createC1(docs)
D = map(set, docs)

#print('C1 is : ', type(C1))   # map
#print('D is : ', type(D))     # map

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
    numItems = 10    # float(len(D)) , 오류 잡을 것
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

L1 = scanD(D, C1, 0.5)
print(type(L1))

###
# [1,3,2,5] 를
# [1,3] [2,5] [2,3] [3,5] 를
# [2,3,5] 이런식으로 만드는 함수
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
def apriori(dataset, minSupport = 0.5):
    C1 = createC1(dataset)
    D = map(set, dataset)
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


x = apriori(docs)
print(x)
print(type(x))




