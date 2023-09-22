import streamlit as st
import pandas as pd
import numpy as np

st.write("Streatlit example of dataframe")
##df = pd.read_excel (".master/deduct_factors.xlsx")
##df = pd.DataFrame(
  ## np.random.randn(50, 20),
   ## columns=('col %d' % i for i in range(20)))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  ##st.write(df)
  
st.dataframe(df)
