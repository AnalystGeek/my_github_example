import streamlit as st
import pandas as pd

st.write("Streatlit example of dataframe")

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)
