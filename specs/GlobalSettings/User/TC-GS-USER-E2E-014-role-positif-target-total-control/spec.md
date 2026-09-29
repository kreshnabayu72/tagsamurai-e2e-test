---
id: TC-GS-USER-E2E-014-role-positif-target-total-control
title: Aktor Total Control dan Default User dapat mengelola target Total Control
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-79
  - TC-GS-USER-82
coverage:
  web: automated
---

# Aktor Total Control dan Default User dapat mengelola target Total Control

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji:

| Role | Akun | Keterangan |
|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | Total Control biasa, bukan Default User |
| Default User | `totalControlGlobalSettings_automated_qaTeam1` | Super admin pertama |

- Entity Client
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login
- Reset Authenticator adalah aksi yang endpoint-nya masih ditunda di modul. Spec ini hanya memverifikasi aksi itu aktif atau tidak aktif, dan tidak pernah menjalankannya

## Test Steps

Lakukan langkah 1–6 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Siti Rahmawati", verifikasi Toggle Active [Global] aktif
3. Verifikasi row action `Delete` aktif
4. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, aktif
5. Klik `✕` untuk menutup modal
6. Verifikasi row action `Reset Authenticator` aktif

## Notes

- Ini spec positif untuk target Total Control dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Pasangan negatifnya adalah `TC-GS-USER-E2E-019-role-negatif-holder-ke-total-control` dan `TC-GS-USER-E2E-018-role-negatif-target-terlindungi`.
- Remove Access tidak punya row action. Titik masuknya adalah checkbox Access di Modal Edit (`GAP-239`), sehingga langkah 4 memeriksanya di sana walaupun TC-GS-USER-79 dan 82 menyebutnya sebagai satu dari empat aksi.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-153, 156). TC-GS-USER-79 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.
