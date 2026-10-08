---
id: TC-GS-USER-E2E-130-role-positif-resend-activation
title: Role berhak Update berhasil mengirim ulang Activation Email
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-589
coverage:
  web: automated
---

# Role berhak Update berhasil mengirim ulang Activation Email

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Nia Kusuma" adalah User Basic biasa berstatus Pending Activation, tidak sedang cooldown

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Klik row action `Resend Activation Email` pada "Nia Kusuma"
3. Verifikasi toast "Success, activation email has been sent." muncul
4. Verifikasi tombol `Resend Activation Email` tetap berlabel yang sama tetapi Disabled dengan tooltip "Please wait {X} seconds before resending." dan hitung mundur dari 60 detik

## Notes

- Cooldown 60 detik diatur `user.md` §9.2 [F-USER-07]. Tombol kembali Enabled setelah 60 detik dan itu diverifikasi di spec Resend milik Total Control, bukan di sini.
- Target harus di-seed ulang atau menunggu cooldown berakhir sebelum run berikutnya.
