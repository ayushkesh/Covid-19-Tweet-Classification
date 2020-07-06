# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:37:09 2020

@author: Ayush
"""
# covid 19 tweets
import streamlit as st
import pickle
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from PIL import Image
import re


def main():
    
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:black;text-align:center;">Covid-19 Related Tweets Classification System</h2>
    </div>
    """
    
    st.markdown(html_temp , unsafe_allow_html= True)
    image = Image.open('h1.jpeg')
    st.image(image, use_column_width=True,format='PNG')
    
    
    ps = PorterStemmer()
    model = pickle.load(open('covid.pkl', 'rb'))
    vec = pickle.load(open('vec.pkl', 'rb'))     
    def clean_text(text):
        text = re.sub(pattern='[^a-zA-Z]', repl=' ', string=text)
        text = text.lower()
        #text = text.split()
        #words = [word for word in words if word not in set(stopwords.words('english'))]
        #words = [ps.stem(word) for word in words]
        #text = ' '.join(text)
        return text

    st.markdown("<body style = 'background-color: white;'><h3 style = 'text-align: center; color :black;'> Enter the text to know weather Tweet is Covid-19 Related or Not </h3></body>", unsafe_allow_html = True)
    text = st.text_input(" ", ' ')
    text = clean_text(text)
    
    if st.button('Predict'):
        text_vec = vec.transform([text])
        pred= model.predict(text_vec)
       
        if pred== 0:
            st.error('Not Covid-19 Related Tweets')
        else:
            st.info('Hey!!  This Tweet is Related to Covid-19')
            st.balloons()
    #st.success('{}'.format(pred))
    if st.button("Lets Get in Touch"):
        st.text("Stay Home 💦 Stay Safe.")
        st.text("Github link: https://github.com/ayushkesh/Covid-19-Tweet-Classification")         
         
    html_temp1 = """
    <div style="background-color:blue">
    <p style="color:white;text-align:center;"><b>Made with ❤️ by Ayush Kumar</b> </p>
    </div>
    """
    st.markdown(html_temp1,unsafe_allow_html=True)    
    
if __name__ =='__main__':
    main()
       
    
      