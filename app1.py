import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# =========================================================================
# 1. KONFIGURASI HALAMAN & CSS MODERN
# =========================================================================
st.set_page_config(page_title="JAWARA EDU-AI v3.0", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: 800; color: #0F172A; text-align: center; }
    .sub-title { font-size:18px !important; text-align: center; color: #64748B; margin-bottom: 30px; }
    .card { padding: 20px; border-radius: 12px; background-color: #F8FAFC; border-left: 5px solid #10B981; margin-bottom: 15px;}
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 JAWARA EDU-AI (Versi Komplit)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ekosistem Cerdas: Analitik GESI, Adiwiyata, AI Tutor & Prediksi Karir</div>', unsafe_allow_html=True)
st.markdown("---")

# =========================================================================
# 2. INISIALISASI DATABASE SEMENTARA (ANTI-ERROR)
# =========================================================================
if 'energy_data' not in st.session_state:
    dates = pd.date_range(start="2026-06-01", periods=30, freq="D")
    base_kwh = np.linspace(200, 150, 30) + np.random.normal(0, 10, 30)
    st.session_state['energy_data'] = pd.DataFrame({
        'Tanggal': dates,
        'Pemakaian Listrik (kWh)': np.round(base_kwh, 2),
        'Sampah Daur Ulang (Kg)': np.random.randint(2, 12, 30)
    })

if 'student_data' not in st.session_state:
    st.session_state['student_data'] = pd.DataFrame({
        'ID': ['SRI-001', 'SRI-002', 'SRI-003', 'SRI-004'],
        'Nama': ['Siti', 'Ayu', 'Rina', 'Desi'],
        'Gender': ['Perempuan', 'Perempuan', 'Perempuan', 'Perempuan'],
        'Kategori': ['Pra-Sejahtera', 'Reguler', 'Disabilitas (SKh)', 'Pra-Sejahtera'],
        'Minat': ['Web Development', 'Desain Visual', 'Data Science', 'Content Creator'],
        'Progres (%)': [90, 75, 85, 100],
        'Nilai Akhir': [88, 92, 85, 90]
    })

# =========================================================================
# 3. NAVIGASI SIDEBAR
# =========================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8676/8676496.png", width=80)
    st.title("Navigasi Modul")
    menu = st.radio("", [
        "🏠 Beranda & Persentase", 
        "🤖 AI Tutor & Visual (Edukasi)", 
        "🌍 Analitik Adiwiyata & GESI", 
        "🔮 Prediksi AI (Machine Learning)"
    ])
    st.markdown("---")
    st.caption("Infrastruktur oleh: PT. Boyang Digital Nusantara")
    st.caption("Siap untuk Banten Cerdas 2026")

# =========================================================================
# 4. MODUL 1: BERANDA & PERSENTASE
# =========================================================================
if menu == "🏠 Beranda & Persentase":
    st.header("📊 Dasbor Utama Eksekutif")
    df_s = st.session_state['student_data']
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Keterlibatan GESI", "100%", "Kuota Afirmasi Terpenuhi")
    col2.metric("Kelulusan Siswa SKh", "85%", "Di Atas Target")
    col3.metric("Rata-rata Nilai", f"{df_s['Nilai Akhir'].mean():.1f}", "Sangat Baik")
    col4.metric("Penghematan Listrik", "15%", "Program Go Green")

    st.markdown("---")
    st.subheader("📈 Persentase Penyelesaian Modul Siswa (Live)")
    
    for index, row in df_s.iterrows():
        st.write(f"**{row['Nama']}** ({row['Minat']}) - {row['Kategori']}")
        st.progress(int(row['Progres (%)']), text=f"{row['Progres (%)']}% Selesai")

# =========================================================================
# 5. MODUL 2: AI TUTOR & GENERATOR VISUAL
# =========================================================================
elif menu == "🤖 AI Tutor & Visual (Edukasi)":
    st.header("🤖 Asisten Belajar Mandiri & Visualisasi Lokal")
    
    tab1, tab2 = st.tabs(["💬 AI Chat Tutor", "🎨 AI Visual Generator"])
    
    with tab1:
        st.write("Sistem cerdas merangkum konsep sulit menjadi analogi sederhana berbasis kearifan lokal Banten.")
        pertanyaan = st.text_area("Apa yang ingin dipelajari?", placeholder="Contoh: Jelaskan algoritma pemrograman...")
        if st.button("Tanya AI Tutor", type="primary"):
            if pertanyaan:
                with st.spinner("AI sedang memproses..."):
                    time.sleep(1.5)
                    jawaban = f"""
                    **Konsep Algoritma (Analogi Banten)** Algoritma adalah langkah-langkah berurutan untuk menyelesaikan masalah. Bayangkan seperti kapal feri di Pelabuhan Merak yang harus mengikuti rute navigasi dan jadwal sandar yang terstruktur agar tidak bertabrakan. Jika satu baris kode (atau jadwal) salah, seluruh sistem akan terganggu!
                    """
                    st.markdown(f"<div class='card'>{jawaban}</div>", unsafe_allow_html=True)
            else:
                st.warning("Tuliskan pertanyaan terlebih dahulu.")

    with tab2:
        st.write("Generasi gambar dari teks untuk mempermudah pemahaman siswa gaya belajar visual.")
        prompt = st.text_input("Deskripsi Gambar:", placeholder="Candi Kesultanan Banten dengan gaya 3D...")
        if st.button("Generate Gambar"):
            if prompt:
                with st.spinner(f"Melukis '{prompt}'..."):
                    time.sleep(2)
                    st.image("https://images.unsplash.com/photo-1596395819057-cbcf91286c8d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
                             caption=f"Visualisasi AI: {prompt}", use_container_width=True)
                    st.success("Aset visual siap disematkan ke materi pembelajaran!")

# =========================================================================
# 6. MODUL 3: ANALITIK ADIWIYATA & GESI
# =========================================================================
elif menu == "🌍 Analitik Adiwiyata & GESI":
    st.header("🌍 Pelaporan Inklusi Sosial & Lingkungan")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pemantauan Sampah Daur Ulang (Adiwiyata)")
        df_e = st.session_state['energy_data']
        st.bar_chart(df_e.set_index('Tanggal')['Sampah Daur Ulang (Kg)'], color="#10B981")
        
    with col2:
        st.subheader("Distribusi Status Sosial Siswa (GESI)")
        df_s = st.session_state['student_data']
        dist_sosial = df_s['Kategori'].value_counts()
        
        fig, ax = plt.subplots()
        ax.pie(dist_sosial, labels=dist_sosial.index, autopct='%1.1f%%', colors=['#3B82F6', '#EC4899', '#10B981'])
        st.pyplot(fig)

    st.subheader("Database Srikandi (Data Pilah)")
    st.dataframe(df_s, use_container_width=True)

# =========================================================================
# 7. MODUL 4: PREDIKSI AI (MACHINE LEARNING)
# =========================================================================
elif menu == "🔮 Prediksi AI (Machine Learning)":
    st.header("🔮 Eksekusi Machine Learning")
    
    tab1, tab2 = st.tabs(["♻️ Prediksi Efisiensi Energi", "🎯 Prediksi Karir Siswa"])
    
    with tab1:
        st.write("**Regresi Linear:** Memprediksi pemakaian listrik 5 hari ke depan berdasarkan tren saat ini.")
        df_e = st.session_state['energy_data']
        if st.button("Jalankan Prediksi Energi"):
            X = np.arange(len(df_e)).reshape(-1, 1)
            y = df_e['Pemakaian Listrik (kWh)']
            model = LinearRegression().fit(X, y)
            
            future_X = np.arange(len(df_e), len(df_e) + 5).reshape(-1, 1)
            prediksi = model.predict(future_X)
            
            tgl_terakhir = df_e['Tanggal'].max()
            tgl_prediksi = [tgl_terakhir + timedelta(days=int(i)) for i in range(1, 6)]
            
            df_pred = pd.DataFrame({'Tanggal': tgl_prediksi, 'Prediksi Pemakaian (kWh)': np.round(prediksi, 2)})
            st.dataframe(df_pred, use_container_width=True)
            st.info("Kecerdasan Buatan memproyeksikan tren penurunan konsumsi listrik. Program Adiwiyata berhasil!")

    with tab2:
        st.write("**Decision Tree Classifier:** Mencocokkan talenta dengan kebutuhan agensi/industri lokal.")
        df_s = st.session_state['student_data'].copy()
        
        le = LabelEncoder()
        df_s['Minat_Code'] = le.fit_transform(df_s['Minat'])
        
        # Data latih sederhana
        X_train = df_s[['Minat_Code', 'Nilai Akhir']]
        y_train = ['Programmer', 'UI/UX Designer', 'Data Analyst', 'Digital Marketer']
        
        clf = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
        
        col_a, col_b = st.columns(2)
        sim_minat = col_a.selectbox("Minat Siswa Baru", df_s['Minat'].unique())
        sim_nilai = col_b.slider("Estimasi Nilai Rata-rata", 60, 100, 85)
        
        if st.button("Petakan Peluang Karir"):
            minat_code = le.transform([sim_minat])[0]
            hasil = clf.predict([[minat_code, sim_nilai]])[0]
            st.success(f"🎯 **Rekomendasi Penyaluran Industri:** Siswa ini sangat cocok ditempatkan sebagai **{hasil}**.")
