---
id: TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip
title: "Filter Panel Tab Total Control dan Tab Read Only: Screening Field, Opsi Dropdown, dan Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-142
  - TC-GS-ROLE-143
  - TC-GS-ROLE-148
  - TC-GS-ROLE-149
  - TC-GS-ROLE-150
coverage:
  web: automated
---

# Filter Panel Tab Total Control dan Tab Read Only: Screening Field, Opsi Dropdown, dan Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control (Search, Filter, dan kolom tabel dalam keadaan bawaan).
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup; hanya dibaca): Tab Total Control berisi Ahmad Fauzi (IT Manager, IT), Budi Santoso (Default User), Dewi Lestari (Staff, Finance, Inactive), dan Bayu Nugraha (baris 19). Tab Read Only berisi Siti Nurhaliza (Position `Finance Staff`, hanya dimiliki user Tab Read Only), Rina Putri (HR Manager, HR, Inactive), dan Intan Permata (baris 19). Kedua tab masing-masing berisi 3 user atau lebih dengan Position dan Division berbeda.
- Custom Field aktif `Region` (tipe Dropdown) tersedia dan diisi pada user Total Control (precondition TC-GS-ROLE-146); disediakan tim FE. Field filter-nya berlabel `Region` dengan placeholder `All regions`.
- Data Dinamis milik spec (hook `before`, lewat seeding API): user Total Control `Hesti Uji {runId}-051` (`hestiuji+{runId}-051@qwertysystem.net`, Position `HR Manager`, Division `HR`, Active), supaya Tab Total Control memiliki sedikitnya satu baris Position `HR Manager` untuk TC-GS-ROLE-148, 149, dan 150 (Position `HR Manager` di Tab Total Control tidak disebut di Pre-setup).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user `Hesti Uji {runId}-051`; filter dibersihkan lewat `[Clear Field]` dan `[Apply]` (langkah 55; hook `after` sebagai cadangan).
- Kemampuan teknis: membaca nilai distinct satu kolom dari seluruh halaman tabel (menelusuri semua halaman); membaca isi daftar opsi dropdown filter; mengetik di kotak search di dalam dropdown filter; klik `(X)` pada chip filter; seeding API disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD, tidak dikarang di spec).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-142: Screening Filter Panel Tab Total Control dan Tab Read Only

1. Untuk setiap baris tabel Tab uji TC-GS-ROLE-142 (Tab Total Control, Tab Read Only) (langkah 1 sampai 12): Klik Tab sesuai baris tabel
2. Klik Filter
3. Verifikasi field `Position` dengan placeholder `All positions` bertipe multi-select searchable
4. Verifikasi field `Division` dengan placeholder `All divisions` bertipe multi-select searchable
5. Verifikasi field `Status` dengan placeholder `All statuses` bertipe multi-select searchable
6. Verifikasi field `Activation Status` dengan placeholder `All statuses` bertipe multi-select searchable
7. Verifikasi field `Temporary User` dengan placeholder `All options` bertipe multi-select searchable
8. Verifikasi field `Temporary Until` dengan placeholder `Select date` bertipe date range picker
9. Verifikasi field Custom Field aktif `Region` dengan placeholder `All regions` sesuai tipe Dropdown
10. Verifikasi field `Modified By` dengan placeholder `All users` bertipe multi-select searchable
11. Verifikasi field `Last Updated` dengan placeholder `Select date` bertipe date range picker
12. Tutup Filter Panel

### TC-GS-ROLE-143: Opsi dropdown filter Tab Total Control diisi dari data tab itu

13. Klik Tab Total Control
14. Catat himpunan nilai distinct Position, Division, Status, dan Modified By dari seluruh baris Tab Total Control (semua halaman)
15. Klik Filter
16. Buka dropdown Position
17. Verifikasi opsi Position sama dengan himpunan Position pada baris Tab Total Control
18. Verifikasi opsi `Finance Staff` (Position user yang hanya ada di Tab Read Only) tidak muncul
19. Buka dropdown Division
20. Verifikasi opsi Division sama dengan himpunan Division pada baris Tab Total Control
21. Buka dropdown Status
22. Verifikasi opsi Status sama dengan himpunan Status pada baris Tab Total Control (`Active` dan `Inactive`)
23. Buka dropdown Modified By
24. Verifikasi opsi Modified By sama dengan himpunan nama Modified By pada baris Tab Total Control
25. Tutup Filter Panel

### TC-GS-ROLE-148: Search di dalam dropdown filter dan chip terpilih

26. Klik Filter
27. Buka dropdown Position, ketik `man` pada kotak search di dalam dropdown
28. Verifikasi daftar opsi memuat `IT Manager` dan `HR Manager`
29. Verifikasi setiap opsi yang tampil mengandung `man` (tanpa membedakan huruf besar kecil)
30. Centang opsi `IT Manager`
31. Centang opsi `HR Manager`
32. Verifikasi dua chip `IT Manager` dan `HR Manager` tampil di dalam field Position
33. Klik `[Clear Field]`

### TC-GS-ROLE-149: Hapus chip filter lewat (X) pada chip

34. Pilih Position `IT Manager` dan `HR Manager`
35. Klik `[Apply]`
36. Klik Filter
37. Klik (X) pada chip `HR Manager` tanpa membuka dropdown
38. Verifikasi chip `HR Manager` hilang
39. Verifikasi chip `IT Manager` tetap
40. Buka dropdown Position
41. Verifikasi checkbox `HR Manager` di dropdown ter-uncheck
42. Klik `[Apply]`
43. Verifikasi baris `Ahmad Fauzi` tampil
44. Verifikasi hanya baris ber-Position `IT Manager` yang tampil

### TC-GS-ROLE-150: Hapus pilihan filter lewat uncheck di dropdown

45. Klik Filter, lalu klik `[Clear Field]`
46. Pilih Position `IT Manager` dan `HR Manager`
47. Klik `[Apply]`
48. Klik Filter
49. Buka dropdown Position, lalu uncheck opsi `IT Manager`
50. Verifikasi chip `IT Manager` hilang
51. Verifikasi chip `HR Manager` tetap
52. Klik `[Apply]`
53. Verifikasi baris `Hesti Uji {runId}-051` tampil
54. Verifikasi hanya baris ber-Position `HR Manager` yang tampil
55. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per baris tabel parameter: TC-GS-ROLE-142 langkah 1 sampai 12 (2 iterasi: Tab Total Control dan Tab Read Only).
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup Filter Panel (langkah 12 dan 25), mencatat himpunan nilai (langkah 14), `[Clear Field]` dan membuka ulang Filter Panel sesudah `[Apply]` (langkah 33, 36, 45), serta pembersihan filter di akhir spec (langkah 55). TC-GS-ROLE-148 dan 150 memakai Tab Total Control; TC sumber tidak menyebut tab untuk TC-GS-ROLE-148, 149, 150.
- Spec melewati sekitar 35 langkah (55 langkah nominal, sekitar 67 dengan ekspansi perulangan) karena lima TC menguji Filter Panel yang sama dan tiap field, tiap tab, dan tiap klausa Expected menjadi langkah sendiri (S-01). Seluruh blok satu kelas harness (fungsional), satu aktor, satu dataset; tiap blok membersihkan filter yang dibuatnya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Anchor absence (bagian 8b butir 2): opsi Position milik Tab Total Control tampil (anchor) sebelum asersi ketiadaan `Finance Staff`; baris `Ahmad Fauzi` dan `Hesti Uji {runId}-051` tampil sebelum asersi "hanya baris ber-Position ...".
- Temuan untuk QA:
  - TC-GS-ROLE-142 menyebut "[Custom Field aktif Dropdown/Date]" tanpa precondition dan tanpa data uji; spec mengasersi hanya Custom Field `Region` (Dropdown, dari TC-GS-ROLE-146). Custom Field bertipe Date tidak diasersi karena tidak ada data di sumber.
  - TC-GS-ROLE-142 menulis tipe Custom Field "sesuai tipe" tanpa menyebut apakah Dropdown berupa multi-select searchable; spec mengasersi label dan placeholder `All regions` dan tipe Dropdown.
  - TC-GS-ROLE-148, 149, 150 menyebut Position `HR Manager` dan `IT Manager` tanpa menyebut tab dan tanpa menyebut user Tab Total Control ber-Position `HR Manager` (Pre-setup hanya menyebut Rina Putri HR Manager di Tab Read Only); spec memakai Tab Total Control dan men-seed user `Hesti Uji {runId}-051`.
  - TC-GS-ROLE-143 Expected e ("Position user yang hanya ada di Tab Read Only tidak muncul") tidak menyebut nilainya; spec memakai `Finance Staff` (Siti Nurhaliza).
