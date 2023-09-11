#!/usr/bin/env python
# coding: utf-8

# In[15]:


from astroquery.mast import Observations
import pandas as pd


###  read in TIC ID from a file

#data=pd.read_csv('/Users/weichunjao/GSU/TESS/HRHI.EDR3.TESS.CHIRON.results.csv')
data=pd.read_csv('/Users/vaths/Desktop/GSU REU RECONS/2 min-cadence 22 stars.csv')
targetID=data['TICID']
#targetID=['33911269']

#data=pd.read_csv('/Users/vaths/GSUREURECONS/TESS/2min-cadence22stars.csv')
#targetID=data['TIC']

## loop through IDs

#for TIC in targetID:
    #TICID=TIC
for TIC in data['TICID']:
    TICID=TIC
    #print(TICID)
    ###send query command to MAST to get TESS data
   
    obs_table = Observations.query_criteria(obs_collection = ['TESS'], provenance_name=["SPOC"],
                                dataproduct_type = ["TIMESERIES"], target_name=TIC, t_exptime=[0, 120])
    #print(obs_table)

    ### get product list
    data_products = Observations.get_product_list(obs_table)
    #print (data_products)
    arr=[]

    ### loop through the list and obtain the array index which file name contains lc.fits
   
    for index, uri in enumerate(data_products["productFilename"]):
        if "lc.fits" in uri:
            arr+=[index]
    subdata=data_products[arr]
    print (subdata)

    #### the data will be downloaded and saved in a directory called "masterDownlad".
   
    manifest = Observations.download_products(subdata)
    #print (manifest)


# In[6]:


import lightkurve as lk

## use lightkurve to read in FITS data
fits_file='C:/Users/vaths/mastDownload/TESS/tess2022085151738-s0050-0000000168706566-0222-s/tess2022085151738-s0050-0000000168706566-0222-s_lc.fits'

lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value

print(flux)#hz
print(time)#days

#for TIC in data['']:
    #TICID=TIC

#forloop
#willdownloadasonefolderwithmultiplefiles


# In[58]:


import matplotlib.pyplot as plt
#import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')
#zoom graph

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()
#ax.set_title("PDCSAP light curve of Kepler-8")


# In[59]:


import lightkurve as lk

## use lightkurve to read in FITS data
fits_file='C:/Users/vaths/mastDownload/TESS/tess2022057073128-s0049-0000000168706566-0221-s/tess2022057073128-s0049-0000000168706566-0221-s_lc.fits'

lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value

print(flux)#hz
print(time)#days


# In[60]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()
#ax.set_title("PDCSAP light curve of Kepler-8")


# In[66]:


fits_file='C:/Users/vaths/mastDownload/TESS/tess2022027120115-s0048-0000000165685335-0219-s/tess2022027120115-s0048-0000000165685335-0219-s_lc.fits'

lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value

print(flux)#hz
print(time)#days


# In[67]:


import matplotlib.pyplot as plt
#import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()
#ax.set_title("PDCSAP light curve of Kepler-8")


# In[65]:


fits_file='C:/Users/vaths/mastDownload/TESS/tess2021336043614-s0046-0000000281930612-0217-s/tess2021336043614-s0046-0000000281930612-0217-s_lc.fits'

lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[64]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()
#ax.set_title("PDCSAP light curve of Kepler-8")


# In[ ]:


#fixed="C:\Users\vaths\mastDownload\TESS\tess2022085151738-s0050-0000000168706566-0222-s\tess2022085151738-s0050-0000000168706566-0222-s_lc.fits"+"C:\Users\vaths\mastDownload\TESS\tess2022057073128-s0049-0000000168706566-0221-s\tess2022057073128-s0049-0000000168706566-0221-s_lc.fits"+
str1+str2+str3
str1='C:'
str2=


# In[31]:


fits_file='C:/Users/vaths/mastDownload/TESS/tess2021336043614-s0046-0000000094892194-0217-s/tess2021336043614-s0046-0000000094892194-0217-s_lc.fits'
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[32]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[33]:


fits_file='C:/Users/vaths/mastDownload/TESS/tess2021310001228-s0045-0000000281930612-0216-s/tess2021310001228-s0045-0000000281930612-0216-s_lc.fits'
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[34]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[35]:


fits_file="C:/Users/vaths/mastDownload/TESS/tess2021258175143-s0043-0000000419954601-0214-s/tess2021258175143-s0043-0000000419954601-0214-s_lc.fits"
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[36]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[37]:


fits_file="C:/Users/vaths/mastDownload/TESS/tess2021258175143-s0043-0000000405293306-0214-s/tess2021258175143-s0043-0000000405293306-0214-s_lc.fits"
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[38]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[40]:


fits_file="C:/Users/vaths/mastDownload/TESS/tess2021258175143-s0043-0000000365190599-0214-s/tess2021258175143-s0043-0000000365190599-0214-s_lc.fits"
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[41]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[44]:


fits_file='C:/Users/vaths/mastDownload/TESS/tess2021232031932-s0042-0000000419954601-0213-s/tess2021232031932-s0042-0000000419954601-0213-s_lc.fits'
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[45]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[46]:


fits_file="C:/Users/vaths/mastDownload/TESS/tess2021232031932-s0042-0000000405293306-0213-s/tess2021232031932-s0042-0000000405293306-0213-s_lc.fits"
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[47]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[48]:


fits_file="C:/Users/vaths/mastDownload/TESS/tess2021232031932-s0042-0000000069745467-0213-s/tess2021232031932-s0042-0000000069745467-0213-s_lc.fits"
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)


# In[49]:


import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
x = time 
#x=time
#y=flux
y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
fig, ax = plt.subplots()

ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

plt.show()


# In[ ]:


fits_file='C:/Users/vaths/MastDownload/TESS"+
fits_file1=''+''
lc=lk.read(fits_file, quality_bitmask='default')

time=lc.time.value

flux=lc.flux.value

flux_err=lc.flux_err.value
print(flux)
print(time)
"C:\Users\vaths\mastDownload\TESS\tess2022085151738-s0050-0000000168706566-0222-s\tess2022085151738-s0050-0000000168706566-0222-s_lc.fits"


# In[92]:


import pandas as pd

###  read in TIC ID from a file

#data=pd.read_csv('/Users/weichunjao/GSU/TESS/HRHI.EDR3.TESS.CHIRON.results.csv')
#data=pd.read_csv('C:/Users/vaths/Desktop/TESSIDs.csv')
#targetID=data['Folder']
#targetID=['33911269']

#data=pd.read_csv('/Users/vaths/GSUREURECONS/TESS/2min-cadence22stars.csv')
#targetID=data['TIC']

## loop through IDs

#for TIC in targetID:
    #TICID=TIC
#print (TICID) 
for fits_file in data['Folder']:
    fits_file="C:/Users/vaths/mastDownload/TESS/"+"C:/Users/vaths/Desktop/TESSIDs.csv"+"_lc.fits"
    print(data['Folder'])
"""
    
    data=pd.read_csv('C:/Users/vaths/Desktop/TESSIDs.csv')
    targetID=data['Folder']
    #lc=lk.read(fits_file, quality_bitmask='default')
    time=lc.time.value
    flux=lc.flux.value
    flux_err=lc.flux_err.value
    print(flux)
    print(time)
    #TICID=TIC
#print(fits_file)
    import matplotlib.pyplot as plt
#import numpy as np

#plt.style.use('_mpl-gallery')
#plt.style.use()

# make data
    x = time 
#x=time
#y=flux
    y = flux
#4 + 2 * #np.sin(2 * x) #flux

# plot
    fig, ax = plt.subplots()

    ax.plot(x, y, 'ko') #linewidth=2.0)

#ax.set(xlim=(0, 8), xticks=#np.arange(1, 8),
       #ylim=(0, 8), yticks=#np.arange(1, 8))

    plt.show()
"""
    


# In[ ]:




