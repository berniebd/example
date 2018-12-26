# -*- coding: utf-8 -*-
# Created by bida on 2018/8/28

import matplotlib.pyplot as plt
import numpy as np

# data = np.arange(100, 201)
# plt.plot(data)
#
# data2 = np.arange(200, 301)
# plt.figure()
# plt.plot(data2)

data = np.arange(100, 201)
plt.subplot(221)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(223)
plt.plot(data2)

plt.show()