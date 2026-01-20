import streamlit as st 
import pandas as pd 
import numpy as np 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.compose import ColumnTransformer 
from sklearn.ensemble import RandomForestClassifier 
import unicodedata 
 
st.set_page_config(page_title='Triagem Inteligente - PC Brasília', layout='centered') 
 
st.title('Triagem Inteligente – PC Brasília (Demo)') 
st.caption('Modelo didático com Machine Learning + Mini-RAG') 
