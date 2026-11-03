---
id: TC-FA-PREF-E2E-132-sinkronisasi-chart-of-accounts-nama-akun-inactive-dan-function-berubah
title: "Sinkronisasi Chart of Accounts: Nama Akun, Akun Inactive, dan Function Akun Berubah pada Select Akun Preferences"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-401
  - TC-FA-PREF-402
  - TC-FA-PREF-403
  - TC-FA-PREF-405
coverage:
  web: automated
---

# Sinkronisasi Chart of Accounts: Nama Akun, Akun Inactive, dan Function Akun Berubah pada Select Akun Preferences

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Chart of Accounts (PC-5): 4-9100 – Laba Pelepasan Aset (Gain on Disposal, Active), 5-9100 – Rugi Pelepasan Aset, 4-1500 – Pendapatan Lain-lain. Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6) untuk TC-FA-PREF-403.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): perubahan nama, status, dan function akun 4-9100 di Chart of Accounts lewat fixture BE sebagai pelaku perubahan state (hanya pemicu, bukan objek asersi; TC menulisnya sebagai aksi UI di Chart of Accounts tanpa merinci UI-nya); function pengganti akun pada TC-FA-PREF-405 ditetapkan tim FE. Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, kunci periode) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: nama, status, dan function akun 4-9100 serta Preferences company. Seluruhnya dipulihkan antar-TC dan di hook `after` (nama akun kembali "Laba Pelepasan Aset", status Active, function Gain on Disposal; DC-6).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-401: Select akun Preferences mencerminkan nama akun yang diubah di Chart of Accounts

1. Seed Preferences: Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" hingga tersimpan (precondition TC, tidak diasersi)
2. Ubah nama akun 4-9100 menjadi "Laba Penjualan Aset" di Settings > Accounting > Chart of Accounts lewat fixture BE hingga tersimpan
3. Buka Settings > Accounting > Preferences
4. Verifikasi Select Default Gain on Disposal menampilkan nilai terpilih "4-9100 – Laba Penjualan Aset"
5. Buka Select Default Gain on Disposal
6. Verifikasi opsi akun 4-9100 pada daftar tampil sebagai "4-9100 – Laba Penjualan Aset"
7. Tutup daftar opsi Select Default Gain on Disposal
8. Kembalikan nama akun 4-9100 menjadi "Laba Pelepasan Aset" lewat fixture BE hingga tersimpan (DC-6), lalu pulihkan Preferences ke nilai awal PC-1 lewat seed

### TC-FA-PREF-402: Akun default yang menjadi Inactive menampilkan helper peringatan dan nilainya dipertahankan

9. Seed Preferences: Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" hingga tersimpan (precondition TC, tidak diasersi)
10. Ubah status akun 4-9100 menjadi Inactive di Settings > Accounting > Chart of Accounts lewat fixture BE hingga tersimpan
11. Buka Settings > Accounting > Preferences dan amati field Default Gain on Disposal
12. Verifikasi Select Default Gain on Disposal tetap memuat nilai tersimpan "4-9100 – Laba Pelepasan Aset"
13. Verifikasi helper berseverity warning "This account is inactive. Journals using it are held at export." tampil pada field
14. Kembalikan status akun 4-9100 menjadi Active lewat fixture BE hingga tersimpan, lalu pulihkan Preferences ke nilai awal PC-1 lewat seed

### TC-FA-PREF-403: Akun default tersimpan yang Inactive tidak memblokir Save setting lain

15. Seed Preferences: Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" hingga tersimpan (precondition TC, tidak diasersi), lalu ubah status akun 4-9100 menjadi Inactive lewat fixture BE hingga tersimpan
16. Buka Settings > Accounting > Preferences
17. Ubah Default Capitalization Threshold menjadi "10000000"
18. Klik [Save changes]
19. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
20. Klik [Save] pada dialog Save Changes
21. Verifikasi toast "Success, accounting preferences have been saved." tampil
22. Verifikasi tidak ada caption V-04 pada field akun mana pun
23. Amati field Default Gain on Disposal
24. Verifikasi Default Gain on Disposal tetap "4-9100 – Laba Pelepasan Aset"
25. Verifikasi helper "This account is inactive. Journals using it are held at export." tampil pada field Default Gain on Disposal
26. Kembalikan status akun 4-9100 menjadi Active lewat fixture BE hingga tersimpan, lalu pulihkan Preferences ke nilai awal PC-1 lewat seed

### TC-FA-PREF-405: Akun default yang function-nya berubah menampilkan helper peringatan dan nilai tersimpan dipertahankan

27. Seed Preferences: Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" hingga tersimpan (precondition TC, tidak diasersi)
28. Ubah function akun 4-9100 di Chart of Accounts lewat fixture BE menjadi function selain Gain on Disposal dan Loss on Disposal hingga tersimpan
29. Buka Settings > Accounting > Preferences dan amati field Default Gain on Disposal
30. Verifikasi helper peringatan tampil pada field Default Gain on Disposal (teks helper untuk kasus function berubah menunggu keputusan PM, OI-12; teks tidak diasersi)
31. Verifikasi Select tetap memuat nilai tersimpan "4-9100 – Laba Pelepasan Aset"
32. Kembalikan function akun 4-9100 menjadi Gain on Disposal lewat fixture BE hingga tersimpan, lalu pulihkan Preferences ke nilai awal PC-1 lewat seed

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Accounting Period, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 7, 8, 9, 14, 15, 26, 27, 32 (seed precondition TC, menunggu aksi selesai, Search untuk menemukan baris target (R-16, 8b butir 12), membersihkan Search, pemulihan state antar-TC).
- Perubahan akun 4-9100 (nama, status, function) dijalankan lewat fixture BE yang menggantikan langkah UI Chart of Accounts pada TC (S-04: dijalankan lewat seeding API; S-13: UI Chart of Accounts tidak dirinci di TC dan modulnya bukan objek uji). Langkah ditulis "... hingga ... tersimpan" (R-20).
- TC-FA-PREF-403 asersi absence "tidak ada caption V-04 pada field akun mana pun" didahului `Verifikasi` toast sukses (respons server selesai; 8b butir 2).
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected a TC-FA-PREF-405 menyebut teks helper "menunggu keputusan PM (OI-12)"; teks helper tidak diasersi.
  - Post Condition TC-FA-PREF-401 sampai 405 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).
  - TC-FA-PREF-405 tidak menyebut function pengganti akun 4-9100; spec menyebut "selain Gain on Disposal dan Loss on Disposal" dan meminta tim FE menetapkan function-nya.
