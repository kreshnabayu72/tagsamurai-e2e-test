---
id: TC-GS-USER-E2E-004-empty-state-client-baru-hanya-default-user
title: "Empty State Client Baru: Hanya Baris Default User Tanpa Ilustrasi, Toggle dan Checkbox Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-9
coverage:
  web: automated
---

# Empty State Client Baru: Hanya Baris Default User Tanpa Ilustrasi, Toggle dan Checkbox Disabled

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`); hook suite menyetel flag itu juga untuk akun Default User client baru di bawah (kemampuan disediakan tim FE/BE).
- Akun aktor: Default User (Hendra Gunawan) pada client baru yang hanya berisi Default User, tanpa user lain. Client dan akun ini disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup No. 1-26, yang mendaftarkan Default User client Pre-setup). Kredensial `Spectra.env.GS_DEFAULT_PASSWORD`. Login sekali di hook `before` (akun aktor pertama spec ini); hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_DEFAULT_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data: client baru hanya berisi Default User; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-USER-9: Genuinely empty User List tetap menampilkan baris Default User tanpa ilustrasi

1. Buka Global Settings > User > User List
2. Verifikasi tabel menampilkan 1 baris Default User (Hendra Gunawan)
3. Verifikasi tidak ada ilustrasi empty state
4. Verifikasi toggle Active baris Default User tampil (visible)
5. Verifikasi toggle Active baris Default User disabled
6. Verifikasi checkbox baris Default User tampil (visible)
7. Verifikasi checkbox baris Default User disabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memakai akun Default User client baru, bukan akun default suite, sehingga login akun itu dilakukan di hook `before` dan sesi dikembalikan di hook `after`.
- Temuan untuk QA:
  - TC-GS-USER-9 mensyaratkan "Client baru: hanya berisi Default User" dan login sebagai Default User, tetapi Tabel Pre-setup tidak memuat client atau akun tersebut (No. 1 adalah Default User client Pre-setup yang berisi user lain). Client baru, email akun, dan password disediakan tim FE.
  - TC-GS-USER-9 Expected a menyebut "1 baris Default User" tanpa menyebut Name; spec memakai Name seed Default User `Hendra Gunawan` (TC-GS-USER-1043).
