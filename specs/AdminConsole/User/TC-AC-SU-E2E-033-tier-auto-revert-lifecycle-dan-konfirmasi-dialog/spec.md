---
id: TC-AC-SU-E2E-033-tier-auto-revert-lifecycle-dan-konfirmasi-dialog
title: "Siklus Auto-Revert tier Total Control dan Group Manager saat edit role individual menyimpang dan dialog konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-70
  - TC-AC-SU-107
  - TC-AC-SU-108
  - TC-AC-SU-110
  - TC-AC-SU-112
  - TC-AC-SU-262
  - TC-AC-SU-290
coverage:
  web: automated
---

# Siklus Auto-Revert tier Total Control dan Group Manager saat edit role individual menyimpang dan dialog konfirmasi

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target pengguna Total Control, Group Manager, dan Default User

## Test Steps

### Auto-Revert Total Control: Dialog Konfirmasi dan Pembatalan

1. Buka Detail User > Tab Role untuk pengguna berstatus Total Control
2. Hapus centang (uncheck) pada 1 checkbox CRUD Global Role (contoh: uncheck D pada salah satu role)
3. Verifikasi dialog konfirmasi Auto-Revert muncul memberi peringatan bahwa perubahan akan mencabut tier Total Control
4. Klik tombol `[Cancel]` / `[✕]` pada dialog
5. Verifikasi checkbox kembali tercentang (perubahan dibatalkan), tidak ada request terkirim, dan banner Total Control tetap utuh

### Konfirmasi Auto-Revert Total Control dan Group Manager

1. Uncheck kembali checkbox CRUD tersebut lalu klik tombol `[Confirm]` pada dialog
2. Verifikasi status `access_level` otomatis berubah menjadi `—` (tercabut)
3. Verifikasi banner Total Control seketika hilang, sementara seluruh peran individual lainnya tetap berada pada nilai hasil edit terakhir (tidak di-reset)
4. Buka Detail User > Tab Role untuk pengguna Group Manager
5. Ubah matriks CRUD pada group penugasan GM tersebut hingga tidak lagi full CRUD
6. Verifikasi status Group Manager untuk group tersebut otomatis gugur dan banner GM hilang

### Verifikasi Absennya Auto-Promote dan Imunitas Default User

1. Pada pengguna biasa, susun manual seluruh Global Role dan Group Role hingga mencakup full CRUD di seluruh group
2. Verifikasi `access_level` TETAP bernilai `—` (tidak ada auto-promote ke Total Control secara otomatis tanpa penugasan eksplisit di Role & Permission)
3. Buka Tab Role Default User, verifikasi seluruh kontrol terkunci dan kebal terhadap mekanisme auto-revert

## Notes

- Auto-revert mencabut tier secara cerdas saat konfigurasi hak akses tidak lagi memenuhi pola mutlak tier tersebut.
