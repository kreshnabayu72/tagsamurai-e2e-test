---
id: TC-GS-FILEMGR-E2E-066-storage-state-laporan-kuota-dan-batas-persentase
title: "Kartu Storage Usage: Laporan Terlama, Kuota Belum Dialokasikan, Melewati Kuota, dan Batas Persentase"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-271
  - TC-GS-FILEMGR-273
  - TC-GS-FILEMGR-274
  - TC-GS-FILEMGR-275
coverage:
  web: automated
---

# Kartu Storage Usage: Laporan Terlama, Kuota Belum Dialokasikan, Melewati Kuota, dan Batas Persentase

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah laporan Storage dan kuota Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanisme laporan app tidak didefinisikan di TC, lihat Temuan untuk QA): seeding laporan Storage per app dan kuota Client skenario Tabel A5 berikut (1 GB = 1.073.741.824 byte, waktu laporan format General Settings default dd/MM/yy HH:mm). Tiap skenario menggantikan skenario sebelumnya.

  | Skenario | Kuota | Laporan |
  |---|---|---|
  | S4 | 50 GB | Fixed Asset 3.2 GB dan Admin Console 1.4 GB (14/09/26 02:00); Global Settings 204.8 MB dengan laporan terakhir 10/09/26 02:00 |
  | S3 | belum pernah dialokasikan | Global Settings 204.8 MB, 13/09/26 02:00 |
  | S2 | 4 GB | Fixed Asset 3.2 GB, Admin Console 1.4 GB, Global Settings 204.8 MB (Total Used 4.8 GB), 14/09/26 02:00 |
  | S8 | 5 GB | Fixed Asset 5.368.709.119 byte (`5.0 GB`), 14/09/26 02:00 |
  | S7 | 5 GB | Fixed Asset 5.368.709.120 byte (`5.0 GB`), 14/09/26 02:00 |

- State global yang diubah: laporan Storage dan kuota Client uji. Hook `after` (tetap jalan walau spec gagal di tengah) memulihkan laporan Storage awal.
- Data: Data Pre-setup Tabel A2 (33 file aktif, termasuk `siti-profile.png` F02) di-seed idempotent di hook `before`; TC-274 hanya membuka menu row action `siti-profile.png` tanpa memilih opsi sehingga data tidak berubah (S-06).
- Dependensi TC (TC-268 kartu Storage Usage) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`): pulihkan laporan Storage dan kuota seperti di atas.

## Test Steps

### TC-GS-FILEMGR-271: Last updated memakai laporan paling lama (S4)

1. Siapkan laporan Storage skenario S4 lewat fixture BE, lalu muat ulang Global Settings > File Manager
2. Verifikasi label `Last updated 10/09/26 02:00` (laporan paling lama, bukan 14/09/26 02:00)
3. Verifikasi `Global Settings 204.8 MB` tetap tampil di daftar app dengan laporan terakhirnya
4. Verifikasi tidak ada penanda error, peringatan, atau toast untuk app yang tidak melapor

### TC-GS-FILEMGR-273: Kuota belum dialokasikan (S3)

5. Siapkan laporan Storage skenario S3 lewat fixture BE, lalu muat ulang Global Settings > File Manager
6. Verifikasi `Storage Quota` menampilkan `—`
7. Verifikasi ProgressBar tidak tampil
8. Verifikasi `Total Used` `204.8 MB`
9. Verifikasi daftar app memuat `Global Settings 204.8 MB`
10. Verifikasi `Last updated 13/09/26 02:00`

### TC-GS-FILEMGR-274: Melewati kuota tanpa memblokir aksi (S2)

11. Siapkan laporan Storage skenario S2 lewat fixture BE, lalu muat ulang Global Settings > File Manager
12. Verifikasi label ProgressBar `120%`
13. Verifikasi bar penuh
14. Verifikasi severity ProgressBar danger
15. Verifikasi label persentase tetap tampil sebagai penanda selain warna
16. Verifikasi tidak ada toast maupun dialog peringatan
17. Klik ikon (⋯) baris `siti-profile.png`
18. Verifikasi opsi `Delete` tampil dan enabled
19. Tutup menu row action lewat `Esc`

### TC-GS-FILEMGR-275: Batas persentase (S8 lalu S7)

20. Siapkan laporan Storage skenario S8 lewat fixture BE, lalu muat ulang Global Settings > File Manager
21. Verifikasi label ProgressBar `99%` (dibulatkan ke bawah)
22. Verifikasi severity ProgressBar default
23. Verifikasi `Total Used` `5.0 GB`
24. Verifikasi `Storage Quota` `5.0 GB`
25. Siapkan laporan Storage skenario S7 lewat fixture BE, lalu muat ulang Global Settings > File Manager
26. Verifikasi label ProgressBar `100%`
27. Verifikasi bar penuh
28. Verifikasi severity ProgressBar danger (Total Used ≥ Storage Quota)
29. Verifikasi `Total Used` `5.0 GB`
30. Verifikasi `Storage Quota` `5.0 GB`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas fungsional (kartu Storage Usage).
- Urutan TC di spec berbeda dari sumber (271, 273, 274, 275 setelah screening di spec 065): TC-275 menjalankan S8 lalu S7 sesuai langkah TC. Tidak ada aksi yang menghabiskan data.
- Nilai turunan (Q-14): S2 120% (4.8/4); S8 99% (5.368.709.119/5.368.709.120 dibulatkan ke bawah); S7 100%; label `5.0 GB` pada S7 dan S8 karena pembulatan satu desimal.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 5, 11, 20, 25 (menyiapkan skenario dan memuat ulang), langkah 19 (menutup menu row action).
- Asersi absence (langkah 4, 7, 16) didahului anchor positif pada kartu yang sama: Total Used dan daftar app tampil (S4 langkah 2 sampai 3, S3 langkah 6 dan 8, S2 langkah 12 sampai 15).
- Temuan untuk QA:
  - Mekanisme seeding laporan Storage per app dan kuota (Q-4) tidak didefinisikan di TC; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-274 langkah 2 hanya meminta "amati opsi Delete" tanpa menyebut menu ditutup; langkah 19 adalah langkah penghubung.
