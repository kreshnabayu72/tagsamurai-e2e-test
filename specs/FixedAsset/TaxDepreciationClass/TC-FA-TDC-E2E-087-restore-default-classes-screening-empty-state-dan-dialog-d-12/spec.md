---
id: TC-FA-TDC-E2E-087-restore-default-classes-screening-empty-state-dan-dialog-d-12
title: "Restore Default Classes: Screening Empty State, Posisi Tombol, dan Dialog D-12 (Cancel dan Esc)"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-8
  - TC-FA-TDC-315
  - TC-FA-TDC-319
  - TC-FA-TDC-321
  - TC-FA-TDC-322
sourceRules: ["ST-23", "FATDC-LOGIC-02k", "§4.1.1#b7", "§4.1.1#r2", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "§4.1.1#p5", "§4.6#b5", "§4.1.1#b4", "D-12", "FATDC-LOGIC-02f", "§4.1.5#r1", "§4.1.5#r2", "§4.1.5#r3", "§4.1.5#r4", "§4.1.5#r5", "§4.1.5#r6", "§4.1.5#r7", "E-FATDC-45", "§4.1#r6"]
smoke: []
dependsOn: []
trace:
  "ST-23": [2, 3, 4, 5, 8, 25, 29]
  "FATDC-LOGIC-02k": [5, 25]
  "§4.1.1#b7": 6
  "§4.1.1#r2": 7
  "§4.1.1#r8": 7
  "§4.1.1#r9": 7
  "§4.1.1#r10": 7
  "§4.1.1#p5": 10
  "§4.6#b5": [11, 14]
  "§4.1.1#b4": 13
  "D-12": [18, 19, 20, 22, 24, 29]
  "FATDC-LOGIC-02f": [19, 20, 30]
  "§4.1.5#r1": 19
  "§4.1.5#r2": 19
  "§4.1.5#r3": 19
  "§4.1.5#r4": 19
  "§4.1.5#r5": 19
  "§4.1.5#r6": 19
  "§4.1.5#r7": 19
  "E-FATDC-45": 21
  "§4.1#r6": 22
anchor: [26]
coverage:
  web: automated
---

# Restore Default Classes: Screening Empty State, Posisi Tombol, dan Dialog D-12 (Cancel dan Esc)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Data: tabel Tax Depreciation Class tanpa class sama sekali (semua status): di hook `before` seluruh class company uji dihapus lewat seeding API (company yang disediakan tim FE khusus automation) sebelum `beforeEach` membuka halaman, sehingga Empty State tampil. Hook `after` memulihkan tujuh class seed bawaan lewat seeding API (`suite.md`). Spec tidak mengubah data tabel.
- Master Data Count Limit tidak membatasi tujuh class (TC-319).
- Kemampuan teknis: mengosongkan seluruh class dan memulihkan tujuh class seed lewat API; menekan `Esc`; membuka overlay Column Visibility (⋯) pada header kolom.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-8: Screening Empty State tabel tanpa class

1. Amati area tabel
2. Verifikasi Illustration tampil di area tabel
3. Verifikasi Title `No tax depreciation class`
4. Verifikasi Description `Tax depreciation cannot be calculated.`
5. Verifikasi tombol `Restore default classes` tampil
6. Verifikasi chip filter dan `Clear all` tidak tampil
7. Verifikasi header kolom tabel tetap dirender di atas area Empty State (Class Code, Allowed Methods, Used By, Effective From)

### TC-FA-TDC-315: Restore default classes hanya tampil di Empty State

8. Verifikasi Empty State menampilkan Title "No tax depreciation class", Description "Tax depreciation cannot be calculated.", dan tombol `Restore default classes`
9. Amati toolbar
10. Verifikasi toolbar tampil dengan Search, Filter, Download, Changelog, dan `+ Class`
11. Verifikasi toolbar tidak memuat `Restore default classes`
12. Klik ⋯ pada header kolom untuk membuka overlay Column Visibility
13. Verifikasi overlay ⋯ tampil dengan daftar kolom
14. Verifikasi overlay ⋯ tidak memuat `Restore default classes`
15. Klik `[×]` pada overlay Column Visibility

### TC-FA-TDC-319: Screening dialog Restore default classes (D-12)

16. Klik `Restore default classes` di Empty State
17. Amati dialog dari atas ke bawah
18. Verifikasi header: judul dialog `Restore default classes`
19. Verifikasi bagian "To be created" dengan tujuh bullet berurutan: "• NB-1 – Bukan bangunan – Kelompok 1"; "• NB-2 – Bukan bangunan – Kelompok 2"; "• NB-3 – Bukan bangunan – Kelompok 3"; "• NB-4 – Bukan bangunan – Kelompok 4"; "• BLD-P – Bangunan permanen"; "• BLD-NP – Bangunan tidak permanen"; "• LAND – Tanah"
20. Verifikasi bagian "To be reactivated" dan "Skipped, already exists" tidak tampil
21. Verifikasi teks "All default classes already exist." tidak tampil
22. Verifikasi footer: tombol `[Cancel]` dan `[Restore]` (enabled)

### TC-FA-TDC-321: Tombol Cancel pada D-12

23. Klik `[Cancel]`
24. Verifikasi dialog D-12 tertutup
25. Verifikasi Empty State tetap tampil dengan tombol `Restore default classes`
26. Verifikasi tidak ada toast

### TC-FA-TDC-322: Esc pada D-12

27. Klik `Restore default classes`
28. Tekan `Esc`
29. Verifikasi dialog D-12 tertutup dan Empty State tetap tampil
30. Verifikasi tidak ada class dibuat dan tidak ada toast

## Notes

- Langkah penghubung (S-03): langkah 1, 9, 17 ("Amati" tanpa asersi) dan langkah 15 (menutup overlay Column Visibility; TC tidak menyebut cara menutupnya).
- Langkah 12 dan 13 dipakai sebagai anchor positif untuk absence pada langkah 14 (8b.2): overlay sudah terbuka dan memuat daftar kolom; langkah 10 adalah anchor untuk absence pada langkah 11. Anchor untuk absence toast pada langkah 26 dan 30 adalah Empty State yang tampil (langkah 25 dan 29).
- Langkah 8 dan 5 mengasersi komponen Empty State yang sama dari dua sudut (TC-8 dan TC-315 butir a); langkah 8 dibiarkan satu `Verifikasi` karena Expected TC-315 menyebut ketiganya dalam satu butir.
- Post Condition TC-321 ("tidak ada class dibuat", "tidak ada entri log") tidak punya langkah observasi di TC; "tidak ada class dibuat" diamati lewat Empty State yang tetap tampil (langkah 25), entri log tidak diasersi (S-01).
- Dialog D-12 tidak dikonfirmasi `[Restore]` di spec ini; Restore ada di spec 088 dan 239.
- Temuan untuk QA:
  - Isi tabel tanpa class tidak dapat dibuat lewat UI tanpa menghapus seluruh class; spec memakai seeding API (company khusus automation).
  - TC-315 menyebut "overlay ⋯" tanpa langkah membukanya; spec membukanya dan menutupnya dengan `[×]`.
  - Email akun Total Control tidak tertulis di TC.
