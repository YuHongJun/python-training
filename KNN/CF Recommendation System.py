
# coding: utf-8

# **Examples of Collaborative Filtering based Recommendation Systems**

#make necesarry imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation, cosine
import ipywidgets as widgets
from IPython.display import display, clear_output
from sklearn.metrics import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys, os, time
from contextlib import contextmanager


local_data = '/Users/yuhongjun/Python/python-training/data/qraved_1k_user.csv'
trans_data = '/Users/yuhongjun/Python/python-training/KNN/new_trans_data.csv'

#declaring k,metric as global which can be changed by the user later

global k, metric, productLength, headerNamesFilter, headerNamesFilterWithNan
k=4
metric='correlation' #can be changed to 'correlation' for Pearson correlation similaries
productLength=5


# headerNames = ['user_id', 'restaurant_id', 'PageViews', 'Reviews', 'Photo Upload',
#                'Bookings', 'Calls', 'Map', 'Direction', 'Like Photo', 'Like View',
#                'Like Event', 'Comment Review', 'Comment Photo', 'Search Suggestion',
#                'Saved', 'Rating', 'No Show'] resource
headerNamesFilter = ['user_id', 'restaurant_id', 'PageViews', 'Reviews', 'Photo Upload',
                     'Bookings', 'Calls', 'Map', 'Direction', 'Like Photo', 'Like View',
                     'Like Event', 'Comment Review', 'Comment Photo', 'Search Suggestion',
                     'Saved']
headerNamesFilterWithNan = ['Reviews', 'Photo Upload',
                            'Bookings', 'Calls', 'Map', 'Direction', 'Like Photo', 'Like View',
                            'Like Event', 'Comment Review', 'Comment Photo', 'Search Suggestion',
                            'Saved']
# 'qraved_input.csv'

def xlsx_to_csv_pd():
    data_xls = pd.read_excel('qraved_1k_user.xlsx', index_col=0)
    data_xls.to_csv('qraved_1k_user.csv', encoding='utf-8')
# xlsx_to_csv_pd()

def dataSet2Matrix(filename):
    start_time = time.clock()

    df_weight = [0.5,3,5,4,4.5,3.5,3.5,3,3,3.5,2,2,1,4]
    reader = pd.read_csv(filename, iterator=True, header=0, usecols=headerNamesFilter, nrows=340)
#     reader = pd.read_csv(local_data, iterator=True, header=0, usecols=headerNamesFilter, names=headerNames, nrows=1000)

    loop = True
    chunkSize = 100000
    chunks = []
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    df = pd.concat(chunks, ignore_index=True)
    df = df.replace([0, 0.0], [np.nan, np.nan])
    df = df.dropna(axis=0, how='all', subset=headerNamesFilterWithNan)
    df = df.drop_duplicates()

    # print(df)
    # df = df.iloc[0:].dropna(axis=0, how='all')
    # df = df.drop_duplicates()
    # print(df.iloc[0:,0:])
    # slice 'user_id', 'restaurant_id'

    df_columns = df.columns[2:].tolist()
    for c in df_columns:
        df[c] = df[c]*df_weight[df_columns.index(c)]

    # to_drop = ['user_id', 'restaurant_id']
    # df_sum = df.drop(to_drop, axis = 1)
    df_user_id = df.pop('user_id')
    df_restaurant_id = df.pop('restaurant_id')
    userItemData = pd.DataFrame({
        'user_id': df_user_id,
        'restaurant_id': df_restaurant_id,
    })
    userItemData['ratings'] = df.apply(lambda x: x.sum(), axis=1)
    print(userItemData.shape)
    userItemData.to_csv("new_trans_data.csv", encoding = "utf-8", index=False)
    end_time = time.clock()
    time_spent = end_time - start_time
    print("\ntime spent:", time_spent)
# dataSet2Matrix(local_data)
# (4769, 3)


def readTransData(filename):
    start_time = time.clock()
    userItemData = pd.read_csv(filename, header=0)
    # print(userItemData)
    global userList, itemList, M
    #Get list of unique items
    itemList = list(set(userItemData['restaurant_id']))
    #Get list of unique userId
    userList = list(set(userItemData['user_id']))
    # print(itemList)
    # print(userList)

    M = pd.DataFrame(columns=itemList, index=userList)
    for index,row in userItemData.iterrows():
        M.loc[row['user_id'], row['restaurant_id']] = row['ratings']

    # M = M.dropna(axis=1, how='all')
    # M = M.drop_duplicates()
    M = M.fillna(0)
    # print(M)
    end_time = time.clock()
    time_spent = end_time - start_time
    print("\ntime spent:", time_spent)
    # return M


# readTransData(trans_data)
# M


# **User-based Recommendation Systems**

# In[5]:


#get pearson similarities for ratings matrix M; pairwise_distances returns the distances between ratings and hence
#similarities are obtained by subtracting distances from 1
# pearson_sim = 1-pairwise_distances(M, metric="correlation")


# In[6]:


#Pearson correlation similarity matrix
# pd.DataFrame(pearson_sim)


# In[7]:


#This function finds k similar users given the user_id and ratings matrix M
#Note that the similarities are same as obtained via using pairwise_distances
def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.loc[user_id, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    ratingsIndex = ratings.index.tolist()    
    # print( '{0} most similar users for User {1}:\n'.format(k,user_id))
    for i in range(0, len(indices.flatten())):
        if ratingsIndex[indices.flatten()[i]] == user_id:
            continue;

        # else:
        #     print( '{0}: User {1}, with similarity of {2}'.format(i, ratingsIndex[indices.flatten()[i]], similarities.flatten()[i]))
            
    return similarities,indices


# In[8]:


# similarities,indices = findksimilarusers(100061,M, metric=metric, k=k)


# In[9]:


#This function predicts rating for specified user-item combination based on user-based approach
def predict_userbased(user_id, item_id, ratings, k=k, metric = metric):
    similarities, indices=findksimilarusers(user_id, ratings,metric, k=k) #similar users based on Pearson correlation similarity
    mean_rating = ratings.loc[user_id,:].mean() #to adjust for zero based indexing
    sum_wt = np.sum(similarities)-1
    product=1
    wtd_sum = 0 
    ratingsIndex = ratings.index.tolist()  
    for i in range(0, len(indices.flatten())):
        if ratingsIndex[indices.flatten()[i]] == user_id:
            continue;
        else: 
            ratings_diff = ratings.loc[ratingsIndex[indices.flatten()[i]],item_id]-np.mean(ratings.loc[ratingsIndex[indices.flatten()[i]],:])
            product = ratings_diff * (similarities[i])
            wtd_sum = wtd_sum + product
    
    prediction = round(mean_rating + (wtd_sum/sum_wt))
    # print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id,item_id,prediction))
    return prediction


# In[10]:


# predict_userbased(100061,31237,M,k,metric);


# In[11]:


def runMain(ratings,k,productLength):
    start_time = time.clock()
    n_users = ratings.shape[0]
    n_items = ratings.shape[1]
    # print(userList)

    prediction = pd.DataFrame(columns=itemList, index=userList)
    for i in range(n_users):
        for j in range(n_items):
            prediction.loc[userList[i], itemList[j]] = predict_userbased(userList[i], itemList[j], ratings, k, metric)

    for i in range(n_users):
        products = prediction.loc[userList[i]].nlargest(productLength)
        productsIndex = products.index.tolist()
        print('\nPredicted {0} products for user {1} -> products {2}'.format(productLength,userList[i],productsIndex))
#     abc=prediction.loc[116096].sort_values(ascending=False).head(5)
#     abc=prediction.loc[116096].nlargest(10)
    end_time = time.clock()
    time_spent = end_time - start_time
    print("\ntime spent:", time_spent)
    return prediction
# runMain(M,k,productLength)


# In[12]:


#Root Mean Square Error, 均方根误差是观测值与真值偏差
def sortRMSE():
    readTransData(trans_data)
    RMSEDict = {}
    for k in range(1,10):
        prediction = runMain(M,k,productLength)
        MSE = mean_squared_error(prediction, M)
        RMSE = round(sqrt(MSE),3)
        RMSEDict[k] = RMSE
        print ("\n{0} RMSE using k is {1}, approach is: {2}".format('Pearson correlation similaries', k, RMSE))
    
    sortDict = sorted(RMSEDict.items(),key=lambda x:x[1])
    print(sortDict)
    return sortDict
# sortRMSE()

if __name__ == '__main__':
    readTransData(trans_data)
    runMain(M, 8, productLength)

    # sortRMSE()
    # runMain(M, k, productLength)
    # print(M.loc[109818])