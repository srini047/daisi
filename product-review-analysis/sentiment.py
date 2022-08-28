#!/usr/bin/env python
# coding: utf-8

# # Text Based Sentiment Analysis

# # IMPORTING NECESSARY MODULES




import numpy as np # For linear algebra
import pandas as pd # Data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt  # For Visualisation
# get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns  # For Visualisation
from bs4 import BeautifulSoup  # For Text Parsing


# # IMPORTING DATASET




data = pd.read_csv('daisi\product-review-analysis\Reviews.csv')
# data


# # DATA PREPROCESSING & VISUALISATION




#data.isnull().sum()





data=data.dropna()
#data.isnull().sum()





#data.shape





score_unique = data['Score'].unique()
#print(score_unique)





#   0-> NEGATIVE REVIEW
#   1-> NEUTRAL REVIEW
#   2-> POSTIVE REVIEW
a=[]
for i in data['Score']:
    if i <3:                              
        a.append(0)
    if i==3:
        a.append(1)
    if i>3:
        a.append(2)





r_0, r_1, r_2 = 0, 0, 0
for i in a:
    if i == 0:
        r_0 += 1
    elif i == 1:
        r_1 += 1
    else:
        r_2 += 1

# print('Negative Reviews:',r_0)
# print('Neutral Reviews:',r_1)
# print('Positive Reviews:',r_2)





# sns.countplot(a)
# plt.xlabel('Reviews', color = 'red')
# plt.ylabel('Count', color = 'red')
# plt.xticks([0,1,2],['Negative','Neutral','Positive'])
# plt.title('COUNT PLOT', color = 'r')
# plt.show()





data['sentiment']=a
#data
final_dataset = data[['Text','sentiment']]
#final_dataset





data_p=final_dataset[data['sentiment']==2]
data_n=final_dataset[data['sentiment']==0]
#len(data_p), len(data_n)





datap = data_p.iloc[np.random.randint(1,443766,5000), :]
datan = data_n.iloc[np.random.randint(1, 82007,5000), :]
#len(datan), len(datap)





data = pd.concat([datap,datan])
len(data)





c=[]
for i in data['sentiment']:
    if i==0:
        c.append(0)
    if i==2:
        c.append(1)
data['sentiment']=c





# sns.countplot(data['sentiment'])
# plt.show()





def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
data['review'] = data['Text'].apply(strip_html)

data=data.drop('Text',axis=1)

#data.head()


# # MODEL BUILDING




import nltk  #Natural Language Processing Toolkit
def punc_clean(text):
    import string as st
    a=[w for w in text if w not in st.punctuation]
    return ''.join(a)
data['review'] = data['review'].apply(punc_clean)
#data.head(2)





def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)
#data['review'] = data['review'].apply(remove_stopword)





from sklearn.feature_extraction.text import TfidfVectorizer

vectr = TfidfVectorizer(ngram_range=(1,2),min_df=1)
vectr.fit(data['review'])

vect_X = vectr.transform(data['review'])





from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

clf=model.fit(vect_X,data['sentiment'])
#clf.score(vect_X,data['sentiment'])*100


# # PREDICTION




clf.predict(vectr.transform(['''Nice look and build quality with moderately fast everything such as refresh rate, display quality, sound, processing, gaming experience and many more ..
I didn't find any lagging or heating issue..And battery health I won't say great but I'll take that

Only cons I can say about it is camera.. sharpening picture a little much at day light and low light photo you have to compromise.''']))





clf.predict(vectr.transform(['''Phone has bugs , and screen quality is poor , Avoid realme. Gaming was just over hyped''']))





clf.predict(vectr.transform(['''No lags found super speed and very good performance nice phone in this budget''']))




def prediction(comments):
    """
    This function is used to get the prediction of a comment.

    Parameters:
    - comments (string) : Any comments from 

    Return:
    - object type : description
    """
    sentiment = 1
    if (clf.predict(vectr.transform([comments]))):
        return sentiment
    else:
        sentiment = 0
    return sentiment




