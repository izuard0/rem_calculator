import streamlit as st
import pandas as pd

# Data rubrik remunerasi berdasarkan SK 2025
remun_data = {
    'A. MENGAJAR': {
        'Mengajar pada Program Diploma 3/Sarjana Reguler Kelas Pagi': {'unit': 'Per Mahasiswa/SKS', 'nilai': 0.025},
        'Mengajar pada Program Magister': {'unit': 'Per SKS', 'nilai': 2},
        'Mengajar pada Program Doktor': {'unit': 'Per SKS', 'nilai': 3},
        'Mengajar pada Program Profesi': {'unit': 'Per Mahasiswa/SKS', 'nilai': 0.05},
        'Mengajar pada Program Diploma 3/Sarjana Kelas Internasional': {'unit': 'Per Mahasiswa/SKS', 'nilai': 0.05},
        'Mengajar pada Program Diploma 3/Sarjana Reguler Kelas Sore dan Malam': {'unit': 'Per Mahasiswa/SKS', 'nilai': 0.03},
    },
    'B. MEMBIMBING': {
        'Membimbing Tugas Akhir Diploma 3': 0.85,
        'Membimbing Skripsi': 0.85,
        'Membimbing Tesis (Pembimbing Utama)': 1.6,
        'Membimbing Tesis (Pembimbing Pendamping)': 1.35,
        'Membimbing Disertasi (Pembimbing Utama)': 4.6,
        'Membimbing Disertasi (Pembimbing Pendamping)': 3.7,
        'Membimbing Tugas Akhir Profesi': 0.85,
        'Membimbing PPL/Magang/Kerja Praktek/Kuliah Kerja Lapangan': 0.1,
        'Membimbing MBKM': 0.4,
        'Membimbing Akademik': 0.06,
    },
    'C. MENGUJI': {
        'Menguji Tugas Akhir D3': 0.15,
        'Menguji seminar proposal/seminar hasil skripsi': 0.15,
        'Menguji Skripsi': 0.15,
        'Menguji Tesis': 0.6,
        'Menguji Disertasi Ujian Tertutup': 1,
        'Menguji Disertasi Ujian Terbuka': 1,
    },
    'D. PENELITIAN': {
        'Ketua Penelitian': 1.8,
        'Anggota Penelitian (poin dibagi jumlah anggota)': 1.2,
    },
    'E. PENGABDIAN KEPADA MASYARAKAT': {
        'Ketua Pengabdian': 1,
        'Anggota Pengabdian (poin dibagi jumlah anggota)': 1,
    },
    'F. UNSUR PENUNJANG': {
        'Kegiatan Sidang Senat': 0.25,
        'Reviewer Penelitian dan PKM': 0.2,
        'Asesor BKD': 0.2,
        'Ketua/Wakil Ketua Kepanitiaan Kegiatan Adhoc': 0.6,
        'Sekretaris Kepanitiaan Kegiatan Adhoc': 0.45,
        'Anggota Kepanitiaan Kegiatan Adhoc': 0.45,
    },
     'G. PUBLIKASI': {
        'Publikasi Ilmiah Jurnal Internasional Q4': 26,
        'Publikasi Ilmiah Jurnal Internasional Q3': 37,
        'Publikasi Ilmiah Jurnal Internasional Q2': 41,
        'Publikasi Ilmiah Jurnal Internasional Q1': 45,
        'Publikasi Ilmiah Jurnal Nasional Terakreditasi S1 atau S2': 14,
    }
}


st.set_page_config(layout="wide")
st.title('🧮 Kalkulator Poin Remunerasi Dosen UNTAN')
st.info('Kalkulator ini mengacu pada **SK Rektor No. 1080/UN22/HK.02/2025** yang berlaku mulai Semester II Tahun 2025.')
st.success('For Education Purposes Only. Made with Love by Izu')
total_poin = 0

# --- TAHAP 1: MENGAJAR ---
st.header('Tahap 1: A. Kegiatan Mengajar')
poin_mengajar = 0
container_mengajar = st.container()

with container_mengajar:
    jumlah_kelas = st.number_input('Masukkan jumlah kelas yang diajar:', min_value=0, step=1, key='jumlah_kelas')
    
    if jumlah_kelas > 0:
        cols = st.columns(jumlah_kelas)
        for i in range(jumlah_kelas):
            with cols[i]:
                st.subheader(f'Kelas {i+1}')
                kegiatan = st.selectbox(
                    f'Pilih Jenis Program', 
                    options=list(remun_data['A. MENGAJAR'].keys()), 
                    key=f'kegiatan_{i}'
                )
                
                info_kegiatan = remun_data['A. MENGAJAR'][kegiatan]
                poin_satuan = info_kegiatan['nilai']
                
                jumlah_sks = st.number_input(f'Jumlah SKS', min_value=0, step=1, key=f'sks_{i}')
                
                poin_kelas = 0
                if 'Per Mahasiswa' in info_kegiatan['unit']:
                    jumlah_mhs = st.number_input(f'Jumlah Mahasiswa', min_value=0, step=1, key=f'mhs_{i}')
                    poin_kelas = jumlah_mhs * jumlah_sks * poin_satuan
                else: # Per SKS
                    poin_kelas = jumlah_sks * poin_satuan

                is_tandem = st.checkbox('Team Teaching?', key=f'tandem_{i}')
                if is_tandem:
                    poin_kelas /= 2
                
                st.metric(label=f"Poin Kelas {i+1}", value=f"{poin_kelas:.3f}")
                poin_mengajar += poin_kelas
    
    # Menampilkan total poin untuk tahap mengajar
    st.success(f"**Total Poin Tahap Mengajar: {poin_mengajar:.3f}**")


st.markdown("---")
total_poin += poin_mengajar

# --- TAHAP 2: MEMBIMBING ---
st.header('Tahap 2: B. Kegiatan Membimbing')
poin_membimbing = 0
for kegiatan, nilai in remun_data['B. MEMBIMBING'].items():
    jumlah = st.number_input(f"Jumlah mahasiswa untuk '{kegiatan}'", min_value=0, step=1, key=f"b_{kegiatan}")
    poin_membimbing += jumlah * nilai
st.success(f"**Total Poin Tahap Membimbing: {poin_membimbing:.3f}**")
total_poin += poin_membimbing

st.markdown("---")


# --- TAHAP 3: MENGUJI ---
st.header('Tahap 3: C. Kegiatan Menguji')
poin_menguji = 0
for kegiatan, nilai in remun_data['C. MENGUJI'].items():
    jumlah = st.number_input(f"Jumlah mahasiswa untuk '{kegiatan}'", min_value=0, step=1, key=f"c_{kegiatan}")
    poin_menguji += jumlah * nilai
st.success(f"**Total Poin Tahap Menguji: {poin_menguji:.3f}**")
total_poin += poin_menguji

st.markdown("---")


# --- TAHAP 4: PENELITIAN ---
st.header('Tahap 4: D. Kegiatan Penelitian')
poin_penelitian = 0
ketua_penelitian = st.number_input("Jumlah proposal sebagai 'Ketua Penelitian'", min_value=0, max_value=1, step=1)
poin_penelitian += ketua_penelitian * remun_data['D. PENELITIAN']['Ketua Penelitian']

anggota_penelitian = st.number_input("Jumlah proposal sebagai 'Anggota Penelitian'", min_value=0, step=1)
if anggota_penelitian > 0:
    jumlah_anggota = st.number_input("Total anggota dalam tim penelitian tsb:", min_value=1, step=1, key='jml_anggota_penelitian')
    if jumlah_anggota > 0:
        poin_penelitian += (anggota_penelitian * remun_data['D. PENELITIAN']['Anggota Penelitian (poin dibagi jumlah anggota)']) / jumlah_anggota
st.success(f"**Total Poin Tahap Penelitian: {poin_penelitian:.3f}**")
total_poin += poin_penelitian

st.markdown("---")


# --- TAHAP 5: PENGABDIAN ---
st.header('Tahap 5: E. Kegiatan Pengabdian Kepada Masyarakat')
poin_pengabdian = 0
ketua_pengabdian = st.number_input("Jumlah proposal sebagai 'Ketua Pengabdian'", min_value=0, max_value=1, step=1)
poin_pengabdian += ketua_pengabdian * remun_data['E. PENGABDIAN KEPADA MASYARAKAT']['Ketua Pengabdian']

anggota_pengabdian = st.number_input("Jumlah proposal sebagai 'Anggota Pengabdian'", min_value=0, step=1)
if anggota_pengabdian > 0:
    jumlah_anggota_abdi = st.number_input("Total anggota dalam tim pengabdian tsb:", min_value=1, step=1, key='jml_anggota_abdi')
    if jumlah_anggota_abdi > 0:
        poin_pengabdian += (anggota_pengabdian * remun_data['E. PENGABDIAN KEPADA MASYARAKAT']['Anggota Pengabdian (poin dibagi jumlah anggota)']) / jumlah_anggota_abdi
st.success(f"**Total Poin Tahap Pengabdian: {poin_pengabdian:.3f}**")
total_poin += poin_pengabdian

st.markdown("---")


# --- TAHAP 6: PENUNJANG & PUBLIKASI ---
st.header('Tahap 6: F & G. Kegiatan Penunjang dan Publikasi')
col1, col2 = st.columns(2)

with col1:
    st.subheader("F. Unsur Penunjang")
    poin_penunjang = 0
    for kegiatan, nilai in remun_data['F. UNSUR PENUNJANG'].items():
        jumlah = st.number_input(f"Jumlah kegiatan '{kegiatan}'", min_value=0, step=1, key=f"f_{kegiatan}")
        poin_penunjang += jumlah * nilai
    st.success(f"**Total Poin Penunjang: {poin_penunjang:.3f}**")
    total_poin += poin_penunjang

with col2:
    st.subheader("G. Publikasi")
    poin_publikasi = 0
    for kegiatan, nilai in remun_data['G. PUBLIKASI'].items():
        jumlah = st.number_input(f"Jumlah publikasi '{kegiatan}'", min_value=0, step=1, key=f"g_{kegiatan}")
        poin_publikasi += jumlah * nilai
    st.success(f"**Total Poin Publikasi: {poin_publikasi:.3f}**")
    total_poin += poin_publikasi
st.markdown("---")


# --- TOTAL POIN ---
st.header('TOTAL AKUMULASI POIN')

st.metric(
    label="Total Poin Kinerja Anda",
    value=f"{total_poin:.3f}"
)

if total_poin > 12:
    st.balloons()