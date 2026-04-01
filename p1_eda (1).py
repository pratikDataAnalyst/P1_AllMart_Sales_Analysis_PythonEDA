#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[ ]:


df=pd.read_csv(r'AllMart Sales Data.csv',encoding='unicode_escape')
##The r stands for "Raw String." In Windows, file paths use backslashes (\). Normally, Python thinks \ is a special command (like \n for a new line). The r tells Python: "Ignore the special meanings and just read the path exactly as it is written."
##encoding='unicode_escape'	This is the "Translator." Sometimes CSV files contain special characters (like symbols or non-English letters). This specific encoding helps Python read those characters without crashing.


# In[38]:


df.shape


# In[39]:


df.head(8)


# In[42]:


df.tail(4)


# In[40]:


df.info()


# In[41]:


pd.isnull(df) ##toFind NUll Data 


# In[43]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[44]:


df.info()


# In[45]:


pd.isnull(df)


# In[47]:


pd.isnull(df).sum()


# In[48]:


df.shape


# In[49]:


df.dropna(inplace=True)


# In[51]:


df.shape


# In[52]:


pd.isnull(df).sum()


# In[53]:


##Drop Null Values
df.dropna(inplace=True)


# In[56]:


data_test=[['madhav',11],['Gopi',15],['keshav',],['Lalita',18]]
df_test=pd.DataFrame(data_test,columns=['name','age'])
df_test


# In[57]:


df_test.dropna()


# In[61]:


df_test


# In[59]:


df_test.dropna(inplace=True)


# In[60]:


df_test


# In[62]:


##Change  data type
df['Amount']=df['Amount'].astype('int')


# In[63]:


df['Amount'].dtypes


# In[64]:


df.columns


# In[66]:


##To reName Column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[67]:


## describe() method returns description of the data in the Dataframe (i.e. count,mean,std,etc)
df.describe()


# In[68]:


##use  describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exporatory Data Analysis
# 

#  Gender
# 

# In[71]:


df.columns


# In[72]:


ax = sns.countplot(x='Gender',data=df)


# In[80]:


ax = sns.countplot( x = 'Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[82]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[83]:


sales_gen =df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x ='Gender',y='Amount',data= sales_gen)


# From above graphs we can see that most of the buyers are femels and even the purchasing power of femeles are greter than men
# 
#Age
# In[87]:


ax = sns.countplot(data=df,x='Age Group',hue='Gender')


# In[89]:


ax = sns.countplot(data=df,x='Age Group',hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[ ]:


# Total Amount Vs Age  Group 
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x= 'Age Group', y='Amount',data=sales_age)


# From the above graph we can see that most of the buyers are of age group between 26-35 yre females.

# ### State

# In[92]:


df.columns


# In[111]:


#Total numbers of orders from top 10 states
sales_State = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,6)})
sns.barplot(data=sales_State,x='State',y='Orders')


# In[112]:


#Total amount / sales from top 10 states
sales_State = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(data=sales_State,x='State',y='Amount')


# From above graphs we can see that most of the orders and total sales /amount are from uttar pradesh , maharashtra and karnataka respectively.

# ### Marital Status

# In[113]:


ax=sns.countplot(data=df,x='Marital_Status')
## if you dont give widht and hight it will give last graph width and height
for bars in ax.containers:
    ax.bar_label(bars)


# In[116]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x='Marital_Status',y='Amount',hue='Gender')


# From Above graph we can see that most of the buyers are married (womens) and they have high purchasing power

# ### Occupation 

# In[118]:


sns.set(rc={'figure.figsize':(18,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[119]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graph we can see th most of the working in IT,Healthcare and Aviation sector

# In[122]:


df.columns


# ### Product  category

# In[125]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[126]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[127]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[131]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion 

# ### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category.

# In[ ]:




