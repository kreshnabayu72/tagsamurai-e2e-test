---
id: TC-FA-FACO-E2E-042-gating-read
title: "Manage accounting huruf Read hanya mendapat elemen baca"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r3", "§2.1#r5", "EB-AKS-4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": 15
  "§2.1#r5": [13, 42, 44, 46]
  "EB-AKS-4": [22, 28, 29, 33, 35, 36, 39]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r4": [11, 13]
  "§4.8#r5": 15
  "§4.8#r6": [16, 18]
  "§4.8#r7": 19
  "§4.8#r8": 19
  "§4.8#r9": 19
  "§4.8#r10": 20
  "§4.8#r11": 20
  "§4.8#r12": 20
anchor: [5, 31]
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
  - DU-042-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.

## Test Steps

### Menu dan alat baca tampil
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

### Link Used By membuka popup
11. Verifikasi angka Used By `3` pada baris Account Code `1-1001-{runId}` dapat diklik
12. Klik angka Used By `3` pada baris Account Code `1-1001-{runId}`
13. Verifikasi popup `Used By` tampil
14. Klik ikon close pada popup `Used By`

### Huruf Read tidak mendapat elemen tulis
15. Verifikasi tombol `+ Account` tidak dirender di toolbar
16. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
17. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
18. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
19. Verifikasi kolom Checkbox tidak dirender di tabel sehingga Bulk Action Bar dengan aksi bulk `Activate`, `Deactivate`, dan `Delete` tidak tersedia
20. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}` sehingga row action `Edit` dan `Delete` tidak tersedia

### Membuka tab, melihat tabel, Changelog, Download, serta Search, Filter, Sort, Pagination, dan Setup Column aktif
21. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
22. Verifikasi hanya baris Account Code `5-6001-{runId}` yang tampil sebagai hasil Search
23. Klik `(←)` pada kotak Search
24. Ketik Search `{runId}`, tekan Enter
25. Klik kontrol `Filter`
26. Pilih nilai `Inactive` pada Filter `Active`
27. Klik `[Apply]`
28. Verifikasi baris Account Code `4-7001-{runId}` tampil
29. Verifikasi baris Account Code `5-6001-{runId}` tidak tampil
30. Klik `Clear all` pada chip filter
31. Verifikasi baris Account Code `5-6001-{runId}` tampil kembali
32. Klik header kolom Account Name
33. Verifikasi urutan baris dari atas: Account Code `5-6001-{runId}`, `1-1001-{runId}`, `4-7001-{runId}`
34. Klik header kolom Account Name
35. Verifikasi urutan baris dari atas: Account Code `4-7001-{runId}`, `1-1001-{runId}`, `5-6001-{runId}`
36. Verifikasi Paginator tampil dengan pilihan ukuran halaman `25`
37. Klik ikon `⋯` pada header kolom Actions
38. Klik `Setup Column...`
39. Verifikasi modal `Setup Column` terbuka
40. Klik ikon close pada modal `Setup Column`
41. Klik kontrol `Download`
42. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
43. Klik `Download as CSV`
44. Verifikasi berkas bernama `Chart-of-Accounts` terunduh
45. Klik ikon `Changelog` di toolbar
46. Verifikasi modal `Changelog: Chart of Accounts` terbuka
47. Klik ikon close pada modal `Changelog: Chart of Accounts`
