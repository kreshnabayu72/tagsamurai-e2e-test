---
id: TC-FA-FAAM-E2E-242-sinkron-cascade-category-ke-aset-dan-lisensi-addon
title: "Sinkron Lintas Modul: Cascade Category ke Aset dan Lisensi Addon Berakhir Setelah Tersimpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-602
  - TC-FA-FAAM-609
coverage:
  web: automated
---

# Sinkron Lintas Modul: Cascade Category ke Aset dan Lisensi Addon Berakhir Setelah Tersimpan

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 (`Dell Latitude`, Total Asset 42, Category `IT Equipment`), No. 22 (Category `Office Equipment`). `Dell Latitude` tidak dapat digandakan dan menjadi target Edit Category TC-FA-FAAM-602 (cascade ke 42 aset); hook `before` dan hook `after` menyediakannya ulang ke keadaan Pre-setup No. 10 lewat seed API (kemampuan disediakan tim BE/FE). Efek: Last Updated `Dell Latitude` dan Category 42 aset berubah sampai dipulihkan; suite berjalan serial. Pernyataan ini belum ada di `suite.md` (lihat Temuan untuk QA).
- Data Dinamis, di-seed lewat API di hook `before`: `Addon Grand Item {runId}-242` (fixture No. 10c, Default Addon `Maps`, lisensi Maps sudah berakhir, Total Asset 0).
- Kemampuan teknis: Fixed Asset > Assets (tabel aset) dan lisensi Maps yang diakhiri lewat seed API.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Addon Grand Item {runId}-242` dan pulihkan `Dell Latitude`.
- State global yang diubah: Category `Dell Latitude` dan aset-asetnya (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-602 dan 609: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-609: Lisensi addon berakhir setelah addon tersimpan

1. Ketik Search `Addon Grand Item {runId}-242`, tekan Enter
2. Klik `⋯` baris `Addon Grand Item {runId}-242` lalu `Edit`
3. Verifikasi chip `Maps` tampil terkunci 🔒
4. Verifikasi chip `Maps` dapat dilepas
5. Klik `✕` pada Modal Edit

### TC-FA-FAAM-602: Perubahan Category tercermin ke Category aset secara atomik

6. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
7. Klik `⋯` baris `Dell Latitude` lalu `Edit`
8. Ubah Category menjadi `Office Equipment`
9. Klik `[Save]`
10. Konfirmasi dialog dampak
11. Buka Asset List modul asset
12. Ketik Search `Dell Latitude`, tekan Enter
13. Verifikasi 42 aset `Dell Latitude` tampil
14. Verifikasi kolom Category 42 aset menampilkan `Office Equipment`
15. Sediakan ulang `Dell Latitude` ke keadaan Pre-setup No. 10 lewat seed API

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 6 (Search tabel utama), langkah 5 (menutup Modal Edit tanpa perubahan, sehingga tidak ada dialog Unsaved Changes), langkah 11 (navigasi), langkah 12 (Search), dan langkah 15 (pemulihan).
- Pembagian TC lintas spec: TC-FA-FAAM-597, 600, 601, dan 603 ada di spec 241 dan 221. Absence baris log per aset atas perubahan Category ada di spec 240 (TC-FA-FAAM-577).
- Urutan TC: TC-FA-FAAM-609 (hanya baca) sebelum TC-FA-FAAM-602 (mengubah data).
- Temuan untuk QA:
  - TC-FA-FAAM-602 mengubah `Dell Latitude` (Pre-setup No. 10); S-06 mensyaratkan fixture pemulihan dinyatakan di `suite.md` (belum ada).
  - TC-FA-FAAM-602 tidak menyebut tombol pada dialog dampak Change Category; spec menulis "Konfirmasi dialog dampak".
  - TC-FA-FAAM-609 butir "dapat dilepas" tidak menyebut pelepasan dilakukan; spec hanya mengasersi bahwa chip dapat dilepas dan menutup form tanpa perubahan.
