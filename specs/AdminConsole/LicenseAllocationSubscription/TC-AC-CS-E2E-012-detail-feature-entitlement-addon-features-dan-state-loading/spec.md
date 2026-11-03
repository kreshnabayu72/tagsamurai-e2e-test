---
id: TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading
title: "Detail: Feature Entitlement, Addon Features, dan State Loading"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-45
  - TC-AC-CS-48
  - TC-AC-CS-46
  - TC-AC-CS-47
  - TC-AC-CS-49
coverage:
  web: automated
---

# Detail: Feature Entitlement, Addon Features, dan State Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #61 `SUBS-20260101-00001` (Plan Professional Default Plan, Maintenance 2 pada ledger #76), #130 `SUBS-20260101-00005` (Toko Plan Custom, Custom Plan `Maju Custom`), #51 `SUBS-20250801-00001` (Custom Plan `Mitra Premium`), #74 Client `Bengkel Cahaya Motor` (term paid FAMS plan Free `rank=0` Active, Plan Owner CV Karya Mandiri), #53 `SUBS-20260303-00001` (SIEM).
- Kemampuan teknis: pembacaan feature matrix Plans & Features (nama dan urutan fitur) untuk pembanding TC-AC-CS-45 Expected d, disediakan tim FE/BE (sumber tidak disebut TC selain "feature matrix Plans & Features"); `Spectra.intercept()` parsial untuk menunda respons endpoint Detail, endpoint ditentukan tim FE (S-13) dan intercept dilepas segera setelah asersi loading (S-09).

## Test Steps

### TC-AC-CS-45: Feature Entitlement term FAMS: sub-section, nilai, dan badge Source (Default Plan)

1. Ketik Search `SUBS-20260101-00001`, tekan Enter
2. Klik baris `SUBS-20260101-00001`
3. Susuri SectionCard Feature Entitlement
4. Verifikasi sub-section `Fixed Asset Module`, `Feature Suites`, dan `Addon Features` tampil berurutan dengan kolom Feature | Value | Source
5. Verifikasi sedikitnya satu baris tampil pada sub-section Fixed Asset Module dan Feature Suites
6. Verifikasi seluruh baris Fixed Asset Module dan Feature Suites menampilkan badge Source "Plan Default"
7. Verifikasi nama dan urutan fitur identik dengan feature matrix Plans & Features

### TC-AC-CS-48: Addon Features mengikuti alokasi lisensi dan bukan plan config

8. Verifikasi addon `Maintenance` menampilkan Value 2 sesuai alokasi aktif pada term ini
9. Verifikasi baris addon memakai bentuk tabel Feature | Value | Source yang sama dengan sub-section lain

### TC-AC-CS-46: Baris Asset cap hanya tampil pada plan default Free (term Professional)

10. Verifikasi Detail plan Paid Professional tidak memuat baris Asset cap

### TC-AC-CS-45: Feature Entitlement term FAMS: badge Source (Custom Plan)

11. Klik segmen `Client Subscription` pada Breadcrumb
12. Ganti isi kotak search dengan `SUBS-20260101-00005`, tekan Enter
13. Klik baris `SUBS-20260101-00005`
14. Susuri SectionCard Feature Entitlement
15. Verifikasi sedikitnya satu baris tampil pada sub-section Fixed Asset Module dan Feature Suites
16. Verifikasi seluruh baris Fixed Asset Module dan Feature Suites menampilkan badge Source "Custom Plan" severity primary

### TC-AC-CS-46: Baris Asset cap hanya tampil pada plan default Free (Custom Plan dan plan Free)

17. Klik segmen `Client Subscription` pada Breadcrumb
18. Ganti isi kotak search dengan `SUBS-20250801-00001`, tekan Enter
19. Klik baris `SUBS-20250801-00001`
20. Verifikasi sedikitnya satu baris tampil pada sub-section Fixed Asset Module dan Feature Suites Detail Custom Plan `Mitra Premium`
21. Verifikasi Detail Custom Plan `Mitra Premium` tidak memuat baris Asset cap
22. Klik segmen `Client Subscription` pada Breadcrumb
23. Ganti isi kotak search dengan `Bengkel Cahaya Motor`, tekan Enter
24. Klik baris term paid plan Free
25. Verifikasi Detail plan Free memuat baris Asset cap pada Fixed Asset Module

### TC-AC-CS-47: Feature Entitlement Product SIEM hanya memuat dua baris Plan Default

26. Klik segmen `Client Subscription` pada Breadcrumb
27. Ganti isi kotak search dengan `SUBS-20260303-00001`, tekan Enter
28. Klik baris `SUBS-20260303-00001`
29. Verifikasi hanya bagian SIEM yang tampil sebagai bagian biasa pada halaman (bukan tab)
30. Verifikasi baris `Log Source cap` 50 dan `Concurrent User cap` 10 keduanya berbadge "Plan Default"
31. Verifikasi tidak ada sub-section Fixed Asset Module, Feature Suites, maupun Addon Features

### TC-AC-CS-49: State loading Detail memakai Shimmer Complex Grid

32. Klik segmen `Client Subscription` pada Breadcrumb
33. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
34. Tunda respons endpoint Detail melalui intercept jaringan
35. Klik baris `SUBS-20260101-00001`
36. Verifikasi halaman menampilkan Shimmer Complex Grid selama respons tertunda
37. Lepas tahanan respons endpoint Detail
38. Verifikasi tiga SectionCard tampil setelah respons diterima

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik segmen `Client Subscription` pada Breadcrumb yang mengembalikan List, dan langkah menunda serta melepas tahanan respons (kebutuhan intercept ada di Prerequisites).
- Urutan TC: 45 (Default Plan), 48, 46 (Professional), 45 (Custom Plan), 46 (Custom Plan dan plan Free), 47, 49. TC-AC-CS-45, TC-AC-CS-46 ditulis dalam dua blok tiap TC karena asersinya berada di Detail yang berbeda; langkah pindah Detail diminimalkan (S-10).
- Baris term paid plan Free Client `Bengkel Cahaya Motor` ditemukan lewat Search nama Client karena TC tidak menyebut Subscription ID-nya.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (SectionCard Feature Entitlement pada Detail) pada data Pre-setup baca-saja, dan berdiri sendiri; asersi tiap plan membutuhkan Detail yang berbeda sehingga langkah Search dan buka Detail tidak dapat dilebur.
- Verifikasi sedikitnya satu baris pada Detail Custom Plan `Mitra Premium` mendahului asersi absence baris Asset cap pada TC-AC-CS-46 sebagai anchor positif (bagian 8b butir 2); TC tidak menulisnya.
- Temuan untuk QA:
  - TC-AC-CS-46 langkah 1 "Buka Detail term plan Free" tidak menyebut Subscription ID; Pre-setup #74 hanya menyebut Client `Bengkel Cahaya Motor`, dan Client itu juga punya trial FAMS Growth Active sehingga baris paid plan Free dipilih dari kolom Plan.
  - TC-AC-CS-45 Expected d ("identik dengan feature matrix Plans & Features") tidak menyebut cara memperoleh feature matrix; kemampuan disediakan tim FE/BE (S-11).
  - TC-AC-CS-49 tidak menyebut nama endpoint Detail; endpoint ditentukan tim FE (S-13).
