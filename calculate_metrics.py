#!/usr/bin/env python
# coding: utf-8

# In[1]:


class calculate():
    
    def __init__(self,x1y1,x2y2):
        self.x1y1 = x1y1 # ---- (-1,12)
        self.x2y2 = x2y2 # ----- (22,10)
        
    def calc_distanc(self):
        x1,y1 = self.x1y1
        x2,y2 = self.x2y2
        
        return ((y2-y1)**2 + (x2-x1)**2)**0.5

    def calc_slope(self):
        x1,y1 = self.x1y1
        x2,y2 = self.x2y2
        
        return (y2-y1)/(x2-x1)


# In[ ]:




