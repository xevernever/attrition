#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:16:31 2017

@author: kimba
"""

import datetime
import logging
import os
#import os import zipfile
import pandas as pd
import sys
from urllib.request import urlretrieve
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

LOG_FILENAME = os.path.dirname(os.path.realpath(__file__)) + 'runtime.log'



def download_if_needed(url, url_filename, force_download=False):
    """ Downloads from a url and stores in filename.
        Check if download is already completed or if a reload is desired.
    """
    if force_download or not os.path.exists(url_filename):
        print('Attempting download')
        try:
            urlretrieve(url, url_filename)
        except Exception as err:
            print('Problem retrieving url')
    else:
        print('File already downloaded.')


def load_csv_data(url_filename, csv_filename):
    """Load csv data into a DataFrame, checking if unzip is needed first"""

    try:
        # Handle different filetypes
        if url_filename.endswith('.zip'):
            zipf = zipfile.ZipFile(url_filename)
            return pd.read_csv(zipf.open(csv_filename))
        elif url_filename.endswith('.csv'):
            return pd.read_csv(csv_filename)
        else:
            print('Unknown File Type! Please retry.')
    except IOError as err:
        print('Problem reading csvfile: %csv_filename')% csv_filename
         #  {csv_filename}: {err}'.format(csv_filename, err))



def parseCLI():
    parser = ArgumentParser(description = 'Attrition Analysis' , __doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    valid_mode = ['run','test']
    parser.add_argument('mode', 
                        default = 'pipeline',
                        type='str',
                        required=False,                        
                        choices=valid_mode,
                        help='run pipeline or test using pytest?')
    parser.add_argument('force_download', 
                        default = False,
                        type='boolean',
                        required=False,                        
                        choices=valid_mode,
                        help='Force Download from url')     
    parser.add_argument('url', 
                        default = NULL,
                        type='str',
                        required=False,                        
                        choices=valid_mode,
                        help='url from which to download data')    
    parser.add_argument('url_filename', 
                        default = NULL,
                        type='str',
                        required=False,                        
                        choices=valid_mode,
                        help='url_filename from which to download data')  
    parser.add_argument('csv_filename', 
                        default = NULL,
                        type='str',
                        required=False,
                        choices=valid_mode,
                        help='csv_filename from which to download data')  
     

    return parser

class Logger():
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(LOG_FILENAME, 'a')
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

if __file__ == 'main':
    #start logging
    sys.stdout = Logger()
    start = datetime.datetime.now()
    

    # !python name.py '..' '...'
    sys.argv  = feature_summary.py, 'run', './data/HR_comma_sep.csv'
    argz = parseCLI().parse_args()
    mode = args.mode
    force_download = args.force_download
    url = args.url
    url_filename = args.url_filename
    csv_filename = args.csv_filename

    print('Arguments: ' + argz)   
 
    # Download from url if needed
    if url:
        download_if_needed(url, url_filename, force_download)
    
    data = load_csv_data(csv_filename, url_filename)
    
    print(url, url_filename, csv_filename)
    
    #data = load_csv_data(url, filename)
    data.head()
    
    
    
    
    
    
    