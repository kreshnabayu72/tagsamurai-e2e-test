---
id: TC-FA-FACO-E2E-090-konsumen-tab-accounts-dep-custom-asset-id
title: "Akun tercermin di tab Accounts Custom Asset ID"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.3#p2", "§9.7#p4", "§9.11#p1", "§11.1#r3", "EB-XM-2@custom-asset-id"]
smoke: []
dependsOn: ["Settings > Custom Asset ID: tab Accounts"]
trace:
  "§9.3#p2": [6, 7]
  "§9.7#p4": [27, 28]
  "§9.11#p1": [7, 17]
  "§11.1#r3": 27
  "EB-XM-2@custom-asset-id": [17, 27, 28, 38, 39, 49]
anchor: [2, 48]
coverage:
  web: automated
---
# Akun tercermin di tab Accounts Custom Asset ID

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-090-1: Account Code `CAI1-{runId}`, Account Name `Pipeline Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, belum pernah diekspor, ada di entitas aktor.
  - DU-090-2: Account Code `CAI2-{runId}`, Account Name `Conduit Cost {runId}`, Account Function `Asset Cost`, dibuat oleh spec ini lewat `[+ Account]`.
  - DU-090-3: Account Code baru `CAI1R-{runId}` untuk DU-090-1.
  - DU-090-4: Account Name baru `Conduit Cost Revised {runId}` untuk DU-090-2.
  - Keempat data DU-090-1 sampai DU-090-4 adalah seluruh akun milik spec ini.

## Test Steps

### Tab Accounts di Custom Asset ID hanya menampilkan Account Name dan Account Code dengan himpunan akun yang sama
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `CAI1-{runId}` tampil dengan Account Name `Pipeline Cost {runId}`
3. Buka Settings > Custom Asset ID
4. Klik tab `Accounts`
5. Cari akun dengan Account Code `CAI1-{runId}` di daftar tab `Accounts`
6. Verifikasi daftar akun di tab `Accounts` hanya memuat kolom `Account Name` dan `Account Code`, tanpa kolom `Account Function`, `Status`, `Used By`, atau `Last Used in Journal`
7. Verifikasi akun `CAI1-{runId}` tampil di tab `Accounts` dengan Account Name `Pipeline Cost {runId}` dan Account Code `CAI1-{runId}`, sama persis dengan baris di Chart of Accounts dan tanpa nilai yang di-mask

### Akun yang dibuat muncul di tab Accounts Custom Asset ID
8. Buka Settings > Accounting > Chart of Accounts
9. Klik `[+ Account]`
10. Isi Account Code `CAI2-{runId}`
11. Isi Account Name `Conduit Cost {runId}`
12. Pilih `Asset Cost` pada field Account Function
13. Klik `[Submit]`
14. Buka Settings > Custom Asset ID
15. Klik tab `Accounts`
16. Cari akun dengan Account Code `CAI2-{runId}` di daftar tab `Accounts`
17. Verifikasi akun `CAI2-{runId}` tampil di tab `Accounts` dengan Account Name `Conduit Cost {runId}`

### Account Code yang diubah langsung tampil di tab Accounts Custom Asset ID
18. Buka Settings > Accounting > Chart of Accounts
19. Ketik Search `CAI1-{runId}`, tekan Enter
20. Klik `⋯` pada baris `CAI1-{runId}`
21. Klik `Edit`
22. Ganti isi field Account Code dengan `CAI1R-{runId}`
23. Klik `[Save]`
24. Buka Settings > Custom Asset ID
25. Klik tab `Accounts`
26. Cari akun dengan Account Name `Pipeline Cost {runId}` di daftar tab `Accounts`
27. Verifikasi akun `Pipeline Cost {runId}` tampil di tab `Accounts` dengan Account Code `CAI1R-{runId}`
28. Verifikasi Account Code `CAI1-{runId}` tidak tampil lagi di tab `Accounts`

### Account Name yang diubah tercermin di tab Accounts Custom Asset ID
29. Buka Settings > Accounting > Chart of Accounts
30. Ketik Search `CAI2-{runId}`, tekan Enter
31. Klik `⋯` pada baris `CAI2-{runId}`
32. Klik `Edit`
33. Ganti isi field Account Name dengan `Conduit Cost Revised {runId}`
34. Klik `[Save]`
35. Buka Settings > Custom Asset ID
36. Klik tab `Accounts`
37. Cari akun dengan Account Code `CAI2-{runId}` di daftar tab `Accounts`
38. Verifikasi akun `CAI2-{runId}` tampil di tab `Accounts` dengan Account Name `Conduit Cost Revised {runId}`
39. Verifikasi Account Name `Conduit Cost {runId}` tidak tampil lagi di tab `Accounts`

### Akun yang dihapus hilang dari tab Accounts Custom Asset ID
40. Buka Settings > Accounting > Chart of Accounts
41. Ketik Search `CAI2-{runId}`, tekan Enter
42. Klik `⋯` pada baris `CAI2-{runId}`
43. Klik `Delete`
44. Klik `[Delete]` pada dialog konfirmasi
45. Buka Settings > Custom Asset ID
46. Klik tab `Accounts`
47. Cari akun dengan Account Code `CAI1R-{runId}` di daftar tab `Accounts`
48. Verifikasi akun `CAI1R-{runId}` tampil di tab `Accounts`
49. Verifikasi akun `CAI2-{runId}` tidak tampil di tab `Accounts`
