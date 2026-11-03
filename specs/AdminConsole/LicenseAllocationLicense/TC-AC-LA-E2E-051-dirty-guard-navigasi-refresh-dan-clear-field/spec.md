---
id: TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field
title: "Dirty-Guard Navigasi, Refresh F5, dan Clear Field Form Allocate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-180
  - TC-AC-LA-181
  - TC-AC-LA-183
  - TC-AC-LA-184
coverage:
  web: automated
---

# Dirty-Guard Navigasi, Refresh F5, dan Clear Field Form Allocate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 (konfirmasi `beforeunload` dan penutupan dialog `Unsaved Changes`) dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`).
- Data Dinamis: tidak ada; tidak ada `[Submit]` yang berhasil pada spec ini (satu `[Submit]` kosong pada langkah 32 diblokir validasi).
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (mengamati kemunculan dan membatalkan muat ulang); menekan tombol Back browser.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-180: Navigasi sidebar dan tombol Back browser pada form dirty memunculkan D-02

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera`
3. Klik menu lain di sidebar
4. Verifikasi perubahan route dicegat dan dialog D-02 `Unsaved Changes` tampil
5. Klik `[Cancel]` pada dialog
6. Verifikasi navigasi dibatalkan dan tetap di form dengan Client `PT Sejahtera`
7. Klik tombol Back browser
8. Verifikasi perubahan route dicegat dan dialog D-02 `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Verifikasi navigasi dilanjutkan dan form ditutup tanpa menyimpan
11. Buka Allocation > License Allocation tab Current

### TC-AC-LA-181: Refresh F5 pada form dirty memunculkan konfirmasi bawaan browser

12. Klik `[+ Allocation]`
13. Pilih Client `PT Sejahtera`
14. Tekan `F5`
15. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
16. Batalkan muat ulang pada konfirmasi bawaan browser
17. Klik `[✕]` pada header
18. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
19. Klik `[Leave]`
20. Klik `[+ Allocation]`
21. Tekan `F5` pada form pristine
22. Verifikasi halaman termuat ulang tanpa konfirmasi bawaan browser (tombol `[+ Allocation]` tampil)

### TC-AC-LA-183: Clear Field mengosongkan field data, mempertahankan checkbox Stay, dan tidak memunculkan dialog

23. Klik `[+ Allocation]`
24. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `7`, dan centang `Stay on this form after submitting`
25. Klik `[Clear Field]`
26. Verifikasi Client, Target, Type, dan Additional Quantity kosong kembali
27. Verifikasi Target dan Type Disabled
28. Verifikasi checkbox Stay tetap tercentang
29. Verifikasi form tetap terbuka
30. Verifikasi kursor fokus ke field pertama
31. Verifikasi tidak ada dialog konfirmasi

### TC-AC-LA-184: Clear Field menghapus pesan error inline

32. Klik `[Submit]` pada form kosong
33. Verifikasi pesan `Client must not be empty`, `Target must not be empty`, dan `Type must not be empty` tampil
34. Klik `[Clear Field]`
35. Verifikasi seluruh pesan error inline hilang dan border error dibersihkan
36. Verifikasi form tetap terbuka
37. Klik `[✕]` pada header

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 4 kali, kejadian menutup 4 (langkah 9 sampai 10, 17 sampai 19, 21 yang memuat ulang halaman, dan 37).
- Spec 37 langkah, di atas smell 35 langkah, dengan empat blok satu topik (dirty-guard dan Clear Field pada form Allocate) yang berdiri sendiri: tiap blok memakai satu form dan tidak bergantung pada blok lain, sehingga tidak dipecah.
- Penyimpangan urutan (S-10): TC-AC-LA-184 melanjutkan form TC-AC-LA-183 (semua field sudah kosong setelah `[Clear Field]`), sehingga `[Submit]` kosong pada langkah 32 tidak membuka form baru. Checkbox Stay tetap tercentang pada TC-AC-LA-184 dan bukan field data, sehingga form tertutup tanpa dialog pada langkah 37.
- Langkah penghubung (S-03): langkah 11 (kembali ke List setelah navigasi), langkah 16 (membatalkan muat ulang), langkah 17 sampai 19 (menutup form dirty, S-08), dan langkah 37 (menutup form pristine). Langkah 33 adalah anchor positif untuk asersi absence pesan pada langkah 35 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-180 Langkah 2 ("Klik menu lain di sidebar") tidak menyebut menu tujuan; spec tidak memilih menu tertentu dan memakai menu mana pun yang tersedia di sidebar.
  - TC-AC-LA-181 Expected b ("Form pristine atau setelah Submit sukses: tidak muncul") memuat dua kondisi, tetapi Langkah Uji hanya menguji form pristine; kondisi setelah Submit sukses tidak diasersi.
  - TC-AC-LA-181 tidak menyebut apa yang terjadi bila konfirmasi dilanjutkan; spec membatalkan muat ulang lalu menutup form lewat `[Leave]` (S-08).
  - TC-AC-LA-184 Data Uji menyebut pesan V-01, V-02, dan V-04 tampil, sedangkan TC-AC-LA-118 dan TC-AC-LA-109 hanya mengharapkan pesan Client pada Submit kosong; spec memakai tiga pesan sesuai TC-AC-LA-184 sebagai anchor.
