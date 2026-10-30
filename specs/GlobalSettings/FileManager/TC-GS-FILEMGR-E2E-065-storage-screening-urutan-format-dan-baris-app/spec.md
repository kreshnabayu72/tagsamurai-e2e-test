---
id: TC-GS-FILEMGR-E2E-065-storage-screening-urutan-format-dan-baris-app
title: "Kartu Storage Usage: Screening, Urutan Daftar App, Format Angka, dan Baris App Tanpa Aksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-268
  - TC-GS-FILEMGR-269
  - TC-GS-FILEMGR-270
  - TC-GS-FILEMGR-286
coverage:
  web: automated
---

# Kartu Storage Usage: Screening, Urutan Daftar App, Format Angka, dan Baris App Tanpa Aksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah laporan Storage Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanisme laporan app tidak didefinisikan di TC, lihat Temuan untuk QA): seeding laporan Storage per app dan kuota Client skenario S1, S10, dan S9 (Tabel A5, 1 GB = 1.073.741.824 byte, waktu laporan format General Settings default dd/MM/yy HH:mm). Tiap skenario menggantikan skenario sebelumnya.
  - S1: kuota 50 GB; Fixed Asset 3.2 GB, Admin Console 1.4 GB, Global Settings 204.8 MB, semuanya 14/09/26 02:00; Total Used 4.8 GB.
  - S10: kuota 50 GB; Fixed Asset 1.0 GB dan Admin Console 1.0 GB, keduanya 14/09/26 02:00.
  - S9: kuota 50 GB; Global Settings 0.0 KB dan Fixed Asset 3.2 GB, keduanya 14/09/26 02:00.
- State global yang diubah: laporan Storage dan kuota Client uji. Hook `after` (tetap jalan walau spec gagal di tengah) memulihkan laporan Storage awal.
- Data: Data Pre-setup Tabel A2 (33 file aktif) di-seed idempotent di hook `before` dan hanya dibaca (tidak diubah, S-06; lihat Temuan untuk QA tentang hitungan 33).
- Dependensi TC (TC-01 tabel utama) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`): pulihkan laporan Storage dan kuota seperti di atas.

## Test Steps

### Skenario S1

1. Siapkan laporan Storage skenario S1 lewat fixture BE, lalu muat ulang Global Settings > File Manager
2. Tunggu kartu dan tabel selesai dimuat

#### TC-GS-FILEMGR-268: Screening kartu Storage Usage

3. Verifikasi kartu `Storage Usage` tampil di bawah Breadcrumb
4. Verifikasi kartu `Storage Usage` berada di atas tabel utama
5. Verifikasi kartu `Storage Usage` berdiri sendiri, terpisah dari kartu tabel
6. Verifikasi judul kartu `Storage Usage`
7. Verifikasi header kartu menampilkan `Last updated 14/09/26 02:00`
8. Verifikasi `Total Used` `4.8 GB`
9. Verifikasi `Storage Quota` `50.0 GB`
10. Verifikasi ProgressBar berlabel `9%`
11. Verifikasi ProgressBar berseverity default
12. Verifikasi daftar per app berurutan: `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB` (pemakaian terbesar di atas; sekaligus TC-GS-FILEMGR-269 butir a)
13. Verifikasi kartu tidak memuat Search, Filter, Checkbox, tombol aksi, maupun pagination

#### TC-GS-FILEMGR-286: Baris app tanpa aksi dan tabel tetap hanya foto profil

14. Hover baris `Fixed Asset` di kartu
15. Verifikasi baris `Fixed Asset` tidak berubah saat hover
16. Klik baris `Fixed Asset` di kartu
17. Verifikasi baris `Fixed Asset` tidak berubah saat klik
18. Verifikasi tidak ada daftar file, preview, maupun navigasi setelah klik baris `Fixed Asset`
19. Tekan Tab berulang dari kartu menuju tabel
20. Verifikasi baris app tidak menerima fokus sebagai kontrol
21. Verifikasi tabel utama memuat 33 baris foto profil Tabel A2
22. Verifikasi tabel utama tidak memuat file milik Fixed Asset atau Admin Console pada kolom File Name

### Skenario S10

23. Siapkan laporan Storage skenario S10 lewat fixture BE, lalu muat ulang Global Settings > File Manager

#### TC-GS-FILEMGR-269: Urutan A-Z pada pemakaian sama

24. Verifikasi pemakaian `Fixed Asset` dan `Admin Console` sama `1.0 GB`
25. Verifikasi `Admin Console` tampil di atas `Fixed Asset` (urutan A-Z menurut nama app)

### Skenario S9

26. Siapkan laporan Storage skenario S9 lewat fixture BE, lalu muat ulang Global Settings > File Manager

#### TC-GS-FILEMGR-270: Format angka kartu

27. Verifikasi `Global Settings 0.0 KB` tetap tampil di daftar (app dengan pemakaian nol tidak disembunyikan)
28. Verifikasi `Fixed Asset 3.2 GB` tampil di daftar
29. Verifikasi `Total Used` `3.2 GB`
30. Verifikasi `Storage Quota` `50.0 GB`
31. Verifikasi format angka kartu mengikuti kolom Size tabel utama (satuan naik pada 1024 satuan di bawahnya, satu desimal)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas fungsional (kartu Storage Usage). Mobile (TC-284) ada di spec `TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip`.
- Urutan TC di spec berbeda dari sumber: skenario S1 lebih dulu (TC-268, TC-286, dan butir a TC-269), lalu S10 (butir b TC-269), lalu S9 (TC-270), agar laporan diganti sekali per skenario. Screening (TC-268) berada di awal. Butir a TC-269 sama dengan butir e TC-268; satu `Verifikasi` (langkah 12) memetakan keduanya.
- Hitungan 9% pada langkah 10 konsisten dengan aturan pembulatan ke bawah (4.8/50 = 9.6%), bagian dari nilai turunan Q-14.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 23, 26 (menyiapkan skenario laporan Storage; precondition TC dijadikan langkah), langkah 2 (menunggu muat), langkah 14, 16, 19 (aksi klik, hover, Tab pada TC-286).
- Verifikasi langkah 3 sampai 5 memecah butir a TC-268 menjadi tiga klausa (posisi di bawah Breadcrumb, di atas tabel utama, berdiri sendiri) sesuai S-01.
- Temuan untuk QA:
  - Mekanisme seeding laporan Storage per app dan kuota (Q-4) tidak didefinisikan di TC; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - Hitungan 33 baris (TC-286) bergantung pada dataset Pre-setup yang tidak diubah spec lain (Q-7); dataset di-seed idempotent oleh hook spec ini.
  - TC-286 langkah "Tekan Tab berulang dari kartu menuju tabel" tidak menyebut jumlah tekanan Tab; spec mengikuti TC.
