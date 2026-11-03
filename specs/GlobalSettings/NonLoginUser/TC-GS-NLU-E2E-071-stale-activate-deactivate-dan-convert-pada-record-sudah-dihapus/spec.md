---
id: TC-GS-NLU-E2E-071-stale-activate-deactivate-dan-convert-pada-record-sudah-dihapus
title: "Stale: Activate, Deactivate, dan Convert pada Record Sudah Dihapus atau di-Convert Admin Lain"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-212
  - TC-GS-NLU-238
  - TC-GS-NLU-239
coverage:
  web: automated
---

# Stale: Activate, Deactivate, dan Convert pada Record Sudah Dihapus atau di-Convert Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata). Admin lain dijalankan lewat sesi API aktor.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): `Hendra Dua {runId}-071`, `Konversi Dua {runId}-071` (Email `konversidua+{runId}-071@qwertysystem.net`), `Konversi Tiga {runId}-071`. Search `{runId}-071` menyaring tiga baris.
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint). Login User hasil Convert dihapus hook `after` lewat API.
- Mail-catcher: inbox per alamat email dapat dibaca dan jumlah email per alamat dapat dicatat sebelum aksi (baseline; kemampuan disediakan tim FE/BE).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix unik (baseline nol).

## Test Steps


### TC-GS-NLU-212: Deactivate pada record yang sudah dihapus admin lain

1. Ketik Search `{runId}-071`, tekan Enter
2. Klik switch Active pada baris `Hendra Dua {runId}-071` (ON)
3. Di sesi API aktor (dialog sudah terbuka), hapus `Hendra Dua {runId}-071` hingga penghapusan tersimpan
4. Klik `[Deactivate]`
5. Verifikasi toast netral: `This non-login user is no longer available.`
6. Verifikasi list di-refresh dan baris `Hendra Dua {runId}-071` tidak ada

### TC-GS-NLU-238: Convert pada user yang sudah menjadi Login User oleh admin lain (idempotent)

7. Klik `⋯` pada baris `Konversi Dua {runId}-071` > `Convert to Login User`
8. Di sesi API aktor (dialog sudah terbuka), Convert `Konversi Dua {runId}-071` ke Login User hingga konversi tersimpan
9. Catat baseline jumlah email di mail-catcher untuk `konversidua+{runId}-071@qwertysystem.net` setelah konversi sesi API
10. Klik `[Convert]`
11. Verifikasi toast sukses T-09: `Success, Konversi Dua {runId}-071 has been converted to a login user.`
12. Verifikasi tidak ada toast error dan tidak ada dialog blok
13. Klik sub-tab `Login User`
14. Ketik Search `Konversi Dua {runId}-071`, tekan Enter
15. Verifikasi tepat satu baris `Konversi Dua {runId}-071` di sub-tab Login User (tidak ada duplikat)
16. Verifikasi jumlah email di mail-catcher untuk `konversidua+{runId}-071@qwertysystem.net` sama dengan baseline (tidak ada email aktivasi baru)
17. Klik icon `Changelog` pada Table Tools untuk membuka Modal Changelog agregat
18. Verifikasi tepat satu entri dengan Action `Convert to Login User` dan nama `Konversi Dua {runId}-071` (entri dari sesi API, tidak bertambah oleh Convert kedua)
19. Tutup Modal Changelog dengan `✕`

### TC-GS-NLU-239: Convert pada record yang sudah dihapus admin lain

20. Klik sub-tab `Non-Login User`
21. Ketik Search `Konversi Tiga {runId}-071`, tekan Enter
22. Klik `⋯` pada baris `Konversi Tiga {runId}-071` > `Convert to Login User`
23. Di sesi API aktor (dialog sudah terbuka), hapus `Konversi Tiga {runId}-071` hingga penghapusan tersimpan
24. Klik `[Convert]`
25. Verifikasi toast netral: `This non-login user is no longer available.`
26. Verifikasi list di-refresh dan baris `Konversi Tiga {runId}-071` tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 9, 17, 19, 20.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 14, 21.
- Klausa "tidak ada email aktivasi baru dan tidak ada entri log baru" (TC-238 Expected c) diasersi sebagai jumlah terhadap baseline (S-12), bukan sebagai spec absence: baseline email dicatat sesudah sesi API selesai dan sebelum `[Convert]`; entri log dihitung lewat nama bersuffix unik (tepat satu).
- Temuan untuk QA:
  - TC-212 judul menyebut Activate dan Deactivate, tetapi Langkah Uji hanya menonaktifkan; spec hanya menulis Deactivate.
  - TC-238 Expected a menyebut "toast sukses `T-09`" tanpa teks; spec memakai teks toast Convert yang sama dengan TC-234 (`Success, [Full Name] has been converted to a login user.`).
  - TC-238 Expected c tidak menyebut surface log; spec memakai Modal Changelog agregat.
