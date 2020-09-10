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
    
    """
    
    Checks if zip file exists and downloads if it does not
    
    """
    
    zip_filename = 'movielens_' + datasize +'.zip'
    
    
    if not check_if_zip_exists(zip_filename):
        
        url = 'http://files.grouplens.org/datasets/movielens/ml-' + datasize + '.zip'
    
        download_data(url, zip_filename)  
    
    extract_zip(zip_filename) 
    return 



def check_if_folder_exists(foldername):
    from os import path
    return path.isdir(foldername)



def extract_zip(zipfile):
    from zipfile import ZipFile
    print('Unzipping...')
    with ZipFile(zipfile,"r") as zipped:
        zipped.extractall()



def get_data(datasize):
    """
    Checks for the data and gathers it if not present.
    
    If folder does not exist - extracts zip.
    If zip does not exist - downloads it.
    
    """
    datasize = datasize.lower()
    assert datasize in ['100k', '25m'] , 'Only 25M or 100k size datasets available'
    
    # if dir not exists:
        #get zip
        # extract zip
    # load data
    # return data
    
    foldername = 'ml-' + datasize
    
    if not check_if_folder_exists(foldername):
        get_zip(datasize)
    
    return

