---
id: TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation
title: "Modul Konsumen: Client Detail, Dashboard, dan License Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-474
  - TC-AC-CS-476
  - TC-AC-CS-479
  - TC-AC-CS-475
coverage:
  web: automated
---

# Modul Konsumen: Client Detail, Dashboard, dan License Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit): Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed yang dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12), semua bersuffix `+{runId}-129`:
  1. TC-AC-CS-474: Client `Client Tanpa Subscription+{runId}-129` (setara Pre-setup #48: binaan langsung PT Maju Bersama, group `Jawa`, belum punya term maupun trial) diberi term Active (Add Subscription, Dependensi TC-AC-CS-143; endpoint tulis tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE).
  2. TC-AC-CS-476: sebuah term Active baru dan sebuah term Archive hasil Cancel Subscription (Dependensi TC-AC-CS-262) milik Client `Client Konsumen Status+{runId}-129` (setara Client binaan PT Maju Bersama yang belum punya term lain).
  3. TC-AC-CS-475: Client `Client Total Subscription+{runId}-129` milik Distributor `PT Maju Bersama` dengan lima term: 1 Active, 1 Pending, 1 Waiting for Approval, 1 Rejected, dan 1 Canceled (Dependensi TC-AC-CS-143 dan 144); Total Subscription yang diharapkan: 2.
- Data Pre-setup baca-saja (TC-AC-CS-479): Client `Toko Prima Sentosa` (binaan langsung PT Maju Bersama) dengan term SAMS Active `SUBS-20251001-00001` (berkuota Concurrent User 20) dan successor Renewal Pending `SUBS-20260801-00001` (#116).
- Kemampuan teknis (disediakan tim FE/BE): membuat term lewat sesi API aktor; membuat Client.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-474: Term baru muncul di Client Detail tab Subscription

1. Buka Client Detail `Client Tanpa Subscription+{runId}-129`
2. Klik tab `Subscription`
3. Verifikasi riwayat memuat term baru dengan Status Active dan Plan Owner `PT Maju Bersama (Distributor)`
4. Klik baris term baru
5. Verifikasi Subscription Detail terbuka dalam mode read-only tanpa tombol aksi

### TC-AC-CS-476: Perubahan status langganan dari modul ini terbaca di List dan Dashboard memuat tanpa error

6. Klik menu `Client Subscription` di sidebar
7. Ketik Search `Client Konsumen Status+{runId}-129`, tekan Enter
8. Verifikasi tab `Current` memuat term baru berstatus Active
9. Klik tab `History`
10. Verifikasi tab `History` memuat term hasil Cancel Subscription berstatus Archive
11. Klik menu `Dashboard` di sidebar
12. Verifikasi bagian ringkasan status langganan pada Dashboard dimuat tanpa error

### TC-AC-CS-479: License Allocation memakai term Active atau Pending sebagai Target dan ledger successor mulai kosong

13. Klik menu `License Allocation` di sidebar
14. Klik tombol Allocate License
15. Pilih Client `Toko Prima Sentosa`
16. Buka dropdown Target term
17. Verifikasi term Active `SUBS-20251001-00001` dan term Pending `SUBS-20260801-00001` dapat dipilih sebagai Target
18. Pilih term Pending `SUBS-20260801-00001`
19. Verifikasi ledger successor Pending dimulai kosong dan kuota predecessor tidak terbawa
20. Verifikasi alokasi pada term Pending tampil belum efektif
21. Klik `✕` pada form
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]` pada dialog `Unsaved Changes`

### TC-AC-CS-475: Total Subscription pada tab Client Distributor dan Partner mengikuti term Active atau Pending

24. Logout
25. Login sebagai Total Control Distributor `Eko Saputra`
26. Buka Detail Distributor `PT Maju Bersama`
27. Klik tab `Client`
28. Verifikasi kolom Total Subscription Client `Client Total Subscription+{runId}-129` menghitung term Active dan Pending (nilai 2)
29. Verifikasi term Waiting for Approval, Rejected, dan Canceled tidak dihitung pada Total Subscription Client `Client Total Subscription+{runId}-129`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC berbeda dari sumber: TC-AC-CS-475 (Distributor) dijalankan terakhir supaya hanya terjadi satu pergantian akun (S-07). TC-AC-CS-480 (Auto-Archive Client setelah Cancel Subscription terakhir) ada di spec 161.
- Langkah penghubung (S-03): langkah 6, 11, 13 (pindah halaman), langkah 7 (Search untuk menemukan baris target, R-16), langkah 9 (pindah tab), langkah 21 dan 23 (menutup form dirty dengan Verifikasi dialog pada langkah 22, S-08), dan langkah 24 (Logout sebagai bagian ganti akun).
- Langkah 29 memakai Total Subscription = 2 pada langkah 28 sebagai anchor positif untuk asersi bahwa term WfA/Rejected/Canceled tidak dihitung (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-474, 475, 476, 479 tidak menyebut label menu dan jalur navigasi ke Client Detail, Detail Distributor, Dashboard, dan License Allocation; spec memakai label menu seperti nama modul dan perlu dikonfirmasi tim FE.
  - TC-AC-CS-475 Expected a tidak menyebut angka Total Subscription; angka 2 diturunkan dari seed spec (Active + Pending). Judul TC menyebut Distributor dan Partner tetapi langkah hanya Distributor; Partner tidak diuji.
  - TC-AC-CS-476 Expected c (angka Dashboard) sengaja tidak diasersi menurut TC.
  - TC-AC-CS-479 Expected b dan c tidak menyebut cara mengamati "ledger kosong" dan "belum efektif" pada form Allocate License; spec memakai Verifikasi pada form tanpa mengarang nama elemen, perlu dilengkapi QA. Label tombol Allocate License tidak disebut TC.
  - TC-AC-CS-474 dan 475 bergantung pada term hasil TC lain (Dependensi TC-AC-CS-143, 144, 262); pemicu ditulis sebagai seeding sesi API aktor yang disediakan tim FE/BE (S-13).
