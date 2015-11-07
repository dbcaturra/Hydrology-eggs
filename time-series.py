# coding: utf-8
# In[1]:

import pandas
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
#from bokeh.plotting import figure, output_notebook, show
#output_notebook()
# In[17]:
import os, datetime
pwd = os.path.abspath(os.path.dirname("__main__"))
pwd = os.path.join(pwd, "data/MENSUALES")
filenames = os.listdir(pwd)
filenames.sort()

for file_ in filenames:
    print file_
    data = pandas.read_excel(os.path.join(pwd, file_), "VALOR")
    info = pandas.read_excel(os.path.join(pwd, file_), "INVENTARIO")
    codes = info["CODIGO"]
    codes = codes.tolist()
    index = []

    for i in range(len(data.ANO)):
        index.insert(i, datetime.datetime(data.ANO[i],data.MES[i],data.DIA[i],data.HORA[i],data.MINUTO[i],data.SEGUNDO[i]))

    for i in data.columns[6:len(data.columns)]:
        idx = codes.index(i)
        name = info["NOMBRE"][idx]
        code_ = i
        current = info["CORRIENTE"][idx]
        fig = plt.figure()
        fig.suptitle("%s [%s] - %s \n %s"%(name, code_,current, file_))
        plt.plot(index, data[i])
        plt.xlabel('time')
        plt.ylabel('Q')
        fig.savefig("%s_%s.png"%(file_, code_))




