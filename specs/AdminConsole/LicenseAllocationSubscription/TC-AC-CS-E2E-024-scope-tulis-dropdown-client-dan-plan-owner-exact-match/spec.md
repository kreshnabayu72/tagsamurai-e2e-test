---
id: TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match
title: "Scope Tulis: Dropdown Client dan Plan Owner Exact Match"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-94
  - TC-AC-CS-95
  - TC-AC-CS-96
  - TC-AC-CS-97
coverage:
  web: automated
---

# Scope Tulis: Dropdown Client dan Plan Owner Exact Match

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, Total Control, Distributor PT Maju Bersama; Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`
  - `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`, Total Control, Partner CV Karya Mandiri; Pre-setup #11), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: Client `Apotek Sehat Sentosa` (binaan langsung PT Maju Bersama pada group `Jawa`; #29), `Bengkel Maju Jaya` (binaan langsung CV Karya Mandiri; #30) dengan `SUBS-20250819-00002` Expired (#50), `Bengkel Cahaya Motor` (binaan langsung CV Karya Mandiri) dengan term paid Active plan Free (#74), `SUBS-20250815-00001` (Warung Kopi Senja, Active, Plan Owner PT Maju Bersama; #69), Client binaan CV Sinar Abadi dari jaringan PT Nusa Link (#102).
- Tabel "Role yang diuji": Total Control Distributor (#9, TC-AC-CS-94 dan 95), Total Control Principal (#1, TC-AC-CS-96), Total Control Partner (#11, TC-AC-CS-97).

## Test Steps

### TC-AC-CS-94: Dropdown Client form hanya memuat Client binaan langsung Distributor

1. Ketik Search `Bengkel Maju Jaya`, tekan Enter
2. Verifikasi baris Client `Bengkel Maju Jaya` (binaan Partner) tampil di List
3. Klik `(←)` pada kotak Search
4. Klik `[+ Subscription]`
5. Buka dropdown Client
6. Verifikasi `Apotek Sehat Sentosa` (binaan langsung) ada di dropdown
7. Verifikasi `Bengkel Maju Jaya` (binaan Partner) tidak ada di dropdown
8. Verifikasi Client di luar jaringan (binaan CV Sinar Abadi) tidak ada di dropdown
9. Klik `✕` pada modal `Add Subscription`

### TC-AC-CS-95: Distributor tidak dapat Renew atau Cancel baris yang Plan Owner-nya Partner

10. Ketik Search `Bengkel Maju Jaya`, tekan Enter
11. Klik ikon `⋯` pada baris `SUBS-20250819-00002` (Expired)
12. Verifikasi menu row action berisi hanya Detail dan Subscription Log
13. Verifikasi Renew Hidden karena Plan Owner baris adalah CV Karya Mandiri dan bukan PT Maju Bersama
14. Ganti isi kotak search dengan `Bengkel Cahaya Motor`, tekan Enter
15. Klik ikon `⋯` pada baris term paid Active
16. Verifikasi menu row action berisi hanya Detail dan Subscription Log
17. Verifikasi Cancel Subscription Hidden karena Plan Owner baris adalah CV Karya Mandiri dan bukan PT Maju Bersama
18. Klik `(←)` pada kotak Search

### TC-AC-CS-96: Principal dikecualikan dari exact match Plan Owner untuk Renew dan Cancel Subscription

19. Logout lalu login sbg Role: Total Control (Principal) `Hendra Wijaya`
20. Buka menu `Allocation > Client Subscription`
21. Ketik Search `SUBS-20250815-00001`, tekan Enter
22. Klik ikon `⋯` pada baris `SUBS-20250815-00001`
23. Verifikasi menu berisi Detail, Subscription Log, Renew, Cancel Subscription
24. Verifikasi aksi tersedia walau Plan Owner baris adalah Distributor (scope WRITE Principal = semua Client)
25. Klik `(←)` pada kotak Search

### TC-AC-CS-97: Partner hanya dapat menulis untuk Client binaan langsungnya

26. Logout lalu login sbg Role: Total Control (Partner) `Lestari Wulandari`
27. Buka menu `Allocation > Client Subscription`
28. Klik `[+ Activate Trial]`
29. Buka dropdown Client
30. Verifikasi `Bengkel Maju Jaya` ada di dropdown
31. Verifikasi `Apotek Sehat Sentosa` (binaan PT Maju Bersama) tidak ada di dropdown
32. Klik `✕` pada modal `Activate Trial`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok akun karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, dan `✕` pada modal. Spec read-only; tidak menulis data.
- Verifikasi baris `Bengkel Maju Jaya` tampil di List pada TC-AC-CS-94 adalah anchor positif untuk asersi absence di dropdown (bagian 8b butir 2); Verifikasi `Apotek Sehat Sentosa` ada di dropdown mendahului asersi absence yang lain.
- Temuan untuk QA:
  - TC-AC-CS-94 Expected a menyebut `Apotek Sehat Sentosa` ada di dropdown "bila punya Product tanpa baris Current" (kondisi data); spec mengasersinya ada tanpa kondisi karena Pre-setup #29 punya Product tanpa baris Current.
  - TC-AC-CS-94 Expected c menyebut "Client di luar jaringan" tanpa nama; spec memakai Client binaan CV Sinar Abadi (Pre-setup #102) sebagai contoh jaringan lain.
  - TC-AC-CS-95 Expected a menyebut menu "hanya Detail dan Subscription Log" untuk dua baris dalam satu butir; spec memverifikasinya per baris.
