#!/usr/bin/env python
# coding: utf-8

# In[7]:




# In[1]:


import pandas as pd
import streamlit as st

import plotly.express as px

import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
from plotly.subplots import make_subplots
import re
import time
import os
from PIL import Image
import PIL


# In[10]:




# In[8]:


#pip install streamlit


# In[3]:


data1 = pd.read_csv('Final_review.csv')
data2 = pd.read_csv('Inalsa_file.csv')


# In[4]:


# TODO: Change values below and observer the changes in your app
st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
    unsafe_allow_html=True,
)


header_container = st.beta_container()
stats_container = st.beta_container()


# In[7]:


st.title("Amazon Inalsa Airfryer Analysis")
st.header("Welcome!")
st.subheader("This is a Amazon Airfryer Reviews sentiment Analysis app")
st.write("Lets go")


option = st.sidebar.selectbox(
    'Please select an option',
    ('', 'Show Data', 'Ratings Distribution', 'Word Cloud', 'Reviews Sentiment'))
st.write('Displaying the DataFrame/Dashboard you have selected above')
if option:
    st.success('Yay! 🎉')
    st.write('You selected:', option)

    if option == 'Show Data':
        st.table(data2.head(10))
    elif option == 'Ratings Distribution':
        data1_temp_rate = data1.groupby(['Rating'])[['name']].count()
        data1_temp_rate.reset_index(inplace=True)

        st.header("Rating Distribution Percentage")
        fig_pie = px.pie(data1_temp_rate, values='name',
                         names='Rating', title='Rating Distribution')
        st.plotly_chart(fig_pie)
        st.header("Rating Distribution")
        df = data1.groupby(by=["Rating"]).size().reset_index(name="counts")
        fig = px.bar(data_frame=df, x="Rating", y="counts",
                     barmode="group", color='Rating')

        st.plotly_chart(fig)

    elif option == 'Word Cloud':
        def wordcloud(cleaned_reviews):

            wordcloud_words = " ".join(cleaned_reviews)
            wordcloud = WordCloud(
                height=300, width=500, background_color="black", random_state=100,
            ).generate(wordcloud_words)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.savefig("cloud.jpg")
            img = Image.open("cloud.jpg")
            return img

        st.header('WordCloud')
        img = wordcloud(data1["Reviews"])
        st.image(img)

    elif option == 'Reviews Sentiment':
        st.header("Reviews Sentiment")
        df1 = data1.groupby(by=["vader_labels"]).size(
        ).reset_index(name="Sentiment score")
        fig1 = px.bar(data_frame=df1, x="vader_labels",
                      y="Sentiment score", barmode="group", color='vader_labels')

        st.plotly_chart(fig1)


else:
    st.warning('No option is selected')





