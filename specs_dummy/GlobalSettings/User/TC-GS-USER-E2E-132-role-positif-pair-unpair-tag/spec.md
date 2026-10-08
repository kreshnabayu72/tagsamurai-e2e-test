---
id: TC-GS-USER-E2E-132-role-positif-pair-unpair-tag
title: Role berhak Update berhasil memasang dan melepas TAG di User Detail
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-591
coverage:
  web: automated
---

# Role berhak Update berhasil memasang dan melepas TAG di User Detail

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client pada plan Growth atau lebih tinggi (Scan TAG tampil)
- Target "Dian Anggraini" adalah User Basic biasa tanpa TAG terpasang
- "TAG A" adalah TAG RFID yang sudah diaktivasi, belum dipasang ke user lain, dan peruntukannya user
- Simulasi scan RFID: skrip bisa memasukkan kode TAG seolah hasil scan hardware. Kebutuhan ini disediakan tim FE

## Test Steps

1. Login sebagai role yang diuji, lalu buka User Detail "Dian Anggraini"
2. Klik `Scan TAG` di sub-section User TAG, lalu scan "TAG A"
3. Verifikasi badge "Verified" dan toast "Success, TAG has been paired." muncul
4. Klik `Unpair`
5. Verifikasi dialog "Unpair TAG from this user?" muncul, lalu klik `[Unpair]`
6. Verifikasi badge "Unverified" dan toast "Success, TAG has been unpaired." muncul

## Notes

- Ini spec positif Pair dan Unpair dari Role Matrix. Pair dan Unpair digerbang izin Update (`user.md` §4.8, §9.2 [F-USER-08]). Pasangan negatifnya adalah `TC-GS-USER-E2E-016`.
- Validasi urutan cek TAG diuji di `TC-GS-USER-E2E-032`.
- TAG A kembali bebas setelah Unpair, sehingga tidak butuh cleanup tambahan.
