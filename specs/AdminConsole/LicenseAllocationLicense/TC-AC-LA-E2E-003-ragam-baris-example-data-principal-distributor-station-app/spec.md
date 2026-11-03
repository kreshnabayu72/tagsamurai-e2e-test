---
id: TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app
title: "Ragam Baris Example Data: Principal, Distributor, Station, Storage, dan App"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-18
  - TC-AC-LA-19
  - TC-AC-LA-20
  - TC-AC-LA-21
  - TC-AC-LA-22
coverage:
  web: automated
---

# Ragam Baris Example Data: Principal, Distributor, Station, Storage, dan App

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #19 PT Sejahtera, #20 Klinik Medika Jaya, #52 alokasi `Active` Asset Control Station +2 dan Storage +50 GB Client-wide Klinik Harapan Bunda, #53 alokasi `Active` Addon Asset Control App CV Mitra Sejati. Alokasi `Sari P` (Pre-setup #2), alokasi `Dewi A` (Pre-setup #4), baris Log Source +10 Cost $480.00, Addon (Audit), dan Addon (IT Inventory) ada di seed #54; Allocation ID-nya dirujuk lewat `Fixture.license-allocation-license` (kunci seedLogSource10, seedStation, seedStorage, seedAppActive, seedAddonAudit, seedAddonItInventory). Pembuat seed (`Sari P`, `Dewi A`) tidak login di spec ini.
- Konfigurasi kolom Setup Column yang disimpan spec (kolom Plan, Payment, Paid From, dan Cost) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-18: Baris alokasi Principal tampil Payment Free

1. Klik ikon `⋯` pada header kolom, lalu klik `Setup Column...`
2. Centang kolom Plan, Payment, Paid From, dan Cost, lalu klik `[Save]`
3. Ketik Search `LALC-20260105-00001`, tekan Enter
4. Verifikasi Payment: `Free`
5. Verifikasi Paid From: `—`
6. Verifikasi Cost: `—`
7. Verifikasi Quantity: `+5`
8. Verifikasi Plan Owner: `PT Maju Bersama (Distributor)`
9. Verifikasi Status: `Active` dengan severity success

### TC-AC-LA-19: Baris alokasi Distributor tampil Payment Wallet

10. Ganti isi kotak search dengan Allocation ID seed Log Source +10 pada Klinik Medika Jaya (`Fixture.license-allocation-license.seedLogSource10`), tekan Enter
11. Verifikasi Payment: `Wallet`
12. Verifikasi Paid From: `PT ABC (Principal)`
13. Verifikasi Cost: `$480.00`
14. Verifikasi Allocated By: `Dewi A`
15. Klik ikon Filter dan amati daftar field filter
16. Verifikasi panel Filter tampil dengan field `License Type`, `Client`, dan `Status`
17. Verifikasi tidak ada kolom Payment Method pada tabel
18. Verifikasi tidak ada filter Payment Method pada panel Filter
19. Tutup panel Filter

### TC-AC-LA-20: Baris Asset Control Station dan Storage

20. Ganti isi kotak search dengan Allocation ID seed Asset Control Station +2 Klinik Harapan Bunda (`Fixture.license-allocation-license.seedStation`), tekan Enter
21. Verifikasi License Type baris Station: `Asset Control Station`
22. Verifikasi Product, Subscription ID, Plan, dan Plan Owner baris Station: `—`
23. Verifikasi Quantity baris Station: `+2`
24. Verifikasi Status baris Station: `Active` pada tab Current
25. Ganti isi kotak search dengan Allocation ID seed Storage +50 GB Klinik Harapan Bunda (`Fixture.license-allocation-license.seedStorage`), tekan Enter
26. Verifikasi License Type baris Storage: `Storage`
27. Verifikasi Product, Subscription ID, Plan, dan Plan Owner baris Storage: `—`
28. Verifikasi Quantity baris Storage: `+50 GB`
29. Verifikasi Status baris Storage: `Active` pada tab Current

### TC-AC-LA-21: Baris Asset Control App

30. Ganti isi kotak search dengan Allocation ID seed Addon Asset Control App CV Mitra Sejati (`Fixture.license-allocation-license.seedAppActive`), tekan Enter
31. Verifikasi License Type: `Addon (Asset Control App)`
32. Verifikasi Product: `SAMS`
33. Verifikasi Quantity: `—`
34. Verifikasi Status: `Active`

### TC-AC-LA-22: Format License Type Addon Audit dan IT Inventory

35. Ganti isi kotak search dengan Allocation ID seed Addon Audit pada FAMS (`Fixture.license-allocation-license.seedAddonAudit`), tekan Enter
36. Verifikasi License Type baris pertama: `Addon (Audit)`
37. Verifikasi Product baris pertama: `FAMS`
38. Ganti isi kotak search dengan Allocation ID seed Addon IT Inventory pada FAMS (`Fixture.license-allocation-license.seedAddonItInventory`), tekan Enter
39. Verifikasi License Type baris kedua: `Addon (IT Inventory)`
40. Verifikasi Product baris kedua: `FAMS`
41. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah Setup Column yang menampilkan kolom (tanpa `Verifikasi`), langkah membuka dan menutup panel Filter, dan langkah `(←)` pada kotak Search yang mengosongkan Search di akhir spec.
- Spec ini lebih dari 35 langkah. Alasannya: semua blok satu topik (ragam baris Example Data pada List), memakai seed baca-saja dan konfigurasi kolom yang sama, dan berdiri sendiri, sehingga kegagalan satu blok baris tidak membuat blok baris lain kehilangan makna. Satu pembukaan Setup Column dipakai bersama TC-AC-LA-18 sampai TC-AC-LA-22.
- Akun `defaultUserLic` (Pre-setup #2) dan `dewiFullLic` (Pre-setup #4) hanya pembuat seed pada baris yang diasersi; keduanya tidak login karena aktor TC adalah Total Control Principal.
- Langkah 16 adalah anchor positif untuk absence Payment Method pada langkah 17 dan 18 (bagian 8b butir 2): panel Filter terbukti terbuka dan memuat field lain sebelum ketiadaan filter Payment Method diasersi.
- Temuan untuk QA:
  - TC-AC-LA-22 langkah 1 tidak menyebut cara mencari baris Addon Audit dan Addon IT Inventory maupun Client-nya; spec memakai Allocation ID seed dari fixture.
  - TC-AC-LA-19 Expected e (`Tidak ada kolom atau filter Payment Method`) tidak punya langkah yang membuka panel Filter; spec menambah langkah membuka dan menutup panel Filter (S-03).
  - TC-AC-LA-20 dan TC-AC-LA-21 tidak menyebut Allocation ID baris yang dicari; identitas baris dibaca dari fixture seed (#52 dan #53).
  - TC-AC-LA-18 Expected e menyebut Plan Owner `PT Maju Bersama (Distributor)` untuk alokasi Principal berstatus Payment Free; hubungan Plan Owner dan pembuat alokasi tidak dijelaskan di TC.
