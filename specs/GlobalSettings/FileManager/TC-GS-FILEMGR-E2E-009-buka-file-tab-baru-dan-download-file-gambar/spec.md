---
id: TC-GS-FILEMGR-E2E-009-buka-file-tab-baru-dan-download-file-gambar
title: "Buka File di Tab Baru dan Download File Gambar dari Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-48
  - TC-GS-FILEMGR-50
  - TC-GS-FILEMGR-55
coverage:
  web: automated
---

# Buka File di Tab Baru dan Download File Gambar dari Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2 (33 file aktif) dengan F01 `budi-avatar.jpg` (Uploaded By Budi Santoso) yang file fisiknya tersedia; Tabel A3 (16 file di Recycle Bin) dengan R01 `old-avatar.png` yang file fisiknya tersedia. Spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: fixture BE untuk Tabel A2 dan A3 beserta file fisik (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); membaca jumlah dan URL tab browser, membaca isi file terunduh (binary buffer), dan membandingkannya dengan file gambar sumber `budi-avatar.jpg` yang disediakan tim FE sebagai fixture (kelas f untuk TC-55, P-5).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-48: Klik File Name di tabel utama membuka file di tab browser baru

1. Klik teks `budi-avatar.jpg` di kolom File Name
2. Amati tab browser dan halaman File Manager
3. Verifikasi satu tab browser baru terbuka menampilkan gambar `budi-avatar.jpg` lewat viewer native browser
4. Verifikasi tidak ada dialog atau modal File Preview, metadata, maupun tombol `[Download File]` di halaman File Manager
5. Verifikasi tab asal tetap di Global Settings > File Manager tanpa perubahan halaman
6. Verifikasi tab asal tanpa Search, filter, sort, dan baris terpilih, dengan paginasi tetap di halaman 1
7. Verifikasi tidak ada toast
8. Tutup tab browser baru dan kembali ke tab asal

### TC-GS-FILEMGR-50: Membuka file dari klik File Name di modal Recycle Bin

9. Klik tombol Recycle Bin di toolbar
10. Catat jumlah total baris Recycle Bin dari info pagination
11. Klik teks `old-avatar.png` di kolom File Name
12. Verifikasi satu tab browser baru terbuka menampilkan gambar `old-avatar.png` lewat viewer native browser
13. Verifikasi modal Recycle Bin tetap terbuka di tab asal
14. Verifikasi tidak ada dialog atau modal File Preview
15. Tutup tab browser baru dan kembali ke tab asal
16. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-55: Download file dari row action tabel utama tanpa toast sukses

17. Catat jumlah total baris tabel utama dari info pagination
18. Klik ikon (⋯) baris `budi-avatar.jpg`
19. Klik `Download`
20. Verifikasi file gambar `budi-avatar.jpg` terunduh ke perangkat
21. Verifikasi isi file terunduh sama dengan file sumber `budi-avatar.jpg`
22. Verifikasi tidak ada toast sukses
23. Verifikasi jumlah total baris tabel utama sama dengan hasil langkah 17
24. Buka modal Recycle Bin
25. Verifikasi jumlah total baris Recycle Bin sama dengan hasil langkah 10
26. Tutup modal Recycle Bin dengan `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian P-5 (butir b): TC-55 (isi file terunduh dibandingkan secara binary, kelas f) berada di spec fungsional ini sebagai satu objek uji ringan tanpa harness eksternal selain pembacaan file terunduh.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 dan 15 (menutup tab baru), langkah 10, 17 (mencatat baseline jumlah baris untuk klausa "Tabel dan Recycle Bin tidak berubah"), langkah 16 dan 26 (menutup modal), langkah 24 (membuka Recycle Bin untuk memeriksa jumlah baris).
- Langkah 4 dan 7 (asersi absence) didahului anchor positif tab baru terbuka (langkah 3) pada pemicu yang sama; langkah 22 didahului file terunduh (langkah 20) sesuai 8b butir 11.
- Langkah 6 mengasersi bahwa Search, filter, sort, paginasi, dan pilihan baris tetap pada keadaan awal (tanpa Search, filter, sort, atau baris terpilih; halaman 1) karena TC-48 tidak mengubahnya sebelum klik.
- Temuan untuk QA:
  - TC-48 Expected c ("tanpa perubahan ... Search, filter, sort, paginasi, dan pilihan baris") tidak menyebut keadaan awal yang diubah sebelum klik; spec mengasersi keadaan default tetap.
  - TC-55 Expected a ("isi sama dengan file sumber") tidak menyebut file sumber pembanding; spec memakai file gambar sumber `budi-avatar.jpg` yang disediakan tim FE.
  - F01 dan R01 adalah baris Pre-setup bersama yang hanya dibaca. Bila spec lain menghapus baris itu, spec ini gagal; seeding ulang Tabel A2 dan A3 di hook `before` disediakan tim FE/BE.
  - Mekanisme fixture BE untuk file fisik tidak disebut di TC, PRD, atau LLD (S-13).
