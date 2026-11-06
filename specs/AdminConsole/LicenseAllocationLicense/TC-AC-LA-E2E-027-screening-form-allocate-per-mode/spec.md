---
id: TC-AC-LA-E2E-027-screening-form-allocate-per-mode
title: "Screening Form Allocate License per Mode: Principal, Concurrent User, App, Station, Storage, dan Loading"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-99
  - TC-AC-LA-100
  - TC-AC-LA-101
  - TC-AC-LA-102
  - TC-AC-LA-103
  - TC-AC-LA-107
coverage:
  web: automated
---

# Screening Form Allocate License per Mode: Principal, Concurrent User, App, Station, Storage, dan Loading

## Prerequisites

- Mode: FE+BE. Respons daftar Target dan Current Quota ditahan lewat `Spectra.intercept()` di atas backend nyata (TC-AC-LA-107); selebihnya memakai backend nyata.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 (konfirmasi `beforeunload` dan penutupan dialog `Unsaved Changes`) dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga Product Price.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`), Bengkel Cahaya Motor (#23, term FAMS Professional), Klinik Harapan Bunda (#24, Client-wide). ID term FAMS Professional Bengkel Cahaya Motor tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Dinamis: tidak ada; spec ini tidak mengirim Submit sehingga tidak membuat alokasi.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons daftar Target dan respons Current Quota selama 5 detik lalu melepasnya; kemampuan membaca saldo ledger Current Quota (disediakan tim FE/BE).
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-99: Screening Popup Allocate License kondisi awal (Principal)

1. Klik `[+ Allocation]`
2. Verifikasi Header: judul `Allocate License` dan tombol silang `[✕]`
3. Verifikasi Body: field Client (Required, Select searchable) berplaceholder `Select client` dengan helper text di bawahnya `Only clients with a subscription are listed. Add a subscription in Client Subscription first.`
4. Verifikasi Body: field Target (Required, Select) berplaceholder `Select target` dan Disabled
5. Verifikasi Body: field Type (Required, Select) berplaceholder `Select type` dan Disabled
6. Verifikasi Body: Current Quota dan Additional Quantity belum tampil
7. Verifikasi Body: section Payment Method tidak dirender untuk Principal
8. Verifikasi Footer: checkbox `Stay on this form after submitting` tidak dicentang dan rata kanan di atas tombol
9. Verifikasi Footer: `[Clear Field]` dan `[Submit]` rata kanan

### TC-AC-LA-100: Screening mode A, Type Concurrent User pada Target term Subscription

10. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`
11. Verifikasi urutan field: Client, Target, Type, Current Quota (read-only, `FLD-04`), Additional Quantity (placeholder `Enter additional quantity`), checkbox Stay, `[Clear Field]`, `[Submit]`
12. Verifikasi Current Quota menampilkan saldo ledger term `SUBS-20260101-A1B2C`
13. Verifikasi section Payment tidak dirender (Principal)

### TC-AC-LA-101: Screening mode A-biner, Type Asset Control App

14. Pilih Client `Bengkel Cahaya Motor`, Target term FAMS Professional, Type `Asset Control App`
15. Verifikasi form hanya berisi Client, Target, dan Type
16. Verifikasi Current Quota dan Additional Quantity tidak tampil (tidak ada dimensi kuantitas)

### TC-AC-LA-102: Screening mode B, Asset Control Station pada Target Client-wide

17. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Asset Control Station`
18. Verifikasi Current Quota (Stations) tampil read-only dengan nilai `—`
19. Verifikasi Additional Quantity berlabel `Additional Quantity` dengan placeholder `Enter additional quantity`
20. Verifikasi tidak ada pilihan Subscription

### TC-AC-LA-103: Screening mode B-GB, Storage

21. Ganti Type ke `Storage`
22. Verifikasi Current Quota (GB) tampil read-only dengan nilai `—`
23. Verifikasi label field `Additional Quantity (GB)` dengan placeholder `Enter additional quantity (GB)`

### TC-AC-LA-107: Loading form, skeleton pada Target dan Current Quota

24. Atur intercept: tunda 5 detik respons daftar Target
25. Pilih Client `PT Sejahtera`
26. Verifikasi skeleton tampil pada field Target setelah Client dipilih
27. Lepas tahanan respons daftar Target, lalu pilih Target `SUBS-20260101-A1B2C`
28. Atur intercept: tunda 5 detik respons Current Quota
29. Pilih Type `Concurrent User`
30. Verifikasi skeleton tampil pada Current Quota setelah Type dipilih
31. Lepas tahanan respons Current Quota dan lepas intercept
32. Klik `[×]` pada header
33. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
34. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Tidak ada `[Submit]` pada spec ini; jumlah buka form 1 dan kejadian menutup 1 (langkah 32 sampai 34).
- Penyimpangan urutan (S-10): TC-AC-LA-101, 102, 103, dan 107 dijalankan dalam satu sesi form yang dibuka di TC-AC-LA-99 (prinsip 6: halaman yang sama dipakai berulang tanpa Submit). Mengganti Client mereset Target dan Type (TC-AC-LA-136) sehingga state awal tiap TC sama dengan form baru; langkah 21 hanya mengganti Type karena Client dan Target TC-AC-LA-103 sama dengan TC-AC-LA-102.
- Langkah penghubung (S-03): langkah 27 dan 31 (melepas tahanan respons agar field berikutnya dapat dipilih) dan langkah 32 sampai 34 (menutup form dirty secara deterministik, S-08).
- Verifikasi skeleton (langkah 26 dan 30) ditulis sebelum respons dilepas (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-LA-102 Expected a dan TC-AC-LA-103 Expected a menyebut Current Quota `—` karena Klinik Harapan Bunda "belum punya alokasi Station/Storage pada baseline TC ini", sedangkan Pre-setup #52 men-seed alokasi Active Station +2 dan Storage +50 GB Client-wide untuk Client yang sama dan TC-AC-LA-135 mengharapkan `2` dan `50`. Spec mengikuti TC (`—`); pembuat baseline perlu memastikan kondisi tanpa alokasi Station/Storage atau TC diselaraskan.
  - TC-AC-LA-100 Expected b tidak menyebut nilai Current Quota PT Sejahtera; spec hanya membandingkan dengan saldo ledger term yang dibaca lewat kemampuan baca (disediakan tim FE/BE).
  - TC-AC-LA-101 menyebut "Target term FAMS Professional" tanpa ID Subscription dan Pre-setup #23 tidak mencantumkan ID; spec memilih satu-satunya term FAMS Professional Bengkel Cahaya Motor.
  - TC-AC-LA-107 Data Uji "Intercept respons: tunda 5 detik" tidak menyebut endpoint daftar Target dan Current Quota; endpoint tidak dikarang (S-13) dan ditentukan tim FE.
