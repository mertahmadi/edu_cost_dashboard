import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('international.csv')
df['Total_Cost_USD'] = (
    df['Tuition_USD'] +
    (df['Rent_USD'] + df['Insurance_USD']) * df['Duration_Years'] +
    df['Visa_Fee_USD']
)

st.title("🌍 International Education Cost Explorer")

country = st.selectbox("Select Country", df['Country'].unique())
filtered_df = df[df['Country'] == country]

fig = px.bar(filtered_df, x='University', y='Total_Cost_USD', color='Program',
             title=f'Total Cost in {country}')
st.plotly_chart(fig)

st.write("Data Preview", filtered_df.head())
