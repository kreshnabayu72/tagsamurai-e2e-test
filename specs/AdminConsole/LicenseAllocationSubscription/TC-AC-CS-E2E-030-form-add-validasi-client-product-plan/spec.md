---
id: TC-AC-CS-E2E-030-form-add-validasi-client-product-plan
title: "Form Add: Validasi Client, Product, Plan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-112
  - TC-AC-CS-113
  - TC-AC-CS-114
  - TC-AC-CS-115
  - TC-AC-CS-116
coverage:
  web: automated
---

# Form Add: Validasi Client, Product, Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-030` (padanan Pre-setup #48: tanpa term dan tanpa trial) untuk TC-AC-CS-112, 114, 115, 116; Client `Client Dihapus+{runId}-030` (kondisi sama) untuk TC-AC-CS-113; Custom Plan FAMS `Maju Custom` milik PT Maju Bersama.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; sesi API aktor Principal): menghapus Client seed hingga tersimpan, mengarsipkan Custom Plan `Maju Custom` hingga tersimpan lalu memulihkannya (Un-archive) di hook `after`, dan membaca jumlah term Client seed lewat fixture BE.

## Test Steps

### TC-AC-CS-112: Validasi Client wajib saat Submit varian Add

1. Klik `[+ Subscription]`
2. Isi Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26` tanpa memilih Client
3. Klik `[Submit]`
4. Verifikasi error inline di bawah field Client "Client must not be empty"
5. Verifikasi modal tetap terbuka
6. Verifikasi jumlah term Client `Client Tanpa Subscription+{runId}-030` tetap 0 (dibaca lewat fixture BE)
7. Klik `[Clear Field]`

### TC-AC-CS-114: Validasi Product wajib saat Submit varian Add

8. Pilih Client `Client Tanpa Subscription+{runId}-030`, isi Duration `1` dan Start Date `19/08/26` tanpa memilih Product
9. Klik `[Submit]`
10. Verifikasi error inline di bawah field Product "Product must not be empty"
11. Verifikasi modal tetap terbuka
12. Klik `[Clear Field]`

### TC-AC-CS-115: Validasi Plan wajib saat Submit varian Add

13. Pilih Client `Client Tanpa Subscription+{runId}-030` dan Product `SAMS`, isi Duration `1` dan Start Date `19/08/26` tanpa memilih Plan
14. Klik `[Submit]`
15. Verifikasi error inline di bawah field Plan "Plan must not be empty"
16. Verifikasi modal tetap terbuka
17. Klik `[Clear Field]`

### TC-AC-CS-113: Client dihapus sesi lain antara form dibuka dan Submit

18. Pilih Client `Client Dihapus+{runId}-030`, Product `SAMS`, Plan `Growth`, isi Duration `1` dan Start Date `19/08/26`
19. Hapus Client `Client Dihapus+{runId}-030` lewat sesi API aktor hingga penghapusan tersimpan
20. Klik `[Submit]`
21. Verifikasi error inline "This client no longer exists. Please select another."
22. Buka dropdown Client
23. Verifikasi dropdown Client memuat sedikitnya satu opsi Client
24. Verifikasi field Client dikosongkan dan opsi dimuat ulang tanpa `Client Dihapus+{runId}-030`
25. Tekan `Esc` untuk menutup dropdown Client
26. Verifikasi Product `SAMS`, Plan `Growth`, Duration `1`, dan Start Date `19/08/26` dipertahankan
27. Klik `[Clear Field]`

### TC-AC-CS-116: Plan di-Archive atau di-Delete sesi lain sebelum Submit varian Add

28. Pilih Client `Client Tanpa Subscription+{runId}-030`, Product `FAMS`, Plan `Maju Custom`, isi Duration `1` dan Start Date `19/08/26`
29. Arsipkan Custom Plan `Maju Custom` lewat sesi API aktor hingga status Archive tersimpan
30. Klik `[Submit]`
31. Verifikasi error inline "This plan no longer exists. Please select another."
32. Buka dropdown Plan
33. Verifikasi dropdown Plan memuat sedikitnya satu opsi plan
34. Verifikasi field Plan dikosongkan dan opsi dimuat ulang tanpa plan yang di-Archive
35. Tekan `Esc` untuk menutup dropdown Plan
36. Verifikasi Client `Client Tanpa Subscription+{runId}-030`, Product `FAMS`, Duration `1`, dan Start Date `19/08/26` dipertahankan
37. Pulihkan Custom Plan `Maju Custom` (Un-archive) lewat sesi API aktor, lalu klik `[✕]` pada header modal
38. Verifikasi dialog Unsaved Changes tampil
39. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC-AC-CS-112, 114, 115 mengikuti kelompok validasi field wajib sebelum validasi server (TC-AC-CS-113 dan 116) sesuai S-10; nomor TC tidak berurutan di spec.
- Langkah penghubung (S-03): `[Clear Field]` di antara kasus dengan error inline berbeda (R-12; langkah 7, 12, 17, 27), membuka dropdown Client dan Plan sebagai anchor absence (butir 8b.2; langkah 22 sampai 25 dan 32 sampai 35, positif sebelum absence pada langkah 24 dan 34), `Esc` menutup dropdown (langkah 25, 35), dan pemulihan Un-archive plan (langkah 37). Pemulihan plan juga dijalankan di hook `after`.
- Ukuran: 39 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (validasi form Add) dengan satu dataset seed, kegagalan satu blok validasi tidak menghalangi blok lain, dan tambahan langkah berasal dari anchor absence dropdown (butir 8b.2) serta Verifikasi per klausa Expected (S-01); pemecahan menambah login dan seeding tanpa menambah isolasi.
- Penghapusan Client dan arsip Plan lewat sesi API ditulis "... hingga ... tersimpan" (R-20).
- Penutupan form dirty pada langkah 37 sampai 39 mengikuti S-08.
- Temuan untuk QA:
  - TC-AC-CS-113 dan TC-AC-CS-116 tidak menyebut cara sesi lain menghapus Client atau mengarsipkan Plan (endpoint tidak ada di TC, PRD, atau LLD); ditulis sebagai kemampuan "disediakan tim FE/BE" (S-13).
  - TC-AC-CS-116 judul menyebut "Archive atau Delete" sedangkan Langkah dan Expected hanya Archive; spec menguji Archive.
  - TC-AC-CS-112 Expected b "tidak ada record dibuat" tidak menyebut cara cek; spec memakai pembacaan jumlah term lewat fixture BE.
