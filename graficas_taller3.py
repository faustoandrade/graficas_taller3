
# coding: utf-8

# In[62]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[130]:

#se define los valores
x = [2,4,6]
y = [0, 20, 0]

plt.plot(x,y, linestyle='-', color='c')
plt.show()
#plt.title("GRAFICA TRIANGULAR")


# In[135]:

x = [2,3,5,6]
y = [10, 21,21,10]

plt.plot(x,y)
plt.show()
# plt.title('TRAPEZOIDAL')


# In[134]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[118]:

y = np.random.normal(loc=1, scale=1, size=2000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))


# In[119]:

plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.010)
plt.title('SIGMOIDAL')
plt.grid(True)


# In[ ]:



