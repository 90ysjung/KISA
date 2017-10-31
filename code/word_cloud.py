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

file_path = "C:\ysjung\KISA\data\TEST"
file_name = "A128.mlf"

with io.open(file_path + "\\" + file_name, 'r', encoding='utf8') as file:
   data = file.read()

#print(type(data))  # str

# 한글만 추출
data_han = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자(필터 조건)

han_suss = data_han.sub('', data)
han_fail = data_han.findall(data)

#print(type(han_suss))  # str

tokens = twitter.pos(han_suss, norm=True, stem=True)   # 정규화의 의미..?
# 동사, 형용사, 명사만 추출
tokens = [word for word, part in tokens if part == "Noun"]
#tokens = [word for word, part in tokens if part == "Verb" or part == "Adjective" or part == "Noun"]
#[word for word, part in tokens if part == "Verb" or part == "Adjective" or part == "Noun"]

print(tokens)

# 불용어 사전 및 사용자 전처리 추가 한다


# 빈도수 계산 , 정렬
frequency = {}
for i in tokens:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency [i] += 1

#sort
tokens_sort = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
print('')
print('Top5 = ', tokens_sort[:5])   # list , top5
print('')
#print(tokens_sort.most_common(5)) 
#list 못 읽음, max, min, top10 가져오는 방법을 연구한다
#print(dir(tokens_sort))

tag_tmp = tokens_sort[:10]
tag_list = pytagcloud.make_tags(tag_tmp, maxsize=50)
#print(tag_list)


# C:%PYTHON_HOME%\Lib\site-packages\pytagcloud\fonts
pytagcloud.create_tag_image(
tag_list,
'wc_1.jpg',
size=(600, 300),
fontname='NanumGothic', 
rectangular=False)


'''
#counter() 사용해 결과 낼수 있다
#countert(), most_common()
word_count = Counter(tokens)
#print(type(word_count))    # collections.Counter
print('')
print(word_count.most_common(5))
'''


