#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:10:44 2020

@author: abdulahfawaz
"""


def check_if_zip_exists(filename):
    from os import path

    return path.isfile(filename)


def download_data(url, name):
    import requests
    print('Downloading Data')
    r = requests.get(url, allow_redirects=True)




    open(str(name), 'wb').write(r.content)
    
    return


def get_zip(datasize):
    datasize = datasize.lower()
    assert datasize in ['100k', '25m'] , 'Only 25M or 100k size datasets available'
    
    filename = 'movielens_' + datasize +'.zip'
    
    
    if not check_if_zip_exists(filename):
        
        url = 'http://files.grouplens.org/datasets/movielens/ml-' + datasize + '.zip'
    
        download_data(url, filename)  
    
        
    return 