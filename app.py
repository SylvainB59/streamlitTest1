import streamlit as st
import pandas as pd


dataset = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv'

df = pd.read_csv(dataset)

a=df['pickup_borough'].unique()
# b=df['dropoff_borough'].unique()

# st.write(a)
# st.write(b)
# st.dataframe(df)

st.title('Bienvenue sur le 1er test streamlit de SYL')

choix_r = st.selectbox('Indiquez votre arrondissement de récupération',
             a)

st.write('Tu as choisis: ', choix_r)

img = f'./images/{str(choix_r).lower()}.jpg'
st.image(img)