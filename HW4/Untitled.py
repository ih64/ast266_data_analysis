
# coding: utf-8

# In[1]:

#import some useful things
from astropy.table import Table
from astropy.io import fits
import numpy as np
import pdb

# ## Problem 2: Sigma Clipping

# In[2]:

#read in our data file
#hdulist=fits.open('0631_gmos_q2006_i.fits')
#imdata=hdulist[0].data

#make a copy of the data and flatten it
#temp_imdata=imdata.copy().flatten()

#calculate the mean and std of the data
#print "the mean and std of the data is %.3f and %.3f counts respectively" %(temp_imdata.mean(), temp_imdata.std())


# In[23]:

def sigmaClip(data, nsigma, call=0):
    '''sigma clipping algorithm. recieves a numpy array, identifies mean, std, discards elements
    above or below thresh*std away from mean, repeat until no more elements are outside threshold
    inputs:
        data: a 1d numpy array
        nsigma: the number of sigma away from the mean you want to clip off
    outputs: 
        clipped_data: a numpy array containing the surviving elements from input data
    '''
    
    #calculate the mean, std, and threshold
    mean=data.mean()
    std=data.std()
    threshold=nsigma*std
    
    up_thresh=mean+threshold
    down_thresh=mean-threshold
    
    #create the mask to identify elements between thresholds
    good_mask= ((data <= up_thresh) & (data >= down_thresh))

    #define the testcase. if this is true the program will exit
    #if there are no elements above or below threshold, we're done. return the masked array 
    if data[~good_mask].size == 0:
        pdb.set_trace()
        print data.mean()
        print data.std()
        return data
    
    #if that's not the case, recurse on the subproblem. keep using the same nsigma
    else:
        call+=1
        return sigmaClip(data[good_mask], nsigma, call=call)




