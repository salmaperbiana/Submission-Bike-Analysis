# 🚲 Bike Sharing Data Analysis Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-4CAF50?style=for-the-badge)

## 👤 Informasi
Nama: Salma Perbiana  
Email: cdcc200d6x2466@student.devacademy.id  
ID Dicoding: CDCC200D6X2466  

## 🎯 Pertanyaan Bisnis
1. Seberapa besar perbedaan rata-rata jumlah penyewaan sepeda (cnt) antara kondisi cuaca buruk (weathersit ≥ 3) dan cuaca normal (weathersit < 3) pada data per jam selama tahun 2011–2012?
2. Pada jam berapa terjadi jumlah penyewaan tertinggi oleh pengguna registered pada hari kerja selama musim panas (summer) tahun 2011-2012?
3. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda antara pengguna casual dan registered pada akhir pekan (weekend) selama tahun 2011-2012?
4. Bagaimana hubungan antara suhu (temp) dan jumlah penyewaan sepeda (cnt) pada kondisi suhu rendah dan tinggi selama tahun 2011–2012?

## 📊 Dataset
- day.csv
- hour.csv

## 🎯 Tujuan
1. Menganalisis pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda
2. Mengidentifikasi pola waktu (jam) dengan tingkat penyewaan tertinggi oleh pengguna registered
3. Membandingkan perilaku penggunaan antara pengguna casual dan registered pada akhir pekan
4. Menganalisis hubungan antara suhu dan jumlah penyewaan sepeda

## 📁 Struktur Direktori

```bash
submission-bike-analysis/
├── dashboard/
│   ├── dashboard.py
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## ▶️ Cara Menjalankan

### 1. Instalasi Library
```bash
pip install -r requirements.txt
```

### 2. Menjalankan Dashboard
```bash
streamlit run dashboard/dashboard.py
```

atau

```bash
python -m streamlit run dashboard/dashboard.py
```
