---
id: TC-FA-FACO-E2E-022-edit-account
title: "Edit Account menyimpan field yang diubah dan mempertahankan field lain"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["F-FACO-02", "FACO-LOGIC-04c", "R-02", "§[F-FACO-02] Edit Account#b4", "§9.4.2#r37", "§9.5#r8", "§9.7#r18", "EB-FRM-1@form-edit-account", "EB-FRM-9", "L-02", "T-02", "EB-ERR-4"]
smoke: ["L-02", "T-02", "EB-ERR-4"]
dependsOn: []
trace:
  "F-FACO-02": [23, 24, 25]
  "FACO-LOGIC-04c": 24
  "R-02": [23, 24, 29, 30]
  "§[F-FACO-02] Edit Account#b4": [23, 33, 35]
  "§9.4.2#r37": 45
  "§9.5#r8": [5, 6, 7]
  "§9.7#r18": 24
  "EB-FRM-1@form-edit-account": [33, 35, 37]
  "EB-FRM-9": [10, 11, 26, 29, 30]
  "L-02": [33, 34, 36]
  "T-02": 23
  "EB-ERR-4": [14, 16]
anchor: [2]
coverage:
  web: automated
  android: automated
---

# Edit Account menyimpan field yang diubah dan mempertahankan field lain

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-022-1: akun Active dengan Account Code `5-6001-{runId}`, Account Name `Depreciation Expense Admin {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; belum pernah diekspor, sehingga seluruh field dapat diedit.
  - DU-022-2: akun Active dengan Account Code `5-6002-{runId}`, Account Name `Depreciation Expense Warehouse {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; belum pernah diekspor.

## Test Steps

### Save ditolak saat Account Code sudah dipakai akun lain
1. Ketik Search `5-6002-{runId}`, tekan Enter
2. Verifikasi baris `5-6002-{runId}` tampil pada tabel
3. Klik `⋯` pada baris `5-6002-{runId}`
4. Klik `Edit`
5. Verifikasi field Account Code berisi `5-6002-{runId}`
6. Verifikasi field Account Name berisi `Depreciation Expense Warehouse {runId}`
7. Verifikasi field Account Function berisi `Depreciation Expense`
8. Ganti isi Account Code dengan `5-6001-{runId}`
9. Klik `[Save]`
10. Verifikasi caption `Account code already exists` tampil pada field Account Code
11. Verifikasi toast `Success, account has been updated.` tidak tampil
12. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
13. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
14. Verifikasi tepat satu baris tampil, yaitu baris `5-6001-{runId}` dengan Account Name `Depreciation Expense Admin {runId}`
15. Ganti isi kotak search dengan `5-6002-{runId}`, tekan Enter
16. Verifikasi baris `5-6002-{runId}` tampil dengan Account Name `Depreciation Expense Warehouse {runId}`

### Account Name dan Account Function tersimpan, Account Code tetap
17. Ganti isi kotak search dengan `5-6001-{runId}`, tekan Enter
18. Klik `⋯` pada baris `5-6001-{runId}`
19. Klik `Edit`
20. Ganti isi Account Name dengan `Depreciation Expense Admin Office {runId}`
21. Pilih Account Function `Capitalization Offset`
22. Klik ganda `[Save]`
23. Verifikasi toast `Success, account has been updated.` tampil
24. Verifikasi Account Name pada baris `5-6001-{runId}` berubah menjadi `Depreciation Expense Admin Office {runId}`
25. Verifikasi Account Function pada baris `5-6001-{runId}` berubah menjadi `Capitalization Offset`
26. Verifikasi Account Code pada baris itu tetap `5-6001-{runId}`
27. Muat ulang halaman
28. Ketik Search `5-6001-{runId}`, tekan Enter
29. Verifikasi baris `5-6001-{runId}` tampil dengan Account Name `Depreciation Expense Admin Office {runId}`
30. Verifikasi baris `5-6001-{runId}` tampil dengan Account Function `Capitalization Offset`

### Satu entri Changelog per field yang berubah
31. Klik ikon Changelog
32. Ketik Search `5-6001-{runId}`, tekan Enter
33. Verifikasi tepat satu baris Changelog dengan Action `Edit` dan Field `Account Name`
34. Verifikasi baris Field `Account Name` itu memuat Old Value `Depreciation Expense Admin {runId}` dan New Value `Depreciation Expense Admin Office {runId}`
35. Verifikasi tepat satu baris Changelog dengan Action `Edit` dan Field `Account Function`
36. Verifikasi baris Field `Account Function` itu memuat Old Value `Depreciation Expense` dan New Value `Capitalization Offset`
37. Verifikasi tidak ada baris Changelog dengan Action `Edit` dan Field `Account Code`
38. Klik `✕` pada modal Changelog

### Account Name yang sama dengan akun lain diizinkan saat Edit
39. Ganti isi kotak search dengan `5-6002-{runId}`, tekan Enter
40. Klik `⋯` pada baris `5-6002-{runId}`
41. Klik `Edit`
42. Ganti isi Account Name dengan `Depreciation Expense Admin Office {runId}`
43. Klik `[Save]`
44. Ketik Search `Depreciation Expense Admin Office {runId}`, tekan Enter
45. Verifikasi baris `5-6001-{runId}` dan baris `5-6002-{runId}` tampil dengan Account Name yang sama `Depreciation Expense Admin Office {runId}`
