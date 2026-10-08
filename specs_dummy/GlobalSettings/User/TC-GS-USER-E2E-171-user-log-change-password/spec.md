---
id: TC-GS-USER-E2E-171-user-log-change-password
title: Tab User Log menampilkan Activity Change Password
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-631
coverage:
  web: automated
---

# Tab User Log menampilkan Activity Change Password

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Doni Pratama" pernah Change Password berhasil dan sekali gagal karena password lama salah
- Riwayat login disediakan tim FE lewat seeding, spec ini hanya membaca data

## Test Steps

1. Buka User Detail "Doni Pratama" > Tab User Log
2. Cari baris Activity "Change Password" dengan Status "Success" dan verifikasi Note "Password changed"
3. Cari baris Activity "Change Password" dengan Status "Failed" dan verifikasi Note "Incorrect current password"
4. Verifikasi Status kedua baris tampil sebagai teks biasa, bukan badge

## Notes

- Sumber `user.md` §8.4. Pasangan `TC-GS-USER-E2E-068` untuk Login/Logout/Session.
- Baris Reset Password tidak dicakup karena tidak ada di tabel §8.4 (`GAP-305`).
