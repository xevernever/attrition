""""Goal 0: Tee Up Project; Why Do We Care?"""
import pandas as pd

## Import Data ##
df = pd.read_csv('HR_comma_sep.csv')
#df.head()
df.dtypes

#df[df['left']==0]['left']
import matplotlib
%matplotlib inline

## DV1: Left-or-Stayed (binary variable); Display Attrition Level ##
(stayed_count, left_count) = pd.value_counts(df['left'])
attrition_percentage = round(100 * left_count/(left_count+stayed_count),1)
print("Percentage of employees that have left: {0}".format(attrition_percentage))

## DV2: Tenure (Years with Company); Distribution
# histogram of education
df.satisfaction_level.hist()
plt.title('Histogram of Salary')
plt.xlabel('Salary Category')
plt.ylabel('Frequency')

