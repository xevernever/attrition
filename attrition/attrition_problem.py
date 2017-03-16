""""Goal 0: Tee Up Project; Why Do We Care?"""
import pandas as pd
import matplotlib.pyplot as plt

## Import Data ##
df = load_data() # df = pd.read_csv('HR_comma_sep.csv')
#df.head()
#df.dtypes

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