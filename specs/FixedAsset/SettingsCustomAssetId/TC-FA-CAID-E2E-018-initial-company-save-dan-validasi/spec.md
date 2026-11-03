---
id: TC-FA-CAID-E2E-018-initial-company-save-dan-validasi
title: "Initial Company: Validasi Kosong Diblokir dan Save Nilai Valid"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-57
  - TC-FA-CAID-55
  - TC-FA-CAID-56
  - TC-FA-CAID-59
  - TC-FA-CAID-60
coverage:
  web: automated
---

# Initial Company: Validasi Kosong Diblokir dan Save Nilai Valid

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan baseline B2 (Separator `- (Dash)`, Initial Company `ABC` dan Division Code tercentang di atas B1). B1 dipakai TC-FA-CAID-57, 55, 56, dan 59; B2 dipakai TC-FA-CAID-60 dan di-seed lewat sesi API aktor pada langkah 34. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): pemulihan baseline B1 dan B2 lewat sesi API aktor; konfirmasi otomatis dialog `beforeunload` bawaan browser oleh harness untuk muat ulang pada form yang belum disimpan (langkah 8).
- State: spec ini menyimpan konfigurasi Company Alpha. Pemulihan antar TC lewat langkah penghubung (langkah 17, 25, 33) dan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-57: Save dengan Initial Company dicentang dan input kosong ditolak

1. Centang checkbox `Initial Company` dan biarkan input kosong
2. Klik `[Save]`
3. Verifikasi error `Initial company must not be empty` tampil tepat di bawah input Initial Company
4. Verifikasi helper text `Prefix identifier representing your company entity (up to 5 characters, letters and numbers only). Required when checked.` tidak tampil karena digantikan error
5. Verifikasi tidak ada toast sukses maupun toast error
6. Verifikasi tidak ada alert di atas `[Save]`
7. Verifikasi form tetap terbuka dengan checkbox `Initial Company` tercentang
8. Muat ulang halaman
9. Verifikasi checkbox `Initial Company` tidak tercentang

### TC-FA-CAID-55: Initial Company 1 karakter valid disimpan

10. Centang checkbox `Initial Company`
11. Ketik `A` pada input Initial Company
12. Klik `[Save]`
13. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
14. Muat ulang halaman
15. Verifikasi input Initial Company berisi `A`
16. Verifikasi Live Preview menampilkan `A/JKT/LAP/T490/0926/1`
17. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-56: Initial Company 5 karakter alfanumerik valid disimpan

18. Centang checkbox `Initial Company`
19. Ketik `AB1CD` pada input Initial Company
20. Klik `[Save]`
21. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
22. Muat ulang halaman
23. Verifikasi input Initial Company berisi `AB1CD`
24. Verifikasi Live Preview menampilkan `AB1CD/JKT/LAP/T490/0926/1`
25. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-59: Save dengan Initial Company bernilai ABC menyimpan segmen pada formula

26. Centang checkbox `Initial Company` dan ketik `ABC` pada input Initial Company
27. Klik `[Save]`
28. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
29. Muat ulang halaman
30. Verifikasi checkbox `Initial Company` tercentang
31. Verifikasi input Initial Company berisi `ABC`
32. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0926/1`
33. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-60: Save setelah Initial Company di-uncheck tidak menyimpan nilainya

34. Setel konfigurasi Company Alpha ke baseline B2 lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman
35. Hilangkan centang checkbox `Initial Company`
36. Klik `[Save]`
37. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
38. Muat ulang halaman
39. Verifikasi checkbox `Initial Company` tidak tercentang
40. Verifikasi input Initial Company berstatus disabled
41. Verifikasi input Initial Company kosong dan nilai `ABC` tidak tersimpan
42. Verifikasi Live Preview menampilkan `JKT-LAP-T490-0000-0926-1` tanpa token Initial Company

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 42 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Initial Company pada form konfigurasi), satu kelas harness, dan berdiri sendiri karena baseline dipulihkan lewat seed antar blok (langkah 17, 25, 33, 34), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pola berulang blok Save sukses adalah langkah 10 sampai 16, 18 sampai 24, 26 sampai 32, dan 35 sampai 42.
- Urutan mengikuti S-10: validasi diblokir (TC-FA-CAID-57) lebih dulu, lalu Save sukses. Baris `sourceTc` TC-FA-CAID-57 ditempatkan pertama mengikuti urutan itu.
- Langkah penghubung (tanpa `Verifikasi`): langkah 17, 25, 33, dan 34 (pemulihan atau penyetelan baseline lewat sesi API aktor).
- Langkah 8 memuat ulang form yang masih dirty (checkbox tercentang tanpa disimpan); konfirmasi `beforeunload` ditangani harness sesuai Prerequisites. Absence pada langkah 5 dan 6 memakai error inline langkah 3 sebagai anchor positif pada surface yang sama.
- Temuan untuk QA:
  - TC-FA-CAID-60 menyebut baseline B2 "Initial Company tercentang bernilai `ABC`, Separator Dash, Division Code tercentang" tetapi Expected c memakai Live Preview dengan pemisah Dash dan Division `0000`; spec mengikuti TC apa adanya.
  - TC-FA-CAID-57 b menyebut "tidak ada alert di atas `[Save]`" tanpa menyebut elemen pembanding; anchor yang dipakai spec adalah error inline langkah 3.
