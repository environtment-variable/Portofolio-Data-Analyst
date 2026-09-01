import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Superstore", layout="wide")
st.title("📊 Dashboard Analisis Penjualan Superstore")

# Load data
df = pd.read_csv('/home/roboto/Downloads/superstore_data/train.csv')
df = df.drop_duplicates().fillna(0)

# Sidebar Filter
st.sidebar.header("Filter")
region_filter = st.sidebar.multiselect("Pilih Region", options=df['Region'].unique(), default=df['Region'].unique())
df_filtered = df[df['Region'].isin(region_filter)]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df_filtered['Sales'].sum():,.2f}")
col2.metric("Rata-rata Transaksi", f"${df_filtered['Sales'].mean():,.2f}")
col3.metric("Jumlah Transaksi", f"{len(df_filtered):,}")

# Grafik 1: Sales per Region
st.subheader("Penjualan per Region")
fig1, ax1 = plt.subplots()
sns.barplot(x=df_filtered.groupby('Region')['Sales'].sum().index, 
            y=df_filtered.groupby('Region')['Sales'].sum().values, ax=ax1)
st.pyplot(fig1)

# Grafik 2: Top Products
st.subheader("Top 10 Produk")
top_prod = df_filtered.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_prod.index, x=top_prod.values, ax=ax2)
st.pyplot(fig2)