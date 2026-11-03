---
id: TC-AC-DS-E2E-005-isi-kolom-foto-stok-dan-kolom-curated
title: "Isi Kolom Photo, Current Stock, serta Kolom Curated Hardware Type, Range Type, dan TAG Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-13
  - TC-AC-DS-14
  - TC-AC-DS-15
  - TC-AC-DS-16
  - TC-AC-DS-17
coverage:
  web: automated
---

# Isi Kolom Photo, Current Stock, serta Kolom Curated Hardware Type, Range Type, dan TAG Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100` dengan 2 foto dan foto kedua sebagai default, `HHR-ARC-200`, `HHR-BIG-01` stok 12500, `SFR-VEL-4P`, `BLE-KIN-GW1`, `TAG-ARC-USR`, `TAG-ARC-OBJ`) dan seed #30 (129 SKU Principal). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Spec ini mengubah visibilitas kolom List (Hardware Type, Range Type, dan TAG Type dari Hidden menjadi tampil) lewat overlay Column Visibility; pemulihan ke default Hidden ditulis sebagai langkah di akhir spec dan oleh hook `after` suite bila spec gagal di tengah.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding.

## Test Steps

### TC-AC-DS-13: Foto default pada kolom Photo dan kolom Photo tidak dapat diurutkan

1. Ketik Search `HHR-ARC-100`, tekan Enter
2. Verifikasi thumbnail baris `HHR-ARC-100` adalah foto yang ditandai default (foto kedua), bukan foto pertama
3. Klik `(←)` pada kotak Search
4. Verifikasi baris dengan satu foto menampilkan foto itu sebagai thumbnail
5. Verifikasi tidak ada sel Photo yang kosong
6. Verifikasi header kolom Photo tidak memiliki ikon sort

### TC-AC-DS-14: Current Stock sebagai angka bulat

7. Ketik Search `HHR-BIG-01`, tekan Enter
8. Verifikasi sel Current Stock baris `HHR-BIG-01` menampilkan `12500` tanpa pemisah ribuan dan tanpa desimal

### TC-AC-DS-15: Kolom Hardware Type

9. Klik header kolom Actions (⋯)
10. Centang kolom `Hardware Type` pada overlay Column Visibility
11. Tutup overlay Column Visibility
12. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
13. Verifikasi kolom Hardware Type baris `HHR-ARC-100` menampilkan badge `Handheld Reader`
14. Ganti isi kotak search dengan `SFR-VEL-4P`, tekan Enter
15. Verifikasi kolom Hardware Type baris `SFR-VEL-4P` menampilkan badge `Smart Fixed Reader`
16. Ganti isi kotak search dengan `BLE-KIN-GW1`, tekan Enter
17. Verifikasi kolom Hardware Type baris `BLE-KIN-GW1` menampilkan badge `BLE Gateway`
18. Ganti isi kotak search dengan `TAG-ARC-USR`, tekan Enter
19. Verifikasi kolom Hardware Type baris `TAG-ARC-USR` menampilkan `—` karena ancestry bukan hardware

### TC-AC-DS-16: Kolom Range Type

20. Klik header kolom Actions (⋯)
21. Centang kolom `Range Type` pada overlay Column Visibility
22. Tutup overlay Column Visibility
23. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
24. Verifikasi kolom Range Type baris `HHR-ARC-100` menampilkan badge `Long Range`
25. Ganti isi kotak search dengan `HHR-ARC-200`, tekan Enter
26. Verifikasi kolom Range Type baris `HHR-ARC-200` menampilkan badge `Short Range`
27. Ganti isi kotak search dengan `SFR-VEL-4P`, tekan Enter
28. Verifikasi kolom Range Type baris `SFR-VEL-4P` menampilkan `—` karena bukan Handheld Reader

### TC-AC-DS-17: Kolom TAG Type

29. Klik header kolom Actions (⋯)
30. Centang kolom `TAG Type` pada overlay Column Visibility
31. Tutup overlay Column Visibility
32. Ganti isi kotak search dengan `TAG-ARC-USR`, tekan Enter
33. Verifikasi kolom TAG Type baris `TAG-ARC-USR` menampilkan badge `User`
34. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
35. Verifikasi kolom TAG Type baris `TAG-ARC-OBJ` menampilkan badge `Object`
36. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
37. Verifikasi kolom TAG Type baris `HHR-ARC-100` menampilkan `—` karena bukan TAG

### Pemulihan kolom

38. Klik header kolom Actions (⋯)
39. Hilangkan centang kolom `Hardware Type`, `Range Type`, dan `TAG Type` pada overlay Column Visibility
40. Tutup overlay Column Visibility
41. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-13, TC-14, TC-15, TC-16, TC-17, lalu blok pemulihan kolom.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3, 7, 12, 14, 16, 18, 23, 25, 27, 32, 34, 36 (Search untuk menemukan baris target, R-16); langkah 9 sampai 11, 20 sampai 22, 29 sampai 31 (membuka overlay, memilih kolom, menutup overlay; TC menulis satu langkah "Centang kolom"); blok pemulihan langkah 38 sampai 41 (mengembalikan kolom ke default Hidden dan mengosongkan Search, S-09).
- Spec berisi 41 langkah dan melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok memeriksa isi kolom baris List yang sama pada satu halaman dalam satu kelas (screening isi kolom, tanpa seeding dan tanpa mengubah data); langkah berulang per baris SKU pada TC-15, TC-16, dan TC-17 diperlukan karena nilai kolom curated diasersi pada baris berbeda yang tidak muncul bersamaan dalam satu hasil Search; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 4 dan 5 memeriksa baris-baris List yang ada di halaman 1 setelah Search dikosongkan; TC tidak menyebut baris tertentu untuk "baris dengan satu foto" (semua SKU Pre-setup #29 memiliki 1 foto kecuali `HHR-ARC-100` dan `SFR-VEL-4P`).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal dan nilai Pre-setup #29/#30 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 di environment belum diverifikasi.
  - TC-13 (Photo): cara membedakan foto pertama dari foto kedua pada thumbnail tidak dirinci TC; cara pembeda disediakan tim FE.
  - TC-15, TC-16, TC-17 tidak menyebut apakah pilihan Column Visibility tersimpan antar sesi; spec memulihkannya secara eksplisit.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
