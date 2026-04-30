import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

# =========================
# LOAD DATA
# =========================
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.title("Filter Data")

year_filter = st.sidebar.selectbox("Pilih Tahun", [2011, 2012, "All"])

# =========================
# APPLY FILTER
# =========================
filtered_day = day_df.copy()
filtered_hour = hour_df.copy()

if year_filter != "All":
    year_code = year_filter - 2011
    filtered_day = filtered_day[filtered_day['yr'] == year_code]
    filtered_hour = filtered_hour[filtered_hour['yr'] == year_code]

# =========================
# HEADER
# =========================
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis Penyewaan Sepeda 2011–2012")

# =========================
# KPI (BIAR KEREN ⭐)
# =========================
st.subheader("📊 Ringkasan Data")

col1, col2, col3 = st.columns(3)

with col1:
    total_rentals = filtered_hour['cnt'].sum()
    st.metric("Total Rentals", total_rentals)

with col2:
    avg_rentals = round(filtered_hour['cnt'].mean(), 2)
    st.metric("Rata-rata Rentals", avg_rentals)

with col3:
    max_rentals = filtered_hour['cnt'].max()
    st.metric("Max Rentals", max_rentals)

# =========================
# Q1 - CUACA
# =========================
st.subheader("1. Pengaruh Cuaca terhadap Penyewaan")

weather_df = filtered_hour.copy()
weather_df['weather_group'] = weather_df['weathersit'].apply(
    lambda x: 'Bad Weather' if x >= 3 else 'Normal Weather'
)

weather_plot = weather_df.groupby('weather_group')['cnt'].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=weather_plot, x='weather_group', y='cnt', ax=ax)
ax.set_title("Cuaca vs Penyewaan")
st.pyplot(fig)

# =========================
# Q2 - JAM PUNCAK
# =========================
st.subheader("2. Jam Puncak Pengguna Registered")

hour_plot = filtered_hour.groupby('hr')['registered'].mean().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=hour_plot, x='hr', y='registered', ax=ax)
ax.set_title("Pola Registered per Jam")
ax.set_xticks(range(0,24))
st.pyplot(fig)

# =========================
# Q3 - WEEKEND (PAKAI DAY)
# =========================
st.subheader("3. Casual vs Registered (Weekend)")

weekend = filtered_day[filtered_day['workingday'] == 0]

user_plot = weekend[['casual','registered']].mean().reset_index()
user_plot.columns = ['user_type','avg_rentals']

fig, ax = plt.subplots()
sns.barplot(data=user_plot, x='user_type', y='avg_rentals', ax=ax)
ax.set_title("Weekend Usage Comparison")
st.pyplot(fig)

# =========================
# Q4 - SUHU
# =========================
st.subheader("4. Pengaruh Suhu terhadap Penyewaan")

temp_df = filtered_hour.copy()
temp_df['temp_group'] = temp_df['temp'].apply(
    lambda x: 'High Temp' if x >= 0.5 else 'Low Temp'
)

temp_plot = temp_df.groupby('temp_group')['cnt'].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=temp_plot, x='temp_group', y='cnt', ax=ax)
ax.set_title("Suhu vs Penyewaan")
st.pyplot(fig)

# =========================
# TAMBAHAN (BIAR NILAI NAIK ⭐)
# =========================
st.subheader("📈 Tren Penyewaan Harian")

daily_trend = filtered_day[['dteday','cnt']]

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(daily_trend['dteday'], daily_trend['cnt'])
ax.set_title("Tren Penyewaan Harian")
st.pyplot(fig)

# =========================
# FOOTER
# =========================
st.caption("Bike Sharing Dashboard - Salma Perbiana 🚲")
