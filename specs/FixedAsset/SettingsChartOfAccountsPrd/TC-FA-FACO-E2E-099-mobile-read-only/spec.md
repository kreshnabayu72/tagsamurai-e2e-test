---
id: TC-FA-FACO-E2E-099-mobile-read-only
title: "Elemen tulis tersembunyi dan alasan Disabled tampil lewat tap di aplikasi mobile"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§4.6#b5", "§4.6#b7"]
smoke: []
dependsOn: []
trace:
  "§4.6#b5": [4, 5, 6, 10]
  "§4.6#b7": [8, 9, 11, 13]
anchor: [3]
coverage:
  android: automated
---

# Elemen tulis tersembunyi dan alasan Disabled tampil lewat tap di aplikasi mobile

## Prerequisites
- Aktor: User `Hendra Kusuma {runId}` (Read Only) di aplikasi Android.
- Layar awal: Beranda aplikasi Fixed Asset di perangkat Android.
- Data:
  - DU-099-1: User `Hendra Kusuma {runId}` dengan access level Read Only, scope seluruh client.
  - DU-099-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.

## Test Steps

### Elemen tulis tersembunyi dan Switch Status Disabled
1. Buka halaman Chart of Accounts di aplikasi Android
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
4. Verifikasi tombol `+ Account` tidak dirender
5. Verifikasi ikon `⋯` tidak dirender pada card dengan Account Code `5-6001-{runId}` sehingga aksi `Edit` dan `Delete` tidak tersedia
6. Verifikasi switch Status pada card dengan Account Code `5-6001-{runId}` Disabled

### Alasan state Disabled tampil lewat tap
7. Ketuk switch Status pada card dengan Account Code `5-6001-{runId}`
8. Verifikasi alasan `You don't have permission to edit.` tampil
9. Verifikasi alasan `You don't have permission to edit.` hilang otomatis tanpa interaksi pengguna
10. Verifikasi switch Status pada card dengan Account Code `5-6001-{runId}` tetap Active

### Titik masuk Changelog
11. Verifikasi ikon Changelog tampil di header halaman
12. Klik ikon Changelog di header halaman
13. Verifikasi modal `Changelog: Chart of Accounts` terbuka
14. Klik ikon close pada modal `Changelog: Chart of Accounts`
