---
id: TC-GS-USER-E2E-135-role-positif-bulk-resend-activation
title: Role berhak Update berhasil mengirim ulang Activation Email ke beberapa user sekaligus
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-594
coverage:
  web: automated
---

# Role berhak Update berhasil mengirim ulang Activation Email ke beberapa user sekaligus

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Citra Dewi" dan "Dedi Hartono" adalah User Basic biasa berstatus Pending Activation, tidak sedang cooldown

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Centang baris "Citra Dewi" dan "Dedi Hartono"
3. Verifikasi aksi `Resend Activation Email` tampil pada bulk bar
4. Klik `Resend Activation Email`
5. Verifikasi toast "Success, activation email has been sent." muncul
6. Verifikasi tombol Resend pada kedua baris Disabled dengan tooltip countdown 60 detik

## Notes

- Aksi ini hanya tampil pada seleksi seragam Pending Activation. Seleksi campuran diuji di spec Bulk milik Total Control.
- Target harus di-seed ulang atau menunggu cooldown berakhir sebelum run berikutnya.
