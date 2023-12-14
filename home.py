import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import os, sys

sns.set()
sns.set_style('whitegrid')

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
df = pd.read_excel(os.path.join(dirname, 'data_source.xlsx'))

fig, axs = plt.subplots()
sns.boxplot(x = 'Datum', y = 'Menge', data=df, orient='v')

st.pyplot(fig)