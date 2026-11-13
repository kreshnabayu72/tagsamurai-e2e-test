---
id: TC-FA-FAREG-E2E-078-registration-log-pengajuan
title: "Registration Log pengajuan: Submitted, keputusan, dan Canceled"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.3#p1", "§8.3#r3", "§8.3#r4", "§8.3#r5"]
smoke: []
dependsOn: []
trace:
  "§8.3#p1": 6
  "§8.3#r3": [3, 4, 5, 35, 36, 37]
  "§8.3#r4": [11, 12, 15, 16, 17, 18, 21, 22, 42, 45]
  "§8.3#r5": [25, 26, 29, 30]
anchor: []
coverage:
  web: automated
---
# Registration Log pengajuan: Submitted, keputusan, dan Canceled

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, pengaju seluruh pengajuan di bawah). Budi S (Manage asset & TAG dengan capability Update) adalah approver yang memutuskan pengajuan Approved, Partially Approved, dan Rejected.
- Layar awal: Fixed Asset > Assets > Registration > Waiting for Approval.
- Data:
  - DU-078-1: pengajuan Waiting for Approval di Group `Gudang Diajukan {runId}`, Total Asset `2`, diajukan Rina W; satu aset di-submit tanpa pairing TAG dengan Reason `TAG not yet available`; batch Draft asalnya dibuat Rina W.
  - DU-078-2: pengajuan Approved di Group `Gudang Disetujui {runId}`, Total Asset `2`, diputuskan Budi S: kedua aset `Approve`; aset ke-1 dengan Reason `Verified on site`.
  - DU-078-3: pengajuan Partially Approved di Group `Gudang Sebagian {runId}`, Total Asset `3`, diputuskan Budi S: aset ke-1 `Approve` dengan Reason `Checked by supervisor`; aset ke-2 `Return to Draft` dengan Reason `Photo is missing`; aset ke-3 `Reject` dengan Reason `Duplicate entry`.
  - DU-078-4: pengajuan Rejected di Group `Gudang Ditolak {runId}`, Total Asset `2`, diputuskan Budi S: kedua aset `Reject` dengan Reason `Asset does not exist`.
  - DU-078-5: pengajuan Canceled di Group `Gudang Batal Draft {runId}`, Total Asset `2`, dibatalkan Rina W dengan `Save as Draft to edit` tercentang.
  - DU-078-6: pengajuan Canceled di Group `Gudang Batal Buang {runId}`, Total Asset `2`, dibatalkan Rina W dengan `Save as Draft to edit` tidak tercentang.
  - DU-078-7: Budi S (Manage asset & TAG dengan capability Update), approver yang memutuskan DU-078-2 sampai DU-078-4.
  - DU-078-8: pengajuan Waiting for Approval di Group `Gudang Sebagian {runId}`, Total Asset `1`, diajukan Rina W sebagai Submit ulang batch Draft kembalian dari pengajuan DU-078-3, sehingga `Resubmitted from` memuat Registration ID milik DU-078-3; satu aset di-submit tanpa pairing TAG dengan Reason `Other` dan catatan `Reader sedang diperbaiki vendor`.
  - Baris log yang diharapkan `Submitted without TAG pairing: 1 — TAG not yet available`, dari Asset Count `1` dan Reason `TAG not yet available`.
  - Baris log yang diharapkan `Submitted without TAG pairing: 1 — Other`, dari Asset Count `1` dan Reason `Other`.
  - Node Registration Log yang diharapkan: `Submitted by Rina W.`, `Approved by Budi S.`, `Partially approved by Budi S.`, `Rejected by Budi S.`, dan `Canceled by Rina W.`, dari pengaju Rina W dan approver Budi S; nama singkat tampil `Rina W.` dan `Budi S.`.

## Test Steps

### Pengajuan Waiting for Approval mencatat Submitted dan peristiwa Draft tetap tampil
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Registration Log` pada baris Group `Gudang Diajukan {runId}`
3. Verifikasi node timeline berjudul `Submitted by Rina W.`[^drift-1]
4. Verifikasi Total Asset pada node `Submitted by Rina W.` bernilai `2`[^drift-1]
5. Verifikasi node itu memuat baris `Submitted without TAG pairing: 1 — TAG not yet available`
6. Verifikasi node timeline berjudul `Draft created by Rina W.` tetap tampil sesudah batch di-Submit[^drift-1]
7. Klik ikon `✕` pada dialog Registration Log

### Keputusan approver mencatat Approved, Partially approved, dan Rejected
8. Klik sub tab `History`
9. Ketik Search `{runId}`, tekan Enter
10. Klik ikon `Registration Log` pada baris Group `Gudang Disetujui {runId}`
11. Verifikasi node timeline berjudul `Approved by Budi S.`[^drift-1]
12. Verifikasi node itu memuat Jumlah Approved `2`
13. Klik ikon `✕` pada dialog Registration Log
14. Klik ikon `Registration Log` pada baris Group `Gudang Sebagian {runId}`
15. Verifikasi node timeline berjudul `Partially approved by Budi S.`[^drift-1]
16. Verifikasi node itu memuat Jumlah Approved `1`, Returned `1`, dan Rejected `1`
17. Verifikasi node itu memuat Reason `Photo is missing` untuk aset yang dikembalikan
18. Verifikasi node itu memuat Reason `Duplicate entry` untuk aset yang ditolak
19. Klik ikon `✕` pada dialog Registration Log
20. Klik ikon `Registration Log` pada baris Group `Gudang Ditolak {runId}`
21. Verifikasi node timeline berjudul `Rejected by Budi S.`[^drift-1]
22. Verifikasi node itu memuat Jumlah Rejected `2` dan Reason `Asset does not exist`
23. Klik ikon `✕` pada dialog Registration Log

### Pembatalan mencatat Canceled beserta dampaknya pada aset
24. Klik ikon `Registration Log` pada baris Group `Gudang Batal Draft {runId}`
25. Verifikasi node timeline berjudul `Canceled by Rina W.`[^drift-1]
26. Verifikasi node itu memuat Dampak `Assets: Returned to Draft`
27. Klik ikon `✕` pada dialog Registration Log
28. Klik ikon `Registration Log` pada baris Group `Gudang Batal Buang {runId}`
29. Verifikasi node timeline berjudul `Canceled by Rina W.`[^drift-1]
30. Verifikasi node itu memuat Dampak `Assets: Discarded`

### Pengajuan hasil Submit ulang mencatat Resubmitted from dan skip pairing Other
31. Klik ikon `✕` pada dialog Registration Log
32. Klik sub tab `Waiting for Approval`
33. Ketik Search `{runId}`, tekan Enter
34. Klik ikon `Registration Log` pada baris Group `Gudang Sebagian {runId}`
35. Verifikasi node timeline berjudul `Submitted by Rina W.` memuat `Resubmitted from` berisi Registration ID pengajuan DU-078-3[^drift-1]
36. Verifikasi node itu memuat baris `Submitted without TAG pairing: 1 — Other`
37. Verifikasi node itu memuat catatan `Reader sedang diperbaiki vendor`
38. Klik ikon `✕` pada dialog Registration Log

### Node keputusan memuat Reason aset yang di-approve
39. Klik sub tab `History`
40. Ketik Search `{runId}`, tekan Enter
41. Klik ikon `Registration Log` pada baris Group `Gudang Disetujui {runId}`
42. Verifikasi node `Approved by Budi S.` memuat Reason `Verified on site` untuk aset yang di-approve[^drift-1]
43. Klik ikon `✕` pada dialog Registration Log
44. Klik ikon `Registration Log` pada baris Group `Gudang Sebagian {runId}`
45. Verifikasi node `Partially approved by Budi S.` memuat Reason `Checked by supervisor` untuk aset yang di-approve[^drift-1]

[^drift-1]: Drift PRD vs override. PRD §8.3 node log `Submitted by [User]`, `Approved by [User]`, `Partially approved by [User]`, `Rejected by [User]`, `Canceled by [User]`, dan `Draft created by [User]` memakai nama singkat pengguna; `prd-conventions.md` §9.13: `[First Name] [Last Initial]` (contoh tanpa titik: `John L`). Baris O-4: nama singkat mengakhiri inisial dengan titik (`John L.`). Diasersi: override O-4 (SB-6), sehingga nama singkat `Rina W.` dan `Budi S.`.
