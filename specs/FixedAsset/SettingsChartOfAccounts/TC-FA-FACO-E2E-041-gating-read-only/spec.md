---
id: TC-FA-FACO-E2E-041-gating-read-only
title: "Read Only hanya melihat, mencari, memfilter, Download, dan membuka Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r2", "§2.2#r3", "§9.4.2#r30", "§9.11#p1", "EB-AKS-4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r2": [34, 36, 38]
  "§2.2#r3": [15, 23, 29, 30, 34, 38]
  "§9.4.2#r30": 15
  "§9.11#p1": 21
  "EB-AKS-4": [23, 29, 30, 41, 43, 44, 48]
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
anchor: [5, 32]
coverage:
  web: automated
---

# Read Only hanya melihat, mencari, memfilter, Download, dan membuka Changelog

## Prerequisites
- Aktor: User `Hendra Kusuma {runId}` (Read Only).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-041-1: User `Hendra Kusuma {runId}` dengan access level Read Only, scope seluruh client.
  - DU-041-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-041-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-041-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.

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

### Aksi tulis tidak tersedia bagi Read Only
15. Verifikasi tombol `+ Account` tidak dirender di toolbar
16. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
17. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
18. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
19. Verifikasi kolom Checkbox tidak dirender di tabel sehingga Bulk Action Bar dengan aksi bulk `Activate`, `Deactivate`, dan `Delete` tidak tersedia
20. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}` sehingga row action `Edit` dan `Delete` tidak tersedia

### Mencari, memfilter, Download, dan membuka Changelog
21. Verifikasi tabel menampilkan `3` baris untuk Search `{runId}`
22. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
23. Verifikasi hanya baris Account Code `5-6001-{runId}` yang tampil sebagai hasil Search
24. Klik `(←)` pada kotak Search
25. Ketik Search `{runId}`, tekan Enter
26. Klik kontrol `Filter`
27. Pilih nilai `Inactive` pada Filter `Active`
28. Klik `[Apply]`
29. Verifikasi baris Account Code `4-7001-{runId}` tampil
30. Verifikasi baris Account Code `5-6001-{runId}` tidak tampil
31. Klik `Clear all` pada chip filter
32. Verifikasi baris Account Code `5-6001-{runId}` tampil kembali
33. Klik kontrol `Download`
34. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
35. Klik `Download as CSV`
36. Verifikasi berkas bernama `Chart-of-Accounts` terunduh
37. Klik ikon `Changelog` di toolbar
38. Verifikasi modal `Changelog: Chart of Accounts` terbuka
39. Klik ikon close pada modal `Changelog: Chart of Accounts`

### Sort, Pagination, dan Setup Column aktif
40. Klik header kolom Account Name
41. Verifikasi urutan baris dari atas: Account Code `5-6001-{runId}`, `1-1001-{runId}`, `4-7001-{runId}`
42. Klik header kolom Account Name
43. Verifikasi urutan baris dari atas: Account Code `4-7001-{runId}`, `1-1001-{runId}`, `5-6001-{runId}`
44. Verifikasi Paginator tampil dengan pilihan ukuran halaman `25`
45. Pilih ukuran halaman `25`
46. Klik ikon `⋯` pada header kolom Actions
47. Klik `Setup Column...`
48. Verifikasi modal `Setup Column` terbuka
49. Klik ikon close pada modal `Setup Column`
