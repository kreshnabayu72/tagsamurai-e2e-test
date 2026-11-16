---
id: TC-FA-FACO-E2E-030-akun-dihapus-pihak-lain
title: "Aksi atas akun yang sudah dihapus pengguna lain menampilkan toast netral"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§7.3#b4", "§[F-FACO-05] Delete Account#r8", "§[F-FACO-05] Delete Account#r9", "§9.4.2#r19", "§[F-FACO-02] Edit Account#r7", "§9.4.2#r41", "EB-ERR-3", "T-12"]
smoke: ["EB-ERR-3", "T-12"]
dependsOn: []
trace:
  "§7.3#b4": [9, 16, 23, 31]
  "§[F-FACO-05] Delete Account#r8": [8, 15, 22, 30]
  "§[F-FACO-05] Delete Account#r9": [9, 16, 23, 31]
  "§9.4.2#r19": [30, 31]
  "§[F-FACO-02] Edit Account#r7": [8, 9, 15, 16, 22, 23]
  "§9.4.2#r41": [8, 9, 15, 16, 22, 23]
  "EB-ERR-3": 30
  "T-12": [8, 15, 22, 30]
anchor: [2, 11, 18, 25]
coverage:
  web: automated
---

# Aksi atas akun yang sudah dihapus pengguna lain menampilkan toast netral

## Prerequisites
- Aktor: Total Control. Aktor lain yang memicu penghapusan: Admin B, Total Control, seluruh client.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-030-1: akun Active dengan Account Code `5-6008-{runId}`, Account Name `Depreciation Expense Gudang Timur {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; sasaran Save Edit.
  - DU-030-2: akun Inactive dengan Account Code `4-7003-{runId}`, Account Name `Gain on Disposal Cabang Timur {runId}`, Account Function `Gain on Disposal`, Used By `0`, Last Used in Journal `—`; sasaran Activate.
  - DU-030-3: akun Active dengan Account Code `5-6009-{runId}`, Account Name `Depreciation Expense Showroom {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; sasaran Deactivate.
  - DU-030-4: akun Active dengan Account Code `5-6010-{runId}`, Account Name `Depreciation Expense Kantor Timur {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; sasaran Delete.

## Test Steps

### Save Edit atas akun yang sudah dihapus pengguna lain
1. Ketik Search `5-6008-{runId}`, tekan Enter
2. Verifikasi baris `5-6008-{runId}` tampil pada tabel
3. Klik `⋯` pada baris `5-6008-{runId}`
4. Klik `Edit`
5. Ganti isi Account Name dengan `Depreciation Expense Gudang Timur Baru {runId}`
6. Admin B menghapus akun `5-6008-{runId}`
7. Klik `[Save]`
8. Verifikasi toast `This account is no longer available.` tampil
9. Verifikasi baris `5-6008-{runId}` tidak tampil, dengan empty state `No results found` pada tabel

### Activate atas akun yang sudah dihapus pengguna lain
10. Ganti isi kotak search dengan `4-7003-{runId}`, tekan Enter
11. Verifikasi baris `4-7003-{runId}` tampil dengan Switch Status berstatus Inactive
12. Klik Switch Status pada baris `4-7003-{runId}`
13. Admin B menghapus akun `4-7003-{runId}`
14. Klik `[Activate]`
15. Verifikasi toast `This account is no longer available.` tampil
16. Verifikasi baris `4-7003-{runId}` tidak tampil, dengan empty state `No results found` pada tabel

### Deactivate atas akun yang sudah dihapus pengguna lain
17. Ganti isi kotak search dengan `5-6009-{runId}`, tekan Enter
18. Verifikasi baris `5-6009-{runId}` tampil dengan Switch Status berstatus Active
19. Klik Switch Status pada baris `5-6009-{runId}`
20. Admin B menghapus akun `5-6009-{runId}`
21. Klik `[Deactivate]`
22. Verifikasi toast `This account is no longer available.` tampil
23. Verifikasi baris `5-6009-{runId}` tidak tampil, dengan empty state `No results found` pada tabel

### Delete atas akun yang sudah dihapus pengguna lain
24. Ganti isi kotak search dengan `5-6010-{runId}`, tekan Enter
25. Verifikasi baris `5-6010-{runId}` tampil pada tabel
26. Klik `⋯` pada baris `5-6010-{runId}`
27. Klik `Delete`
28. Admin B menghapus akun `5-6010-{runId}`
29. Klik `[Delete]`
30. Verifikasi toast `This account is no longer available.` tampil
31. Verifikasi baris `5-6010-{runId}` tidak tampil, dengan empty state `No results found` pada tabel
