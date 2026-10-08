---
id: TC-GS-USER-E2E-131-role-positif-resend-confirmation
title: Role berhak Update berhasil mengirim ulang Confirmation Email
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-590
coverage:
  web: automated
---

# Role berhak Update berhasil mengirim ulang Confirmation Email

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Yoga Pratama" adalah User Basic biasa berstatus Activated dengan pending email change, tidak sedang cooldown

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Klik row action `Resend Confirmation Email` pada "Yoga Pratama"
3. Verifikasi toast "Success, confirmation email has been sent to Yoga Pratama." muncul
4. Verifikasi tombol Disabled dengan tooltip "Please wait {X} seconds before resending." dan hitung mundur dari 60 detik
5. Verifikasi badge pending email pada baris target tetap ada

## Notes

- Pasangan dari `TC-GS-USER-E2E-130`. Perpanjangan masa berlaku link 24 jam tidak terlihat dari UI dan diserahkan ke lapisan BE.
- Target harus di-seed ulang atau menunggu cooldown berakhir sebelum run berikutnya.
