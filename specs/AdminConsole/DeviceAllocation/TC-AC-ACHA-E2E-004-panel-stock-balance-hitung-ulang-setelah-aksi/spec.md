---
id: TC-AC-ACHA-E2E-004-panel-stock-balance-hitung-ulang-setelah-aksi
title: "Panel Stock Balance Summary Dihitung Ulang Setelah Create dan Approve, Tidak Berubah Setelah Reject, Cancel, dan Timeout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-26
  - TC-AC-ACHA-27
  - TC-AC-ACHA-28
coverage:
  web: automated
---

# Panel Stock Balance Summary Dihitung Ulang Setelah Create dan Approve, Tidak Berubah Setelah Reject, Cancel, dan Timeout

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Partner CV Mitra Solusi (Pre-setup #43) `totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_P1_PASSWORD` (TC-28 dan TC-26). Akun kedua: Group Member Partner CV Mitra Solusi toggle ON (Pre-setup #44, alias MB_P1, nama pengguna Andi Wijaya) `memberOnPartner1_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P1_PASSWORD` (TC-28 langkah Cancel dan TC-27). Pelaku kedua penyetuju: Total Control Distributor PT Global Distribusi (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD` (Approve TC-27); hanya memicu perubahan state lewat sesi API aktor, bukan sesi UI.
- Login akun aktor pertama di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-11), dan fixture Pre-setup #20 dinyatakan di `suite.md` (endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48); kantong CV Mitra Solusi saldo $2,000.00 (Pre-setup #17, sumber PT Global Distribusi); transaksi Waiting for Approval NFC Quantity 10 milik MB_P1 (Pre-setup #56, TC-27); tiga transaksi Waiting for Approval NFC Quantity 10 milik MB_P1 (Pre-setup #57, TC-28). Allocation ID Pre-setup #56 dan #57 serta waktu terbit T1 transaksi #57 dibaca lewat fixture seed (disediakan tim FE/BE). Entitas CV Mitra Solusi memakai Client PT Retail Makmur (Pre-setup #8).
- Data Dinamis: dua transaksi Completed NFC milik Client PT Retail Makmur yang dibuat TC-26 (Allocation ID runtime, ditangkap sebagai Dynamic Reference, tidak di-hardcode). Spec ini men-seed ulang baseline lewat fixture dan tidak menumpang hasil spec lain.
- Kemampuan teknis: fixture baseline yang memulihkan seed Pre-setup #48, #56, #57, saldo kantong CV Mitra Solusi, dan kuota (disediakan tim FE/BE; dijalankan di hook `before`, sebagai langkah penghubung sebelum TC-26 dan sebelum TC-27, dan di hook `after`); sesi API aktor penyetuju; geser jam server lewat Pre-setup #20.
- Jam: hanya jam server yang digeser (Approval Timeout 3 hari dihitung murni di server dan tidak diamati lewat UI); T1 dibaca dari fixture seed, jam server diset absolut ke T1 + 3 hari + 1 menit (margin di atas batas 1 menit; dihitung dari T1 hasil fixture, bukan dari waktu nyata). Jam server dipulihkan segera sesudah job selesai dan di hook `after`. Menunggu siklus job memakai idiom polling worker commit (muat ulang halaman tiap 5 detik, batas 2 menit).
- State global: jam server digeser dan dipulihkan; kantong dan kuota diubah dan dipulihkan; suite berjalan serial. Sesi UI dan sesi API tetap valid selama jam server digeser (`suite.md`). Hook `after` memulihkan seed lewat fixture Pre-setup #20 (Lampiran A butir A-11).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_P1_PASSWORD`, `AC_DA_MB_P1_PASSWORD`, dan `AC_DA_TC_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-28: Reject, Cancel, dan Timeout tidak mengubah kuota

1. Catat nilai seluruh baris panel `Allocated quota` (halaman dibuka hook `beforeEach`; selanjutnya disebut nilai awal)
2. Buka Approvals > Device Allocation lewat sidebar
3. Reject satu transaksi Pre-setup #57 dengan Rejection Reason `Tidak sesuai` dan konfirmasi
4. Tunggu aksi selesai
5. Buka Allocation > Device Allocation lewat sidebar
6. Verifikasi nilai panel sama dengan nilai awal setelah Reject
7. Logout dari akun Total Control Partner CV Mitra Solusi
8. Login sebagai MB_P1 (`memberOnPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_P1_PASSWORD`)
9. Buka Allocation > Device Allocation lewat sidebar
10. Klik `Cancel Allocation` pada satu transaksi Pre-setup #57 lalu klik `[Cancel Allocation]` pada dialog
11. Tunggu aksi selesai
12. Muat ulang halaman Allocation > Device Allocation
13. Verifikasi nilai panel sama dengan nilai awal setelah Cancel
14. Logout dari akun MB_P1
15. Login sebagai Total Control Partner CV Mitra Solusi (`totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P1_PASSWORD`)
16. Buka Allocation > Device Allocation lewat sidebar
17. Geser jam server ke T1 + 3 hari + 1 menit lewat Pre-setup #20 (T1 waktu terbit transaksi ketiga Pre-setup #57 dari fixture seed)
18. Muat ulang halaman tiap 5 detik sampai transaksi ketiga Pre-setup #57 (dicari lewat Search Allocation ID) berstatus `Canceled` (batas tunggu 2 menit)
19. Pulihkan jam server ke waktu nyata lewat Pre-setup #20
20. Muat ulang halaman Allocation > Device Allocation
21. Verifikasi nilai panel sama dengan nilai awal setelah Timeout Auto-Cancel

### TC-AC-ACHA-26: Panel dihitung ulang setelah Create jalur langsung

22. Pulihkan baseline lewat fixture Pre-setup #20 (seed Pre-setup #48, #56, #57, saldo kantong CV Mitra Solusi $2,000.00, dan kuota)
23. Muat ulang halaman Allocation > Device Allocation
24. Amati panel `Allocated quota`
25. Verifikasi NFC pada panel bernilai `0`
26. Klik `[+ Allocation]`
27. Pilih Category `TAG - NFC`, pilih Client `PT Retail Makmur`, isi Quantity `10`
28. Klik `[Submit]`
29. Tunggu aksi selesai
30. Verifikasi baris teratas pada List (Last Updated terbaru) adalah transaksi baru berstatus `Completed`
31. Catat Allocation ID baris teratas List (ID transaksi pertama)
32. Verifikasi panel dihitung ulang: NFC berubah dari 0 menjadi 10
33. Klik `[+ Allocation]`
34. Pilih Category `TAG - NFC`, pilih Client `PT Retail Makmur`, isi Quantity `1250`
35. Klik `[Submit]`
36. Tunggu aksi selesai
37. Verifikasi baris teratas pada List adalah transaksi baru berstatus `Completed` dengan Allocation ID berbeda dari ID transaksi pertama
38. Catat Allocation ID baris teratas List (ID transaksi kedua, penanda pembersihan di hook `after`)
39. Verifikasi panel dihitung ulang: NFC berubah dari 10 menjadi `1,260`
40. Pulihkan baseline lewat fixture (seed Pre-setup #48, #56, saldo kantong CV Mitra Solusi $2,000.00)
41. Logout dari akun Total Control Partner CV Mitra Solusi

### TC-AC-ACHA-27: Panel dihitung ulang setelah Approve; Waiting for Approval tidak menambah kuota

42. Login sebagai MB_P1 (`memberOnPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_P1_PASSWORD`)
43. Buka Allocation > Device Allocation lewat sidebar
44. Amati nilai NFC pada panel sebelum persetujuan
45. Verifikasi NFC pada panel tetap `0` (kuota hanya bertambah saat Completed)
46. Approver (Total Control Distributor PT Global Distribusi) menyetujui transaksi Pre-setup #56 lewat sesi API hingga status Completed tersimpan
47. Tunggu aksi selesai
48. Buka kembali halaman Allocation > Device Allocation sebagai MB_P1 (muat ulang halaman)
49. Verifikasi panel menghitung ulang NFC menjadi `10`

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec menulis data (Create, Reject, Cancel, Approve, Timeout) lalu memulihkan baseline lewat fixture.
- Urutan TC di spec: TC-28, TC-26, TC-27 (penyimpangan dari urutan nomor). Alasan: TC-26 dan TC-27 sama-sama mensyaratkan NFC awal 0 sehingga dipisahkan oleh pemulihan baseline (langkah 40), dan TC-28 memakai nilai awal yang dicatat sendiri sehingga ditaruh pertama agar jumlah ganti akun minimal. Blok TC-28 menggeser jam server (langkah 17 sampai 19) dan tidak berada di akhir spec (S-10): efek pergeseran jam pada transaksi lain dinetralkan oleh pemulihan jam pada langkah 19 dan pemulihan baseline pada langkah 22 sebelum TC-26; urutan tetap karena TC-28 mencatat nilai awal panelnya sendiri.
- Langkah penghubung (S-03): langkah 7 sampai 9, 14 sampai 16, dan 41 sampai 43 (ganti akun), langkah 19 (pemulihan jam server), langkah 22 dan 23 (pemulihan baseline dan muat ulang sebelum TC-26, supaya urutan Last Updated tidak terpengaruh jam server yang sempat digeser pada TC-28 dan baris teratas List adalah transaksi baru; baris teratas pertama dicatat pada langkah 31 untuk pembanding langkah 37; ID transaksi kedua dicatat pada langkah 38; kedua ID menjadi penanda pembersihan hook `after`), langkah 40 (pemulihan baseline), langkah 11 dan 18 (tunggu aksi dan polling job; idiom polling bagian 6).
- P-2 (pemicu bukan objek uji): Timeout Auto-Cancel pada TC-28 hanya memicu perubahan yang diamati lewat panel; job latar Timeout hanya memicu kondisi. Approve pada TC-27 oleh pelaku kedua memakai sesi API (R-20), bukan konteks kedua dan bukan penerapan P-2.
- Asersi tambahan yang dicatat (S-03): TC-28 hanya mengamati panel di akhir (Langkah Uji TC nomor lima). Expected menyatakan nilai tidak berubah "setelah Reject, Cancel, maupun Timeout", sehingga spec mengamati panel sesudah masing-masing aksi (langkah 6, 13, 21) dengan nilai awal yang dicatat pada langkah 1. Approve pada TC-27 dilakukan lewat sesi API (R-20), bukan lewat UI Approvals; UI Approve diuji di spec 034.
- Ukuran spec (di atas sekitar 35 langkah): tiga TC berbagi satu permukaan (panel Allocated quota) dan satu entitas (CV Mitra Solusi). Tiap blok TC berdiri sendiri karena baseline dipulihkan sebelum TC-27 dan TC-28 mencatat nilai awalnya sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain (bagian 3, batas ukuran); ganti akun memakai langkah eksplisit.
- Temuan untuk QA:
  - TC-26 Expected memuat dua perhitungan ulang (NFC 0 menjadi 10, lalu 10 menjadi `1,260` setelah "Submit kedua") padahal judul hanya "Create jalur langsung"; Data Uji (Quantity 10 lalu 1250) tidak menjelaskan sumber 1,260. Spec mengikuti TC (dua Submit berurutan).
  - TC-26 dan TC-27 sama-sama mensyaratkan NFC awal 0 untuk CV Mitra Solusi pada seed yang sama, padahal TC-26 menambah kuota; spec memisahkannya dengan pemulihan baseline (kontrak fixture baseline tidak tertulis di TC, PRD, atau LLD; disediakan tim FE/BE).
  - TC-27 Langkah Uji 2 menyebut Approver "Total Control Distributor" membuka Approvals; Pre-setup #56 memakai Pay From PT Global Distribusi sehingga approver dipilih Total Control Distributor (#27). TC-28 langkah 2 memakai Total Control Partner CV Mitra Solusi untuk Reject transaksi MB_P1; kedua approver berbeda tanpa penjelasan di TC.
  - Post Condition TC-26 ("kuota Client PT Retail Makmur bertambah 1,260 NFC; tampil di Client Dashboard") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-28 Langkah Uji 4 tidak menyebut cara mengidentifikasi "transaksi ketiga" yang dibatalkan Timeout; spec memakai Allocation ID dari fixture seed.
