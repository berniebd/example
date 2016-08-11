# -*- encoding:utf-8 -*-
import json
from collections import Counter

from pandas import DataFrame, Series
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'bida'

path = 'C:\\Workspace\\usagov_bitly_data2013-05-17-1368828605.txt'
records = [json.loads(line) for line in open(path, encoding='utf-8')]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
frame = DataFrame(records)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] == 'Unknown'
tz_counts = clean_tz.value_counts()

tz_counts[:10].plot(kind='barh', rot=0)

# results = Series([x.split()[0] for x in frame.a.dropna()])
# results = Series([x.split()[0] for x in frame.a.dropna().drop_duplicates()])

cframe = frame[frame.a.notnull()]
operation_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# print(operation_system[:5])

by_tz_os = cframe.groupby(['tz', operation_system])

agg_counts = by_tz_os.size().unstack().fillna(0)

# print(agg_counts[:10])

indexer = agg_counts.sum(1).argsort()
# print(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]
# print(count_subset)

count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)

normed_subset.plot(kind='barh', stacked=True)

plt.show()