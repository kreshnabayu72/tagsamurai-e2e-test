---
id: TC-FA-FACO-E2E-097-mobile-update-tanpa-delete
title: "Aktor berwenang Update di aplikasi mobile tidak mendapat aksi bulk Delete dan tombol `+ Account`"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.6#b6", "§4.6#b5"]
smoke: []
dependsOn: []
trace:
  "§4.6#b6": [12, 13, 14, 16, 17, 18]
  "§4.6#b5": [4, 5, 6, 8, 9]
anchor: [3]
coverage:
  android: automated
---

# Aktor berwenang Update di aplikasi mobile tidak mendapat aksi bulk Delete dan tombol `+ Account`

## Prerequisites
- Aktor: User `Fajar Nugroho {runId}` (Manage accounting huruf Read dan Update) di aplikasi Android.
- Layar awal: Beranda aplikasi Fixed Asset di perangkat Android.
- Data:
  - DU-097-1: User `Fajar Nugroho {runId}` dengan Global Role Manage accounting huruf Read dan Update (Read baseline terkunci), scope seluruh client.
  - DU-097-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-097-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.

## Test Steps

### Aksi tulis di luar huruf Update tidak tersedia pada card list
1. Buka halaman Chart of Accounts di aplikasi Android
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
4. Verifikasi tombol `+ Account` tidak dirender
5. Verifikasi switch Status pada card dengan Account Code `5-6001-{runId}` Enabled
6. Verifikasi ikon `⋯` tampil pada card dengan Account Code `5-6001-{runId}`
7. Klik ikon `⋯` pada card dengan Account Code `5-6001-{runId}`
8. Verifikasi aksi `Edit` tampil
9. Verifikasi aksi `Delete` tidak dirender
10. Tutup menu aksi pada card

### Seleksi long-press menampilkan aksi bulk menurut capability Update
11. Long-press card dengan Account Code `5-6001-{runId}`
12. Verifikasi counter `1 Selected` tampil pada Floating Bottom Bulk Action Bar
13. Verifikasi aksi bulk `Deactivate` tampil
14. Verifikasi aksi bulk `Delete` tidak tampil
15. Ketuk card dengan Account Code `4-7001-{runId}`
16. Verifikasi counter menunjukkan 2 card terpilih
17. Verifikasi aksi bulk `Activate` dan `Deactivate` tampil
18. Verifikasi aksi bulk `Delete` tidak tampil
19. Klik `[✕]` pada Floating Bottom Bulk Action Bar
