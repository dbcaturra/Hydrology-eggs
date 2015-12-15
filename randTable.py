
# coding: utf-8

# In[7]:

import numpy as np


# In[8]:

def randTable(filename, up, down ):
    tabla = open(filename,"r")
    text = tabla.readlines()
    ntabla = open(filename,"w")
    for line in range(len(text)):
        if line == len(text) - 1: 
            line = text[line].split("\t")
            line[-1]  = str(np.random.uniform(up,down))
            ntabla.writelines("\t".join(line))
        else:
            line = text[line].split("\t")
            line[-1]  = str(np.random.normal())
            ntabla.writelines("\t".join(line)+"\n")


# In[9]:

randTable("Tabla.txt", 1, 3 )


# In[ ]:



