# -*- encoding:utf-8 -*-
__author__ = 'bida'

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('C:\Workspace\dataAnalysis\ml-1m\\users.dat', sep='::', header=None, names=unames)
# print(users[:5])


rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('C:\Workspace\dataAnalysis\ml-1m\\ratings.dat', sep='::', header=None, names=rnames)
# print(ratings[:5])

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('C:\Workspace\dataAnalysis\ml-1m\movies.dat', sep='::', header=None, names=mnames)
# print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)
# print(data)
# print(data.__class__)
# print(dir(data))
# print(data.ix[0])

mean_ratings = data.pivot_table(data, index='title', columns='gender', aggfunc='mean')
# print(mean_ratings[:5])

ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])
#
active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print(active_titles[:10])

mean_ratings = mean_ratings.ix[active_titles[:10]]
# print(mean_ratings)

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
print(top_female_ratings[:10])