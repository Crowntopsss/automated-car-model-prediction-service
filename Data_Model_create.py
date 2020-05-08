
import re
import pandas as pd
import matplotlib.pyplot as plt
import collections
from collections import Counter
import numpy as np
import seaborn as sns
import patsy
import statsmodels.api as sm
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
from sklearn import preprocessing, linear_model, pipeline, metrics
#get_ipython().run_line_magic('pylab', 'inline')


df=pd.read_csv('data/Step3_output_clean_df.csv')

makes = ['Nissan', 'Toyota', 'Honda']
df.make.isin(makes)
filtered_df = df[df.make.isin(makes)]

cleaned_df = filtered_df[[
    'price', 'milage', 'model', 'make', 'transmission', 'fuel', 'Num_Cyl', 'year', 'body_style']]


cleaned_df.head(10)
#cleaned_df.to_csv ('cleaned_df.csv', index = False, header=True)

cleaned_df.info()


# ###  Created a Dataset X (Indipended Variables) and y (Depended Variable) set for Modeling Linear Regression 

# In[147]:


sklearn_df=pd.get_dummies(cleaned_df, columns=[ 'model', 'make', 'transmission', 'fuel', 'body_style'],drop_first=True)
sklearn_df.head()
df_sk_y=sklearn_df['price'].div(1.8)
df_sk_x=sklearn_df.iloc[:,1:]


X_train, X_test, y_train, y_test = model_selection.train_test_split(df_sk_x, df_sk_y, test_size=0.3)


from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score

gbr = GradientBoostingRegressor(loss ='ls', max_depth=6)
gbr.fit (X_train, y_train)
gbr.score(X_train,y_train)

gbr.score(X_test,y_test)


from sklearn.externals import joblib

joblib.dump(gbr, 'model.pkl')





