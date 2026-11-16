---
id: TC-FA-FACO-E2E-038-gating-create-delete-gabungan
title: "Aktor dengan huruf Create dan Delete mendapat gabungan elemen keduanya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.8#b1"]
smoke: []
dependsOn: []
trace:
  "§4.8#b1": [2, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 26, 27]
anchor: [5]
coverage:
  web: automated
---

# Aktor dengan huruf Create dan Delete mendapat gabungan elemen keduanya

## Prerequisites
- Aktor: User `Siti Rahma {runId}` (Manage accounting huruf Read, Create, dan Delete).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-038-1: User `Siti Rahma {runId}` dengan Global Role Manage accounting huruf Read, Create, dan Delete (Read baseline terkunci), scope seluruh client.
  - DU-038-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-038-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.

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

### Aktor Create dan Delete mendapat gabungan elemen keduanya
11. Verifikasi tombol `+ Account` tampil di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
13. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
14. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
15. Verifikasi kolom Checkbox tampil di tabel
16. Centang baris Account Code `5-6001-{runId}`
17. Centang baris Account Code `4-7001-{runId}`
18. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
19. Klik `Bulk Action`
20. Verifikasi aksi bulk `Delete` tampil
21. Verifikasi aksi bulk `Activate` dan `Deactivate` tidak ada pada daftar aksi
22. Tekan Esc untuk menutup daftar aksi bulk
23. Klik ikon `×` pada Bulk Action Bar
24. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
25. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
26. Verifikasi row action `Delete` tampil
27. Verifikasi row action `Edit` tidak dirender
28. Tekan Esc untuk menutup menu aksi baris
