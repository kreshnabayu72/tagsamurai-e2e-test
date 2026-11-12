---
id: TC-AC-LA-E2E-041-skeleton-preview-pay-from-dan-cross-distributor
title: "Skeleton Preview, Harga dan Saldo per Pay From, dan Cross-Distributor Sourcing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-147
  - TC-AC-LA-153
  - TC-AC-LA-506
coverage:
  web: automated
---

# Skeleton Preview, Harga dan Saldo per Pay From, dan Cross-Distributor Sourcing

## Prerequisites

- Mode: FE+BE. Respons preview Cost ditahan lewat `Spectra.intercept()` di atas backend nyata (TC-AC-LA-147); selebihnya memakai backend nyata.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Partner multi kantong `partnerMultiLic_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Pre-setup #16), password `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), PT Abadi Jaya (#25, `SUBS-20260110-C1D2E`), kantong wallet (#33), Product Price (#34: Concurrent User $365 per unit per tahun), Cross-Distributor Sourcing aktif ke `PT Distribusi Utama` dengan kantong sumber saldo $5,000.00 dan harga Concurrent User $365 per unit per tahun (#68). Toggle Require Approval for Allocation OFF (#39) untuk TC-AC-LA-506, diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE); jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: satu alokasi Concurrent User +2 PT Abadi Jaya (Completed, Wallet, Cost $20.00) dari TC-AC-LA-506; tidak dapat dihapus (tanpa Delete), dipulihkan baseline automation; saldo kantong PT Distribusi Utama dipulihkan fixture backend di hook `after`.
- Baseline: saldo kantong sumber dan daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum `[Submit]` (langkah 10 untuk Allocation ID, langkah 21 untuk saldo).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons preview Cost 5 detik; membaca saldo kantong (disediakan tim FE/BE); menampilkan kolom Paid From lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-147: Skeleton pada baris Cost dan Pocket Balance saat preview dimuat

1. Klik `[+ Allocation]`
2. Atur intercept: tunda 5 detik respons preview Cost
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`
4. Verifikasi skeleton tampil pada baris Cost dan `Your pocket balance` sampai preview dimuat
5. Verifikasi warning V-18 belum tampil selama skeleton
6. Lepas tahanan respons preview Cost dan lepas intercept
7. Klik `[×]` pada header
8. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
9. Klik `[Leave]`

### TC-AC-LA-153: Harga dan saldo mengikuti kantong sumber yang dipilih pada Pay From

10. Ganti akun: logout `Dewi A`, login sebagai `Budi Santoso` dengan `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`, buka Allocation > License Allocation tab Current, lalu catat baseline Allocation ID baris di halaman pertama tab Current
11. Klik `[+ Allocation]`
12. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`
13. Pilih Pay From `PT ABC (Principal)`
14. Verifikasi baris `Your pocket balance` dimuat ulang sesuai saldo kantong Principal terpilih
15. Verifikasi harga item untuk Cost diambil dari tarif produk milik entitas sumber kantong `PT ABC (Principal)`
16. Pilih Pay From Distributor relasi utama `PT Maju Bersama (Distributor)`
17. Verifikasi baris `Your pocket balance` dimuat ulang sesuai saldo kantong Distributor terpilih
18. Verifikasi harga item untuk Cost diambil dari tarif produk milik entitas sumber kantong `PT Maju Bersama (Distributor)`

### TC-AC-LA-506: Cross-Distributor Sourcing mendebit kantong Distributor lain yang dipilih

19. Buka dropdown Pay From
20. Verifikasi opsi Pay From memuat `PT Distribusi Utama (Distributor)` selain Distributor relasi utama dan `PT ABC (Principal)`
21. Pilih Pay From `PT Distribusi Utama (Distributor)`, lalu catat saldo semua kantong sumber
22. Verifikasi baris Cost `Cost: $20.00 (2 × $365/unit × 10 days remaining ÷ 365)` memakai harga milik PT Distribusi Utama
23. Verifikasi baris `Your pocket balance: $5,000.00`
24. Klik `[Submit]`
25. Tunggu modal tertutup dan baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 10)
26. Verifikasi saldo kantong PT Distribusi Utama berkurang `$20.00`
27. Verifikasi kantong sumber lain tidak berubah
28. Tampilkan kolom Paid From lewat Setup Column
29. Verifikasi kolom Paid From baris baru `PT Distribusi Utama (Distributor)`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 2 kali, kejadian menutup 2 (langkah 7 sampai 9 dan modal tertutup oleh Submit di langkah 24).
- Penyimpangan urutan (S-10): TC-AC-LA-506 melanjutkan form TC-AC-LA-153 (Client, Target, Type, dan Additional Quantity sama) dan hanya mengganti Pay From (prinsip 6). TC-AC-LA-506 Dependensi TC-AC-LA-105 dipenuhi oleh opsi Pay From pada langkah 13 sampai 20.
- Langkah penghubung (S-03): langkah 2 dan 6 (menahan dan melepas respons), langkah 10 (ganti akun dan baseline Allocation ID), langkah 21 (mencatat saldo semua kantong sumber), langkah 7 sampai 9 (menutup form dirty, S-08), langkah 19 (membuka dropdown), langkah 25 (menunggu aksi selesai), dan langkah 28 (menampilkan kolom Paid From; Setup Column tidak memerlukan Verifikasi).
- Temuan untuk QA:
  - TC-AC-LA-153 Expected a dan b tidak menyebut nilai saldo dan harga kantong Principal serta Distributor relasi utama (Pre-setup #33 hanya menyebut saldo Distributor $10,000.00, Partner $5,000.00, Principal $5,000.00 tanpa memetakannya ke opsi Pay From); spec mengasersi bahwa saldo dan harga mengikuti kantong terpilih tanpa nilai persis.
  - TC-AC-LA-153 menyebut "Distributor relasi utama" tanpa nama; spec memakai `PT Maju Bersama` (Pre-setup #25 dan #33).
  - TC-AC-LA-506 Expected c ("kantong sumber lain tidak berubah") tidak menyebut kantong mana saja; spec membandingkan seluruh kantong sumber yang dicatat pada langkah 21.
  - TC-AC-LA-147 tidak menyebut endpoint preview Cost; endpoint tidak dikarang (S-13) dan ditentukan tim FE.
