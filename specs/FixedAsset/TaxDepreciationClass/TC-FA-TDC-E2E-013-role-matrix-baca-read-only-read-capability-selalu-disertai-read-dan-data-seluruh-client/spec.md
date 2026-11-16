---
id: TC-FA-TDC-E2E-013-role-matrix-baca-read-only-read-capability-selalu-disertai-read-dan-data-seluruh-client
title: "Role Matrix: Akses Baca Read Only, Read, Capability Selalu Disertai Read, dan Data Berlaku Seluruh Client"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-41
  - TC-FA-TDC-42
  - TC-FA-TDC-43
  - TC-FA-TDC-46
sourceRules: ["§4.1.1#r16", "§5#b2", "§4.1#r7", "§4.1.1#p5", "§2.2#r3", "§4.8#r9", "§4.8#r12", "§4.8#r16", "§4.8#r1", "§4.8#r7", "§4.8#b2", "§4.8#r8", "§3.9#r2", "§4.1.1#r17", "§4.1.1#r18", "§4.1.1#r19", "§4.1.1#r20", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§9.11#p1"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r16": [2, 31, 34]
  "§5#b2": [3, 21]
  "§4.1#r7": [5, 23]
  "§4.1.1#p5": 7
  "§2.2#r3": 7
  "§4.8#r9": 8
  "§4.8#r12": 9
  "§4.8#r16": 9
  "§4.8#r1": [12, 19]
  "§4.8#r7": 14
  "§4.8#b2": 14
  "§4.8#r8": 15
  "§3.9#r2": 26
  "§4.1.1#r17": [31, 34]
  "§4.1.1#r18": [31, 34]
  "§4.1.1#r19": [31, 34]
  "§4.1.1#r20": [31, 34]
  "§4.1.1#r21": [31, 34]
  "§4.1.1#r22": [31, 34]
  "§4.1.1#r23": [31, 34]
  "§4.1.1#r24": [31, 34]
  "§9.11#p1": [34, 35]
coverage:
  web: automated
---

# Role Matrix: Akses Baca Read Only, Read, Capability Selalu Disertai Read, dan Data Berlaku Seluruh Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | langkah 1 sampai 10 |
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | langkah 11 sampai 16 |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | langkah 18 sampai 28 (iterasi) |
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 18 sampai 28 (iterasi) |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 18 sampai 28 (iterasi) |
| Total Control (Home Group A) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 29 sampai 31 |
| Read (Manage accounting) (Home Group B) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_HGB_PASSWORD` | langkah 32 sampai 35 |

- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji": `FA_RO_PASSWORD` dan `FA_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; `FA_READ_PASSWORD`, `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, dan `FA_READ_HGB_PASSWORD` belum terdaftar di keduanya dan didaftarkan penulis script.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Tabel "Role yang diuji" TC-FA-TDC-43 terdiri atas tiga role (Create-Only, Update-Only, Delete-Only); tiap role di sana memegang akses baca (Read) sebagai bagian dari capability-nya.
- TC-FA-TDC-46: Total Control dengan Home Group A dan Read (Manage accounting) dengan Home Group B; kedua akun disediakan tim FE.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Read Only (TC-FA-TDC-41)

1. Ketik Search `NB-1`, tekan Enter
2. Verifikasi baris NB-1 tampil
3. Verifikasi tabel hanya memuat baris NB-1
4. Klik ikon Changelog
5. Verifikasi Popup `Changelog: Tax Depreciation Class` terbuka
6. Tutup Popup Changelog
7. Verifikasi toolbar hanya memuat `Search | Filter | Download | Changelog`
8. Verifikasi tombol `+ Class` tidak ada
9. Verifikasi kolom checkbox dan menu `⋯` per baris tidak ada
10. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### Role Read (TC-FA-TDC-42)

11. Ganti akun: logout, login sebagai Read (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
12. Verifikasi tab dan tabel tampil
13. Klik Class Code NB-2
14. Verifikasi Drawer mode Edit terbuka dengan seluruh field Disabled (tampil, non-interaktif)
15. Verifikasi `[Clear Field]` dan `[Save]` tidak tampil
16. Tutup Drawer dengan `[×]`

### Create, Update, dan Delete selalu disertai Read (TC-FA-TDC-43)

17. Untuk setiap role pada tabel "Role yang diuji" (Create-Only, Update-Only, Delete-Only), lakukan langkah 18 sampai 28
18. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
19. Verifikasi tab terbuka
20. Ketik Search `NB-1`, tekan Enter
21. Verifikasi Search menyaring tabel ke baris NB-1
22. Klik ikon Changelog
23. Verifikasi Popup `Changelog: Tax Depreciation Class` terbuka
24. Tutup Popup Changelog
25. Klik Class Code NB-1
26. Verifikasi Drawer NB-1 terbuka
27. Tutup Drawer dengan `[×]`
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### Data berlaku seluruh client (TC-FA-TDC-46)

29. Ganti akun: logout, login sebagai Total Control (Home Group A), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
30. Catat baris tabel yang tampil
31. Verifikasi tabel menampilkan 9 baris Example Data
32. Ganti akun: logout, login sebagai Read (Manage accounting) (Home Group B), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
33. Catat baris tabel yang tampil
34. Verifikasi tabel menampilkan 9 baris yang sama dengan yang dicatat pada Total Control
35. Verifikasi tidak ada penyaringan per Group atau per Class

## Notes

- Satu spec memuat beberapa aksi positif (Search dan Changelog, membuka Drawer, tampilan data seluruh client) karena seluruhnya Role Matrix positif atas tabel yang sama dan berpolaritas seragam (bagian 3a, keputusan 2026-11-02). Blok TC-FA-TDC-43 memakai perulangan atas tiga role pada tabel (langkah 18 sampai 28) dengan langkah ganti akun eksplisit di awal iterasi.
- Spec 35 langkah nominal dan sekitar 57 langkah setelah ekspansi perulangan (tiga iterasi). Alasan: seluruh blok satu kelas (Role Matrix positif), parameter iterasi hanya akun login, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (S-03): langkah 6 dan 24 (menutup popup), langkah 16 dan 27 (menutup Drawer), langkah 10 dan 28 (menutup input Search dan mereset tabel, S-09), langkah 11, 18, 29, dan 32 (ganti akun dan membuka layar), langkah 30 dan 33 (mencatat baris tabel). Langkah 2 (baris NB-1 tampil) dan langkah 7 (toolbar tampil) adalah anchor positif sebelum asersi "hanya" pada langkah 3 dan 8 (8b.2).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Judul TC-41 menyebut memfilter dan Download, tetapi LK dan EXP hanya memuat Search, Changelog, dan elemen toolbar; spec mengikuti LK dan EXP.
  - TC-43 menyebut capability "Create, Update, dan Delete" tanpa menyebut akun gabungan; spec memakai tiga akun satu capability (Create-Only, Update-Only, Delete-Only) seperti Precondition TC.
