---
id: TC-GS-NLU-E2E-068-bulk-convert-sebagian-gagal-seluruh-gagal-dan-baris-dihapus
title: "Bulk Convert: Sebagian Gagal, Seluruh Gagal, dan Baris Dihapus Admin Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-244
  - TC-GS-NLU-245
  - TC-GS-NLU-442
coverage:
  web: automated
---

# Bulk Convert: Sebagian Gagal, Seluruh Gagal, dan Baris Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata). Admin lain dijalankan lewat sesi API aktor.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi, Email bersuffix `{runId}-068` per record): `Konversi Empat {runId}-068`, `Konflik Dua {runId}-068`, `Konflik Tiga {runId}-068`, `Konflik Empat {runId}-068`, `Race Satu {runId}-068`, `Race Dua {runId}-068`. Search `{runId}-068` menyaring enam baris.
- Data pemicu (dibuat lewat sesi API aktor sesudah dialog Convert terbuka, melewati cek `V-09`): Login User dengan Email `konflik2+{runId}-068@qwertysystem.net` (TC-244), Login User dengan Email `konflik3+{runId}-068@qwertysystem.net` dan `konflik4+{runId}-068@qwertysystem.net` (TC-245). Email `konflik2` sampai `konflik4` adalah Email masing-masing record Konflik. Hook `after` menghapus Login User pemicu dan Login User hasil Convert lewat API.
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint). Cara menyisipkan Login User melewati cek `V-09` disediakan tim FE/BE.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-244: Bulk Convert sebagian baris gagal

1. Ketik Search `{runId}-068`, tekan Enter
2. Centang baris `Konversi Empat {runId}-068` dan `Konflik Dua {runId}-068`
3. Pilih `Bulk Action` > `Convert to Login User`
4. Di sesi API aktor (dialog sudah terbuka), buat Login User dengan Email `konflik2+{runId}-068@qwertysystem.net` hingga Login User tersimpan
5. Klik `[Convert]`
6. Verifikasi `Konversi Empat {runId}-068` hilang dari sub-tab Non-Login User (menjadi Login User)
7. Verifikasi `Konflik Dua {runId}-068` tetap Non-Login User
8. Verifikasi toast: `Success, non-login user has been converted. Some users failed.`

### TC-GS-NLU-245: Bulk Convert seluruh baris gagal

9. Centang baris `Konflik Tiga {runId}-068` dan `Konflik Empat {runId}-068`
10. Pilih `Bulk Action` > `Convert to Login User`
11. Di sesi API aktor (dialog sudah terbuka), buat Login User dengan Email `konflik3+{runId}-068@qwertysystem.net` dan Login User dengan Email `konflik4+{runId}-068@qwertysystem.net` hingga keduanya tersimpan
12. Klik `[Convert]`
13. Verifikasi toast error: `Error, failed to convert non-login user.`
14. Verifikasi kedua baris tetap Non-Login User

### TC-GS-NLU-442: Convert berlomba dengan Delete admin lain

15. Centang baris `Race Satu {runId}-068` dan `Race Dua {runId}-068`
16. Pilih `Bulk Action` > `Convert to Login User`
17. Di sesi API aktor (dialog sudah terbuka), hapus `Race Dua {runId}-068` hingga penghapusan tersimpan
18. Klik `[Convert]`
19. Verifikasi `Race Satu {runId}-068` hilang dari sub-tab Non-Login User (menjadi Login User)
20. Verifikasi toast partial: `Success, non-login user has been converted. Some users failed.`
21. Klik sub-tab `Login User`
22. Ketik Search `{runId}-068`, tekan Enter
23. Verifikasi `Konversi Empat {runId}-068` dan `Race Satu {runId}-068` tampil di sub-tab Login User sebagai hasil Convert

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 21.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 22.
- Email `konflik2`, `konflik3`, dan `konflik4` adalah Email record `Konflik Dua {runId}-068`, `Konflik Tiga {runId}-068`, dan `Konflik Empat {runId}-068` (bersuffix `{runId}-068`); Login User pemicu memakai email yang sama sehingga Convert bentrok.
- Temuan untuk QA:
  - TC-244, TC-245, dan TC-442 tidak menyebut kapan Login User pemicu dibuat selain "di sesi lain"; spec membuatnya setelah dialog Convert terbuka (urutan Langkah Uji TC).
  - TC-244 Expected a dan TC-442 Expected a ("menjadi Login User") diamati lewat hilangnya baris dari sub-tab Non-Login User, lalu satu `Verifikasi` akhir di sub-tab Login User untuk dua record berhasil.
  - TC-442 Expected b ("Race Dua gagal") diamati lewat toast partial; baris Race Dua sudah dihapus admin lain.
