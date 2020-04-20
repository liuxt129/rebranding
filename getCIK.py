
# coding: utf-8

# In[11]:


import pandas as pd
from sec_edgar_downloader import Downloader


# In[8]:


cik = pd.read_csv("FINAL_COMPANY_LIST_SEC_INFO.csv")[['cik']]
cik = cik.values.tolist()
print(cik)


# In[9]:


file_location = "/pylon5/tr5pi7p/suli2020/uspto/rebranding/10K"
cik = cik[:10]
dl = Downloader(file_location)


# In[ ]:


num = 0
for lst in cik:
    for c in lst:
        print('Started: ' + c)
        dl.get("10-K", c, 30)
        num += 1
        print('Downloaded: ' + c + ', ' + num +' in total')

