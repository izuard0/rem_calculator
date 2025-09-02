# remun_calc.py

# Data poin telah diupdate dan dilengkapi berdasarkan Rubrik Remunerasi 2025
kegiatan_poin = {
    # --- Kategori: Membimbing ---
    'A01': {'nama': 'Bimbingan Akademik', 'poin': 0.06, 'satuan': 'Per Mhs'},
    'A02': {'nama': 'Bimbingan PPL/Magang/Kerja Praktek', 'poin': 0.1, 'satuan': 'Per Mhs'},
    'A03': {'nama': 'Membimbing Disertasi (Pembimbing Pendamping)', 'poin': 3.7, 'satuan': 'Per Mhs/Dosen'},
    'A04': {'nama': 'Membimbing Disertasi (Pembimbing Utama)', 'poin': 4.6, 'satuan': 'Per Mhs/Dosen'},
    'A05': {'nama': 'Membimbing MBKM', 'poin': 0.4, 'satuan': 'Per Mhs'},
    'A06': {'nama': 'Membimbing Mahasiswa Praktek Klinik', 'poin': 0.2, 'satuan': 'Per Pertemuan'},
    'A07': {'nama': 'Membimbing Praktikum/Tugas Terstruktur', 'poin': 0.1, 'satuan': 'Per Mhs'},
    'A08': {'nama': 'Membimbing Skripsi', 'poin': 0.85, 'satuan': 'Per Mhs/Dosen'},
    'A09': {'nama': 'Membimbing Tesis (Pembimbing Pendamping)', 'poin': 1.35, 'satuan': 'Per Mhs/Dosen'},
    'A10': {'nama': 'Membimbing Tesis (Pembimbing Utama)', 'poin': 1.6, 'satuan': 'Per Mhs/Dosen'},
    'A11': {'nama': 'Membimbing Tugas Akhir Diploma 3', 'poin': 0.85, 'satuan': 'Per Mhs/Dosen'},
    'A12': {'nama': 'Membimbing Tugas Akhir Profesi', 'poin': 0.85, 'satuan': 'Per Mhs/Dosen'},
    'A13': {'nama': 'Membimbing Uji Kompetensi Fak. Kedokteran', 'poin': 1.5, 'satuan': 'Per Mata Kuliah'},
    'A14': {'nama': 'Pembimbing Kompetisi Belmawa', 'poin': 0.45, 'satuan': 'Judul Yang Lolos'},
    'A15': {'nama': 'Pembina Lembaga Kemahasiswaan', 'poin': 0.45, 'satuan': 'Per UKM'},
    'A16': {'nama': 'Pengampu peer teaching PPL', 'poin': 0.1, 'satuan': 'Per Mhs'},
    'A17': {'nama': 'Pengampu/Pembekalan PPL/KKN', 'poin': 0.2, 'satuan': 'Per Pertemuan'},
    # --- Kategori: Mengabdi ---
    'B01': {'nama': 'Anggota Penelitian', 'poin': 1.2, 'satuan': 'Per Judul'},
    'B02': {'nama': 'Ketua Penelitian', 'poin': 1.8, 'satuan': 'Per Judul'},
    # --- Kategori: Mengajar ---
    'C01': {'nama': 'Melakukan Pemeriksaan Dalam Dengan Pembimbingan', 'poin': 3.0, 'satuan': 'Per SKS'},
    'C02': {'nama': 'Membuat Buku Ajar ber ISBN', 'poin': 5.0, 'satuan': 'Per Buku'},
    'C03': {'nama': 'Membuat Soal (bukan untuk mata kuliah)', 'poin': 0.1, 'satuan': 'Per Naskah'},
    'C04': {'nama': 'Mengajar Kelas Internasional', 'poin': 0.05, 'satuan': 'Per Mahasiswa/SKS'},
    'C05': {'nama': 'Mengajar Kelas Reguler Sore & Malam', 'poin': 0.03, 'satuan': 'Per Mahasiswa/SKS'},
    'C06': {'nama': 'Mengajar Matrikulasi', 'poin': 0.25, 'satuan': 'Per Pertemuan'},
    'C07': {'nama': 'Mengajar pada Program D3/S1 Reguler Pagi', 'poin': 25.0, 'satuan': 'Per Mahasiswa/SKS'},
    'C08': {'nama': 'Mengajar pada Program Profesi', 'poin': 0.05, 'satuan': 'Per Mahasiswa/SKS'},
    'C09': {'nama': 'Mengajar pada Program S2/Magister', 'poin': 2.0, 'satuan': 'Per SKS'},
    'C10': {'nama': 'Mengajar pada Program S3/Doktor', 'poin': 3.0, 'satuan': 'Per SKS'},
    'C11': {'nama': 'Menjadi Saksi Ahli Dengan Pembimbingan', 'poin': 1.0, 'satuan': 'Per SKS'},
    # --- Kategori: Menguji ---
    'D01': {'nama': 'Menguji Disertasi Ujian Terbuka', 'poin': 1.0, 'satuan': 'Per Mhs'},
    'D02': {'nama': 'Menguji Disertasi Ujian Tertutup', 'poin': 1.0, 'satuan': 'Per Mhs'},
    'D03': {'nama': 'Menguji Kelayakan/Kolokium Disertasi', 'poin': 0.28, 'satuan': 'Per Mhs'},
    'D04': {'nama': 'Menguji Skripsi', 'poin': 0.15, 'satuan': 'Per Mhs'},
    'D05': {'nama': 'Menguji Tesis', 'poin': 0.6, 'satuan': 'Per Mhs'},
    'D06': {'nama': 'Menguji proposal/seminar hasil skripsi', 'poin': 0.15, 'satuan': 'Per Mhs'},
    'D07': {'nama': 'Pengawas Ujian', 'poin': 0.18, 'satuan': 'Per Mata Kuliah'},
    # --- Kategori: Penjunjang ---
    'E01': {'nama': 'Anggota Dewan Pengawas Rumah Sakit', 'poin': 2.7, 'satuan': 'Per Smt'},
    'E02': {'nama': 'Anggota Kepanitiaan Kegiatan Adhoc', 'poin': 0.45, 'satuan': 'Per Keg'},
    'E03': {'nama': 'Anggota Tim Adhoc', 'poin': 2.7, 'satuan': 'Per Sem'},
    'E04': {'nama': 'Anggota Tim Perumus Kebijakan Universitas', 'poin': 4.5, 'satuan': 'Per Sem'},
    'E05': {'nama': 'Ketua Dewan Pengawas Rumah Sakit', 'poin': 4.5, 'satuan': 'Per Smt'},
    'E06': {'nama': 'Ketua Tim Perumus Kebijakan Universitas', 'poin': 5.95, 'satuan': 'Per Sem'},
    'E07': {'nama': 'Wakil Ketua Tim Perumus Kebijakan Universitas', 'poin': 5.95, 'satuan': 'Per Sem'},
    # --- Kategori: Publikasi ---
    'F01': {'nama': 'Anggota Penyunting Jurnal Sinta 1 & 2', 'poin': 2.0, 'satuan': 'Per Jurnal/Semester'},
    'F02': {'nama': 'Jurnal Nasional Terakreditasi S1/S2', 'poin': 14.0, 'satuan': 'Per Judul'},
    'F03': {'nama': 'Ketua Penyunting Jurnal Sinta 1 & 2', 'poin': 3.0, 'satuan': 'Per Jurnal/Semester'},
    'F04': {'nama': 'Mitra Bestari (Reviewer) Jurnal Sinta 1 & 2', 'poin': 1.0, 'satuan': 'Per Naskah'},
    'F05': {'nama': 'Publikasi Jurnal Internasional Q1', 'poin': 45.0, 'satuan': 'Per Judul'},
    'F06': {'nama': 'Publikasi Jurnal Internasional Q2', 'poin': 41.0, 'satuan': 'Per Judul'},
    'F07': {'nama': 'Publikasi Jurnal Internasional Q3', 'poin': 37.0, 'satuan': 'Per Judul'},
    'F08': {'nama': 'Publikasi Jurnal Internasional Q4', 'poin': 26.0, 'satuan': 'Per Judul'},
}

def hitung_remun():
    total_poin = 0
    print("=== Kalkulator Remunerasi Dosen (Rubrik 2025) ===")
    print("Masukkan kode kegiatan dan jumlahnya. Ketik 'selesai' untuk mengakhiri.")

    while True:
        print("\n--- Daftar Kode Kegiatan (Umum) ---")
        for kode, detail in kegiatan_poin.items():
            print(f"{kode}: {detail['nama']} ({detail['poin']} poin / {detail['satuan']})")
        
        kode_input = input("Masukkan Kode Kegiatan (atau 'selesai'): ").upper()
        if kode_input.lower() == 'selesai':
            break

        if kode_input not in kegiatan_poin:
            print("Kode tidak valid, coba lagi.")
            continue

        detail_kegiatan = kegiatan_poin[kode_input]
        poin_kegiatan = 0

        try:
            # --- BLOK LOGIKA BARU UNTUK KALKULASI KHUSUS ---
            if 'Per Mahasiswa/SKS' in detail_kegiatan['satuan']:
                print(f"Perhitungan Khusus untuk '{detail_kegiatan['nama']}'")
                jumlah_mhs = int(input("  -> Masukkan Jumlah Mahasiswa: "))
                jumlah_sks = int(input("  -> Masukkan Jumlah SKS: "))
                poin_kegiatan = detail_kegiatan['poin'] * jumlah_mhs * jumlah_sks
            # --- AKHIR BLOK LOGIKA BARU ---
            else:
                jumlah = float(input(f"Masukkan jumlah untuk '{detail_kegiatan['nama']}' (sesuai satuan): "))
                poin_kegiatan = detail_kegiatan['poin'] * jumlah
            
            total_poin += poin_kegiatan
            print(f"Poin dari kegiatan ini: {poin_kegiatan:.2f}")
            print(f"Total Poin Saat Ini: {total_poin:.2f}")

        except ValueError:
            print("Jumlah harus berupa angka.")

    print(f"\n================================")
    print(f"Total Akumulasi Poin Remunerasi: {total_poin:.2f}")
    print("================================")

if __name__ == "__main__":
    hitung_remun()
