import streamlit as st
# from PIL import Image
# import cv2 
import pandas as pd
import numpy as np
import os
import random

    
        
def show_heatmap():
	import plotly.express as px

	df = px.data.gapminder().query("year==2007")
	fig = px.choropleth(df, locations="iso_alpha",
	                    color="lifeExp", # lifeExp is a column of gapminder
	                    hover_name="country", # column to add to hover information
	                    color_continuous_scale=px.colors.sequential.Plasma)
	fig.update_layout(
    title_text='Film industry all over the world ')
	st.plotly_chart(fig)

        
    
def load_image(image_path,title='',subheader='',width=100):
    
    st.title(title)  
    st.subheader(subheader)
    print(image_path)
    st.image(image_path,width)

def app():
    # try:

    # user_id = int(st.sidebar.text_input("User ID: "))

    # user_id = 0
    # rec_num = int(st.sidebar.number_input("How many friends do you want: "))
    selected_box = st.sidebar.selectbox(
    'Which type are you interested in?',
    ('Movie','TV show')
    )

    show_heatmap()

    load_image('/Users/luocan/class/2021spring/big_data/final-project/app/actor_net.png',
        title='Actor network',subheader='',
        width = 800)








if __name__ == "__main__":
    app()