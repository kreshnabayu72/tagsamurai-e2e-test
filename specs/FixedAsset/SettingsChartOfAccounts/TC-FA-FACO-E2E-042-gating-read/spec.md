---
id: TC-FA-FACO-E2E-042-gating-read
title: "Manage accounting huruf Read hanya mendapat elemen baca"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r3", "§2.1#r5", "EB-AKS-4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": 11
  "§2.1#r5": [41, 43, 45]
  "EB-AKS-4": [18, 24, 25, 30, 32, 33, 35, 38]
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
anchor: [5, 28]
coverage:
  web: automated
---

# Manage accounting huruf Read hanya mendapat elemen baca

## Prerequisites
- Aktor: User `Maya Lestari {runId}` (Manage accounting huruf Read).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-042-1: User `Maya Lestari {runId}` dengan Global Role Manage accounting huruf Read saja, scope seluruh client.
  - DU-042-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-042-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.

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

### Huruf Read tidak mendapat elemen tulis
11. Verifikasi tombol `+ Account` tidak dirender di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
13. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
14. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
15. Verifikasi kolom Checkbox tidak dirender di tabel sehingga Bulk Action Bar dengan aksi bulk `Activate`, `Deactivate`, dan `Delete` tidak tersedia
16. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}` sehingga row action `Edit` dan `Delete` tidak tersedia

### Membuka tab, melihat tabel, Changelog, Download, serta Search, Filter, Sort, Pagination, dan Setup Column aktif
17. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
18. Verifikasi hanya baris Account Code `5-6001-{runId}` yang tampil sebagai hasil Search
19. Klik `(←)` pada kotak Search
20. Ketik Search `{runId}`, tekan Enter
21. Klik kontrol `Filter`
22. Pilih nilai `Inactive` pada Filter `Active`
23. Klik `[Apply]`
24. Verifikasi baris Account Code `4-7001-{runId}` tampil
25. Verifikasi baris Account Code `5-6001-{runId}` tidak tampil
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Verifikasi baris Account Code `5-6001-{runId}` tampil kembali
29. Klik header kolom Account Name
30. Verifikasi urutan baris dari atas: Account Code `5-6001-{runId}`, `4-7001-{runId}`
31. Klik header kolom Account Name
32. Verifikasi urutan baris dari atas: Account Code `4-7001-{runId}`, `5-6001-{runId}`
33. Verifikasi Paginator tampil dengan pilihan ukuran halaman `25`
34. Pilih ukuran halaman `25`
35. Verifikasi ukuran halaman aktif `25`
36. Klik ikon `⋯` pada header kolom Actions
37. Klik `Setup Column...`
38. Verifikasi modal `Setup Column` terbuka
39. Klik ikon close pada modal `Setup Column`
40. Klik kontrol `Download`
41. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
42. Klik `Download as CSV`
43. Verifikasi berkas bernama `Chart-of-Accounts` terunduh
44. Klik ikon `Changelog` di toolbar
45. Verifikasi modal `Changelog: Chart of Accounts` terbuka
46. Klik ikon close pada modal `Changelog: Chart of Accounts`
