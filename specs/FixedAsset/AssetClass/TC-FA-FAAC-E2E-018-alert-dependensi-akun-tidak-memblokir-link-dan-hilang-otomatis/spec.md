---
id: TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis
title: "Alert Dependensi Akun: Tidak Memblokir Aksi, Link Go to Chart of Accounts, dan Hilang Otomatis Setelah Akun Active Tersedia"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-29
  - TC-FA-FAAC-30
  - TC-FA-FAAC-27
  - TC-FA-FAAC-28
coverage:
  web: automated
---

# Alert Dependensi Akun: Tidak Memblokir Aksi, Link Go to Chart of Accounts, dan Hilang Otomatis Setelah Akun Active Tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global, Chart of Accounts bersama per client): keadaan awal yang disiapkan hook `before` lewat fixture BE adalah tidak ada akun Active ber-Account Function Asset Cost, sembilan Asset Class contoh Pre-setup tersedia (HEAVY-EQ dan delapan lainnya, hanya dibaca; nama literal Tabel Data Uji Pre-setup TC), dan akun Inactive ber-Account Function Depreciation Expense bernama `Beban Penyusutan Uji`. Hook `after` memulihkan Chart of Accounts (status akun `Beban Penyusutan Uji` dan akun Active per function) ke keadaan awal run. Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: fixture BE untuk mengatur akun Active per Account Function dan memulihkannya; kemampuan browser menyimpan unduhan dan membaca nama berkas (TC-FA-FAAC-30); disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah Chart of Accounts yang dipakai bersama.

## Test Steps

### TC-FA-FAAC-29: Alert dependensi akun tidak memblokir + Asset Class

1. Verifikasi Alert dependensi akun tampil
2. Klik `[+ Asset Class]`
3. Verifikasi halaman Detail mode Create terbuka dengan breadcrumb `Settings > Accounting > Asset Class > Add Asset Class`
4. Klik breadcrumb `Asset Class` untuk meninggalkan form

### TC-FA-FAAC-30: Alert dependensi akun tidak memblokir Search dan Download

5. Verifikasi Alert dependensi akun tampil
6. Ketik Search `HEAVY`, tekan Enter
7. Verifikasi Search menyaring tabel hingga baris HEAVY-EQ
8. Klik icon Download
9. Klik opsi `Download as CSV`
10. Verifikasi berkas `Asset-Class.csv` terunduh
11. Verifikasi Alert dependensi akun tetap tampil sepanjang aksi
12. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAC-27: Klik link Go to Chart of Accounts pada Alert

13. Atur Chart of Accounts lewat fixture BE hingga tidak ada akun Active ber-Account Function Depreciation Expense dan akun Active untuk function lain tersedia
14. Refresh halaman
15. Klik tab Asset Class
16. Verifikasi Alert dependensi akun tampil
17. Klik link `[Go to Chart of Accounts]` pada Alert
18. Verifikasi tab `Chart of Accounts` menjadi aktif pada halaman Settings > Accounting

### TC-FA-FAAC-28: Alert hilang otomatis setelah akun Active tersedia

19. Klik tab Asset Class
20. Verifikasi Alert menyebut Depreciation Expense
21. Klik link `[Go to Chart of Accounts]` pada Alert
22. Jadikan akun `Beban Penyusutan Uji` berstatus Active di tab Chart of Accounts
23. Tunggu aksi selesai
24. Klik tab Asset Class
25. Verifikasi tabel Asset Class tampil
26. Verifikasi Alert dependensi akun hilang tanpa aksi lain dari user

## Notes

- Langkah penghubung (S-03): langkah 4 dan 12 (meninggalkan form dan mereset Search sebelum blok berikutnya, S-09), langkah 13 sampai 15 (mengatur Chart of Accounts lewat fixture BE sebagai precondition TC-FA-FAAC-27 dan memuat ulang tab), langkah 19 (kembali ke tab Asset Class agar TC-FA-FAAC-28 langkah 1 terpenuhi), langkah 23 (tunggu aksi selesai sebelum berpindah tab; 8b butir 8).
- Urutan TC dalam spec: 29, 30, 27, 28 (blok yang tidak mengubah Chart of Accounts lebih dulu; TC-FA-FAAC-28 mengaktifkan akun di akhir, S-10).
- TC-FA-FAAC-24, TC-FA-FAAC-25, TC-FA-FAAC-26, dan TC-FA-FAAC-31 (teks dan posisi Alert) ada di spec 012.
- Anchor: langkah 25 (tabel tampil) mendahului absence Alert pada langkah 26 (8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-28 langkah 3 ("Jadikan akun ... berstatus Active di tab Chart of Accounts") tidak menyebut kontrol yang diklik; spec menuliskannya sebagai aksi tanpa mengarang kontrol.
  - TC-FA-FAAC-27 langkah 1 tidak menyebut Chart of Accounts function lain; spec mengandaikan akun Active untuk function lain tersedia (precondition hanya menyebut Depreciation Expense).
  - TC-FA-FAAC-30 butir b menyebut berkas `Asset-Class.csv`; isi berkas tidak diasersi.
