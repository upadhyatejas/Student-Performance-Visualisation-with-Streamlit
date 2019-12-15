import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
df.drop(['parental level of education','lunch','test preparation course'], axis =1, inplace = True)


#show dataframe in sidebar
st.sidebar.subheader("Dataframe")
if st.sidebar.checkbox('click to show dataframe'):
    st.write(df)    

#create a scatter plot on test scores and colour based on gender
st.sidebar.subheader('scatter plot')
col2 = st.sidebar.selectbox('Which feature on y ?', df.columns[2:])
col = st.sidebar.selectbox("which legend scheme on graph ? ", ['Bloom level', 'gender'])

#create figure using plotly express
fig = px.scatter(df, x = range(0, 1000), y = col2, color = col)
fig0 = px.scatter_3d(df, x = df['java score'], y = df['python score'], z = df['DS score'], color = col)
#plot
st.plotly_chart(fig)
st.plotly_chart(fig0)

# create histogram
st.sidebar.subheader('histogram')
feature = st.sidebar.selectbox('which feature ? ', df.columns[2:])
col1 = st.sidebar.selectbox("which feature to merge,", ['gender', 'Bloom level'])
fig2 = px.histogram(df, x = feature, marginal = 'rug', color = col1)
st.plotly_chart(fig2)

