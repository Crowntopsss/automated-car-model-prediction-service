
import re
import pandas as pd
import matplotlib.pyplot
import collections
from collections import Counter
import numpy as np
import seaborn as sns
import patsy
#get_ipython().run_line_magic('pylab', 'inline')


# #### Import the file as DataFrame(df) 


df=pd.read_csv('data/Step3_input_raw_data.csv')

#Remove Unwanted Columns:
df2=df.iloc[:,2:]
#df2.head()
#Rearrange-cols
df3= df2[[ 'vin', 'price',
 'body_style',
 'drive_type',
 'engine',
 'ext_color',
 'fuel',
 'int_color',
 'location',
 'make',
 'milage',
 'model',
 'mpg_city_highway',
 'stock',
 'transmission',
 'year',
 'Region']]



df4 = pd.DataFrame(df3.location.str.split(',',).tolist(),
                                   columns = ['City','State'])


df4a = pd.DataFrame(df3.engine.str.split('Cyl',).tolist(),
                                   columns = ['Num_Cyl','Cyl_Volume'])


df5 = pd.concat([df4, df3,df4a], axis=1)
df5['price']=df5['price'].str.replace(',',"")
df5['price']=df5['price'].str.replace('$',"")
df5['Cyl_Volume']=df5['Cyl_Volume'].str.replace('L',"")
df6 = pd.DataFrame(df3.mpg_city_highway.str.split('/',).tolist(),
                                   columns = ['City_MPG','Highway_MPG'])
df7= pd.concat([df6, df5], axis=1)
df7['year']=df7['year'].str.replace(':',"")
df7['year']=df7['year'].str.replace(',',"")
df7['year']=df7['year'].str.replace(',',"")

df7['milage']=df7['milage'].str.replace('miles',"")
df7['milage']=df7['milage'].str.replace(',',"")
df7['engine']=df7['engine'].str.split('Cyl')
df8=df7.dropna()


#remove items without price
df9=df8[df8['price']!='CallforPrice']
df10=df9[df9['price']!='RequestQuote']


# ### Assign Variables to it's correct TYPE

df10[['price', 'City_MPG','milage','Highway_MPG','year']] = df10[['price', 'City_MPG','milage','Highway_MPG','year']].astype(int)



#Cleaned Data TO ANALYZE!
Cleaned_data =df10[['price','milage','Highway_MPG','make', 'body_style','fuel', 'State','ext_color','int_color','Region','Num_Cyl','Cyl_Volume','year']]
#df10['make'].value_counts()
df10.to_csv('data/Step3_output_clean_df.csv')



