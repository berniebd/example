# -*- coding: utf-8 -*-
# Created by bida on 2018/8/28
import matplotlib.pyplot as plt
import numpy as np

# line
plt.plot([1, 2, 3], [3, 6, 9], '-r')
plt.plot([1, 2, 3], [2, 4, 9], '-g')
plt.subplot(230)
# plt.show()


# dot
N = 20
plt.subplot(231)
plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='r', s=100, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='g', s=200, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='b', s=300, alpha=0.5)

# pie
labels = ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data = np.random.rand(7) * 100

plt.subplot(232)
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

# bar
N = 7
x = np.arange(N)
data2 = np.random.randint(low=0, high=100, size=N)
colors = np.random.rand(N * 3).reshape(N, -1)
plt.title('Weekday Data')
plt.subplot(233)
plt.bar(x, data2, alpha=0.8, color=colors, tick_label=labels)

# hist
data3 = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
labels = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]
plt.subplot(234)
plt.hist(data3, bins=bins, label=labels)
plt.legend()
plt.show()