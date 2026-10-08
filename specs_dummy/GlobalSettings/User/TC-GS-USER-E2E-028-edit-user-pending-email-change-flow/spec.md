---
id: TC-GS-USER-E2E-028-edit-user-pending-email-change-flow
title: "Edit User: Alur perubahan email, status Pending Email Change, resend, dan pembatalan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-201
  - TC-GS-USER-202
  - TC-GS-USER-203
  - TC-GS-USER-204
  - TC-GS-USER-205
  - TC-GS-USER-206
  - TC-GS-USER-207
  - TC-GS-USER-208
  - TC-GS-USER-209
  - TC-GS-USER-210
  - TC-GS-USER-211
  - TC-GS-USER-212
  - TC-GS-USER-213
  - TC-GS-USER-214
  - TC-GS-USER-215
  - TC-GS-USER-216
  - TC-GS-USER-217
  - TC-GS-USER-218
  - TC-GS-USER-219
  - TC-GS-USER-220
coverage:
  web: automated
---

# Edit User: Alur perubahan email, status Pending Email Change, resend, dan pembatalan

## Prerequisites

- Login sebagai Role: Total Control
- User Dewi Lestari berstatus Activated

## Test Steps

### Inisiasi Ganti Email

1. Buka modal Edit user Dewi Lestari, ubah Email menjadi 'dewi.baru@qwertysystem.net', klik '[Save]'
2. Verifikasi toast informasi 'Confirmation email sent.' tampil
3. Verifikasi baris Dewi Lestari di User List kini menampilkan badge 'Pending Email Confirmation'
4. Buka menu (⋯), klik 'Resend Confirmation Email', verifikasi toast sukses kirim ulang
5. Buka Detail Dewi Lestari, klik opsi batalkan perubahan email, verifikasi badge hilang dan email kembali ke email lama

## Notes

- Menggabungkan 20 test case granular (TC-GS-USER-201 s.d. TC-GS-USER-220).
