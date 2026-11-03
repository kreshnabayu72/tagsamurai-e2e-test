---
id: TC-FA-PREF-E2E-133-sinkronisasi-akun-default-tidak-dapat-dihapus-riwayat-log-tidak-berubah-mata-uang-dan-format-tanggal-changelog
title: "Sinkronisasi: Akun Default Tidak Dapat Dihapus, Riwayat Log Tidak Berubah, Mata Uang, dan Format Tanggal Changelog"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-404
  - TC-FA-PREF-406
  - TC-FA-PREF-407
  - TC-FA-PREF-408
coverage:
  web: automated
---

# Sinkronisasi: Akun Default Tidak Dapat Dihapus, Riwayat Log Tidak Berubah, Mata Uang, dan Format Tanggal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Chart of Accounts (PC-5): 4-9100 – Laba Pelepasan Aset (Gain on Disposal, Active), 5-9100 – Rugi Pelepasan Aset (Loss on Disposal, Active). Asset Class (PC-6) dan tiga pelepasan belum diposting (PC-7) untuk TC-FA-PREF-406. Global Settings > General (PC-15): mata uang IDR, format tanggal dd/MM/yy HH:mm 24 jam, Time Zone Asia/Jakarta. Entri Changelog TC-FA-PREF-408 (Edit, Date 23 Oktober 2026 pukul 08:45, Default Capitalization Threshold) disediakan tim FE/BE dan dikenali lewat kolom Date.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): perubahan nama akun 4-9100 lewat fixture BE sebagai pemicu perubahan state; seed entri Changelog bertanggal. Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, kunci periode) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: mata uang Global Settings > General (global; suite serial) dan nama akun 4-9100 serta Preferences company. Mata uang dikembalikan ke IDR di langkah 29 dan di hook `after`; nama akun dan Preferences dipulihkan antar-TC dan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-404: Akun default company tidak dapat dihapus di Chart of Accounts dan nilai tersimpan Preferences tidak berubah

1. Seed Preferences: Default Loss on Disposal tersimpan "5-9100 – Rugi Pelepasan Aset" hingga tersimpan (precondition TC, tidak diasersi)
2. Buka Settings > Accounting > Chart of Accounts
3. Ketik Search "5-9100", tekan Enter
4. Pilih Delete pada akun 5-9100 – Rugi Pelepasan Aset
5. Verifikasi dialog blok berjudul "Cannot Delete Account" tampil
6. Tutup dialog "Cannot Delete Account"
7. Verifikasi akun 5-9100 – Rugi Pelepasan Aset tetap ada di Chart of Accounts (tampil pada hasil Search)
8. Klik (←) pada kotak Search
9. Buka Settings > Accounting > Preferences dan amati field Default Loss on Disposal
10. Verifikasi field Default Loss on Disposal tetap memuat "5-9100 – Rugi Pelepasan Aset"
11. Verifikasi field Default Loss on Disposal tidak menampilkan helper peringatan
12. Pulihkan Preferences ke nilai awal PC-1 lewat seed hingga tersimpan

### TC-FA-PREF-406: Riwayat log tidak berubah saat nama akun diubah di Chart of Accounts

13. Seed kondisi precondition TC: Default Gain on Disposal tersimpan kosong; Asset Class IT Equipment dan Vehicles mengosongkan akun Gain; tiga pelepasan belum diposting (PC-6, PC-7), lalu muat ulang halaman Preferences
14. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE
15. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
16. Klik [Save changes]
17. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
18. Klik [Save] pada dialog Save Changes
19. Tunggu aksi selesai
20. Ubah nama akun 4-9100 menjadi "Laba Penjualan Aset" di Settings > Accounting > Chart of Accounts lewat fixture BE hingga tersimpan
21. Buka Settings > Accounting > Preferences, klik ikon View history, dan amati baris Default Gain on Disposal
22. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
23. Verifikasi baris baru Changelog Field = Default Gain on Disposal tetap New Value = "4-9100 – Laba Pelepasan Aset" (nama lama), tidak berubah menjadi "4-9100 – Laba Penjualan Aset"
24. Tutup modal Changelog
25. Kembalikan nama akun 4-9100 menjadi "Laba Pelepasan Aset" lewat fixture BE hingga tersimpan (DC-6), lalu pulihkan Preferences ke nilai awal PC-1 lewat seed

### TC-FA-PREF-407: Nilai tersimpan threshold tidak dikonversi saat mata uang General Settings berubah

26. Buka Global Settings > General dan ubah mata uang menjadi USD, lalu simpan
27. Buka Settings > Accounting > Preferences
28. Verifikasi CurrencyInput Default Capitalization Threshold menampilkan nilai 5.000.000 tanpa konversi dalam format mata uang USD dengan simbol "$ " dan dua desimal ("$ 5.000.000,00")
29. Kembalikan mata uang Global Settings > General ke IDR hingga tersimpan

### TC-FA-PREF-408: Kolom Date modal Changelog mengikuti format tanggal General Settings

30. Seed entri Changelog Edit tanggal 23 Oktober 2026 pukul 08:45 pada Default Capitalization Threshold dan atur format tanggal Global Settings > General dd/MM/yy HH:mm 24 jam (PC-15) lewat kemampuan BE; muat ulang halaman Preferences
31. Klik ikon View history untuk membuka modal Changelog: Preferences
32. Pindah halaman modal Changelog sampai entri Edit tanggal 23 Oktober 2026 pukul 08:45 pada Default Capitalization Threshold tampil
33. Amati kolom Date pada entri tanggal 23 Oktober 2026
34. Verifikasi kolom Date entri itu tampil 23/10/26 08:45
35. Tutup modal Changelog

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Accounting Period, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 3, 6, 8, 12, 13, 14, 19, 24, 25, 29, 30, 32, 35 (seed precondition TC, menunggu aksi selesai, Search untuk menemukan baris target (R-16, 8b butir 12), membersihkan Search, pemulihan state antar-TC).
- Perubahan nama akun pada TC-FA-PREF-406 dilakukan lewat fixture BE (pemicu perubahan state; "... hingga ... tersimpan", R-20); Delete akun pada TC-FA-PREF-404 dijalankan lewat UI sesuai TC karena dialog blok adalah objek asersi.
- TC-FA-PREF-408: baris seed dikenali lewat kolom Date yang ditulis di Prerequisites dan spec memuat langkah pindah halaman sampai baris itu teramati (S-14).
- `Verifikasi` jumlah baris Changelog bertambah 1 pada TC-FA-PREF-406 ditambahkan sebelum baris Default Gain on Disposal dibaca karena entri hasil aksi spec diperlakukan sebagai entri baru (S-12, S-14, S-03).
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - TC-FA-PREF-407 menulis string "$ 5.000.000,00" yang diturunkan dari aturan GSET-LOGIC-02d, bukan dikutip persis dari General Settings (catatan di TC sendiri); spec mengikuti TC.
  - Post Condition TC-FA-PREF-404, 406, dan 407 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).
  - Expected TC-FA-PREF-404 a menyebut dialog blok "Cannot Delete Account" tanpa label tombol penutup; spec menulis "Tutup dialog" sebagai langkah penghubung.
  - TC-FA-PREF-407 dan 408 tidak menyebut cara menyimpan perubahan Global Settings > General dan cara mengubah format tanggal; spec memakai kemampuan BE untuk format tanggal dan mengikuti teks TC untuk mata uang.
