---
id: TC-FA-FACO-E2E-077-kunci-akun-terekspor-dep-export-journal
title: "Akun yang pernah diekspor mengunci Account Code, Account Function, dan Delete"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [C-01, C-03, D-05, FACO-LOGIC-03a, FACO-LOGIC-04a, FACO-LOGIC-04b, FACO-LOGIC-04c, "§3.8#r4", "§4.1.1#b4", "§4.2b#r1", "§4.2b#r2", "§[F-FACO-02] Edit Account#r1", "§[F-FACO-02] Edit Account#r2", "§[F-FACO-05] Delete Account#r1", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r16", "§9.7#r30", "§9.7#r31"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  C-01: [28, 30]
  C-03: [16, 19]
  D-05: [26, 27, 28]
  FACO-LOGIC-03a: [26, 28, 30]
  FACO-LOGIC-04a: 16
  FACO-LOGIC-04b: 19
  FACO-LOGIC-04c: 22
  "§3.8#r4": 26
  "§4.1.1#b4": 27
  "§4.2b#r1": 18
  "§4.2b#r2": 21
  "§[F-FACO-02] Edit Account#r1": 16
  "§[F-FACO-02] Edit Account#r2": 19
  "§[F-FACO-05] Delete Account#r1": [26, 30]
  "§9.4.2#r5": [16, 18]
  "§9.4.2#r6": [19, 21]
  "§9.4.2#r16": [26, 28]
  "§9.7#r30": [4, 5, 16, 19]
  "§9.7#r31": [9, 26]
coverage:
  web: automated
---

# Akun yang pernah diekspor mengunci Account Code, Account Function, dan Delete

## Prerequisites
- Aktor: Admin dengan role Total Control, yang juga menjalankan Export Journal.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-077-1: Account Code `LKA1-{runId}`, Account Name `Land Improvement Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun pada bullet dialog adalah `LKA1-{runId} – Land Improvement Cost {runId}`, dari Account Code `LKA1-{runId}` dan Account Name `Land Improvement Cost {runId}`.
- Kondisi:
  - Akun DU-077-1 ikut dalam berkas Export Journal yang dijalankan di spec ini, dengan periode jurnal `M0 − 2 bulan`.

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

### Sesudah Export Journal, Account Code dan Account Function terkunci dan Account Name tetap bisa diubah
11. Export Journal untuk periode `M0 − 2 bulan` selesai dan memuat akun `LKA1-{runId}`
12. Muat ulang halaman
13. Ketik Search `LKA1-{runId}`, tekan Enter
14. Klik `⋯` pada baris `LKA1-{runId}`
15. Klik `Edit`
16. Verifikasi field Account Code Disabled
17. Arahkan kursor ke field Account Code
18. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in [Month Year]. Create a new account if needed.` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Code yang Disabled
19. Verifikasi field Account Function Disabled
20. Arahkan kursor ke field Account Function
21. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in [Month Year].` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Function yang Disabled
22. Verifikasi field Account Name tidak Disabled
23. Klik `✕` pada form Edit yang belum diubah

### Delete akun yang pernah diekspor ditolak Guard 1
24. Klik `⋯` pada baris `LKA1-{runId}`
25. Klik `Delete`
26. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `LKA1-{runId} – Land Improvement Cost {runId}`
27. Verifikasi `[Month Year]` pada kalimat pertama dialog berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`, sama dengan periode di kolom Last Used in Journal baris `LKA1-{runId}`
28. Verifikasi kalimat saran `Deactivate it instead.` tampil, karena akun masih Active dan Used By `0`
29. Klik `[OK]`
30. Verifikasi baris `LKA1-{runId}` masih tampil di tabel dengan Status `Active`
