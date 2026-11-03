---
id: TC-AC-CS-E2E-011-detail-license-quota
title: "Detail: License Quota"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-41
  - TC-AC-CS-636
  - TC-AC-CS-42
  - TC-AC-CS-43
  - TC-AC-CS-44
  - TC-AC-CS-59
coverage:
  web: automated
---

# Detail: License Quota

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #53 `SUBS-20260303-00001` (SIEM, Concurrent User 10 Used 4, Log Source 50 Used 31) dan #67 `SUBS-20260819-00003` (Toko Serba Ada, successor Waiting for Approval).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; bentuk Pre-setup #60, #61, #76, #77): Client `PT Sejahtera+{runId}-011` (Plan Owner PT ABC) dengan dua term FAMS dan Asset Client 37. Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai `{idTrial011}` dan `{idPaid011}`:
  1. `{idTrial011}` (TC-AC-CS-41 dan TC-AC-CS-636): term Trial FAMS Active, Trial Asset Quota 100, Concurrent User Quota 5 (Used 2), Maintenance Total 100 Used 12, lima addon Total 100 (bentuk Pre-setup #60); Asset Client `PT Sejahtera+{runId}-011` pada FAMS 37 (bentuk #77).
  2. `{idPaid011}` (TC-AC-CS-42 dan TC-AC-CS-59): term Paid FAMS Active, Concurrent User Total 20 Used 8, Maintenance Total 2 Used 1 (bentuk Pre-setup #61, #76).
- Kemampuan teknis (disediakan tim FE/BE, endpoint tidak tertulis di TC, PRD, atau LLD): mengubah data Asset Client seed `PT Sejahtera+{runId}-011` pada produk FAMS dari 37 menjadi 120 untuk TC-AC-CS-636, dan menambah alokasi +2 Concurrent User pada term `{idPaid011}` untuk TC-AC-CS-59 (alokasi dari modul License Allocation oleh aktor yang sama). Kedua perubahan hanya mengenai data seed milik spec dan dipulihkan sebagai langkah penghubung; seed dihapus di hook `after`. Used Concurrent User berasal dari sesi aktif yang disiapkan seeding (disediakan tim FE/BE).
- Keadaan awal baris License Quota tidak membutuhkan akun lain; seluruh spec memakai Total Control Principal.

## Test Steps

### TC-AC-CS-41: License Quota term Trial FAMS: baris Asset, Concurrent User, dan addon

1. Ketik Search `{idTrial011}`, tekan Enter
2. Klik baris `{idTrial011}`
3. Verifikasi baris `Asset`: Total 100, Used 37, Remaining 63
4. Verifikasi baris `Concurrent User`: Total 5, Used 2, Remaining 3
5. Verifikasi lima baris addon `Audit`, `Maintenance`, `Tracking`, `Maps`, dan `IT Inventory` masing-masing Total 100 (sama dengan Trial Asset Quota)
6. Verifikasi baris `Maintenance`: Used 12, Remaining 88
7. Verifikasi Remaining sama dengan Total dikurangi Used pada setiap baris

### TC-AC-CS-42: License Quota term Paid FAMS tanpa baris Asset

8. Klik segmen `Client Subscription` pada Breadcrumb
9. Ganti isi kotak search dengan `{idPaid011}`, tekan Enter
10. Klik baris `{idPaid011}`
11. Verifikasi baris `Concurrent User`: Total 20, Used 8, Remaining 12
12. Verifikasi baris `Maintenance`: Total 2, Used 1, Remaining 1
13. Verifikasi tidak ada baris `Asset` pada term Paid

### TC-AC-CS-59: Remaining dihitung Total dikurangi Used pada License Quota

14. Verifikasi sebelum alokasi: baris `Concurrent User` Total 20, Used 8, dan Remaining 12
15. Alokasikan +2 Concurrent User pada term `{idPaid011}` sebagai Total Control Principal dari modul License Allocation hingga alokasi tersimpan
16. Muat ulang halaman Detail
17. Verifikasi setelah alokasi +2: Total 22, Used tetap 8 (dihitung dari sesi aktif), dan Remaining 14
18. Verifikasi Remaining selalu Total dikurangi Used
19. Pulihkan alokasi +2 Concurrent User pada term `{idPaid011}` melalui fixture backend

### TC-AC-CS-43: License Quota Product SIEM: dua baris tetap tanpa Addon

20. Klik segmen `Client Subscription` pada Breadcrumb
21. Ganti isi kotak search dengan `SUBS-20260303-00001`, tekan Enter
22. Klik baris `SUBS-20260303-00001`
23. Verifikasi baris `Concurrent User`: Total 10, Used 4, Remaining 6
24. Verifikasi baris `Log Source`: Total 50, Used 31, Remaining 19
25. Verifikasi tidak ada baris addon maupun Asset

### TC-AC-CS-44: License Quota term suksesor Renewal dimulai kosong

26. Klik segmen `Client Subscription` pada Breadcrumb
27. Ganti isi kotak search dengan `SUBS-20260819-00003`, tekan Enter
28. Klik baris `SUBS-20260819-00003`
29. Verifikasi baris `Concurrent User`: Total 0, Used 0, Remaining 0
30. Verifikasi tidak ada EmptyState pada tabel
31. Verifikasi kuota predecessor (Concurrent User 20) tidak terbawa ke ledger successor

### TC-AC-CS-636: License Quota term Trial: Remaining 0 saat Used melebihi Total

32. Atur data Asset Client seed `PT Sejahtera+{runId}-011` pada produk FAMS menjadi 120 Asset melalui fixture backend
33. Klik segmen `Client Subscription` pada Breadcrumb
34. Ganti isi kotak search dengan `{idTrial011}`, tekan Enter
35. Klik baris `{idTrial011}`
36. Verifikasi baris `Asset`: Total 100, Used 120, Remaining 0
37. Verifikasi Remaining tidak menampilkan angka negatif dan baris `Asset` tidak disembunyikan
38. Verifikasi baris `Concurrent User`: Total 5, Used 2, Remaining 3 tidak terpengaruh
39. Pulihkan data Asset Client seed `PT Sejahtera+{runId}-011` pada produk FAMS menjadi 37 Asset melalui fixture backend

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik segmen `Client Subscription` pada Breadcrumb yang mengembalikan List, langkah mengubah dan memulihkan data Asset Client (TC-AC-CS-636) dan alokasi +2 Concurrent User (TC-AC-CS-59).
- Urutan TC: 41, 42, 59, 43, 44, 636 (TC-AC-CS-59 mengubah Total term `{idPaid011}` sehingga TC-AC-CS-42 yang mengasersi Total awal 20 ditempatkan sebelum TC-AC-CS-59; TC-AC-CS-636 memakai Asset Client 120 sesudah TC-AC-CS-41 memakai 37; S-10).
- Spec ini 39 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (tabel License Quota pada Detail) dan berdiri sendiri; TC-AC-CS-59 dan TC-AC-CS-636 memerlukan langkah ubah dan pulihkan data yang tidak dapat dilebur dengan blok lain.
- Temuan untuk QA:
  - TC-AC-CS-41 (Asset Client 37, #77) dan TC-AC-CS-636 (Asset Client 120, #140) mengacu pada Client dan baris Trial yang sama dengan nilai data berbeda; spec mengatur data seed `PT Sejahtera+{runId}-011` lewat fixture backend di antara kedua TC (kemampuan disediakan tim FE/BE).
  - TC-AC-CS-41, 42, 59, dan 636 menyebut baris Pre-setup (`SUBS-20260810-00001`, `SUBS-20260101-00001`, Client `PT Sejahtera`) padahal TC-AC-CS-59 dan TC-AC-CS-636 menulisnya; spec memakai seed milik spec dengan nilai kuota yang sama (S-06) dan Used Concurrent User dari sesi aktif disiapkan seeding (asumsi, mekanisme tidak tertulis di TC).
  - TC-AC-CS-59 langkah 2 ("Alokasikan +2 Concurrent User ... dari modul License Allocation") tidak menyebut halaman, form, atau endpoint; spec menuliskannya sebagai langkah pemicu "hingga alokasi tersimpan" (R-20) dengan mekanisme ditentukan tim FE/BE, tanpa endpoint karangan (S-13).
  - TC-AC-CS-41 Expected c dan d bermajemuk (lima addon dengan Total 100 dan rumus Remaining pada tiap baris); spec memecahnya menjadi Verifikasi berkelompok.
