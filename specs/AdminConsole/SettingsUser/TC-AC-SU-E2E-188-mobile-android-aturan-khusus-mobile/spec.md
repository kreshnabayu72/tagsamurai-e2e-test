---
id: TC-AC-SU-E2E-188-mobile-android-aturan-khusus-mobile
title: "Mobile Android Snackbar Kontrol Disabled, Countdown Cooldown Resend, Selection Mode Bulk, dan Bottom Sheet Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-636
  - TC-AC-SU-637
  - TC-AC-SU-638
  - TC-AC-SU-639
coverage:
  mobile: automated
---

# Mobile Android Snackbar Kontrol Disabled, Countdown Cooldown Resend, Selection Mode Bulk, dan Bottom Sheet Auto-Revert

## Prerequisites

- Mode: FE+BE (Android).
- Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list dan bottom sheet. Spec memakai perangkat fisik bersama sehingga suite berjalan serial (`parallel: false`).
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang, serta kemampuan mengetuk elemen UI, long-press, dan membaca teks tombol.
- Akun aktor pertama: Manage user and role (Update) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD` (blok TC-636). Login di aplikasi Android dilakukan di hook `before` spec ini; halaman Settings > User dibuka hook `beforeEach` suite. Akun kedua (ganti akun eksplisit, langkah 5 dan 6): Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_TC_PASSWORD` (blok TC-637 dan TC-638). Akun ketiga (ganti akun eksplisit, langkah 24 dan 25): Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DU_PASSWORD` (blok TC-639). Hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Dewi Lestari {runId}-188A` | `dewilestari+{runId}-188a@qwertysystem.net` | Activated, Active, bertier Total Control (TC-636) |
| U2 | `Sarah Lee {runId}-188B` | `sarahlee+{runId}-188b@qwertysystem.net` | Pending Activation, di luar cooldown Resend (TC-637) |
| U3 | `Jane Smith {runId}-188C` | `janesmith+{runId}-188c@qwertysystem.net` | Activated, Inactive (TC-638) |
| U4 | `John Doe {runId}-188D` | `johndoe+{runId}-188d@qwertysystem.net` | Activated, Active (TC-638) |
| U5 | `Rina Putri {runId}-188E` | `rinaputri+{runId}-188e@qwertysystem.net` | Activated, bertier Total Control (TC-639) |

- Kemampuan teknis: Fixture BE (seeding user dan tier); jam server dan jam perangkat Android diatur bersama untuk countdown cooldown Resend 60 detik (dibekukan pada waktu Resend lalu dimajukan ke T + 59 detik dan T + 60 detik, dipulihkan di hook `after`; bagian 6 konvensi). Tanpa intercept dan klien HTTP.
- State global yang diubah spec: jam server dan jam perangkat; suite berjalan serial.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-636: Tap kontrol Disabled menampilkan snackbar
1. Di card list Settings > User, ketik Search `Dewi Lestari {runId}-188A`, tekan Enter
2. Tap switch Active pada card U1
3. Verifikasi snackbar singkat `"You don't have permission to edit."`
4. Verifikasi switch Active card U1 tidak berubah
### TC-AC-SU-637: Countdown cooldown sebagai teks tombol
5. Lakukan Logout dari akun Manage user and role (Update)
6. Login sebagai Total Control
7. Buka Settings > User lewat sidebar
8. Ketik Search `Sarah Lee {runId}-188B`, tekan Enter, lalu buka Detail U2
9. Tap Resend Activation Email
10. Catat waktu Resend sebagai T, lalu bekukan jam server dan jam perangkat pada T
11. Verifikasi tombol menampilkan `"Resend Activation Email (60s)"`
12. Majukan jam server dan jam perangkat ke T + 59 detik
13. Verifikasi tombol menampilkan `"Resend Activation Email (1s)"`
14. Majukan jam server dan jam perangkat ke T + 60 detik
15. Verifikasi label tombol kembali `Resend Activation Email` dan enabled
16. Pulihkan jam server dan jam perangkat
### TC-AC-SU-638: Long-press card masuk selection mode bulk
17. Kembali ke card list Settings > User, ganti isi kotak search dengan `{runId}-188`, tekan Enter
18. Long-press card U3 (`Jane Smith {runId}-188C`), lalu tap card U4 (`John Doe {runId}-188D`)
19. Verifikasi selection mode aktif dengan checkbox tampil
20. Verifikasi counter `2 Selected`
21. Verifikasi aksi bulk Activate dan Deactivate tampil
22. Verifikasi Resend Activation Email Hidden (seleksi memuat user Activated)
23. Keluar dari selection mode (batalkan seleksi)
### TC-AC-SU-639: Dialog Auto-Revert sebagai bottom sheet
24. Lakukan Logout dari akun Total Control
25. Login sebagai Default User
26. Buka Settings > User lewat sidebar
27. Ketik Search `Rina Putri {runId}-188E`, tekan Enter, buka Detail U5, ketuk Tab Role, lalu sub-tab Global Role
28. Uncheck Delete pada "Manage group"
29. Verifikasi bottom sheet `Remove Total Control` dengan bullet `Rina Putri {runId}-188E` dan tombol `[Cancel]` serta `[Remove]`
30. Tap `[Cancel]` pada bottom sheet

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), pembukaan Settings > User lewat sidebar sesudah login (langkah 7 dan 26), pembukaan Detail, pembekuan dan pemajuan jam (R-10), keluar dari selection mode, dan `[Cancel]` pada bottom sheet agar perubahan Delete tidak tersimpan (S-09).
- Countdown TC-637 dihitung dengan mengatur jam server dan jam perangkat bersama: label `(60s)` diasersi pada waktu Resend, `(1s)` pada T + 59 detik, dan label kembali normal pada T + 60 detik. Asersi tiap detik di antaranya tidak ditulis; TC menyebut "menghitung mundur sampai `(1s)`" tanpa nilai tengah.
- Empat blok kelas hardware (Android) berurutan: akun kedua dan ketiga berganti eksplisit pada langkah 5 dan 6 serta langkah 24 dan 25; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-636 menyebut aktor Manage user and role (Update) dan target Dewi Lestari tanpa menyebut email aktor; spec memakai akun Pre-setup #4. TC-638 dan TC-639 tidak menyebut state awal Jane Smith dan John Doe; spec memakai Inactive dan Active agar aksi bulk campuran tersedia.
  - TC-638 butir b ("sesuai seleksi") tidak menyebut aksi yang tersedia, dan seleksi (U3 Inactive dan U4 Active) sama-sama Activated; PRD §4.2a menyatakan bulk Resend hanya bila semua baris terpilih Pending Activation (TC-106 dan TC-107 menyembunyikannya). Spec mengasersi Activate dan Deactivate tampil serta Resend Activation Email Hidden mengikuti PRD, selaras dengan TC-638 butir b.
  - TC memakai nama literal (`Dewi Lestari`, `Sarah Lee`, `Jane Smith`, `John Doe`, `Rina Putri`); spec memakai nama bersuffix (S-12).
