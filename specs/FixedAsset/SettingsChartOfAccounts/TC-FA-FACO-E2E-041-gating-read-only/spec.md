---
id: TC-FA-FACO-E2E-041-gating-read-only
title: "Read Only hanya melihat, mencari, memfilter, Download, dan membuka Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r2", "§2.2#r3", "§9.4.2#r30", "§9.11#p1", "EB-AKS-4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r2": [31, 33, 35]
  "§2.2#r3": [11, 19, 25, 26, 31, 35]
  "§9.4.2#r30": 11
  "§9.11#p1": 17
  "EB-AKS-4": [19, 25, 26, 38, 40, 41, 43, 46]
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
anchor: [5, 29]
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

### Aksi tulis tidak tersedia bagi Read Only
11. Verifikasi tombol `+ Account` tidak dirender di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
13. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
14. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
15. Verifikasi kolom Checkbox tidak dirender di tabel sehingga Bulk Action Bar dengan aksi bulk `Activate`, `Deactivate`, dan `Delete` tidak tersedia
16. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}` sehingga row action `Edit` dan `Delete` tidak tersedia

### Mencari, memfilter, Download, dan membuka Changelog
17. Verifikasi tabel menampilkan `2` baris untuk Search `{runId}`
18. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
19. Verifikasi hanya baris Account Code `5-6001-{runId}` yang tampil sebagai hasil Search
20. Klik `(←)` pada kotak Search
21. Ketik Search `{runId}`, tekan Enter
22. Klik kontrol `Filter`
23. Pilih nilai `Inactive` pada Filter `Active`
24. Klik `[Apply]`
25. Verifikasi baris Account Code `4-7001-{runId}` tampil
26. Verifikasi baris Account Code `5-6001-{runId}` tidak tampil
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Verifikasi baris Account Code `5-6001-{runId}` tampil kembali
30. Klik kontrol `Download`
31. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
32. Klik `Download as CSV`
33. Verifikasi berkas bernama `Chart-of-Accounts` terunduh
34. Klik ikon `Changelog` di toolbar
35. Verifikasi modal `Changelog: Chart of Accounts` terbuka
36. Klik ikon close pada modal `Changelog: Chart of Accounts`

### Sort, Pagination, dan Setup Column aktif
37. Klik header kolom Account Name
38. Verifikasi urutan baris dari atas: Account Code `5-6001-{runId}`, `4-7001-{runId}`
39. Klik header kolom Account Name
40. Verifikasi urutan baris dari atas: Account Code `4-7001-{runId}`, `5-6001-{runId}`
41. Verifikasi Paginator tampil dengan pilihan ukuran halaman `25`
42. Pilih ukuran halaman `25`
43. Verifikasi ukuran halaman aktif `25`
44. Klik ikon `⋯` pada header kolom Actions
45. Klik `Setup Column...`
46. Verifikasi modal `Setup Column` terbuka
47. Klik ikon close pada modal `Setup Column`
