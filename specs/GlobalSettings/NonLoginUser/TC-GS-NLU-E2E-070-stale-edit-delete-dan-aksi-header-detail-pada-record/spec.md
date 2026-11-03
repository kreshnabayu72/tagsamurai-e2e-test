---
id: TC-GS-NLU-E2E-070-stale-edit-delete-dan-aksi-header-detail-pada-record
title: "Stale: Edit, Delete, dan Aksi Header Detail pada Record Dihapus atau di-Convert Admin Lain"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-185
  - TC-GS-NLU-186
  - TC-GS-NLU-194
  - TC-GS-NLU-255
  - TC-GS-NLU-256
coverage:
  web: automated
---

# Stale: Edit, Delete, dan Aksi Header Detail pada Record Dihapus atau di-Convert Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata). Admin lain dijalankan lewat sesi API aktor.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi, Email bersuffix `{runId}-070`): `Edit Target 49 {runId}-070`, `Edit Target 50 {runId}-070`, `Rani Lestari {runId}-070`, `Hendra Enam {runId}-070`, `Konversi Lima {runId}-070`. Search `{runId}-070` menyaring lima baris.
- Hook `after` menghapus lima record dan Login User hasil Convert lewat API.
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-185: Edit pada record yang sudah dihapus admin lain

1. Ketik Search `{runId}-070`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 49 {runId}-070` > `Edit`
3. Tunggu Popup Edit Non-Login User terbuka dengan seluruh field terisi
4. Di sesi API aktor, hapus `Edit Target 49 {runId}-070` hingga penghapusan tersimpan
5. Ubah First Name
6. Klik `[Save]`
7. Verifikasi toast netral (Info, tanpa prefix): `This non-login user is no longer available.`
8. Verifikasi list di-refresh dan baris `Edit Target 49 {runId}-070` tidak ada

### TC-GS-NLU-186: Edit pada record yang sudah di-Convert admin lain

9. Klik `⋯` pada baris `Edit Target 50 {runId}-070` > `Edit`
10. Tunggu Popup Edit Non-Login User terbuka dengan seluruh field terisi
11. Di sesi API aktor, Convert `Edit Target 50 {runId}-070` ke Login User hingga konversi tersimpan
12. Ubah First Name
13. Klik `[Save]`
14. Verifikasi toast netral: `This non-login user is no longer available.`
15. Verifikasi list di-refresh dan baris `Edit Target 50 {runId}-070` tidak ada di sub-tab Non-Login User

### TC-GS-NLU-194: Delete pada record yang sudah dihapus admin lain

16. Klik `⋯` pada baris `Rani Lestari {runId}-070` > `Delete`
17. Di sesi API aktor (dialog sudah terbuka), hapus `Rani Lestari {runId}-070` hingga penghapusan tersimpan
18. Klik `[Delete]`
19. Verifikasi toast netral: `This non-login user is no longer available.`
20. Verifikasi list di-refresh dan baris `Rani Lestari {runId}-070` tidak ada

### TC-GS-NLU-255: Aksi header Detail pada record yang sudah dihapus admin lain

21. Klik teks Name `Hendra Enam {runId}-070` untuk membuka Detail
22. Di sesi API aktor, hapus `Hendra Enam {runId}-070` hingga penghapusan tersimpan
23. Klik switch Active di header
24. Klik `[Deactivate]`
25. Verifikasi toast netral: `This non-login user is no longer available.`
26. Verifikasi halaman kembali ke List
27. Verifikasi list di-refresh

### TC-GS-NLU-256: Aksi header Detail pada record yang sudah di-Convert admin lain

28. Klik teks Name `Konversi Lima {runId}-070` untuk membuka Detail
29. Di sesi API aktor, Convert `Konversi Lima {runId}-070` ke Login User hingga konversi tersimpan
30. Klik switch Active di header
31. Klik `[Deactivate]`
32. Verifikasi toast netral: `This non-login user is no longer available.`
33. Verifikasi Detail dimuat ulang dan dirender sebagai Detail Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 3, 10.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Dialog Delete pada TC-194 dibuka lebih dulu lalu record dihapus di sesi API (urutan Langkah Uji TC: dialog dibuka dulu, baru pihak lain menghapus, baru konfirmasi; S-04).
- Temuan untuk QA:
  - TC-185 dan TC-186 tidak menyebut apakah Popup Edit tertutup sesudah toast netral; spec tidak menambah langkah penutupan dan langkah berikutnya mengandalkan `⋯` pada baris berikut.
  - TC-185 dan TC-186 "Ubah First Name" tidak menyebut nilai baru; spec mengetik teks bebas.
  - TC-255 dan TC-256 Langkah Uji tidak menyebut tindakan sebelum sesi lain; spec membuka Detail lewat klik Name dari list yang sedang tersaring.
  - TC-256 Expected b ("dirender sebagai Detail Login User") tidak menyebut penanda; spec memverifikasi badge `Non Login` hilang dari Detail.
