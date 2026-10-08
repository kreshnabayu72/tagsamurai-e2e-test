---
id: TC-GS-USER-E2E-018-role-negatif-target-terlindungi
title: Default User dan akun sendiri terlindungi dari aksi tulis
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-80
  - TC-GS-USER-81
  - TC-GS-USER-83
  - TC-GS-USER-86
coverage:
  web: automated
---

# Default User dan akun sendiri terlindungi dari aksi tulis

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan target yang diperiksa yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan target yang diperiksa:

| Role | Akun | Target Default User | Target akun sendiri |
|---|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | Baris Default User, tooltip "Default User cannot be modified." | Baris `totalControl2_automated_qaTeam1`, tooltip "You can't manage your own account from here." |
| Default User | `totalControlGlobalSettings_automated_qaTeam1` | Baris Default User adalah akun sendiri, tooltip "You can't manage your own account from here." | Baris yang sama |

- Entity Client
- Reset Authenticator adalah aksi yang endpoint-nya masih ditunda di modul. Spec ini hanya memverifikasi aksi itu tidak aktif dan tidak pernah menjalankannya

## Test Steps

Lakukan langkah 1–7 untuk setiap role pada tabel "Role yang diuji", dan untuk setiap target pada baris role itu.

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris target, verifikasi Toggle Active [Global] Disabled dengan tooltip sesuai tabel
3. Verifikasi row action `Delete` Disabled dengan tooltip yang sama
4. Buka Modal Edit target dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, Disabled dengan tooltip yang sama
5. Klik `✕` untuk menutup modal
6. Verifikasi row action `Reset Authenticator` Disabled dengan tooltip yang sama
7. Verifikasi teks tooltip pada keempat aksi persis sama, dan tooltip Default User tidak pernah tertukar dengan tooltip akun sendiri

## Notes

- Ini spec negatif target terlindungi dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Perlindungan ini berlaku untuk semua aktor tanpa kecuali (`USER-LOGIC-01`, `USER-LOGIC-02`).
- Remove Access tidak punya row action. Titik masuknya adalah checkbox Access di Modal Edit (`GAP-239`), sehingga langkah 4 memeriksanya di sana.
- Untuk aktor Default User, target Default User dan target akun sendiri adalah baris yang sama, sehingga langkah 1–7 cukup dijalankan sekali dengan tooltip akun sendiri.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-154, 155, 157, 160). TC-GS-USER-80 dan 81 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.
