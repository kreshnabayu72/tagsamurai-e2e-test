---
id: TC-GS-USER-E2E-133-role-positif-reset-authenticator
title: Role berhak Update berhasil mereset Authenticator user
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-592
coverage:
  web: automated
---

# Role berhak Update berhasil mereset Authenticator user

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Rina Wijaya" adalah User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login) dengan Authenticator enrolled
- Reset Authenticator butuh flow enrollment MFA ulang. Kebutuhan akun dengan MFA yang bisa dikendalikan skrip disediakan tim FE

## Test Steps

1. Login sebagai role yang diuji, lalu buka User Detail "Rina Wijaya"
2. Verifikasi section Authenticator menampilkan badge "Enrolled" dan tombol `Reset Authenticator`
3. Klik `Reset Authenticator`, lalu klik `[Reset]` pada dialog konfirmasi
4. Verifikasi toast "Success, authenticator has been reset for Rina Wijaya." muncul
5. Verifikasi badge berubah menjadi "Not Enrolled" dan tombol `Reset Authenticator` hilang

## Notes

- Ini spec positif Reset Authenticator dari Role Matrix, digerbang izin Update dan target yang bukan Total Control, Read Only, atau Default User (`user.md` §4.8). Alur Total Control ada di `TC-GS-USER-E2E-037`.
- Target harus dienroll ulang oleh seeding sebelum run berikutnya.
