---
id: TC-GS-NLU-E2E-064-bulk-deactivate-kelompok-di-skip-sebagian-gagal-seluruh-gagal
title: "Bulk Deactivate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-227
  - TC-GS-NLU-228
  - TC-GS-NLU-470
  - TC-GS-NLU-474
  - TC-GS-NLU-475
coverage:
  web: automated
---

# Bulk Deactivate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Rina Marlina {runId}-064` (Active, Position Driver), `Joko Susilo {runId}-064` (Inactive manual), `Rina Marlina Dua {runId}-064` (Active), `Hendra Tiga {runId}-064` (Active), `Skip Penuh Satu {runId}-064` dan `Skip Penuh Dua {runId}-064` (Active), `Gagal Satu {runId}-064` dan `Gagal Dua {runId}-064` (Active), `Campur Aktif {runId}-064` (Active), `Campur Mati {runId}-064` (Inactive). Search `{runId}-064` menyaring sepuluh baris pada satu halaman. Rina Marlina Dua dipakai TC-228 karena `Rina Marlina {runId}-064` sudah Inactive sesudah TC-227.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-227: Bulk Deactivate memuat baris Inactive

1. Ketik Search `{runId}-064`, tekan Enter
2. Centang baris `Rina Marlina {runId}-064` (Active) dan `Joko Susilo {runId}-064` (Inactive)
3. Pilih `Bulk Action` > `Deactivate`
4. Verifikasi dialog dengan dua kelompok bullet: `The following will be deactivated:` (`Rina Marlina {runId}-064`) dan `The following will be skipped (already inactive):` (`Joko Susilo {runId}-064`), `Are you sure you want to continue?` dengan tombol `[Cancel]` dan `[Continue]`
5. Klik `[Continue]`
6. Verifikasi toast sukses varian skip: `Success, non-login user has been deactivated. Some users were skipped.`
7. Verifikasi `Rina Marlina {runId}-064` OFF
8. Verifikasi `Joko Susilo {runId}-064` tetap OFF

### TC-GS-NLU-470: Bulk Deactivate seluruh baris sudah Inactive di sesi lain

9. Centang baris `Skip Penuh Satu {runId}-064` dan `Skip Penuh Dua {runId}-064`
10. Pilih `Bulk Action` > `Deactivate`
11. Di sesi API aktor (dialog sudah terbuka), nonaktifkan `Skip Penuh Satu {runId}-064` dan `Skip Penuh Dua {runId}-064` hingga status Inactive tersimpan
12. Klik `[Deactivate]`
13. Verifikasi toast varian skip: `Success, non-login user has been deactivated. Some users were skipped.`
14. Verifikasi kedua baris tetap OFF

### TC-GS-NLU-228: Bulk Deactivate sebagian baris gagal

15. Centang baris `Rina Marlina Dua {runId}-064` dan `Hendra Tiga {runId}-064`
16. Pilih `Bulk Action` > `Deactivate`
17. Di sesi API aktor (dialog sudah terbuka), hapus `Hendra Tiga {runId}-064` hingga penghapusan tersimpan
18. Klik `[Deactivate]`
19. Verifikasi `Rina Marlina Dua {runId}-064` dinonaktifkan (switch OFF)
20. Verifikasi toast sukses partial: `Success, non-login user has been deactivated. Some users failed.`

### TC-GS-NLU-474: Bulk Deactivate seluruh baris gagal

21. Centang baris `Gagal Satu {runId}-064` dan `Gagal Dua {runId}-064`
22. Pilih `Bulk Action` > `Deactivate`
23. Di sesi API aktor (dialog sudah terbuka), hapus `Gagal Satu {runId}-064` dan `Gagal Dua {runId}-064` hingga penghapusan tersimpan
24. Klik `[Deactivate]`
25. Verifikasi toast error: `Error, failed to deactivate non-login user.` (bukan toast sukses)

### TC-GS-NLU-475: Bulk Deactivate campuran di-skip dan gagal tanpa baris berhasil

26. Centang baris `Campur Aktif {runId}-064` (Active) dan `Campur Mati {runId}-064` (Inactive)
27. Pilih `Bulk Action` > `Deactivate`
28. Di sesi API aktor (dialog dua kelompok sudah terbuka), hapus `Campur Aktif {runId}-064` hingga penghapusan tersimpan
29. Klik `[Continue]` pada dialog dua kelompok bullet
30. Verifikasi toast error: `Error, failed to deactivate non-login user.` (bukan toast sukses varian skip)
31. Verifikasi `Campur Mati {runId}-064` tetap Inactive

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Urutan: aksi skip (TC-227, TC-470) lebih dulu, lalu kegagalan berbasis hapus di sesi API (TC-228, TC-474, TC-475) di akhir (S-10).
- Pembagian TC lintas spec: Bulk Activate (TC-225, TC-226, TC-229, TC-230, TC-476) ada di spec 063; Log Bulk Deactivate (TC-506) bukan bagian spec ini.
- Temuan untuk QA:
  - TC-475 Langkah 4 menyebut dialog dua kelompok sebagai langkah (bukan Expected); spec tidak menambah asersi dialog dan hanya mengklik `[Continue]`.
  - TC-470 Expected a ("tanpa baris berhasil dan tanpa baris gagal") tidak teramati terpisah di UI; diamati lewat toast varian skip dan status OFF.
  - Seleksi sesudah aksi bulk tidak dibersihkan secara eksplisit karena TC tidak menyebut apakah seleksi dipertahankan sesudah aksi sukses.
