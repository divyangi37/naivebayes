#!/usr/bin/env python
# coding: utf-8

# In[21]:


from sklearn.naive_bayes import GaussianNB

#[size,wheels,cost,wight]
f=[[0,2,3,0],[1,3,4,0],[2,4,5,1],[2,6,5,1],[0,4,4,0]]
l=['bike','auto','car','truck','car']

clf = GaussianNB()

trained = clf.fit(f,l)
q=1
while(q):
    a=int(input('what is the size small(0), medium(1), big(2) '))
    b=int(input('no of wheels'))
    c=int(input('whats the cost low(3), medium(4), high(5)'))
    d=int(input('whats the weight- normal(0), heavy(1)'))
    res=trained.predict([[a,b,c,d]])
    
    print(res)
    q=int(input('would you like to ask again > choose from 1 and 0 : '))


# In[ ]:





# In[ ]:




