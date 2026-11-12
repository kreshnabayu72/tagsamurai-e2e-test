---
id: TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan
title: "Tampilan Tabel Asset Class: Loading, Empty State Search, Urutan Awal, Link Asset Names, Tooltip Accounts, dan Format Commercial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-7
  - TC-FA-FAAC-10
  - TC-FA-FAAC-11
  - TC-FA-FAAC-12
  - TC-FA-FAAC-13
  - TC-FA-FAAC-670
  - TC-FA-FAAC-671
coverage:
  web: automated
---

# Tampilan Tabel Asset Class: Loading, Empty State Search, Urutan Awal, Link Asset Names, Tooltip Accounts, dan Format Commercial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Asset Names 12), VEHICLES, IT-EQ, MACHINERY (Units of Production, Total Estimated Units 80,000 Unit Type Hour meter), BLDG (Asset Names 0), STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive).
- Data Pre-setup tambahan per TC (hanya dibaca): B-ACCINA (Active) memetakan kelima akun dengan dua akun Inactive 11004 dan 11005 (TC-FA-FAAC-670); Asset Class Straight Line tanpa Residual Value B-LIFE1 (Useful Life 12 bulan), B-LIFE2 (18), B-LIFE3 (8), B-LIFE4 (120) (TC-FA-FAAC-671). Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk menahan respons request data tabel Asset Class dan melepasnya (TC-FA-FAAC-7, menahan respons hanya untuk mengamati Loading). Endpoint yang ditahan tidak tertulis di TC, PRD, atau LLD sumber dan ditentukan tim FE (S-13).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-7: Tampilan loading tabel Asset Class

1. Tahan respons request data tabel Asset Class dengan intercept
2. Klik menu Accounting di sidebar
3. Klik tab Asset Class
4. Verifikasi tabel menampilkan loading Shimmer selama respons ditahan
5. Lepas tahanan respons dan hapus intercept
6. Verifikasi Shimmer hilang
7. Verifikasi baris Asset Class tampil

### TC-FA-FAAC-10: Empty state hasil Search tidak ditemukan

8. Ketik Search `zzzzzz`, tekan Enter
9. Verifikasi EmptyState menampilkan illustration, title `No results found`, dan description `Try adjusting your search or filter.`
10. Verifikasi tidak ada link `Use recommended classes` pada EmptyState
11. Verifikasi tidak ada tombol aksi pada EmptyState
12. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
13. Ubah ukuran halaman menjadi 100

### TC-FA-FAAC-11: Urutan awal tabel Asset Class

14. Verifikasi baris terurut Class Code A-Z dengan urutan relatif baris contoh BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES

### TC-FA-FAAC-12: Kolom Asset Names, link untuk angka lebih dari 0

15. Verifikasi angka 12 pada kolom Asset Names baris HEAVY-EQ tampil sebagai link (Clickable)
16. Verifikasi angka 0 pada kolom Asset Names baris BLDG tampil sebagai teks biasa (Not clickable)
17. Klik angka 0 pada baris BLDG
18. Verifikasi tidak ada halaman yang terbuka dan tabel Asset Class tetap tampil

### TC-FA-FAAC-670: Tooltip ikon Accounts bentuk jamak untuk dua akun Inactive

19. Arahkan kursor ke ikon Accounts pada baris B-ACCINA
20. Verifikasi ikon Accounts berstatus warning (kelima akun terpetakan dengan akun Inactive)
21. Verifikasi tooltip berbunyi `Accounts 11004, 11005 are inactive. Journals for this asset class will be held at export.` dengan kode akun berurutan A-Z dipisah koma
22. Verifikasi label aksesibilitas ikon Accounts berbunyi `Accounts 11004, 11005 are inactive. Journals for this asset class will be held at export.`

### TC-FA-FAAC-671: Format ringkasan Useful Life dan Units of Production pada kolom Commercial

23. Verifikasi sel Commercial baris B-LIFE1 berbunyi `Straight Line · 1 yr`
24. Verifikasi sel Commercial baris B-LIFE2 berbunyi `Straight Line · 1 yr 6 mo`
25. Verifikasi sel Commercial baris B-LIFE3 berbunyi `Straight Line · 8 mo`
26. Verifikasi sel Commercial baris B-LIFE4 berbunyi `Straight Line · 10 yrs`
27. Verifikasi sel Commercial baris MACHINERY berbunyi `Units of Production · 80,000 Hour meter`

### TC-FA-FAAC-13: Klik angka Asset Names lebih dari 0 membuka Detail tab Asset Names

28. Ubah ukuran halaman kembali menjadi 10
29. Ketik Search `HEAVY-EQ`, tekan Enter
30. Klik angka 12 pada kolom Asset Names baris HEAVY-EQ
31. Verifikasi halaman Detail Asset Class HEAVY-EQ terbuka dengan tab `Asset Names` aktif

## Notes

- Langkah penghubung (S-03): langkah 12 (menutup input Search dan mereset tabel, S-09; R-16), langkah 13 (ukuran halaman 100 agar baris contoh dan baris B-* terjangkau sesuai butir Precondition TC-11, 12, 670, 671; S-14), langkah 28 (memulihkan ukuran halaman 10), langkah 29 (Search untuk menemukan baris target karena HEAVY-EQ tidak dijamin berada di halaman 1; R-16).
- TC-FA-FAAC-13 diletakkan terakhir karena membuka halaman Detail (aksi yang meninggalkan tabel diletakkan di akhir, S-10).
- Nama literal Pre-setup (HEAVY-EQ, BLDG, B-ACCINA, B-LIFE1 sampai B-LIFE4, dan sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, nilai, dan urutan persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-FAAC-670 butir a berbunyi "berkondisi lengkap dengan akun Inactive (warning)" tanpa menyebut warna atau ikon; spec mengasersi status warning.
  - TC-FA-FAAC-11 menyebut "urutan relatif baris contoh" sementara data B-* ikut berada di tabel; spec mengasersi urutan relatif sembilan baris contoh pada ukuran halaman 100.
