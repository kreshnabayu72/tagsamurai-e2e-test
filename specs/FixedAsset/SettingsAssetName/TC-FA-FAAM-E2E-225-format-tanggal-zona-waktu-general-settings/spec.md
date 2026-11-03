---
id: TC-FA-FAAM-E2E-225-format-tanggal-zona-waktu-general-settings
title: "Format Tanggal dan Zona Waktu General Settings pada Tabel Utama, Filter Last Updated, dan Tab Total Assets"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-607
  - TC-FA-FAAM-608
coverage:
  web: automated
---

# Format Tanggal dan Zona Waktu General Settings pada Tabel Utama, Filter Last Updated, dan Tab Total Assets

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) dengan akses ke Global Settings > General Settings. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 (`Dell Latitude`, Total Asset 42, Last Updated terisi; hanya dibaca, tidak diubah). Nilai awal Date Format, Time Format, dan Time Zone General Settings dibaca hook `before` dan dipulihkan di hook `after`.
- Data uji: nilai baru Date Format, Time Format, dan Time Zone yang berbeda dari nilai awal disediakan tim FE (TC tidak menyebut nilainya); TC-FA-FAAM-607 memakai satu set nilai baru dan TC-FA-FAAM-608 memakai Date Format lain yang berbeda dari set TC-FA-FAAM-607.
- Kemampuan teknis: pembukaan Global Settings > General Settings; Filter Last Updated pada tabel utama; tab Total Assets pada Popup Detail `Dell Latitude`; jam server dan klien sinkron (S-12).
- State global yang diubah: Date Format, Time Format, dan Time Zone General Settings client utama. Dipulihkan oleh langkah 19 dan 20 serta hook `after` (tetap jalan walau spec gagal di tengah). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`): pulihkan Date Format, Time Format, dan Time Zone ke nilai awal.
- Precondition TC-FA-FAAM-607 dan 608: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-607: Format tanggal dan zona waktu pada tabel utama dan Filter Last Updated

1. Buka Global Settings > General Settings
2. Ubah Date Format, Time Format, dan Time Zone ke nilai baru set TC-FA-FAAM-607
3. Klik `[Save]`
4. Buka Fixed Asset > Settings > Asset Master > Asset Name
5. Ketik Search `Dell Latitude`, tekan Enter
6. Verifikasi kolom Last Updated baris `Dell Latitude` menampilkan tanggal, jam, dan zona waktu sesuai pengaturan baru
7. Klik Filter lalu pilih tanggal pada Filter Last Updated
8. Verifikasi teks tanggal terpilih di input Filter mengikuti Date Format
9. Tutup Filter

### TC-FA-FAAM-608: Format tanggal pada Tab Total Assets

10. Buka Global Settings > General Settings
11. Ubah Date Format ke nilai baru set TC-FA-FAAM-608
12. Klik `[Save]`
13. Buka Fixed Asset > Settings > Asset Master > Asset Name
14. Ketik Search `Dell Latitude`, tekan Enter
15. Klik nama `Dell Latitude` lalu klik tab `Total Assets (42)`
16. Verifikasi kolom Last Updated tabel memakai format baru
17. Tutup Popup Detail
18. Buka Global Settings > General Settings
19. Pulihkan Date Format, Time Format, dan Time Zone ke nilai awal
20. Klik `[Save]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 4, 10, 13, 18 (navigasi), langkah 5, 14 (Search untuk menemukan baris target), langkah 9 dan 17 (menutup Filter atau Popup Detail), dan langkah 19 serta 20 (pemulihan state global; hook `after` sebagai cadangan; S-09).
- P-5(b): TC-FA-FAAM-607 dan 608 adalah dua TC objek uji ringan (format tanggal General Settings) pada permukaan yang sama (tabel utama dan Popup Detail), tanpa harness eksternal dan tanpa state berat sendiri.
- Pembagian TC lintas spec: format tanggal Last Updated pada isi berkas CSV tab Total Assets (kelas f) ada di spec 141 (TC-FA-FAAM-846).
- Temuan untuk QA:
  - TC-FA-FAAM-607 dan 608 tidak menyebut nilai Date Format, Time Format, dan Time Zone baru; spec memakai "nilai baru" disediakan tim FE.
  - Langkah 7 memilih tanggal Filter Last Updated tanpa nilai tanggal dari TC.
