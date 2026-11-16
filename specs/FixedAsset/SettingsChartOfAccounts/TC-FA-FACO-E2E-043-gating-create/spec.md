---
id: TC-FA-FACO-E2E-043-gating-create
title: "Manage accounting huruf Create hanya menambah aksi `+ Account`"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r3", "§2.1#r6", "§[F-FACO-01] Create Account#p1", "EB-AKS-5@create-account", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": 11
  "§2.1#r6": [22, 25]
  "§[F-FACO-01] Create Account#p1": 22
  "EB-AKS-5@create-account": [22, 25]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r5": 11
  "§4.8#r6": [12, 14]
  "§4.8#r7": 15
  "§4.8#r8": 15
  "§4.8#r9": 15
  "§4.8#r10": 16
  "§4.8#r11": 16
  "§4.8#r12": 16
anchor: [5]
coverage:
  web: automated
---

# Manage accounting huruf Create hanya menambah aksi `+ Account`

## Prerequisites
- Aktor: User `Rudi Hartono {runId}` (Manage accounting huruf Read dan Create).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-043-1: User `Rudi Hartono {runId}` dengan Global Role Manage accounting huruf Read dan Create (Read baseline terkunci), scope seluruh client.
  - DU-043-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-043-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.

## Test Steps

### Tab dan alat baca tampil
1. Buka halaman Settings > Accounting
2. Verifikasi tab `Chart of Accounts` tampil pada tab bar halaman Accounting
3. Klik tab `Chart of Accounts`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris dengan Account Code `5-6001-{runId}` tampil di tabel
6. Verifikasi kontrol `Search` tampil di toolbar
7. Verifikasi kontrol `Filter` tampil di toolbar
8. Verifikasi kontrol `Download` tampil di toolbar
9. Verifikasi kontrol `Changelog` tampil di toolbar
10. Verifikasi ikon `⋯` pada header kolom Actions tampil

### Huruf Create hanya menambah tombol `+ Account`
11. Verifikasi tombol `+ Account` tampil di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
13. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
14. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
15. Verifikasi kolom Checkbox tidak dirender di tabel sehingga Bulk Action Bar dengan aksi bulk `Activate`, `Deactivate`, dan `Delete` tidak tersedia
16. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}` sehingga row action `Edit` dan `Delete` tidak tersedia

### Create Account dijalankan sampai sukses
17. Klik `+ Account`
18. Isi Account Code `7-2001-{runId}`
19. Isi Account Name `Office Equipment Cost {runId}`
20. Pilih Account Function `Asset Cost`
21. Klik `[Submit]`
22. Verifikasi toast `Success, account has been created.` tampil
23. Muat ulang halaman
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi baris Account Code `7-2001-{runId}` tampil dengan Account Name `Office Equipment Cost {runId}` dan Account Function `Asset Cost`
