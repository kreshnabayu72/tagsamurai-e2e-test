---
id: TC-AC-SU-E2E-044-cross-module-synchronization-gs-dan-approvals
title: "Sinkronisasi lintas modul: pembaruan foto profil di Global Settings dan fan-out data transaksi Approvals"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-56
  - TC-AC-SU-185
  - TC-AC-SU-186
coverage:
  web: automated
---

# Sinkronisasi lintas modul: pembaruan foto profil di Global Settings dan fan-out data transaksi Approvals

## Prerequisites

- Login sebagai Role: Principal Total Control
- Akses ke modul Global Settings > User dan modul Admin Console > Approvals

## Test Steps

### Sinkronisasi Foto Profil dari Global Settings

1. Buka modul `Global Settings > User` dan ubah foto profil salah satu pengguna
2. Buka modul `Admin Console > Settings > User` lalu buka Detail User pengguna tersebut
3. Verifikasi foto profil pada Avatar Header di Admin Console seketika ter-update mencerminkan foto baru dari Global Settings tanpa membutuhkan upload manual di AC

### Fan-Out Transaksi Pending Approval dari Modul Approvals

1. Buka modul `Admin Console > Approvals` (ACAP) dan buat transaksi baru yang membutuhkan persetujuan dari target user
2. Buka `Admin Console > Settings > User` > Detail User target > Tab `Responsibilities`
3. Verifikasi transaksi yang baru dibuat tersebut otomatis muncul di tabel Pending Approvals tanpa jeda

## Notes

- Sinkronisasi lintas modul menjamin integritas data real-time antar subsistem TAG Samurai.
