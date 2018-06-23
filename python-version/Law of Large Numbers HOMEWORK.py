
# coding: utf-8

# In[ ]:


# Create a script that will count how many of N total fall between -1 and 1, when the mean is 0 and sd is 1
# The expected value is 68.2%. By LLN, the larger N is, the closer our experimental value will be to 68.2%


# In[ ]:


import numpy as np
from numpy.random import randn


# In[ ]:


# The larger 'N' is, the closer expVal will
N = 10000
fellBetween = 0
for i in range(N):
    x = randn()
    if x < 1 and x > -1:
        fellBetween += 1

expVal = (fellBetween / N) * 100
print(expVal, "%")


# ---

# In[ ]:


# Instructor's solution


# In[ ]:


import numpy as np
from numpy.random import randn


# In[ ]:


randn(100) # Should make an array of 100 random numbers


# In[ ]:


N = 10000
counter = 0
for i in randn(N):
    if i > -1 and i < 1:
        counter = counter + 1
counter / N

