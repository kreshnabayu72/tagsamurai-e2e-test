---
id: TC-FA-COA-E2E-041-search-tabel-perilaku-kotak-search-dan-trim-spasi
title: "Search Tabel: Perilaku Kotak Search dan Trim Spasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-229
  - TC-FA-COA-316
  - TC-FA-COA-317
  - TC-FA-COA-318
  - TC-FA-COA-319
coverage:
  web: automated
---

# Search Tabel: Perilaku Kotak Search dan Trim Spasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`): akun P1 sampai P5 ada di tabel; pada ukuran halaman bawaan (10 baris, urut Account Code A-Z) berdasarkan kode Pre-setup di TC hanya P3 yang tampil di halaman 1 tanpa filter, P1, P2, dan P5 berada di halaman lain dan dibuktikan lewat Search.
  - P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Function Depreciation Expense).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Account Name `Repairs & Maintenance Expense`).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Function Gain on Disposal; tidak mengandung `Repairs` maupun `Depreciation`).
  - P5 `Fixture.settingsChartOfAccounts.p5` (Account Name `Capitalization Clearing – Repairs`).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-316: Ikon Search membuka kotak dengan auto-focus, tooltip, dan placeholder

1. Arahkan kursor ke ikon Search
2. Verifikasi tooltip ikon Search `Search`
3. Klik ikon Search
4. Verifikasi kotak Search terbuka dengan fokus pada input
5. Verifikasi placeholder kotak Search `Search account...`
6. Klik `(←)` pada kotak Search

### TC-FA-COA-317: Ikon (✕) menghapus teks tanpa mereset tabel

7. Ketik Search `Repairs`, tekan Enter
8. Verifikasi tabel menampilkan hasil yang cocok (baris P2 `Fixture.settingsChartOfAccounts.p2.code` dan P5 `Fixture.settingsChartOfAccounts.p5.code` tampil)
9. Klik ikon `(✕)` di kotak Search
10. Verifikasi teks Search kosong
11. Verifikasi tabel tetap menampilkan hasil sebelumnya (baris P2 dan P5 tampil)
12. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tidak tampil (tabel belum direset)
13. Klik `(←)` pada kotak Search

### TC-FA-COA-318: Enter pada input kosong mereset hasil pencarian

14. Ketik Search `Repairs`, tekan Enter
15. Klik ikon `(✕)` di kotak Search
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan seluruh akun (baris P3 `Fixture.settingsChartOfAccounts.p3.code` tampil pada halaman 1; P3 tidak mengandung `Repairs`, jadi tampilnya membuktikan hasil Search sudah direset)
18. Klik `(←)` pada kotak Search

### TC-FA-COA-319: Ikon collapse (←) menutup kotak Search dan langsung mereset hasil

19. Ketik Search `Repairs`, tekan Enter
20. Klik ikon `(←)` di kotak Search
21. Verifikasi kotak Search tertutup menjadi ikon
22. Verifikasi tabel langsung kembali menampilkan seluruh akun (baris P3 `Fixture.settingsChartOfAccounts.p3.code` tampil pada halaman 1; P3 tidak mengandung `Repairs`)

### TC-FA-COA-229: Spasi awal dan akhir dibuang, spasi di tengah dipertahankan

23. Ketik Search `Depreciation`, tekan Enter
24. Catat daftar baris hasil Search `Depreciation`
25. Ganti isi kotak Search dengan ` Depreciation ` (dengan spasi di awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan hasil query `Depreciation` yang dicatat pada langkah 24
27. Verifikasi isi kotak Search tidak berubah (tetap ` Depreciation `)
28. Verifikasi tidak ada pesan atau indikator
29. Ganti isi kotak Search dengan `Depreciation Expense` (spasi di tengah), tekan Enter
30. Verifikasi hasil memuat akun yang mengandung `Depreciation Expense` (baris P1 tampil)
31. Verifikasi spasi di tengah menjadi bagian substring (setiap baris hasil mengandung frasa `Depreciation Expense` utuh)
32. Ganti isi kotak Search dengan tiga spasi saja, tekan Enter
33. Verifikasi query dianggap kosong dan tabel kembali ke semua data (baris P3 `Fixture.settingsChartOfAccounts.p3.code` tampil pada halaman 1; P3 tidak mengandung `Depreciation`)
34. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 6, 13, 18, 34 (`(←)` menutup kotak Search dan mereset tabel sebelum TC berikutnya, S-09); langkah 24 (mencatat hasil `Depreciation` sebagai pembanding "hasil sama dengan query `Depreciation`").
- Langkah 14 sampai 16 menyalin langkah 1 dan 2 TC-FA-COA-318 secara utuh (S-04); TC itu tidak bergantung pada hasil langkah 7 sampai 12.
- Langkah 17, 22, dan 33: tabel tanpa filter menampilkan 10 baris per halaman urut Account Code A-Z; berdasarkan kode Pre-setup di TC hanya P3 (sekitar posisi 7) berada di halaman 1, sedangkan P1 (sekitar posisi 25), P2 (sekitar posisi 53), dan P5 (sekitar posisi 56) berada di halaman lain, jadi P3 dipakai sebagai pembanding reset (S-14, R-23). Hasil Search yang tidak lagi menjadi satu-satunya isi tabel dibuktikan oleh tampilnya P3 yang tidak cocok dengan query.
- Langkah 8 menjadi anchor positif bagi asersi absence langkah 12 (8b.2).
- Kotak Search pada tabel mulai dalam keadaan tertutup (ikon); langkah "Ketik Search X, tekan Enter" membuka input bila perlu (8b.9). Langkah 1 sampai 4 menguji pembukaan lewat klik ikon.
- Temuan untuk QA:
  - TC-FA-COA-229 Expected butir a ("hasil sama dengan query `Depreciation`") tidak menyebut pembanding; spec mencatat hasil query `Depreciation` lebih dulu (langkah 24).
  - TC-FA-COA-229 Expected butir b ("spasi di tengah menjadi bagian substring") tidak menyatakan cara memeriksanya; spec mengasersi setiap baris hasil mengandung frasa `Depreciation Expense` utuh.
  - TC-FA-COA-317 butir b ("tabel tetap menampilkan hasil sebelumnya") tidak menyebut baris yang dicek; spec memakai P2 dan P5 (mengandung `Repairs`) dan P1 sebagai pembanding yang tidak tampil.
