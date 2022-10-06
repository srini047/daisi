import pandas as pd #Dataframe Manipulation library
import numpy as np #Data Manipulation library
from pathlib import Path

#sklearn modules for Feature Extraction & Modelling
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Libraries for Plotting 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

#Read files Iteratively
import glob
# import os

# def load_data(folder_names, root_path):
#     fileNames = [path + "./BBC News Summary/News Articles/" + folder + '/' + "*.txt"
#         for path,folder in zip([root_path]*len(folder_names), folder_names)]

#     doc_list = []
#     tags = folder_names
#     for docs in fileNames:
#         #print(docs)
#         doc = glob.glob(docs)#glob method iterates through all files and reads the text in documents in the folders
#         for text in doc:
#             with open(text, encoding="latin-1") as f:
#                 topic = docs.split('/')[len(docs.split('/'))-2]
#                 lines = f.readlines()
#                 heading = lines[0].strip()#stripping the text by spaces and using first element into heading
#                 body = ' '.join([l.strip() for l in lines[1:]])
#                 doc_list.append([topic,heading,body])
#     #     print(f"Loading data from \033[1m{topic}\033[0m directory")
#     # print("\nEntire Data is loaded successfully")
    
#     return doc_list
# folder_names = ['business','entertainment','politics','sport','tech']
# docs = load_data(folder_names=folder_names,root_path=os.getcwd())

# data = pd.DataFrame(docs, columns = ['Category','Heading','Article'])
# data.head()

data = pd.read_csv('./headings.csv')

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(data["Heading"].values) # .values: convert DataFrame columns into List.List of data will be transformed into tfidf vector
# print(f"The shape of the tfidf |matrix : {vectors.shape}")
# print(f"There are {vectors.shape[0]} number of News Articles having {vectors.shape[1]} unique words in tfidf vectors")

new_query = ["Stock Market Rates are rising"]
new_query_vector = vectorizer.transform(new_query)
new_query_vector

sim = cosine_similarity(X = vectors, Y = new_query_vector)

ind = np.argsort(sim,axis = 0)[::-1][:10]
# print("Top 10 News Articles similar to new_query are : \n")
# for i in ind:
    # print(data['Heading'].values[i])

#Extract Index of Maximum Valued similar document
argmax = np.argmax(sim)
# print(f"Index of the maximum valued similar document is : \033[1m{argmax}\033[0m")
# print(f"Retrieved Document Header is : \033[1m{data.Heading[argmax]}\033[0m")

def retrieve_doc(new_query,raw_docs,colname = None): # inputs are new_query,corpus,colname from the dataframe to be used for raw document text
    vectorizer = TfidfVectorizer() #convert to Tfidf Vectorizer
    vectors = vectorizer.fit_transform(raw_docs[colname]) #preprocess the document, fit the model of tfidf document, transform it
    # print(f"The shape of the tfidf matrix : {vectors.shape}")
    shape = vectors.shape
    # print(f"There are {vectors.shape[0]} number of News Articles having {vectors.shape[1]} unique words in tfidf vectors")
    number_of_news_articles = vectors.shape[0]
    new_query = [new_query] #tfidf vectorizer accepts on list or an array(doesn't work on raw text)
    new_query_vector = vectorizer.transform(new_query) #just transforms/calculates the frequency(of new_query) against the tokens we already have in matrix 
    sim = cosine_similarity(X = vectors, Y = new_query_vector)#pairwise cosine similarity
    argmax = np.argmax(sim)
    # print(f"\nIndex of the maximum valued similar document is : \033[1m{argmax}\033[0m")
    # print(f"Retrieved Document Header is : \033[1m{data.Heading[argmax]}\033[0m")
    header = data.Heading[argmax]
    ind = np.argsort(sim,axis = 0)[::-1][:10] #sorts similarity scores in [::-1] descending order ,[:10] top 10 most similar articles
    # print("\nTop 10 News Articles similar to new_query are : \n")
    # for i in ind:
        # print(data.Heading.values[i]) #prints the Headings of the top 10 similar articles
    
    return shape, number_of_news_articles, new_query_vector, argmax, header, ind;
