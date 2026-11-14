---
id: TC-FA-FACO-E2E-028-delete-single
title: "Delete satu akun yang lolos kedua guard"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-07", "F-FACO-05", "FACO-LOGIC-03d", "FACO-LOGIC-03e", "§[F-FACO-05] Delete Account#p3", "§[F-FACO-05] Delete Account#b3", "§9.4.2#r33", "§9.7#r26", "§9.7#r27", "L-04", "T-06", "EB-EDG-3"]
smoke: ["L-04", "T-06", "EB-EDG-3"]
dependsOn: []
trace:
  "D-07": [5, 8]
  "F-FACO-05": [8, 11]
  "FACO-LOGIC-03d": [8, 11]
  "FACO-LOGIC-03e": [16, 17]
  "§[F-FACO-05] Delete Account#p3": [13, 16, 17]
  "§[F-FACO-05] Delete Account#b3": [7, 8, 16, 17]
  "§9.4.2#r33": [13, 16, 17]
  "§9.7#r26": 8
  "§9.7#r27": [16, 17]
  "L-04": [16, 17]
  "T-06": 7
  "EB-EDG-3": [13, 17]
anchor: [2]
coverage:
  web: automated
  android: automated
---

# Delete satu akun yang lolos kedua guard

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-028-1: akun Active dengan Account Code `5-6006-{runId}`, Account Name `Depreciation Expense Cabang {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; bukan nilai default company; Account Label `5-6006-{runId} – Depreciation Expense Cabang {runId}`.
  - DU-028-2: akun Active dengan Account Code `5-6007-{runId}`, Account Name `Depreciation Expense Pusat {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; tidak dihapus.

## Test Steps

### Delete akun yang lolos kedua guard
1. Ketik Search `5-6006-{runId}`, tekan Enter
2. Verifikasi baris `5-6006-{runId}` tampil pada tabel
3. Klik `⋯` pada baris `5-6006-{runId}`
4. Klik `Delete`
5. Verifikasi bullet `5-6006-{runId} – Depreciation Expense Cabang {runId}` tampil pada dialog konfirmasi
6. Klik `[Delete]`
7. Verifikasi toast `Success, account has been deleted.` tampil
8. Verifikasi empty state `No results found` tampil pada tabel
9. Muat ulang halaman
10. Ketik Search `5-6006-{runId}`, tekan Enter
11. Verifikasi empty state `No results found` tampil pada tabel

### Akun lain tidak terdampak
12. Ganti isi kotak search dengan `5-6007-{runId}`, tekan Enter
13. Verifikasi baris `5-6007-{runId}` tampil dengan Account Name `Depreciation Expense Pusat {runId}`

### Kode akun yang dihapus tetap tersimpan di Changelog
14. Klik ikon Changelog
15. Ketik Search `5-6006-{runId}`, tekan Enter
16. Verifikasi tepat satu baris Changelog dengan Action `Delete`, Account Code `5-6006-{runId}`, dan Field `Account Code`
17. Verifikasi baris itu memuat Old Value `5-6006-{runId}` dan New Value `—`
18. Klik `✕` pada modal Changelog
