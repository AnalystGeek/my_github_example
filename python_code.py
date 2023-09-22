import streamlit as st
import pandas as pd
from io import StringIO

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
st.write(spectra_df)
