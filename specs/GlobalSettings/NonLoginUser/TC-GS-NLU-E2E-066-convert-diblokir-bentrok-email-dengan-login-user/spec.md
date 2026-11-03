---
id: TC-GS-NLU-E2E-066-convert-diblokir-bentrok-email-dengan-login-user
title: "Convert Diblokir: Bentrok Email dengan Login User"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-240
  - TC-GS-NLU-444
  - TC-GS-NLU-473
coverage:
  web: automated
---

# Convert Diblokir: Bentrok Email dengan Login User

## Prerequisites

- Mode: FE+BE (backend nyata). Login User pemicu dibuat lewat sesi API aktor setelah list dimuat.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): `Konflik Satu {runId}-066` (Email `konflik1+{runId}-066@qwertysystem.net`), `Konflik Lima {runId}-066` (Email `konflik5+{runId}-066@qwertysystem.net`), `Konflik Enam {runId}-066` (Email `konflik6+{runId}-066@qwertysystem.net`). Search `{runId}-066` menyaring tepat tiga baris.
- Data pemicu (dibuat lewat sesi API aktor sesudah list dimuat, melewati cek `V-09` untuk mensimulasikan dua permintaan bersamaan): Login User dengan Email `konflik1+{runId}-066@qwertysystem.net` (TC-240); Login User dengan Email `konflik5+{runId}-066@qwertysystem.net` (TC-444); Login User `Konflik Pending {runId}-066` berstatus Activated dengan email pending `konflik6+{runId}-066@qwertysystem.net` (TC-473, precondition TC). Hook `after` menghapus ketiga Login User lewat API.
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint). State BE per user yang di-seed (email pending Login User) dan cara menyisipkan Login User melewati cek `V-09` disediakan tim FE/BE; TC tidak menyebut endpoint.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-240: Convert row bentrok email dengan Login User lain

1. Ketik Search `{runId}-066`, tekan Enter
2. Di sesi API aktor, buat Login User dengan Email `konflik1+{runId}-066@qwertysystem.net` hingga Login User tersimpan
3. Klik `⋯` pada baris `Konflik Satu {runId}-066` > `Convert to Login User`
4. Klik `[Convert]`
5. Verifikasi dialog blok dengan Title `Cannot Convert`, body `This email is already used by another login user. Update the email first.`, dan tombol `[OK]`
6. Klik `[OK]`
7. Verifikasi `Konflik Satu {runId}-066` tetap Non-Login User (list di-refresh)

### TC-GS-NLU-473: Convert row bentrok dengan email pending Login User lain

8. Di sesi API aktor, buat Login User `Konflik Pending {runId}-066` berstatus Activated dengan email pending `konflik6+{runId}-066@qwertysystem.net` hingga Login User tersimpan
9. Klik `⋯` pada baris `Konflik Enam {runId}-066` > `Convert to Login User`
10. Klik `[Convert]`
11. Verifikasi dialog blok dengan Title `Cannot Convert`, body `This email is already used by another login user. Update the email first.`, dan tombol `[OK]`
12. Klik `[OK]`
13. Verifikasi `Konflik Enam {runId}-066` tetap Non-Login User (list di-refresh)

### TC-GS-NLU-444: Login User dengan email sama dibuat setelah Non-Login User, Convert divalidasi ulang di server

14. Di sesi API aktor, buat Login User dengan Email `konflik5+{runId}-066@qwertysystem.net` hingga Login User tersimpan
15. Klik `⋯` pada baris `Konflik Lima {runId}-066` > `Convert to Login User`
16. Klik `[Convert]`
17. Verifikasi dialog blok `Cannot Convert` dengan tombol `[OK]` tampil
18. Klik `[OK]`
19. Verifikasi konversi tidak terjadi: `Konflik Lima {runId}-066` tetap Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Pembuatan Login User pemicu memakai sesi API aktor karena pelaku kedua hanya memicu state; spec tidak memakai butir `P-2` untuk itu.
- Temuan untuk QA:
  - TC-240 dan TC-473 Expected b menyebut "list di-refresh" bersama "tetap Non-Login User"; refresh tidak teramati terpisah sehingga ditulis sebagai satu `Verifikasi` keadaan baris.
  - TC-444 duplikat isi dengan TC-240 (hanya berbeda nama record); keduanya tetap dijalankan karena masing-masing punya id sumber sendiri.
  - TC-240 dan TC-444 tidak menyebut email Login User pemicu persis; spec memakai email record yang diblokir.
