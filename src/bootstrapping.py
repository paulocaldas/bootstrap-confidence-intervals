# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:06:18 2020

@author: pcaldas
"""

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import pandas as pd

def confidence_intervals_BS(means, confidence = 0.95): 
    
    lower = (1 - confidence)/2
    upper = 1 - lower
    
    lower_limit = np.round(np.quantile(means, lower), 3)
    upper_limit  = np.round(np.quantile(means, upper), 3)
    
    return lower_limit, upper_limit

def bootstrapping(sample, confidence = 0.90, resamples = 10000, bins = 30):
    ''' returns the BS Confidence interval for the sample'''
    means = []

    for i in range(resamples):
        resampling = np.random.choice(sample, size = len(sample), replace = True)
        means.append(np.mean(resampling))
        
    CI = confidence_intervals_BS(means, confidence = confidence)
    label = "mean = " + str(round(np.mean(means),2)) + '\n' + "C.I = " + str(CI)
    
    print('mean = {:.3}; conf. interval = {}; resamples = {}'.format(np.mean(means), CI, resamples))
    
    fig, ax = plt.subplots(1,2, figsize = (9,3), dpi = 120)
    
    ax[0].hist(sample, edgecolor = 'black', bins = bins,  alpha = 0.8,
               density = True);
    
    ax[0].set_xlabel('$\phi$', fontsize = 12)
    ax[0].set_ylabel('PDF', fontsize = 12)
    ax[0].set_title('original sample')
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['top'].set_visible(False)
    ax[0].tick_params(direction = 'inout')

    ax[1].hist(means, edgecolor = 'black', bins = bins, alpha = 0.8,
               density = True, label = label );
    
    ax[1].set_xlabel('$<\phi$>', fontsize = 12)
    ax[1].set_title('bootstrap distribution')
    ax[1].legend(frameon = False, fontsize = 9, bbox_to_anchor = (0.55,0.95))
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].tick_params(direction = 'inout')
    
    # now we build a confidence interval based on the distribtion of the means
    # by taking the empirical quantiles from the bootstrap distribution of the parameter
      
    return CI