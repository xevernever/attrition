#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Using simulated data provided by 
    This module attempts to understand why
    Why are our best and most experienced employees leaving prematurely? 


"""
import datetime
import logging
import os
import pandas as pd
import sys
import zipfile

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlretrieve

#%matplotlib inline

LOG_FILENAME = os.path.dirname(os.path.realpath(__file__)) + 'runtime.log'


def prep_for_ml(df):
    #Creating dummy variables for the column:sales
    dummies=pd.get_dummies(df['sales'],prefix='sales')
    df=pd.concat([df,dummies],axis=1)
    df.drop(['sales'],axis=1,inplace=True)
    df.head(10)

def plot_avg_hr():
    '''Plot of average hour'''
    data_load = load_data('bike')
    data_load['count'] = data_load['fremont_bridge_nb'] + data_load['fremont_bridge_sb']
    ind = pd.DatetimeIndex(data_load['date'])
    data_load['datetime'] = pd.DatetimeIndex(data_load['date'])
    data_load['year'] = ind.year
    data_load['hour'] = ind.hour
    hour_averages = data_load.groupby('hour').mean()['count']
    print(hour_averages)
    hour_averages.plot()


def plotDf(df):

    # Pairplot
    sns.pairplot(df, hue="left", vars=['satisfaction_level', 'last_evaluation', 'average_montly_hours','number_project'])
    plt.show()

    # Pairplot
    sns.pairplot(df, hue="salary", vars=['satisfaction_level','time_spend_company', 'last_evaluation', 'average_montly_hours','number_project'])
    plt.show()

    # Correlation Matrix Heatmap
    corr=df.corr()
    sns.heatmap(corr,annot=True)

def exploreDf(df):
    """ Explores descriptive statistics of data
    """

    df.columns()
    """ ['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident', 'left',
       'promotion_last_5years', 'sales', 'salary'],
      dtype='object') """

    df.dtypes


    
    # Any NULL Values?
    df.isnull().sum()
    


    # Transform categorical data into numerical data
    df['salary'].replace({'low':1,'medium':5,'high':10},inplace=True)

    # Summary Statistics
    df.info()
    df.describe(include='all')
   
    #   
    #for col in df.columns() for df.dtypes is numeric:
     # unique values
    list(set(df.sales))
    df['sales'].unique()
    
    #Correlation Matrix of Values
    df.corr()
    # Covariance Matrix of Values
    df.cov()
    # Sample Variance
    df.var()
    # Standard Deviation
    df.std()
    # Skew
    df.skew()
    # Kurtosis
    df.kurt()

def load_data(filename):
    '''Load trip data from the zipfile; return as a Dataframe'''
    if filename == 'bike':
        data = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        return pd.read_csv(data)
    elif filename == 'weather':
        data = ('https://raw.githubusercontent.com/UWSEDS/homework_data/master/'
                'weather_data.csv?token=AGL1-mlvl0B-0kLT86lRXBgcGha9E60Tks5Wn-'
                'cVwA%3D%3D')
        return pd.read_csv(data)
    else:
        print("Invalid filename: options- 'weather','bike'")

def load_csv_data(url_filename, csv_filename):
    """Load csv data into a DataFrame, checking if unzip is needed first 
    """

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

def run_tests():
    pass
 
def test_plot_close():
    # numpy.testing.assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)[source]¶
    #numpy.testing.assert_allclose()
    pass
    
def parseCLI():
    """ Parse Command Line Arguments
    """
    parser = ArgumentParser(__doc__, description = 'Attrition Analysis' , formatter_class=ArgumentDefaultsHelpFormatter)
    valid_mode = ['run','test']
    parser.add_argument('mode', 
                        default = 'pipeline',
                        nargs = 1,
                        # type='str',                    
                        choices=valid_mode,
                        help='run pipeline or test using pytest?')
    parser.add_argument(--url,
                        'url', 
                        default = None,
                        type='str',
                        required=False,                        
                        choices=valid_mode,
                        help='url from which to download data')    
    parser.add_argument('url_filename', 
                        default = None,
                        type='str',
                        required=False,                        
                        choices=valid_mode,
                        help='url_filename from which to download data')  
    parser.add_argument('csv_filename', 
                        default = None,
                        type='str',
                        required=False,
                        choices=valid_mode,
                        help='csv_filename from which to download data')  
    parser.add_argument('force_download', 
                        default = False,
                        type='boolean',
                        required=False,                        
                        choices=valid_mode,
                        help='Force Download from url')          

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

    # manual cli 
    #   my_args=[ mode='run', csv_filename = None, url = NULL, url_filename = NULL,
    #             force_download = False]
    sys.argv =['feature_summary.py', 'run', './data/HR_comma_sep.csv'] 

    # !python feature_summary.py run ./data/HR_comma_sep.csv
  
    args = parseCLI().parse_args()
    mode = args.mode
    
    if mode == 'test':
        print('Begin testing')
        run_tests()
 
    elif mode == 'run':
        print('Begin attrition pipeline')
        url = args.url
        url_filename = args.url_filename
        csv_filename = args.csv_filename
        force_download = args.force_download
    
        # Get Data
        if url:
            download_if_needed(url, url_filename, force_download)
        
        hrDf = load_csv_data(csv_filename, url_filename)
    
        # Explore Data
        exploreDf()
    
    
    
    
    
    
    