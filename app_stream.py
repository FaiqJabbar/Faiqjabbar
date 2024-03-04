import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with st.sidebar:
    st.image("faiq.jpg")
    st.text('Muhammad Faiq Jabbar')
    st.text('ML-50')
    st.text('Telkom University')

# Membaca file CSV
merged_df = pd.read_csv('merged_data.csv')

# Judul Dashboard
st.title('Bike Sharing Analysis Dashboard')

# Deskripsi Data
st.write('## Deskripsi dataset:')
st.write(
    """Proses peminjaman sepeda terkait erat dengan kondisi lingkungan dan musiman. Misalnya,
    kondisi cuaca, curah hujan, hari dalam seminggu, musim, jam dalam sehari, dll. 
    dapat memengaruhi perilaku peminjaman. Kumpulan data inti terkait dengan log historis 
    dua tahun yang sesuai dengan tahun 2011 dan 2012 dari sistem Capital Bikeshare, 
    Washington D.C., AS yang tersedia secara publik di http://capitalbikeshare.com/system-data. 
    Kami menggabungkan data dalam interval dua jam dan harian dan kemudian mengekstraksi serta menambahkan 
    informasi cuaca dan musiman yang sesuai. Informasi cuaca diekstraksi dari http://www.freemeteo.com.

    """
)
st.write(merged_df.describe())

# Visualisasi Data
st.write('## Visualisasi Data')

# Visualisasi 1: Total Peminjaman Sepeda per Bulan
monthly_rentals = merged_df.groupby(merged_df['dteday'].str.slice(0, 7))['cnt'].sum()
st.line_chart(monthly_rentals)
with st.expander("See explanation"):
    st.write(
        """Dapat dilihat pada Visualisasi Data Peminjaman Sepeda per Bulan,
        dapat di ketahui bahwa terjadi peningkatan peminjaman sepeda pada setiap bulan maret-april. 
        Tetapi, terdapat penurunan peminjaman sepeda pada bulan oktober menuju ke januari, 
        ini mungkin dikarenakan tahun baru atau natal yang mengakibatkan pengguna sepeda tidak 
        menggunakan peminjaman sepeda.
        """
    )


# Visualisasi 2: Distribusi Peminjaman Sepeda berdasarkan Kondisi Cuaca
# Membuat box plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=merged_df, ax=ax)
ax.set_title('Peminjaman Sepeda berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(ticks=[0, 1, 2, 3])
ax.set_xticklabels(labels=['Clear', 'Mist', 'Light Snow', 'Heavy Rain'], rotation=45)
ax.grid(True)
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)
with st.expander("See explanation"):
    st.write(
        """Dari box plot Peminjaman Sepeda berdasarkan Kondisi Cuaca, 
        dapat di simpulkan bahwa cuaca sangat berpengaruh terhadap jumlah 
        peminjaman sepeda. Ketika cuaca cerah (Clear), banyak orang yang menggunakan 
        peminjaman sepeda. Sedangkan pada cuaca hujan deras (Heavy Rain), dikit sekali 
        orang yang menggunakan peminjaman sepeda.
        """
    )
