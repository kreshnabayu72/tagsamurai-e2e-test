---
id: TC-FA-PREF-E2E-101-changelog-search-kolom-tersembunyi-trim-spasi-serta-kombinasi-search-dan-filter
title: "Changelog Search: Kolom Tersembunyi Tidak Dicari, Trim Spasi, serta Kombinasi Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-303
  - TC-FA-PREF-304
  - TC-FA-PREF-318
  - TC-FA-PREF-319
coverage:
  web: automated
---

# Changelog Search: Kolom Tersembunyi Tidak Dicari, Trim Spasi, serta Kombinasi Search dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PB-1; Changelog Preferences berisi 9 entri contoh PB-C1 (format tanggal dd/MM/yy dan 24 jam). Posisi baris pada urutan default Date Newest First (sama dengan TC-FA-PREF-290): baris 1 Edit Chart of Accounts Default Capitalization Offset (Budi S); baris 2 dan baris 3 Edit Disposal Disposal Documents — Sell dan — Scrap, Optional ke Required (Rina A); baris 4 Edit Journal Export Journal Grouping (Budi S); baris 5 Edit Disposal Default Gain on Disposal (Rina A); baris 6 Edit General Fiscal Year Start, January ke April (Rina A); baris 7 Edit General First Accounting Period (Rina A); baris 8 Edit Capitalization Default Capitalization Threshold (Rina A); baris 9 Create Preferences (Budi S). Urutan tulis seed: pada Date yang sama baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed PB-C1 mengatur Changelog company seed ke tepat 9 entri (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE): pemulihan konfigurasi kolom Changelog dengan menghapus preferensi kolom di browser pada hook `after` sebagai cadangan; pemulihan utama dilakukan langkah 8 (bagian 8b butir 13, R-24).
- Spec ini tidak menulis ke Changelog; Search, Filter, dan Column Visibility tidak mengubah state server.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-303: Search tidak mencari kolom yang disembunyikan dan kembali mencari saat ditampilkan lagi

1. Klik ikon View history di header tab Preferences
2. Klik ikon header kolom Actions (⋯)
3. Hapus centang kolom Field pada panel Column Visibility
4. Tutup panel Column Visibility
5. Ketik Search "Fiscal", tekan Enter
6. Verifikasi tabel menampilkan empty state "No results found"
7. Kosongkan isi kotak search, tekan Enter
8. Klik ikon header kolom Actions (⋯), lalu centang kembali kolom Field pada panel Column Visibility
9. Tutup panel Column Visibility
10. Ketik Search "Fiscal", tekan Enter
11. Verifikasi tabel menampilkan hanya baris 6
12. Kosongkan isi kotak search, tekan Enter

### TC-FA-PREF-304: Search membuang spasi di awal dan akhir kata kunci tanpa mengubah isi input

13. Ketik Search "  Fiscal  " (dua spasi di awal dan akhir), tekan Enter
14. Verifikasi tabel menampilkan hanya baris 6
15. Verifikasi isi kotak pencarian tetap menampilkan spasi yang diketik
16. Kosongkan isi kotak search, tekan Enter

### TC-FA-PREF-318: Search lalu Filter menghasilkan irisan baris

17. Ketik Search "Rina", tekan Enter
18. Verifikasi tabel menampilkan baris 2, 3, 5, 6, 7, dan 8
19. Klik ikon Filter
20. Pilih opsi Disposal pada dropdown Section
21. Klik [Apply]
22. Verifikasi tabel menampilkan baris 2, baris 3, dan baris 5
23. Verifikasi kata kunci Search tetap "Rina"
24. Klik ikon [✕] di header modal Changelog
25. Muat ulang halaman dengan F5

### TC-FA-PREF-319: Filter lalu Search menghasilkan irisan baris yang sama

26. Klik ikon View history di header tab Preferences
27. Klik ikon Filter
28. Pilih opsi Disposal pada dropdown Section
29. Klik [Apply]
30. Verifikasi tabel menampilkan baris 2, baris 3, dan baris 5
31. Ketik Search "Rina", tekan Enter
32. Verifikasi tabel menampilkan baris 2, baris 3, dan baris 5
33. Verifikasi filter Section tetap aktif
34. Klik ikon [✕] di header modal Changelog

## Notes

- Langkah penghubung (S-03, S-09): langkah 4 dan 9 (menutup panel Column Visibility agar toolbar Search dapat diklik), langkah 7, 12, dan 16 (mengosongkan kotak Search dan menyetel ulang tabel), langkah 24 dan 25 (menutup modal dan muat ulang untuk membersihkan Search dan Filter sebelum TC-FA-PREF-319), langkah 34 (menutup modal). Langkah 8 memulihkan kolom Field yang disembunyikan pada langkah 3 (bagian 8b butir 13, R-24) dan sekaligus langkah TC-FA-PREF-303 butir 5; hook `after` hanya cadangan.
- Langkah 6 memakai empty state "No results found" sebagai anchor positif untuk absence hasil Search (bagian 8b butir 2); langkah 11, 14, 18, 22, 30, dan 32 ("hanya baris N") didahului baris seed yang dijamin ada oleh seed PB-C1 (Prerequisites).
- Temuan untuk QA:
  - TC-FA-PREF-303, 304, 318, dan 319 mengasersi posisi baris seed ("baris 6", "baris 2, 3, 5, 6, 7, dan 8") yang bergantung pada Changelog tepat 9 entri seed; Changelog adalah audit trail permanen yang tumbuh karena Save pada spec lain (S-12, S-14). Spec memakai asumsi seed PB-C1 mereset Changelog company seed ke tepat 9 entri (seed terisolasi menurut Catatan TC); bila reset tidak tersedia, Expected perlu ditulis ulang relatif atau dibatasi Filter Date pada tanggal seed.
  - TC-FA-PREF-303 tidak menyebut apakah panel Column Visibility perlu ditutup atau perubahan kolom perlu disimpan; spec menambahkan langkah menutup panel (langkah 4 dan 9) sebagai langkah penghubung dan tidak memakai tombol [Save] karena TC tidak menyebutnya.
  - TC-FA-PREF-318 dan 319 tidak menyebut cara mengosongkan Filter; spec membersihkannya lewat muat ulang halaman (langkah 25).
  - TC-FA-PREF-318 Expected a menyebut baris 2, 3, 5, 6, 7, dan 8 untuk kata kunci "Rina" (kolom Modified By); spec mengasersi himpunan baris tanpa mengandalkan urutan di antara baris yang berbagi Date yang sama.
