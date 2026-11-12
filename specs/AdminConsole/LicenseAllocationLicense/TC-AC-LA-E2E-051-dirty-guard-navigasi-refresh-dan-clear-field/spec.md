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
- Data Dinamis: tidak ada; tidak ada `[Submit]` yang berhasil pada spec ini (satu `[Submit]` kosong pada langkah 40 diblokir validasi).
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (mengamati kemunculan dan membatalkan muat ulang); menekan tombol Back browser.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-180: Navigasi sidebar dan tombol Back browser pada form dirty memunculkan D-02

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera`
3. Klik menu lain di sidebar
4. Verifikasi perubahan route dicegat
5. Verifikasi dialog D-02 `Unsaved Changes` tampil
6. Klik `[Cancel]` pada dialog
7. Verifikasi navigasi dibatalkan
8. Verifikasi tetap di form dengan Client `PT Sejahtera`
9. Klik tombol Back browser
10. Verifikasi perubahan route dicegat
11. Verifikasi dialog D-02 `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Verifikasi navigasi dilanjutkan
14. Verifikasi form ditutup tanpa menyimpan
15. Buka Allocation > License Allocation tab Current

### TC-AC-LA-181: Refresh F5 pada form dirty memunculkan konfirmasi bawaan browser

16. Klik `[+ Allocation]`
17. Pilih Client `PT Sejahtera`
18. Tekan `F5`
19. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
20. Batalkan muat ulang pada konfirmasi bawaan browser
21. Klik `[×]` pada header
22. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
23. Klik `[Leave]`
24. Klik `[+ Allocation]`
25. Tekan `F5` pada form pristine
26. Verifikasi halaman termuat ulang tanpa konfirmasi bawaan browser (tombol `[+ Allocation]` tampil)

### TC-AC-LA-183: Clear Field mengosongkan field data, mempertahankan checkbox Stay, dan tidak memunculkan dialog

27. Klik `[+ Allocation]`
28. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `7`, dan centang `Stay on this form after submitting`
29. Klik `[Clear Field]`
30. Verifikasi Client kosong kembali
31. Verifikasi Target kosong kembali
32. Verifikasi Type kosong kembali
33. Verifikasi Additional Quantity kosong kembali
34. Verifikasi Target Disabled
35. Verifikasi Type Disabled
36. Verifikasi checkbox Stay tetap tercentang
37. Verifikasi form tetap terbuka
38. Verifikasi kursor fokus ke field pertama
39. Verifikasi tidak ada dialog konfirmasi

### TC-AC-LA-184: Clear Field menghapus pesan error inline

40. Klik `[Submit]` pada form kosong
41. Verifikasi pesan `Client must not be empty` tampil
42. Verifikasi pesan `Target must not be empty` tampil
43. Verifikasi pesan `Type must not be empty` tampil
44. Klik `[Clear Field]`
45. Verifikasi seluruh pesan error inline hilang
46. Verifikasi border error dibersihkan
47. Verifikasi form tetap terbuka
48. Klik `[×]` pada header

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 4 kali, kejadian menutup 4 (langkah 12 sampai 14, 21 sampai 23, 25 yang memuat ulang halaman, dan 40).
- Spec 48 langkah, di atas smell 35 langkah, dengan empat blok satu topik (dirty-guard dan Clear Field pada form Allocate) yang berdiri sendiri: tiap blok memakai satu form dan tidak bergantung pada blok lain, sehingga tidak dipecah.
- Penyimpangan urutan (S-10): TC-AC-LA-184 melanjutkan form TC-AC-LA-183 (semua field sudah kosong setelah `[Clear Field]`), sehingga `[Submit]` kosong pada langkah 40 tidak membuka form baru. Checkbox Stay tetap tercentang pada TC-AC-LA-184 dan bukan field data, sehingga form tertutup tanpa dialog pada langkah 48.
- Langkah penghubung (S-03): langkah 15 (kembali ke List setelah navigasi), langkah 20 (membatalkan muat ulang), langkah 21 sampai 23 (menutup form dirty, S-08), dan langkah 48 (menutup form pristine). Langkah 41 sampai 43 (ketiga pesan error inline tampil) adalah anchor positif untuk asersi absence pesan pada langkah 45 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-180 Langkah 2 ("Klik menu lain di sidebar") tidak menyebut menu tujuan; spec tidak memilih menu tertentu dan memakai menu mana pun yang tersedia di sidebar.
  - TC-AC-LA-181 Expected b ("Form pristine atau setelah Submit sukses: tidak muncul") memuat dua kondisi, tetapi Langkah Uji hanya menguji form pristine; kondisi setelah Submit sukses tidak diasersi.
  - TC-AC-LA-181 tidak menyebut apa yang terjadi bila konfirmasi dilanjutkan; spec membatalkan muat ulang lalu menutup form lewat `[Leave]` (S-08).
  - TC-AC-LA-184 Data Uji menyebut pesan V-01, V-02, dan V-04 tampil, sedangkan TC-AC-LA-118 dan TC-AC-LA-109 hanya mengharapkan pesan Client pada Submit kosong; spec memakai tiga pesan sesuai TC-AC-LA-184 sebagai anchor.
