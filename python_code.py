import streamlit as st
import pandas as pd

st.write("Streatlit example of dataframe")

df_deduct_fact = pd.read_excel (r"C:\Users\AZA97096\OneDrive - Mott MacDonald\Documents\Project Docs\Mississippi DOT-PMS\Distress Data\deduct_factors.xlsx")

st.dataframe(df_deduct_fact)
