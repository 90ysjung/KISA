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

input_path = "C:\ysjung\KISA\data\TEST"  # input 절대경로
doc_list_tmp = os.listdir(input_path)    # os.walk 차이점..? 

doc_list_ext = []          # full name
doc_list = []              # name만(확장자 빼고)
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
     
word_dict = [] 
''' 
    전체 words 를 하나의 list로 생성하는건지,
    문서별 word list 를 list 로 생성하는건지
    모르겠음
'''
for j in docs_tmp:
    for k in j:
        word_dict.append(k)

print(word_dict)

#pickle 로 저장한다
with open('word_dict.txt', 'wb') as f:
    pickle.dump(word_dict, f)


######### TF-TDF #########
# TF 가 중요함, TF 셋중에 하나 방법 사용
# 불린 빈도
# 로그 스케일 빈도
# 증가 빈도
# IDF
# TF*IDF
#
# word : 문서별 tokens를 list로 생성
# whole_document : 문서별 word를 list로 생성

def n_containing(word, whole_document):
    return sum(1 for doc in whole_document if word in doc )

def idf(word, whole_document):
    return math.log(len(whole_document) / (1 + n_containing(word, whole_document)))

def tfidf(doc_tokens, whole_document):

    tf_idf = {}

    token_counts = Counter(doc_tokens)

    for token in token_counts:
        tf = token_counts[token] / len(doc_tokens)
        tf_idf[token] = tf * idf(token, whole_document)
    if (len(doc_tokens)>150):
        tf_idf = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)
        if( len(tf_idf) > 70 ):
            for word in tf_idf[70:]:
                while (word[0] in doc_tokens):
                    doc_tokens.remove(word[0])
    # if( len(tf_idf) > 20 ):
    #     for word in tf_idf[:20]:
    #         while (word[0] in doc_tokens):
    #             doc_tokens.remove(word[0])
    # if( len(tf_idf) > 40 ):
    #     for word in tf_idf[40:]:
    #         while (word[0] in doc_tokens):
    #             doc_tokens.remove(word[0])
    #return doc_tokens
    return tf_idf

print(docs)
print('')

# 문서별 words 를 list 로 생성
# tfidf 호출
for w in docs:  
    print(tfidf(w, docs))
    print('')


'''
###################################################
import math
# from text.blob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)



###################################################
# word : dic로 생성 할것 Counter()
# whole_document : 각문서를 element로 하는 list 로 생성할것
# doc 별 word 생성하고 doc list(whole_document) 생성한다

def n_containing(word, whole_document):
    return sum(1 for doc in whole_document if word in doc )

def idf(word, whole_document):
    return math.log(len(whole_document) / (1 + n_containing(word, whole_document)))

def tfidf(doc_tokens, whole_document):

    tf_idf = {}

    token_counts = Counter(doc_tokens)

    for token in token_counts:
        tf = token_counts[token] / len(doc_tokens)
        tf_idf[token] = tf * idf(token, whole_document)
    if (len(doc_tokens)>150):
        tf_idf = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)
        if( len(tf_idf) > 70 ):
            for word in tf_idf[70:]:
                while (word[0] in doc_tokens):
                    doc_tokens.remove(word[0])
    # if( len(tf_idf) > 20 ):
    #     for word in tf_idf[:20]:
    #         while (word[0] in doc_tokens):
    #             doc_tokens.remove(word[0])
    # if( len(tf_idf) > 40 ):
    #     for word in tf_idf[40:]:
    #         while (word[0] in doc_tokens):
    #             doc_tokens.remove(word[0])
    return doc_tokens

#######################################################
import math

def tf(word, doc):
    all_num = sum([doc[key] for key in doc])
    return float(doc[word]) / all_num

def idf(word, doc_list):
    all_num = len(doc_list)
    word_count = 0
    for doc in doc_list:
        if word in doc:
            word_count = 1
    return log(all_num / word_count)

def tfidf(word, doc, doc_list):
    score = tf(word, doc) * idf(word, doc_list)
    return score


'''

