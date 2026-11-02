---
id: TC-AC-CS-E2E-010-detail-subscription-info
title: "Detail: Subscription Info"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-36
  - TC-AC-CS-582
  - TC-AC-CS-57
  - TC-AC-CS-37
  - TC-AC-CS-40
  - TC-AC-CS-38
  - TC-AC-CS-58
coverage:
  web: automated
---

# Detail: Subscription Info

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #61 `SUBS-20260101-00001` (PT Sejahtera, FAMS Professional, Active, 01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama, Previous Subscription `SUBS-20250101-00001` Renewed #62), #51 `SUBS-20250801-00001` (CV Mitra Sejati, Custom Plan `Mitra Premium`, Grace, Grace End 30/08/26), #60 `SUBS-20260810-00001` (PT Sejahtera, Trial Enterprise Active, 10/08/26 sampai 08/09/26, Plan Owner PT ABC).

## Test Steps

### TC-AC-CS-36: Screening halaman Subscription Details term paid FAMS Active

1. Ketik Search `SUBS-20260101-00001`, tekan Enter
2. Klik baris `SUBS-20260101-00001`
3. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
4. Verifikasi Breadcrumb `Allocation > Client Subscription > Detail` dengan segmen tengah `Client Subscription` bisa diklik, segmen pertama dan terakhir label statis
5. Verifikasi tidak ada Page Title terpisah
6. Verifikasi SectionCard `Subscription Info` memuat Subscription ID `SUBS-20260101-00001`, Client `PT Sejahtera`, Product `FAMS`, Plan `Professional`
7. Verifikasi SectionCard `Subscription Info` memuat Status `Active`, Start Date `01/01/26`, End Date `31/12/26`, Grace End `—`
8. Verifikasi SectionCard `Subscription Info` memuat Plan Owner `PT Maju Bersama (Distributor)` dan Previous Subscription `SUBS-20250101-00001`
9. Verifikasi catatan Resubmitted From tidak dirender karena term bukan hasil Resubmit
10. Verifikasi SectionCard `License Quota` memuat tabel dengan kolom License Type | Total | Used | Remaining
11. Verifikasi SectionCard `Feature Entitlement` memuat sub-section Fixed Asset Module, Feature Suites, dan Addon Features
12. Verifikasi tidak ada pagination dan tombol aksi berada di pojok kanan atas card Subscription Info

### TC-AC-CS-582: Subscription Detail tidak menampilkan Purchase History License maupun Asset Control per-client

13. Verifikasi SectionCard License Quota hanya memuat tabel dengan kolom License Type | Total | Used | Remaining
14. Verifikasi tidak ada tabel atau section Purchase History License
15. Verifikasi tidak ada baris atau sub-section Asset Control (per-client) pada License Quota maupun Feature Entitlement
16. Verifikasi Detail hanya memuat tiga SectionCard: Subscription Info, License Quota, dan Feature Entitlement

### TC-AC-CS-57: Tabel License Quota dan Feature Entitlement tanpa kontrol tabel

17. Amati header tabel License Quota dan tiap sub-section Feature Entitlement
18. Verifikasi tidak ada ikon sort pada header kolom kedua tabel
19. Verifikasi tidak ada Search, Filter, Column Visibility `⋯`, maupun pagination pada kedua tabel
20. Muat ulang halaman Detail
21. Verifikasi urutan baris tetap dan tidak berubah setelah dimuat ulang

### TC-AC-CS-37: Link Previous Subscription membuka Detail term predecessor

22. Klik link `SUBS-20250101-00001` pada field Previous Subscription
23. Verifikasi halaman Subscription Detail `SUBS-20250101-00001` (status Renewed) terbuka
24. Verifikasi Previous Subscription term itu menampilkan "—" karena term pertama
25. Verifikasi semua tombol aksi tidak ada karena term data mati

### TC-AC-CS-40: Grace End pada Detail hanya terisi untuk Expired atau Grace

26. Klik segmen `Client Subscription` pada Breadcrumb
27. Ganti isi kotak search dengan `SUBS-20250801-00001`, tekan Enter
28. Klik baris `SUBS-20250801-00001`
29. Verifikasi Detail Grace menampilkan Grace End `30/08/26`
30. Klik segmen `Client Subscription` pada Breadcrumb
31. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
32. Klik baris `SUBS-20260101-00001`
33. Verifikasi Detail Active menampilkan Grace End "—"

### TC-AC-CS-38: Subscription Info baris Trial: tanpa Previous Subscription dan Grace End

34. Klik segmen `Client Subscription` pada Breadcrumb
35. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
36. Klik baris `SUBS-20260810-00001`
37. Verifikasi Plan `Enterprise` dengan penanda Trial, Status `Active`, Start Date `10/08/26`, End Date `08/09/26`
38. Verifikasi Previous Subscription "—" dan Grace End "—"
39. Verifikasi Plan Owner `PT ABC (Principal)`

### TC-AC-CS-58: Nilai kosong pada Detail ditampilkan strip

40. Verifikasi Previous Subscription "—"
41. Verifikasi Grace End "—"
42. Verifikasi tidak ada field yang tampil blank atau memuat teks `null`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16) dan klik segmen `Client Subscription` pada Breadcrumb yang mengembalikan List. TC-AC-CS-582, TC-AC-CS-57, dan TC-AC-CS-37 melanjutkan dari Detail `SUBS-20260101-00001` yang dibuka TC-AC-CS-36; TC-AC-CS-58 melanjutkan dari Detail `SUBS-20260810-00001` yang dibuka TC-AC-CS-38.
- Urutan TC: 36, 582, 57, 37, 40, 38, 58. Rujukan TC-AC-CS-39 (Detail Waiting for Approval) ada di spec 008.
- Spec ini 42 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (Subscription Info pada Detail) pada data Pre-setup baca-saja, dan berdiri sendiri; TC-AC-CS-36 memuat banyak klausa Expected yang wajib dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-CS-36 Expected b memuat nilai sembilan field Subscription Info dalam satu butir; spec memecahnya menjadi tiga Verifikasi berkelompok (identitas, status dan tanggal, Plan Owner dan Previous Subscription).
  - TC-AC-CS-40 mensyaratkan Detail Grace dan Detail Active pada langkah berurutan; Expected b menyebut "Detail Active" tanpa menyebut ID selain di Precondition.
  - TC-AC-CS-58 dan TC-AC-CS-38 mengasersi hal yang tumpang tindih (Previous Subscription dan Grace End "—" pada Detail Trial); keduanya ditulis lengkap karena tiap Expected punya asersi sendiri.
