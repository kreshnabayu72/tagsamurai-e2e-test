---
id: TC-FA-FACO-E2E-077-kunci-akun-terekspor-dep-export-journal
title: "Akun yang pernah diekspor mengunci Account Code, Account Function, dan Delete"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [C-01, C-03, D-05, FACO-LOGIC-03a, FACO-LOGIC-04a, FACO-LOGIC-04b, FACO-LOGIC-04c, "§3.8#r4", "§4.1.1#b3", "§4.2b#r1", "§4.2b#r2", "§[F-FACO-02] Edit Account#r1", "§[F-FACO-02] Edit Account#r2", "§[F-FACO-05] Delete Account#r1", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r16", "§9.7#r30", "§9.7#r31"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  C-01: [26, 28]
  C-03: [14, 17]
  D-05: [24, 25, 26]
  FACO-LOGIC-03a: [24, 26, 28]
  FACO-LOGIC-04a: 14
  FACO-LOGIC-04b: 17
  FACO-LOGIC-04c: 20
  "§3.8#r4": 24
  "§4.1.1#b3": 25
  "§4.2b#r1": 16
  "§4.2b#r2": 19
  "§[F-FACO-02] Edit Account#r1": 14
  "§[F-FACO-02] Edit Account#r2": 17
  "§[F-FACO-05] Delete Account#r1": [24, 28]
  "§9.4.2#r5": [14, 16]
  "§9.4.2#r6": [17, 19]
  "§9.4.2#r16": [24, 26]
  "§9.7#r30": [4, 5, 14, 17]
  "§9.7#r31": [9, 24]
coverage:
  web: automated
---

# Akun yang pernah diekspor mengunci Account Code, Account Function, dan Delete

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-077-1: Account Code `LKA1-{runId}`, Account Name `Land Improvement Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, bukan nilai default company, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-077-2: Account Code `LKA2-{runId}`, Account Name `Repairs Capitalization Offset {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 2 bulan` (sudah pernah diekspor), ada di entitas aktor.
  - Label akun pada bullet dialog adalah `LKA2-{runId} – Repairs Capitalization Offset {runId}`, dari Account Code `LKA2-{runId}` dan Account Name `Repairs Capitalization Offset {runId}`.

## Test Steps

### Akun yang belum diekspor belum terkunci
1. Ketik Search `LKA1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `LKA1-{runId}`
3. Klik `Edit`
4. Verifikasi field Account Code tidak Disabled
5. Verifikasi field Account Function tidak Disabled
6. Klik `✕` pada form Edit yang belum diubah
7. Klik `⋯` pada baris `LKA1-{runId}`
8. Klik `Delete`
9. Verifikasi dialog `Delete Account` tampil, yaitu Delete belum diblokir oleh akun yang pernah diekspor
10. Klik `[Cancel]`

### Akun yang pernah diekspor: Account Code dan Account Function terkunci dan Account Name tetap bisa diubah
11. Ganti isi kotak search dengan `LKA2-{runId}`, tekan Enter
12. Klik `⋯` pada baris `LKA2-{runId}`
13. Klik `Edit`
14. Verifikasi field Account Code Disabled
15. Arahkan kursor ke field Account Code
16. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in [Month Year]. Create a new account if needed.` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Code yang Disabled
17. Verifikasi field Account Function Disabled
18. Arahkan kursor ke field Account Function
19. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in [Month Year].` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Function yang Disabled
20. Verifikasi field Account Name tidak Disabled
21. Klik `✕` pada form Edit yang belum diubah

### Delete akun yang pernah diekspor ditolak Guard 1
22. Klik `⋯` pada baris `LKA2-{runId}`
23. Klik `Delete`
24. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `LKA2-{runId} – Repairs Capitalization Offset {runId}`
25. Verifikasi `[Month Year]` pada kalimat pertama dialog berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`, sama dengan periode di kolom Last Used in Journal baris `LKA2-{runId}`
26. Verifikasi kalimat saran `Deactivate it instead.` tampil, karena akun masih Active dan Used By `0`
27. Klik `[OK]`
28. Verifikasi baris `LKA2-{runId}` masih tampil di tabel dengan Status `Active`
