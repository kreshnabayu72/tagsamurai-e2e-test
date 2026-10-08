---
id: TC-GS-ACTLOG-E2E-014-scope-produk-global-settings-dan-eksklusi-produk-lain
title: "Scope Produk Global Settings: Inklusi Login Platform & Sesi GS serta Eksklusi Modul Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-38
  - TC-GS-ACTLOG-39
  - TC-GS-ACTLOG-40
coverage:
  web: automated
---

# Scope Produk Global Settings: Inklusi Login Platform & Sesi GS serta Eksklusi Modul Lain

## Prerequisites

- Terdapat entri sesi Fixed Asset dan Admin Console pada entitas yang sama
- Terdapat user 'Rudi Hartono' yang hanya memiliki akses Fixed Asset (tanpa akses GS) dan melakukan login platform
- Terdapat mutasi data di modul Fixed Asset (Register Asset) dan modul GS (Create Brand)

## Test Steps

### Sesi GS vs Sesi Produk Lain di Tab Session
1. Buka Tab Session di Global Settings.
2. Terapkan filter Activity = 'Session'.
3. Verifikasi hanya entri lifecycle sesi Global Settings ('Session started' / 'Session ended') yang tampil.
4. Verifikasi sesi dari produk Fixed Asset dan Admin Console tidak dimunculkan di Tab Session GS.
### Inklusi Login Seluruh User Entitas
5. Kosongkan filter Activity, cari user 'Rudi' di kotak Search Tab Session.
6. Verifikasi baris Login milik 'Rudi H' tampil di Tab Session meskipun user tersebut tidak memiliki hak akses ke Global Settings.
### Eksklusi Aktivitas Non-GS di Tab User Action
7. Klik tab 'User Action', buka dropdown filter Object.
8. Verifikasi opsi Object hanya memuat modul-modul Global Settings (misal Brand, User, General Settings).
9. Verifikasi tidak ada entri mutasi dari Fixed Asset (Register Asset) atau Supply Asset pada tabel maupun dropdown filter.

## Notes

- Tab Session GS membaca log platform untuk seluruh pengguna entitas, sedangkan Tab User Action eksklusif mencatat modul GS.
