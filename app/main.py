import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data(country):
    path = f"data/{country}_clean.csv"
    return pd.read_csv(path, parse_dates=["Timestamp"])

st.title("🌞 Solar Dataset Dashboard")
country = st.selectbox("Select a Country", ["benin", "togo", "sierraleone"])
df = load_data(country)

st.subheader(f"{country.capitalize()} - GHI Boxplot")
fig, ax = plt.subplots()
sns.boxplot(y=df["GHI"], ax=ax)
st.pyplot(fig)

if "Region" in df.columns:
    top_regions = df.groupby("Region")["GHI"].mean().sort_values(ascending=False).head(5)
    st.write("Top 5 Regions by Avg GHI")
    st.dataframe(top_regions)

if st.checkbox("Show Summary Stats"):
    st.dataframe(df.describe())
