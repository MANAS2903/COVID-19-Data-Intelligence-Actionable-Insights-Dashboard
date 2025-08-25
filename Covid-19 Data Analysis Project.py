#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[9]:


covid_df=pd.read_csv("C:/Users/Asus/Downloads/covid_19_india.csv")


# In[10]:


covid_df.head(10)


# In[11]:


covid_df.info()


# In[12]:


covid_df.describe()


# In[14]:


vaccine_df=pd.read_csv("C:/Users/Asus/Downloads/covid_vaccine_statewise.csv")


# In[15]:


vaccine_df.head(7)


# In[20]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"] , inplace=True, axis =1)


# In[21]:


covid_df.head()


# In[30]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%Y-%m-%d')


# In[31]:


covid_df.head()


# In[40]:


covid_df['Active_Cases']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])
covid_df.tail(50)


# In[41]:


statewise = pd.pivot_table(covid_df,values=["Confirmed", "Deaths", "Cured"],
                    index ="State/UnionTerritory", aggfunc = max)


# In[42]:


statewise['Recovery Rate']= statewise["Cured"]*100/statewise["Confirmed"]


# In[43]:


statewise['Mortality Rate']= statewise["Deaths"]*100/statewise["Confirmed"]


# In[44]:


statewise=statewise.sort_values(by="Confirmed", ascending=False)


# In[45]:


statewise.style.background_gradient(cmap="cubehelix")


# In[51]:


top_10_active_cases=covid_df.groupby(by ='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()


# In[52]:


fig=plt.figure(figsize=(16,9))


# In[53]:


plt.title("Top 10 states with most active cases in India",size=25)


# In[57]:


ax = sns.barplot(data=top_10_active_cases.iloc[:10],y='Active_Cases',x='State/UnionTerritory',linewidth=2,edgecolor='red')


# In[59]:


top_10_active_cases=covid_df.groupby(by ='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active cases in India",size=25)
ax = sns.barplot(data=top_10_active_cases.iloc[:10],y='Active_Cases',x='State/UnionTerritory',linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[60]:


top_10_deaths=covid_df.groupby(by ='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 states with most Deaths",size=25)
ax = sns.barplot(data=top_10_deaths.iloc[:12],y='Deaths',x='State/UnionTerritory',linewidth=2,edgecolor='black')
plt.xlabel("States")
plt.ylabel("Total Deaths Cases")
plt.show()


# In[74]:


# Growth Trend
fig = plt.figure(figsize=(12,6))
ax = sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Uttar Pradesh'])],
                 x='Date', y='Active_Cases', hue='State/UnionTerritory')
ax.set_title("Top 5 Affected States in India", size=19)


# In[83]:


vaccine_df.rename(columns={'Updated On':'Vaccine_Date'},inplace=True)
vaccine_df.head()


# In[84]:


vaccine_df.info()


# In[85]:


vaccine_df.isnull().sum()


# In[90]:


vaccination=vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis =1)


# In[91]:


vaccination.head()


# In[93]:


#male vs female vaccination

male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination")


# In[94]:


vaccine=vaccine_df[vaccine_df.State!='India']


# In[95]:


vaccine


# In[96]:


vaccine.rename(columns={'Total Individuals Vaccinated':'Total'},inplace=True)
vaccine.head()


# In[102]:


#Most Vaccinated State

max_vac=vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac=max_vac.sort_values('Total',ascending=False)[:5]


# In[100]:


max_vac


# In[106]:


fig= plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India" ,size= 20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x= max_vac.index, linewidth=2,edgecolor='black')
plt.xlabel ( "States" )
plt.ylabel ("Vaccination")
plt.show()


# In[110]:


#least Vaccinated State

les_vac=vaccine.groupby('State')['Total'].sum().to_frame('Total')
les_vac=les_vac.sort_values('Total',ascending=True)[:5]


# In[113]:


fig= plt.figure(figsize=(10,5))
plt.title("Bottom 5 Vaccinated States in India" ,size= 20)
x=sns.barplot(data=les_vac.iloc[:10],y=les_vac.Total,x= les_vac.index, linewidth=2,edgecolor='black')
plt.xlabel ( "States" )
plt.ylabel ("Vaccination")
plt.show()


# In[ ]:




