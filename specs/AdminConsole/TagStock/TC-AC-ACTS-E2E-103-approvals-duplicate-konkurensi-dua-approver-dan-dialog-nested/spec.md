---
id: TC-AC-ACTS-E2E-103-approvals-duplicate-konkurensi-dua-approver-dan-dialog-nested
title: "Approvals Duplicate Konkurensi: Dua Approver Approve Subject yang Sama, Approve dan Reject Bersamaan, Reject Pertama Mengunci, serta Esc pada Dialog Nested"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-290
  - TC-AC-ACTS-291
  - TC-AC-ACTS-808
  - TC-AC-ACTS-809
coverage:
  web: automated
---

# Approvals Duplicate Konkurensi: Dua Approver Approve Subject yang Sama, Approve dan Reject Bersamaan, Reject Pertama Mengunci, serta Esc pada Dialog Nested

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Total Control kedua / Admin B (akun tidak ada di Pre-setup TC; disediakan tim FE) `disediakan tim FE`, password dari `Spectra.env.AC_TC2_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal spec: Approvals > TAG Stock > Tab Active pada Sesi A (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas c (multi-konteks): dua sesi UI Total Control. Sesi A memakai akun hook `before`. Sesi B memakai konteks browser kedua yang login sebagai Total Control kedua (Admin B; akun tidak ada di Pre-setup TC, disediakan tim FE) dan ditutup di hook `after`. Pool approver memuat lebih dari satu approver.
- Data Subject pending disiapkan seeding fixture BE (disediakan tim FE/BE): satu Subject Register Duplicate dari requester Distributor untuk tiap TC (S1 untuk TC-AC-ACTS-290, S2 untuk TC-AC-ACTS-291, S3 untuk TC-AC-ACTS-808, S4 untuk TC-AC-ACTS-809). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca saldo Stock Ledger entitas requester (Device Allocation > Stock Balance Summary Panel) dan Total Registered SKU sebagai baseline (S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_TC2_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-290: Race, dua approver Approve Subject yang sama

1. [Sesi A] Buka Approvals > TAG Stock > Tab Active
2. [Sesi B] Buka Approvals > TAG Stock > Tab Active
3. Catat baseline saldo Stock Ledger entitas requester
4. [Sesi A] Klik `Review` pada S1
5. [Sesi B] Klik `Review` pada S1
6. [Sesi A] Pilih Approve, klik `[Submit]`
7. Verifikasi Sesi A berhasil dengan toast "Success, duplicate TAG has been approved and registered as [TAG Code]."
8. [Sesi B] Pilih Approve, klik `[Submit]`
9. Verifikasi Sesi B melihat dialog nested `Approval cannot be made` dengan teks `This request has already been resolved.` dan tombol `[Close]`
10. [Sesi B] Klik `[Close]`
11. Verifikasi `[Close]` menutup kedua dialog dan Tab Active direfresh
12. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas requester
13. Verifikasi hanya satu kredit Stock Ledger (saldo bertambah 1 terhadap baseline) dan satu TAG Code diterbitkan

### TC-AC-ACTS-291: Race, Approver A Approve sementara Approver B Reject

14. [Sesi A] Klik `Review` pada S2
15. [Sesi B] Klik `Review` pada S2
16. [Sesi A] Pilih Approve, klik `[Submit]`
17. Tunggu aksi selesai (dialog Review Sesi A tertutup)
18. [Sesi B] Pilih Reject, isi Approval Note `Duplicate hardware`, klik `[Submit]`
19. Verifikasi Sesi B menerima dialog nested `Approval cannot be made`
20. [Sesi B] Klik `[Close]`
21. [Sesi A] Buka Approvals > Tab History
22. Verifikasi hanya keputusan pertama berlaku (S2 tercatat Approved oleh Sesi A)
23. Verifikasi tidak ada TAG Code ganda untuk S2

### TC-AC-ACTS-808: Esc pada dialog nested menutup lapisan teratas saja dan klik backdrop tidak menutup dialog apa pun

24. [Sesi A] Buka Tab Active, klik `Review` pada S3
25. [Sesi B] Buka Tab Active, klik `Review` pada S3
26. [Sesi A] Pilih Approve, klik `[Submit]`
27. Tunggu aksi selesai (dialog Review Sesi A tertutup)
28. [Sesi B] Pilih Approve, klik `[Submit]`
29. Verifikasi dialog nested tampil dengan teks `This request has already been resolved.` dan tombol `[Close]`
30. [Sesi B] Klik area backdrop
31. Verifikasi klik backdrop tidak menutup dialog apa pun
32. [Sesi B] Tekan Esc
33. Verifikasi Esc menutup hanya dialog nested
34. Verifikasi Dialog Detail Approval milik Sesi B tetap terbuka
35. [Sesi B] Klik `[Cancel]` pada Dialog Detail Approval
36. Verifikasi `[Cancel]` menutup Dialog Detail Approval dan kembali ke Tab Active

### TC-AC-ACTS-809: Reject pertama dari approver pool langsung mengunci Subject, Approve approver lain sesudahnya ditolak

37. [Sesi A] Catat Total Registered SKU melalui TAG > Stock
38. [Sesi A] Buka Approvals > TAG Stock > Tab Active, klik `Review` pada S4
39. [Sesi B] Buka Tab Active, klik `Review` pada S4
40. [Sesi A] Pilih Reject, isi Approval Note `Duplicate hardware`, klik `[Submit]`
41. Verifikasi setelah Reject Sesi A, Subject langsung Rejected dan tidak menunggu approver lain
42. [Sesi B] Pilih Approve, klik `[Submit]`
43. Verifikasi Sesi B melihat dialog nested `Approval cannot be made` dengan teks `This request has already been resolved.`
44. [Sesi B] Klik `[Close]`
45. [Sesi A] Buka Approvals > TAG Stock > Tab Active dan Tab History
46. Verifikasi Tab Active memuat sedikitnya satu Subject lain (baris pembanding)
47. Verifikasi Tab Active tidak memuat S4
48. Verifikasi Tab History memuat satu baris Rejected untuk S4 dengan Approver Sesi A dan TAG Code `—`
49. Verifikasi tidak ada TAG Code diterbitkan
50. [Sesi A] Buka TAG > Stock dan baca Total Registered SKU itu
51. Verifikasi Total Registered tidak berubah terhadap baseline

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (51 langkah); alasan: semua blok satu kelas harness (kelas c, dua sesi UI Total Control) dan satu dataset Subject pending, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Sesi B adalah objek asersi (dialog nested di sesi itu), jadi sesi UI kedua dipakai; `P-2` tidak dipakai karena Sesi B bukan pemicu semata.
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), membuka layar, "Tunggu aksi selesai" sesudah `[Submit]` Sesi A sebelum Sesi B bertindak (bagian 8b butir 8), dan `[Close]` menutup dialog nested sebelum langkah berikutnya (S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-290 menyebut "dua sesi: Approver A dan Approver B" tanpa menyebut akun Approver B; disediakan tim FE.
  - TC-AC-ACTS-291 menyebut "alasan terisi" tanpa nilai; spec memakai `Duplicate hardware` (nilai TC-AC-ACTS-809).
  - TC-AC-ACTS-291 menyebut "tidak ada TAG Code ganda" tanpa cara mengamati; spec membaca Tab History.
