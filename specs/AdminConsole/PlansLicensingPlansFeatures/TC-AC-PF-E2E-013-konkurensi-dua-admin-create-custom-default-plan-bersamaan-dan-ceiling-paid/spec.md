---
id: TC-AC-PF-E2E-013-konkurensi-dua-admin-create-custom-default-plan-bersamaan-dan-ceiling-paid
title: "Konkurensi Dua Admin: Create Custom Plan dan Default Plan Bersamaan serta Ceiling Paid"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-587
  - TC-AC-PF-588
  - TC-AC-PF-589
coverage:
  web: automated
---

# Konkurensi Dua Admin: Create Custom Plan dan Default Plan Bersamaan serta Ceiling Paid

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor pertama): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun sesi B (konteks browser kedua): Total Control Principal kedua `secondAdminPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`, Pre-setup #9), password dari `Spectra.env.AC_PF_SA_PASSWORD`. Kelas harness: c multi-konteks (dua sesi UI; sesi B menjadi objek asersi).
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Sesi B login pada langkah 1 di konteks browser kedua; hook `after` menutup konteks kedua dan mengembalikan sesi ke akun default suite.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: termasuk default plan `Growth` sebagai Template dan `SIEM` Paid), Dataset Plan S (Pre-setup #31: `Supply Starter` Free dan `Supply Pro` Paid, Product SAMS), Dataset Plan U (Pre-setup #33: Default SIEM dengan 1 Paid aktif `SIEM` dan tanpa Free). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Data Dinamis milik spec (bersuffix, dibuat selama spec, dibersihkan lewat fixture BE di hook `after`): custom plan `Paket Serempak {runId}-013`; default plan `Supply Serempak {runId}-013`; default plan Paid SIEM `SIEM Dua {runId}-013` (ditambahkan fixture BE pada langkah 25 agar SIEM memiliki 2 Paid aktif), `SIEM Serempak A {runId}-013`, dan `SIEM Serempak B {runId}-013`.
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `SIEM`, `Supply Starter`, `Supply Pro`) dipakai karena menentukan Template dan ceiling Paid; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: konteks browser kedua dengan login akun #9; fixture BE (penambahan default plan Paid, pembersihan plan buatan spec, pemulihan Dataset) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: `Spectra.env.AC_TC_PASSWORD` (sesi A) dan `Spectra.env.AC_PF_SA_PASSWORD` (sesi B); nama `AC_PF_SA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-587: Dua admin membuat custom plan dengan nama sama bersamaan: yang kedua ditolak

1. Sesi B: buka konteks browser kedua, login sebagai Total Control kedua (Principal), lalu buka Plans & Licensing > Plans & Features
2. Sesi A: klik tab Custom, klik `+ Custom Plan`, pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Serempak {runId}-013`
3. Sesi B: klik tab Custom, klik `+ Custom Plan`, pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Serempak {runId}-013`
4. Sesi A: klik `[Submit]`
5. Sesi B: klik `[Submit]` tepat sesudah sesi A
6. Verifikasi sesi A menampilkan toast sukses: "Success, custom plan has been created."
7. Verifikasi sesi B menampilkan pesan `Plan name already exists`
8. Verifikasi form di sesi B tetap terbuka
9. Sesi B: klik segmen Breadcrumb `Plans & Features`
10. Verifikasi sesi B menampilkan dialog `Unsaved Changes`
11. Sesi B: klik `[Leave]`
12. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar lalu klik tab Custom
13. Sesi A: ketik Search `Paket Serempak {runId}-013`, tekan Enter
14. Verifikasi sesi A menampilkan tepat satu baris `Paket Serempak {runId}-013` (`Showing 1–1 of 1 entries`)
15. Sesi A: klik `(←)` pada kotak Search

### TC-AC-PF-588: Dua Principal membuat default plan dengan nama sama bersamaan pada Product yang sama: yang kedua ditolak

16. Sesi A: klik tab Default, klik `+ Default Plan`, pilih Product `SAMS`, isi Plan Name `Supply Serempak {runId}-013`, pilih Pricing Type `Paid`
17. Sesi B: klik tab Default, klik `+ Default Plan`, pilih Product `SAMS`, isi Plan Name `Supply Serempak {runId}-013`, pilih Pricing Type `Paid`
18. Sesi A: klik `[Submit]`
19. Sesi B: klik `[Submit]` sesudah sesi A
20. Verifikasi sesi A menampilkan toast sukses: "Success, default plan has been created."
21. Verifikasi sesi B menampilkan pesan `Plan name already exists`
22. Sesi B: klik segmen Breadcrumb `Plans & Features`
23. Verifikasi sesi B menampilkan dialog `Unsaved Changes`
24. Sesi B: klik `[Leave]`

### TC-AC-PF-589: Dua Principal membuat plan Paid terakhir bersamaan: satu berhasil mengisi slot ketiga, yang lain ditolak oleh ceiling

25. Tambahkan default plan Paid SIEM kedua `SIEM Dua {runId}-013` lewat fixture BE hingga tersimpan sehingga SIEM memiliki 2 Paid aktif
26. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, klik `+ Default Plan`, pilih Product `SIEM`, pilih Pricing Type `Paid`, isi Plan Name `SIEM Serempak A {runId}-013`
27. Sesi B: klik menu Plans & Licensing > Plans & Features di sidebar, klik `+ Default Plan`, pilih Product `SIEM`, pilih Pricing Type `Paid`, isi Plan Name `SIEM Serempak B {runId}-013`
28. Sesi A: klik `[Submit]`
29. Sesi B: klik `[Submit]` sesudah sesi A
30. Verifikasi sesi yang ditolak (sesi B) menampilkan pesan "This product already has the maximum number of paid plans (3). Archive an existing one first."
31. Sesi B: klik segmen Breadcrumb `Plans & Features`
32. Verifikasi sesi B menampilkan dialog `Unsaved Changes`
33. Sesi B: klik `[Leave]`
34. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, ketik Search `SIEM Serempak`, tekan Enter
35. Verifikasi sesi A menampilkan hanya satu plan dari `SIEM Serempak A {runId}-013` dan `SIEM Serempak B {runId}-013` yang mengisi slot Paid ketiga (`Showing 1–1 of 1 entries`)
36. Sesi A: klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 9 sampai 11, 22 sampai 24, dan 31 sampai 33 menutup form dirty sesi B (S-08; `Verifikasi` dialog `Unsaved Changes` tidak dicatat ulang di Notes); langkah 12, 13, 15, 34, dan 36 membuka list dan mengosongkan Search untuk mengamati hasil sesi A (Search untuk menemukan baris target, R-16); klik tab Default/Custom pada langkah 2, 3, 16, dan 17 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 25 memenuhi precondition TC-AC-PF-589 (dipakai sebagai precondition TC, tidak diasersi).
- Nama plan memakai suffix `{runId}-013` (S-12) sebagai ganti nama literal TC (`Paket Serempak`, `Supply Serempak`, `SIEM Serempak A`, `SIEM Serempak B`).
- Alasan di atas sekitar 35 langkah (36 langkah): ketiga blok satu kelas harness (c multi-konteks, race Submit dua sesi) dan satu topik (create bersamaan), tiap blok memakai Product dan nama plan sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; menutup form dirty sesi B menambah tiga langkah per blok (S-08).
- Temuan untuk QA:
  - TC-AC-PF-587 dan TC-AC-PF-588: Post Condition "Satu custom plan `Paket Serempak`" dan "Satu default plan `Supply Serempak`". TC-AC-PF-587 memuat Expected "hanya satu plan" sehingga diamati lewat Search (langkah 13 dan 14); TC-AC-PF-588 tidak memberi langkah observasi untuk Post Condition sehingga tidak diasersi.
  - TC-AC-PF-589: TC tidak menyebut sesi mana yang berhasil; spec menganggap sesi A (klik `[Submit]` lebih dulu) berhasil dan sesi B ditolak (langkah 30). Hasil race dapat terbalik; mohon QA menegaskan.
  - TC-AC-PF-589: Post Condition "SIEM memiliki tepat 3 Paid aktif tanpa bentrok tier" tidak punya langkah observasi sehingga tidak diasersi; Expected a diamati lewat hasil Search (langkah 35).
