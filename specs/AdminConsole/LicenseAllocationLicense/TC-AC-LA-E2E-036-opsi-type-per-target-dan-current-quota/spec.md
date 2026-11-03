---
id: TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota
title: "Opsi Type per Target dan Current Quota: FAMS, SIEM, SAMS, dan Asset Control App"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-129
  - TC-AC-LA-130
  - TC-AC-LA-131
  - TC-AC-LA-132
  - TC-AC-LA-133
  - TC-AC-LA-134
  - TC-AC-LA-135
coverage:
  web: automated
---

# Opsi Type per Target dan Current Quota: FAMS, SIEM, SAMS, dan Asset Control App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup (hanya dibaca kecuali disebut): PT Sejahtera (#19, FAMS Professional `SUBS-20260101-A1B2C`), Klinik Medika Jaya (#20, SIEM Growth `SUBS-20260301-P1Q2R`), CV Mitra Sejati (#22, SAMS Growth `SUBS-20260105-K2L3M`), Toko Serba Ada (#21, term Active `SUBS-20250201-J7K8L` dan term Pending `SUBS-20260819-00001`), Klinik Harapan Bunda (#24), alokasi Active Asset Control App pada CV Mitra Sejati (#53), alokasi Active Asset Control App pada term Active Toko Serba Ada (#74), ledger Concurrent User Toko Serba Ada term Active 30 dan term Pending 0 (#75), alokasi Active Station +2 dan Storage +50 GB Client-wide Klinik Harapan Bunda (#52).
- Pengaturan state Pre-setup #53: TC-AC-LA-131 mensyaratkan CV Mitra Sejati tanpa Asset Control App, sedangkan TC-AC-LA-132 memakai Pre-setup #53 (App Active) pada Subscription yang sama. Fixture backend (disediakan tim FE/BE) menyisihkan alokasi #53 di hook `before`, memulihkannya lewat langkah 14, dan memastikan pemulihan di hook `after`; efeknya (Last Updated dan entri audit trail alokasi #53) tercatat di Prerequisites ini.
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- Kemampuan teknis: membaca saldo ledger Current Quota (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-129: Opsi Type untuk Target FAMS

2. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`
3. Buka dropdown Type
4. Verifikasi opsi Type: `Concurrent User`, `Asset License`, `Audit`, `Maintenance`, `Tracking`, `Maps`, `IT Inventory`, `Asset Control App`
5. Verifikasi `Log Source`, `Asset Control Station`, dan `Storage` tidak muncul

### TC-AC-LA-130: Opsi Type untuk Target SIEM

6. Pilih Client `Klinik Medika Jaya`, Target `SUBS-20260301-P1Q2R`
7. Buka dropdown Type
8. Verifikasi opsi Type: `Concurrent User` dan `Log Source`
9. Verifikasi `Asset License`, Addon, dan `Asset Control App` tidak muncul

### TC-AC-LA-131: Opsi Type untuk Target SAMS

10. Pilih Client `CV Mitra Sejati`, Target `SUBS-20260105-K2L3M`
11. Buka dropdown Type
12. Verifikasi opsi Type: `Concurrent User` dan `Asset Control App`
13. Verifikasi `Log Source`, `Asset License`, dan Addon FAMS tidak muncul

### TC-AC-LA-132: Asset Control App tidak tampil bila Subscription sudah punya App Active

14. Pulihkan alokasi Active Asset Control App Pre-setup #53 pada CV Mitra Sejati lewat fixture backend hingga tersimpan
15. Pilih Client `PT Sejahtera`, lalu pilih Client `CV Mitra Sejati` dan Target `SUBS-20260105-K2L3M`
16. Buka dropdown Type
17. Verifikasi opsi `Asset Control App` tidak tampil
18. Verifikasi opsi Type lain `Concurrent User` tetap tampil

### TC-AC-LA-133: Asset Control App dapat dialokasikan ke term successor

19. Pilih Client `Toko Serba Ada`, Target term Pending `SUBS-20260819-00001`
20. Buka dropdown Type
21. Verifikasi opsi `Asset Control App` tampil untuk term successor
22. Verifikasi field Target menampilkan term Pending `SUBS-20260819-00001` sebagai Target App

### TC-AC-LA-134: Current Quota adalah saldo ledger per ID Subscription

23. Pilih Target term Active `SUBS-20250201-J7K8L` dan Type `Concurrent User`
24. Verifikasi Current Quota `30`
25. Ganti Target ke term Pending `SUBS-20260819-00001` dan pilih Type `Concurrent User`
26. Verifikasi Current Quota `0` (tidak digabung dengan term Active)

### TC-AC-LA-135: Current Quota Station dan Storage per Client

27. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Asset Control Station`
28. Verifikasi Current Quota (Stations) `2` untuk Client
29. Ganti Type ke `Storage`
30. Verifikasi Current Quota (GB) `50`
31. Klik `[✕]` pada header
32. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
33. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 31 sampai 33). Semua blok satu topik (opsi Type dan Current Quota per Target) dan berdiri sendiri; mengganti Client atau Target mereset Type (TC-AC-LA-136 dan 137).
- Langkah penghubung (S-03): langkah 3, 7, 11, 16, dan 20 (membuka dropdown Type agar opsi dapat diamati), langkah 14 (memulihkan Pre-setup #53 lewat fixture backend), langkah 15 (memuat ulang opsi dengan mengganti Client), dan langkah 31 sampai 33 (menutup form dirty, S-08).
- Asersi absence (langkah 5, 9, 13, 17) didahului Verifikasi opsi lain pada dropdown yang sama (langkah 4, 8, 12, 18; bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-131 ("CV Mitra Sejati tanpa Asset Control App") bertentangan dengan Pre-setup #53 (alokasi Active Asset Control App pada `SUBS-20260105-K2L3M` CV Mitra Sejati) yang dipakai TC-AC-LA-132. Spec membutuhkan pengaturan state oleh fixture backend; pengaturan itu tidak didefinisikan di TC dan disediakan tim FE/BE (S-13).
  - TC-AC-LA-135 Expected a dan b (`2` dan `50`) bertentangan dengan TC-AC-LA-102 dan TC-AC-LA-103 yang mengharapkan `—` untuk Client dan Type yang sama; lihat Temuan spec 027.
  - TC-AC-LA-132 Expected b ("top-up berulang diizinkan") tidak punya langkah observasi di Langkah Uji; hanya opsi `Concurrent User` yang tetap tampil yang diasersi (langkah 18).
  - TC-AC-LA-133 Expected b ("Target term Pending tampil sebagai Target App") tidak jelas maksudnya; spec mengasersi field Target menampilkan term Pending terpilih (langkah 22).
  - TC-AC-LA-131 menyebut "Addon FAMS tidak muncul" tanpa daftar Addon; spec mengasersi tidak muncul untuk `Audit`, `Maintenance`, `Tracking`, `Maps`, dan `IT Inventory` (daftar dari TC-AC-LA-129).
