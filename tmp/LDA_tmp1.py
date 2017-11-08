# -*- coding: utf-8 -*-
import konlpy
from konlpy.tag import Twitter
import nltk
import pickle
import numpy as np
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
import lda
import lda.datasets

twitter = Twitter()

input_path = "C:\ysjung\KISA\data\TEST"  # input 절대경로
doc_list_tmp = os.listdir(input_path)    # os.walk 차이점..? 

doc_list_ext = []          # full name
doc_list = []              # name만
for i in doc_list_tmp:
     ext = os.path.splitext(i)[-1]
     # 확장자별로 이름만 가져온다
     if ext == '.mlf':
         doc_list_ext.append(i)
         doc_list.append(os.path.splitext(i)[0])

#print(doc_list)
#print(doc_list_ext)


'''
# 불용어 사전 및 사용자 전처리 추가 한다
def text_preprocessing(sentence):
    sentence = re.sub(r"\u3000","", sentence)
    sentence = re.sub(r"[0-9]+","", sentence)
    return sentence
'''


# 모든 문서별 tokens를 list 로 생성
docs = []   
for i in doc_list_ext:
    with io.open(input_path + "\\" + i, 'r', encoding='utf8') as file:
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

    docs.append(tokens)

#pickle 로 저장한다
print(docs)

#######################
## type 
#In [13]: type(titles)
#Out[13]: tuple
#
#In [14]: type(vocab)
#Out[14]: tuple
#
#In [15]: type(X)
#Out[15]: numpy.ndarray
######################## 


x = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
model = lda.LDA(n_topics = 10, n_iter=100, random_state=1)

model.fit(x)
topic_word = model.topic_word_

for i, topic_dist in enumerate(topic_word):
    tpic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1] 




'''
http://khanrc.tistory.com/entry/Latent-Dirichlet-Allocation-LDA 
http://blog.naver.com/PostView.nhn?blogId=pdc222&logNo=220669844374&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView 

'''
    
