---
id: TC-AC-PF-E2E-056-estimated-reference-price-edit-custom-plan-serta-create-dan-edit-default-plan
title: "Estimated Reference Price pada Edit Custom Plan serta Create dan Edit Default Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-217
  - TC-AC-PF-609
  - TC-AC-PF-610
coverage:
  web: automated
---

# Estimated Reference Price pada Edit Custom Plan serta Create dan Edit Default Plan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Harga W (Wallet Feature Pricing): Base Reference Price Principal: Asset Name cap 50 = $10, Group count 3 = $25, Group count 25 = $90, Open API ON = $15; Sell Reference Price Distributor: Asset Name cap 50 = $12, Group count 3 = $30, Group count 25 = $110, Open API ON = $20; field lain tanpa harga terdaftar. Dataset Plan V2 (FAMS dengan slot Paid tersisa). Dataset Plan A dengan default plan `Growth` v5 (Asset Name cap 50, Group count 3, Open API ON, API call quota 100K/month). Growth Tier v20 (Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan Growth v5; satu client `PT Wahana Nusantara` memegang v20).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth` v5, `Growth Tier` v20) dipakai apa adanya, sebagai target Edit yang dibuka lalu ditutup tanpa Save; Last Updated dan Changelog tidak berubah; pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada (spec tidak menyimpan plan).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` memulihkan Dataset dan Wallet Feature Pricing lewat fixture backend dan mengembalikan sesi ke akun default suite.

## Test Steps

### Create Default Plan (TC-AC-PF-609)

1. Buka tab `Default`, sub-tab `Active`
2. Klik `+ Default Plan`
3. Pilih Product `FAMS` dan Pricing Type `Paid`
4. Verifikasi Estimated Total awal `$0`
5. Ubah Asset Name cap ke `50` dan Group count ke `3`
6. Nyalakan Open API lalu pilih API call quota `100K/month`
7. Buka dropdown Group count
8. Verifikasi opsi Group count tampil `3 (+$25)` dan `25 (+$90)`
9. Tekan Esc, lalu buka dropdown Asset Name cap
10. Verifikasi opsi Asset Name cap tampil `50 (+$10)`
11. Tekan Esc untuk menutup dropdown Asset Name cap
12. Verifikasi Estimated Total `$50` (Asset Name cap 50 = $10, Group count 3 = $25, Open API ON = $15)
13. Klik breadcrumb segmen `Plans & Features`
14. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
15. Klik `[Leave]`

### Edit Default Plan (TC-AC-PF-610)

16. Buka Edit `Growth` pada tab `Default`, sub-tab `Active`
17. Verifikasi Estimated Total awal `$50` (Asset Name cap 50 = $10, Group count 3 = $25, Open API ON = $15)
18. Ubah Group count `3` → `25`
19. Verifikasi Estimated Total `$115` (Asset Name cap 50 = $10, Group count 25 = $90, Open API ON = $15)
20. Klik breadcrumb segmen `Plans & Features`
21. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
22. Klik `[Leave]`

### Edit Custom Plan (TC-AC-PF-217)

23. Buka tab `Custom`, sub-tab `Active`
24. Buka Edit `Growth Tier`
25. Verifikasi Estimated Total awal `$105` (Asset Name cap 500 tanpa harga = $0, Group count 25 = $90, Open API ON = $15)
26. Ubah Group count `25` → `3`
27. Verifikasi Estimated Total `$40` (Group count 3 = $25, Open API ON = $15)
28. Klik breadcrumb segmen `Plans & Features`
29. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
30. Klik `[Leave]`

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 9, 11, 13, 20, 23, 28.
- Form dirty ditutup lewat breadcrumb, verifikasi dialog `Unsaved Changes`, lalu `[Leave]` (S-08); form full-page tidak memiliki `✕`. Edit `Growth` dan `Growth Tier` ditutup tanpa `[Save]` sehingga Last Updated dan Changelog keduanya tidak berubah.
- Langkah penghubung: baris target Edit ditemukan pada daftar tab yang sedang terbuka (R-16); jika tidak tampil pada halaman pertama, ketik Search nama plan dan tekan Enter sebagai langkah penghubung.
- Temuan untuk QA: Expected b TC-AC-PF-609 menyebut opsi Asset Name cap `50 (+$10)` tetapi langkah TC hanya membuka dropdown Group count; spec menambahkan langkah membuka dropdown Asset Name cap.
