"""Modules"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tools.plotting import scatter_matrix


def load_data():
    """Load trip data, return as DataFrame"""
    df = pd.read_csv('HR_comma_sep.csv')
    return df

df = load_data()

def separate(attrition):
    '''separate by attrition'''
    df = load_data()
    if attrition == 'left':
        left = df[df['left'] == 1]
        return left
    elif attrition == 'stayed':
        stayed = df[df['left'] == 0]
        return stayed
    else:
        print("Invalid entry- options: 'left','stayed'")


def display_attrition_level():
    """ DV1: Left-or-Stayed (binary variable); Display Attrition Level """
    df = load_data()
    (stayed_count, left_count) = pd.value_counts(df['left'])
    attrition_percentage = round(100 * left_count/(left_count+stayed_count),1)
    print("Percentage of employees that have left: {0}%".format(attrition_percentage))

# def separation(var='left'):
#     df = load_data();
#     if var == 'left':
#         return df.query('left==0')
#     elif var == 'right':
#         return df.query('left==1')
#     else:
#         return False

def display_histogram_tenure():
    """ DV2: Tenure (Years with Company); Distribution """
    #%matplotlib inline
    df = load_data()
    df.time_spend_company.hist()
    #df.time_spend_company.plot.hist()
    plt.title('Histogram of Tenure With Company')
    plt.xlabel('Years With Company')
    plt.ylabel('Frequency')

def summary_stats():
    '''Variable means against attrition'''
    left = separate('left')
    stayed = separate('stayed')
    stayed_summary = pd.DataFrame(stayed.describe())
    left_summary = pd.DataFrame(left.describe())
    mean_stayed = stayed_summary.iloc[1]
    mean_left = left_summary.iloc[1]
    means = pd.concat([mean_stayed,mean_left],axis=1)
    means.columns = ['stayed','left']
    means['difference'] = (means['left']-means['stayed'])/means['stayed']*100.00
    return means.sort('difference',ascending=False)[1:]


def corr_plot():
    '''Correlation Matrix'''
    df = load_data()
    correlations = df.corr()
    sns.heatmap(correlations,vmin=-.5,vmax=.5,square=True,annot=True,cmap='cool_r')
    plt.title('Correlation Matrix')

def hist():
    '''Histogram'''
    left = separate('left')
    stayed = separate('stayed')
    weights_stayed = np.ones_like(stayed['time_spend_company'])/len(stayed)
    weights_left = np.ones_like(left['time_spend_company'])/len(left)
    plt.hist(left['time_spend_company'],bins=10,color='magenta',label='left',weights=weights_left)
    plt.hist(stayed['time_spend_company'],bins=10,rwidth=.5,alpha=0.75,color='cyan',label='stayed',weights=weights_stayed)
    plt.title("Attrition versus Time Spent in Company")
    plt.xlabel("Time Spent in Company")
    plt.ylabel("Count")
    plt.legend()
    plt.show()


def scatter_matrix1():
    '''Scatter plot matrix of our numeric data'''
    # define colors list, to be used to plot survived either red (=0) or green (=1)
    colors=['cyan','magenta']
    df = load_data()
    # make a scatter plot
    df_numeric = df[['satisfaction_level','last_evaluation','average_montly_hours']]
    scatter_matrix(df_numeric,figsize=[20,20],marker='.',c=df.left.apply(lambda x:colors[x]))
