import streamlit as st
import pandas as pd
import numpy as np
import time

# =========================================================================
# 1. KONFIGURASI HALAMAN & TEMA
# =========================================================================
st.set_page_config(
    page_title="BantenEdu-AI Ultimate",
    page_icon="🚀",
    layout="wide"
)

# Kustomisasi CSS untuk tampilan modern
st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: 800; color: #0F172A; text-align: center; }
    .sub-title { font-size:18px !important; text-align: center; color: #64748B; margin-bottom: 30px; }
    .card { padding: 20px; border-radius: 12px; background-color: #F8FAFC; border: 1px solid #E2E8F0; }
    .footer { text-align: center; font-size: 14px; color: #94A3B8; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 BantenEdu-AI Ultimate</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ekosistem Belajar Cerdas Terintegrasi AI, Visualisasi, dan Analitik Data</div>', unsafe_allow_html=True)
st.markdown("---")

# =========================================================================
# 2. NAVIGASI SIDEBAR
# =========================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8676/8676496.png", width=80)
    st.title("Menu Utama")
    menu = st.radio(
        "Pilih Modul Pembelajaran:",
        ["🤖 AI Tutor Edukasi", "🎨 AI Visual Generator", "📊 Dasbor Persentase & GESI"]
    )
    st.markdown("---")
    st.success("✅ Modul Inklusi Sosial\n\n✅ Visualisasi Kearifan Lokal\n\n✅ Analitik Berbasis Data")

# =========================================================================
# 3. MODUL 1: AI TUTOR EDUKASI (BELAJAR INTERAKTIF)
# =========================================================================
if menu == "🤖 AI Tutor Edukasi":
    st.header("🤖 Asisten Belajar Mandiri (AI Tutor)")
    st.write("Sistem cerdas yang membantu siswa merangkum dan menjelaskan konsep pelajaran yang sulit.")

    topik = st.selectbox("Pilih Topik Pembelajaran:", [
        "Sejarah Kesultanan Banten", 
        "Logika Pemrograman Dasar", 
        "Ekonomi Maritim & Pelabuhan"
    ])
    
    pertanyaan = st.text_area("Apa yang ingin kamu pelajari hari ini?", placeholder="Contoh: Tolong jelaskan bagaimana algoritma bekerja dengan bahasa yang sederhana...")

    if st.button("Tanya AI Tutor", type="primary"):
        if pertanyaan:
            with st.spinner("AI sedang memproses jawaban..."):
                time.sleep(2) # Simulasi waktu tunggu API
                st.success("✨ Jawaban Ditemukan!")
                
                # Simulasi balasan AI yang sudah diformat
                jawaban_ai = f"""
                **Memahami {topik}**
                
                Pertanyaan yang sangat bagus! Berikut adalah penjelasan sederhananya:
                * **Konsep Utama:** Dalam konteks ini, semuanya dimulai dari perencanaan yang terstruktur. Seperti halnya membangun sesuatu di dunia nyata, kita butuh fondasi.
                * **Contoh Lokal:** Bayangkan seperti sistem navigasi kapal di Pelabuhan Merak; semuanya harus diatur langkah demi langkah agar tidak terjadi tabrakan. Itulah yang disebut dengan algoritma atau logika terstruktur.
                
                *Apakah penjelasan ini sudah cukup jelas, atau ada bagian yang ingin diperdalam?*
                """
                st.markdown(f"<div class='card'>{jawaban_ai}</div>", unsafe_allow_html=True)
        else:
            st.warning("Silakan tulis pertanyaanmu terlebih dahulu.")

# =========================================================================
# 4. MODUL 2: AI VISUAL GENERATOR (HASIL BUAT GAMBAR)
# =========================================================================
elif menu == "🎨 AI Visual Generator":
    st.header("🎨 AI Generator Gambar Pembelajaran")
    st.write("Ubah teks atau konsep sejarah menjadi gambar ilustrasi untuk memudahkan siswa visual memahami konteks.")

    prompt = st.text_input("Deskripsikan gambar yang ingin dibuat:", placeholder="Contoh: Suasana pelabuhan tradisional Banten di pagi hari dengan kapal layar...")
    gaya_gambar = st.selectbox("Gaya Ilustrasi:", ["Realistis", "Animasi 3D", "Sketsa Pensil"])

    if st.button("Buat Gambar dengan AI", type="primary"):
        if prompt:
            with st.spinner(f"Melukis '{prompt}' dengan gaya {gaya_gambar}..."):
                time.sleep(3) # Simulasi render gambar
                
                # Menggunakan placeholder gambar acak dari Unsplash yang relevan
                st.image("https://images.unsplash.com/photo-1596395819057-cbcf91286c8d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
                         caption=f"Hasil Generasi AI: {prompt} ({gaya_gambar})", use_column_width=True)
                
                st.success("Gambar berhasil dibuat! Ilustrasi ini dapat langsung diunduh dan disematkan ke dalam presentasi siswa.")
        else:
            st.warning("Masukkan deskripsi gambar terlebih dahulu.")

# =========================================================================
# 5. MODUL 3: DASBOR PERSENTASE & ANALITIK (GESI)
# =========================================================================
elif menu == "📊 Dasbor Persentase & GESI":
    st.header("📊 Dasbor Analitik & Persentase Progres")
    st.write("Pemantauan persentase kelulusan, inklusi gender, dan kecepatan belajar siswa.")

    # Membuat Data Simulasi
    df_metrik = pd.DataFrame({
        "Kategori": ["Siswa Laki-laki", "Siswa Perempuan", "Siswa Disabilitas"],
        "Target (%)": [100, 100, 100],
        "Pencapaian (%)": [85, 92, 78]
    })

    st.subheader("1. Persentase Keterlibatan & Kelulusan (Aspek GESI)")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Keterlibatan Perempuan", "52%", "+5% dari bulan lalu")
    col2.metric("Aksesibilitas SKh", "78%", "Target: 80%")
    col3.metric("Rata-rata Nilai Kelas", "86.5", "Sangat Baik")

    st.markdown("---")
    st.subheader("2. Progres Pemahaman Modul (Live Track)")
    
    # Progress bars untuk visualisasi persentase
    st.write("**Modul 1: Literasi Digital**")
    st.progress(90, text="90% Selesai")
    
    st.write("**Modul 2: Pengembangan Web Dasar**")
    st.progress(65, text="65% Selesai")
    
    st.write("**Modul 3: Rekayasa Data & AI**")
    st.progress(30, text="30% Selesai")

    st.markdown("---")
    st.subheader("3. Grafik Komparasi Nilai Siswa")
    
    # Visualisasi Bar Chart menggunakan st.bar_chart
    chart_data = pd.DataFrame(
        np.random.randint(60, 100, size=(6, 3)),
        columns=['Bulan 1', 'Bulan 2', 'Bulan 3'],
        index=['Siswa A', 'Siswa B', 'Siswi C', 'Siswi D', 'Siswa E (SKh)', 'Siswi F']
    )
    st.bar_chart(chart_data)

# =========================================================================
# FOOTER
# =========================================================================
st.markdown('<div class="footer">Dikembangkan oleh Tim Riset PT. Boyang Digital Nusantara - Banten Cerdas 2026</div>', unsafe_allow_html=True)
