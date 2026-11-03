---
id: TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal
title: "Estimated Reference Price dan Estimated Total Create Custom Plan oleh Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-141
  - TC-AC-PF-142
  - TC-AC-PF-144
  - TC-AC-PF-145
coverage:
  web: automated
---

# Estimated Reference Price dan Estimated Total Create Custom Plan oleh Principal

## Prerequisites

- Mode: FE+BE (intercept parsial atas backend nyata untuk TC-AC-PF-145: Spectra.intercept menggagalkan permintaan katalog Wallet Feature Pricing).
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Harga W (Wallet Feature Pricing): Base Reference Price Principal: Asset Name cap 50 = $10, Group count 3 = $25, Group count 25 = $90, Open API ON = $15; Sell Reference Price Distributor: Asset Name cap 50 = $12, Group count 3 = $30, Group count 25 = $110, Open API ON = $20; field lain tanpa harga terdaftar. Dataset Plan A dengan default plan `Growth` (Asset Name cap 50, Group count 3, Open API ON). Kemampuan menyetel Wallet Feature Pricing disediakan tim FE/BE.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-055`: `Paket Harga Nol-{runId}-055` dan `Paket Wallet Down-{runId}-055`; keduanya tersimpan.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-055`) lewat fixture backend, memulihkan Dataset dan Wallet Feature Pricing, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Harga Wallet Principal (TC-AC-PF-141)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Buka dropdown Group count
5. Verifikasi opsi Group count tampil `3 (+$25)` dan `25 (+$90)`
6. Tekan Esc, lalu buka dropdown Asset Name cap
7. Verifikasi opsi Asset Name cap tampil `50 (+$10)`
8. Tekan Esc untuk menutup dropdown Asset Name cap
9. Verifikasi Estimated Total tampil `$50` (Asset Name cap 50 = $10, Group count 3 = $25, Open API ON = $15; field lain $0)

### Real-time (TC-AC-PF-142)

10. Ganti Group count dari `3` ke `25`
11. Verifikasi Estimated Total tampil `$115`
12. Ganti Group count ke `1`
13. Verifikasi Estimated Total tampil `$25` (Group count tanpa harga terdaftar, Open API tetap ON)

### Field tanpa harga (TC-AC-PF-144)

14. Klik `[Clear Field]` agar form kembali ke kondisi awal
15. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Harga Nol-{runId}-055`
16. Pilih Group hierarchy depth `5`
17. Buka dropdown Group hierarchy depth
18. Verifikasi opsi tanpa harga terdaftar tampil `5 (+$0)`
19. Tekan Esc untuk menutup dropdown Group hierarchy depth
20. Verifikasi opsi `5` dihitung `$0` pada Estimated Total (Estimated Total tetap `$50`)
21. Klik `[Submit]`
22. Verifikasi toast sukses: "Success, custom plan has been created."

### Katalog Wallet tidak terjangkau (TC-AC-PF-145)

23. Klik breadcrumb sub-tab `Active`
24. Aktifkan `Spectra.intercept` yang menggagalkan permintaan katalog Wallet Feature Pricing
25. Klik `+ Custom Plan` pada toolbar
26. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Wallet Down-{runId}-055`
27. Hover Estimated Reference Price Group count
28. Verifikasi Estimated Reference Price menampilkan `—` dengan tooltip `Price unavailable`
29. Hover Estimated Total
30. Verifikasi Estimated Total menampilkan `—` dengan tooltip `Price unavailable`
31. Klik `[Submit]`
32. Verifikasi toast sukses: "Success, custom plan has been created."
33. Lepas intercept Wallet Feature Pricing

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 8, 14, 19, 23, 33.
- Pengecualian `P-5`: TC-AC-PF-145 (kegagalan katalog Wallet lewat intercept parsial, kelas b objek-uji ringan, tanpa state berat) berada di spec fungsional ini bersama TC-AC-PF-141 yang menguji harga dari katalog yang sama; hanya satu TC objek-uji ringan di spec ini. Intercept dilepas segera sesudah Submit selesai (S-09).
- TC-AC-PF-143 (aktor Distributor) ada di spec 064 karena butuh akun aktor pertama berbeda.
- Langkah penghubung: `[Clear Field]` sebagai pemulihan antar TC dan breadcrumb sub-tab `Active` untuk membuka form baru setelah plan tersimpan; spec berakhir pada Plan Detail tanpa form dirty.
- Temuan untuk QA: (1) Expected a TC-AC-PF-141 menyebut opsi Asset Name cap `50 (+$10)` tetapi langkah TC hanya membuka dropdown Group count; spec menambahkan langkah membuka dropdown Asset Name cap. (2) Expected a TC-AC-PF-144 "dihitung `$0` pada Estimated Total" tanpa nilai total; spec menurunkan `$50` dari Dataset Harga W (Asset Name cap 50, Group count 3, Open API ON). (3) Hasil TC-AC-PF-145 "Estimated Reference Price tiap field" ditulis sebagai satu `Verifikasi` untuk field Group count yang diamati hover; field lain tidak di-hover.
