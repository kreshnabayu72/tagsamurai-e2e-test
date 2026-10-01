---
id: TC-GS-USER-E2E-141-role-positif-total-control-default-user-target-read-only
title: Total Control dan Default User dapat mengelola user ber-tier Read Only
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-600
coverage:
  web: automated
---

# Total Control dan Default User dapat mengelola user ber-tier Read Only

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun | Keterangan |
|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | Total Control biasa, bukan Default User |
| Default User | `totalControlGlobalSettings_automated_qaTeam1` | Super admin pertama |

- Entity Client
- Target "Rudi Readonly" adalah user ber-`access_level` Read Only, bukan Default User dan bukan akun yang login, dengan Access `[Global Settings, FAMS]` tanpa aset atau approval di FAMS
- Spec ini hanya mengamati keterbukaan aksi dan tidak mengeksekusinya

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Rudi Readonly", verifikasi checkbox tampil dan aktif
3. Verifikasi Toggle Active [Global] aktif
4. Verifikasi row action `Edit` dan `Delete` aktif
5. Buka Modal Edit "Rudi Readonly" dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, aktif
6. Klik `✕` untuk menutup modal

## Notes

- Melengkapi `TC-GS-USER-E2E-014` yang memakai target Total Control. Berlaku `USER-LOGIC-03`: Total Control dan Default User berwenang atas tier Read Only.
- Pasangan negatif untuk aktor Update-saja adalah `TC-GS-USER-E2E-138`.
- Spec ini tidak mengubah data, jadi tidak butuh cleanup.
