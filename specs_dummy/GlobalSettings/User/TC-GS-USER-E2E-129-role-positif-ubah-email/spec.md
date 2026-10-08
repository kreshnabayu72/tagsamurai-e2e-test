---
id: TC-GS-USER-E2E-129-role-positif-ubah-email
title: Role berhak Update berhasil mengubah Email user Activated
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-588
coverage:
  web: automated
---

# Role berhak Update berhasil mengubah Email user Activated

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Eko Santoso" adalah User Basic biasa berstatus Activated, tanpa pending email change
- Email baru yang valid dan belum dipakai user lain tersedia (mis. `eko.baru@example.com`)

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Buka Modal Edit pada "Eko Santoso"
3. Ubah field Email menjadi email baru
4. Klik `[Save]`
5. Verifikasi toast Edit standar "Success, user has been updated." muncul, tanpa toast khusus
6. Verifikasi baris target menampilkan badge status pending email dan email lama tetap tampil sebagai email aktif
7. Verifikasi row action `Resend Confirmation Email` tersedia pada baris target

## Notes

- Badge pending email belum punya teks pasti di PRD, lihat `GAP-279`. Langkah 6 hanya memverifikasi badge pending muncul, bukan teksnya.
- Pengiriman email konfirmasi ke email baru tidak bisa dilihat dari UI. Verifikasi isi email diserahkan ke lapisan BE.
- Target harus di-seed ulang tanpa pending email change setelah run.
