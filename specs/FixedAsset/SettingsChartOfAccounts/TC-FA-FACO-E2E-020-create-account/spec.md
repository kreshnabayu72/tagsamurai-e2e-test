---
id: TC-FA-FACO-E2E-020-create-account
title: "Create Account dari toolbar tersimpan dan tampil di tabel"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FACO-01", "R-01", "ST-04", "§3.1#p1", "§5#b14", "§[F-FACO-01] Create Account#b1", "§[F-FACO-01] Create Account#b3", "§[F-FACO-01] Create Account#b5", "§9.4.2#r32", "§9.4.2#r37", "§9.5#r9", "§9.7#r15", "EB-FRM-1@form-add-account", "L-01", "T-01", "V-04", "EB-FRM-5@account-code", "EB-CON-2"]
smoke: ["L-01", "T-01", "V-04", "EB-FRM-5@account-code", "EB-CON-2"]
dependsOn: []
trace:
  "F-FACO-01": 14
  "R-01": [13, 14, 16]
  "ST-04": 20
  "§3.1#p1": [21, 22, 23]
  "§5#b14": [15, 16, 20, 31]
  "§[F-FACO-01] Create Account#b1": 26
  "§[F-FACO-01] Create Account#b3": [21, 22, 23]
  "§[F-FACO-01] Create Account#b5": [13, 14, 15, 16, 17, 18, 19, 20, 31]
  "§9.4.2#r32": [33, 36]
  "§9.4.2#r37": 46
  "§9.5#r9": [21, 22, 23]
  "§9.7#r15": 14
  "EB-FRM-1@form-add-account": [33, 36]
  "L-01": [37, 38]
  "T-01": 13
  "V-04": 52
  "EB-FRM-5@account-code": 52
  "EB-CON-2": 55
anchor: [7, 30]
coverage:
  web: automated
---

# Create Account dari toolbar tersimpan dan tampil di tabel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-020-1: akun Active dengan Account Code `1-1001-{runId}`, Account Name `Fixed Assets Equipment {runId}`, Account Function `Asset Cost`, Used By `0`, Last Used in Journal `—`, ada di entitas aktor.
  - DU-020-5: 26 akun Active dengan Account Code `1-3{n}-{runId}`, Account Name `Cadangan Penyusutan Aset Tetap {n} {runId}`, `{n}` dari 1 sampai 26, Account Function `Accumulated Depreciation`, Used By `0`, Last Used in Journal `—`, ada di entitas aktor.
  - Pada urutan default Account Code A-Z, DU-020-1 dan DU-020-5 (27 akun) seluruhnya mendahului Account Code `5-6001-{runId}`, lebih banyak daripada ukuran halaman `25` yang dipilih sebelum Create.

## Test Steps

### Search, Filter Panel, sort, dan ukuran halaman aktif sebelum Create
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon Filter pada toolbar
3. Pilih Function `Asset Cost` pada Filter Panel
4. Klik `[Apply]`
5. Klik header kolom `Account Name`
6. Pilih Rows per page `25` pada paginasi tabel
7. Verifikasi baris `1-1001-{runId}` tampil pada tabel

### Create Account tersimpan dan tampil di tabel
8. Klik `[+ Account]`
9. Isi Account Code `5-6001-{runId}`
10. Isi Account Name `  Depreciation Expense Admin {runId}  ` (dua spasi di awal dan dua spasi di akhir)
11. Pilih Account Function `Depreciation Expense`
12. Klik ganda `[Submit]`
13. Verifikasi toast `Success, account has been created.` tampil
14. Verifikasi baris `5-6001-{runId}` tampil pada halaman tabel yang aktif
15. Verifikasi baris `5-6001-{runId}` di-highlight
16. Verifikasi halaman aktif pada paginasi bukan halaman `1`
17. Verifikasi ukuran halaman pada paginasi tetap `25`
18. Verifikasi kotak Search kosong
19. Verifikasi tidak ada chip filter aktif
20. Verifikasi highlight pada baris `5-6001-{runId}` hilang tanpa interaksi pengguna

### Nilai awal akun baru dan nilai tersimpan tanpa spasi tepi
21. Verifikasi Switch Status pada baris `5-6001-{runId}` berstatus Active
22. Verifikasi Used By pada baris `5-6001-{runId}` bernilai `0`
23. Verifikasi Last Used in Journal pada baris `5-6001-{runId}` bernilai `—`
24. Klik `⋯` pada baris `5-6001-{runId}`
25. Klik `Edit`
26. Verifikasi field Account Name berisi `Depreciation Expense Admin {runId}` tanpa spasi di awal dan di akhir
27. Klik `✕` pada form Edit Account (form belum diubah, sehingga tidak ada dialog Unsaved Changes)

### Sort kembali ke default sesudah Create
28. Ketik Search `{runId}`, tekan Enter
29. Pilih Rows per page `100` pada paginasi tabel
30. Verifikasi baris `1-1001-{runId}` dan baris `5-6001-{runId}` tampil pada tabel
31. Verifikasi urutan baris: baris `1-1001-{runId}` tampil di atas baris `5-6001-{runId}`

### Satu klik ganda hanya membuat satu akun dan satu entri log
32. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
33. Verifikasi tepat satu baris tampil pada hasil Search
34. Klik ikon Changelog pada toolbar
35. Ketik Search `5-6001-{runId}`, tekan Enter
36. Verifikasi tepat satu baris Changelog tampil dengan Account Code `5-6001-{runId}`
37. Verifikasi baris Changelog itu memuat Action `Create` dan Field `Account Code`
38. Verifikasi baris Changelog itu memuat Old Value `—` dan New Value `5-6001-{runId}`
39. Klik `✕` pada modal Changelog

### Account Name yang sama dengan akun lain diizinkan
40. Klik `[+ Account]`
41. Isi Account Code `5-6002-{runId}`
42. Isi Account Name `Depreciation Expense Admin {runId}`
43. Pilih Account Function `Depreciation Expense`
44. Klik `[Submit]`
45. Ketik Search `Depreciation Expense Admin {runId}`, tekan Enter
46. Verifikasi baris `5-6001-{runId}` dan baris `5-6002-{runId}` tampil dengan Account Name yang sama `Depreciation Expense Admin {runId}`

### Account Code yang sudah dipakai ditolak
47. Klik `[+ Account]`
48. Isi Account Code `1-1001-{runId}`
49. Isi Account Name `Fixed Assets Duplicate Code {runId}`
50. Pilih Account Function `Asset Cost`
51. Klik `[Submit]`
52. Verifikasi caption `Account code already exists` tampil pada field Account Code
53. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
54. Ganti isi kotak search dengan `1-1001-{runId}`, tekan Enter
55. Verifikasi tepat satu baris `1-1001-{runId}` tampil pada hasil Search
