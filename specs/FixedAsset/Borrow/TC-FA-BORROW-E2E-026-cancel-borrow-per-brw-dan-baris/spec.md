---
id: TC-FA-BORROW-E2E-026-cancel-borrow-per-brw-dan-baris
title: "Cancel Borrow per BRW atau per baris membatalkan baris sebelum handover dan melepas Custody aset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-BORROW-10.k1", "§9.2#r44"]
smoke: []
dependsOn: []
trace:
  "F-BORROW-10.k1": [19, 34]
  "§9.2#r44": [7, 8, 10, 11, 14, 16, 27, 29, 30, 31, 40, 42, 44, 50, 51]
anchor: [4, 24]
coverage:
  web: automated
---

# Cancel Borrow per BRW atau per baris membatalkan baris sebelum handover dan melepas Custody aset

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-026-1: BRW Group `Head Office`, Borrower `Oscar Pratama {runId}`, berisi baris aset DU-026-2 berstatus `Waiting for Approval` dan aset DU-026-3 berstatus `Waiting for Handover`.
  - DU-026-2: aset `Laptop Toshiba {runId}`.
  - DU-026-3: aset `Proyektor Optoma {runId}`.
  - DU-026-4: BRW Group `Head Office`, Borrower `Putri Maharani {runId}`, berisi baris aset DU-026-5, DU-026-6, dan DU-026-7, semuanya `Waiting for Handover`.
  - DU-026-5: aset `Kamera Panasonic {runId}`.
  - DU-026-6: aset `Lensa Canon {runId}`.
  - DU-026-7: aset `Flash Godox {runId}`.
  - DU-026-8: BRW Group `Head Office`, Borrower `Hasan Basri {runId}`, berisi baris aset DU-026-9 berstatus `Borrowed` dan aset DU-026-10 berstatus `Waiting for Handover`.
  - DU-026-9: aset `Mixer Behringer {runId}`.
  - DU-026-10: aset `Speaker Yamaha {runId}`.

## Test Steps

### Cancel Borrow per BRW membatalkan seluruh baris tanpa reason
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Oscar Pratama {runId}`, tekan Enter
4. Verifikasi baris BRW milik DU-026-1 tampil di tabel Transactions
5. Klik menu ⋯ pada baris BRW milik DU-026-1
6. Klik `Cancel Borrow`
7. Verifikasi dialog `Cancel Borrow` tampil dengan bullet BRW milik DU-026-1 dan teks `The assets become available again and the borrower and approvers are notified.` serta `Are you sure you want to cancel it?`
8. Verifikasi dialog `Cancel Borrow` tidak memuat field Reason
9. Klik `[Cancel Borrow]`
10. Verifikasi toast `Success, borrow has been canceled.` tampil
11. Verifikasi baris BRW milik DU-026-1 tidak lagi tampil di tabel Transactions
12. Klik tab `History`
13. Ketik Search `Oscar Pratama {runId}`, tekan Enter
14. Verifikasi baris BRW milik DU-026-1 tampil di tab `History` dengan status `Canceled`
15. Buka Borrow Detail BRW milik DU-026-1 dari tabel History
16. Verifikasi baris aset DU-026-2 dan DU-026-3 berstatus `Canceled`
17. Klik menu ⋯ pada baris aset DU-026-2
18. Klik `Borrow Log`
19. Verifikasi Borrow Log aset DU-026-2 memuat node `Canceled by [Actor]` dengan [Actor] berisi `Agus Pratama {runId}` tanpa Reason

### Cancel Borrow per baris hanya membatalkan baris yang dipilih
20. Klik `Transactions` pada sidebar
21. Klik `Borrow`
22. Ketik Search `Putri Maharani {runId}`, tekan Enter
23. Buka Borrow Detail BRW milik DU-026-4
24. Verifikasi tabel Assets memuat baris aset DU-026-5, DU-026-6, dan DU-026-7 berstatus `Waiting for Handover`
25. Klik menu ⋯ pada baris aset DU-026-5
26. Klik `Cancel Borrow`
27. Verifikasi dialog `Cancel Borrow` tampil dengan bullet aset DU-026-5 saja dan tanpa field Reason
28. Klik `[Cancel Borrow]`
29. Verifikasi toast `Success, borrow has been canceled.` tampil
30. Verifikasi baris aset DU-026-5 berstatus `Canceled`
31. Verifikasi baris aset DU-026-6 dan DU-026-7 tetap `Waiting for Handover`
32. Klik menu ⋯ pada baris aset DU-026-5
33. Klik `Borrow Log`
34. Verifikasi Borrow Log aset DU-026-5 memuat node `Canceled by [Actor]` dengan [Actor] berisi `Agus Pratama {runId}`

### Cancel Borrow per BRW pada BRW campuran hanya membatalkan baris yang belum Borrowed
35. Klik `Transactions` pada sidebar
36. Klik `Borrow`
37. Ketik Search `Hasan Basri {runId}`, tekan Enter
38. Klik menu ⋯ pada baris BRW milik DU-026-8
39. Klik `Cancel Borrow`
40. Verifikasi dialog `Cancel Borrow` tampil dengan bullet BRW milik DU-026-8 dan tanpa field Reason
41. Klik `[Cancel Borrow]`
42. Verifikasi toast `Success, borrow has been canceled.` tampil
43. Buka Borrow Detail BRW milik DU-026-8 dari tabel Transactions
44. Verifikasi baris aset DU-026-10 berstatus `Canceled` dan baris aset DU-026-9 tetap `Borrowed`

### Custody aset yang dibatalkan kembali Available
45. Klik `Transactions` pada sidebar
46. Klik `Borrow`
47. Klik `[+ Borrow]`
48. Klik `[+ Asset]`
49. Ketik Search `{runId}`, tekan Enter
50. Verifikasi baris aset DU-026-2, DU-026-3, dan DU-026-10 tampil di dialog Select Asset karena Custody kembali `Available` sesudah Cancel Borrow
51. Verifikasi baris aset DU-026-9 yang masih `Borrowed` tidak tampil di dialog Select Asset
