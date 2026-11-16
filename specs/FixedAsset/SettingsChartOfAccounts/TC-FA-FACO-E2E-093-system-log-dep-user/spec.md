---
id: TC-FA-FACO-E2E-093-system-log-dep-user
title: "Aksi akun tercatat di System Log pengguna aktor"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8#r2", "§8.2#p1", "§8.2#r1"]
smoke: []
dependsOn: ["Global Settings > User: Detail User > Tab System Log"]
trace:
  "§8#r2": [33, 34, 35, 36, 37, 38]
  "§8.2#p1": [19, 32, 33, 34, 35, 36, 37, 38, 39]
  "§8.2#r1": [33, 34, 35, 36, 37, 38]
coverage:
  web: automated
---
# Aksi akun tercatat di System Log pengguna aktor

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-093-1: Account Code `SYL1-{runId}`, Account Name `Audit Trail Cost {runId}`, Account Function `Asset Cost`, dibuat oleh spec ini lewat `[+ Account]`, belum pernah diekspor, Used By `0`.
  - DU-093-2: Account Name baru `Audit Trail Cost Revised {runId}`.
  - DU-093-3: Account Code baru `SYL2-{runId}`.
  - Akun DU-093-1 dengan Account Code `SYL2-{runId}` adalah satu-satunya akun milik spec ini; seluruh aksinya dilakukan oleh aktor di atas.
- Kondisi:
  - Entri System Log ditulis sesudah commit secara best-effort, sehingga pengamatan setiap baris menunggu sampai baris itu tertulis; data akun itu sendiri sudah tersimpan saat commit.

## Test Steps

### Akun dibuat, diubah, tanpa perubahan, dinonaktifkan, diaktifkan, dan dihapus di tab Chart of Accounts
1. Klik `[+ Account]`
2. Isi Account Code `SYL1-{runId}`
3. Isi Account Name `Audit Trail Cost {runId}`
4. Pilih `Asset Cost` pada field Account Function
5. Klik `[Submit]`
6. Ketik Search `SYL1-{runId}`, tekan Enter
7. Klik `⋯` pada baris `SYL1-{runId}`
8. Klik `Edit`
9. Ganti isi field Account Name dengan `Audit Trail Cost Revised {runId}`
10. Klik `[Save]`
11. Klik `⋯` pada baris `SYL1-{runId}`
12. Klik `Edit`
13. Ganti isi field Account Code dengan `SYL2-{runId}`
14. Klik `[Save]`
15. Ketik Search `SYL2-{runId}`, tekan Enter
16. Klik `⋯` pada baris `SYL2-{runId}`
17. Klik `Edit`
18. Klik `[Save]` tanpa mengubah nilai apa pun
19. Verifikasi toast netral `No changes to save.` tampil sebagai penanda Edit tanpa perubahan nilai yang tidak menulis baris System Log
20. Muat ulang halaman
21. Ketik Search `SYL2-{runId}`, tekan Enter
22. Klik switch Status pada baris `SYL2-{runId}`
23. Klik `[Deactivate]` pada dialog konfirmasi
24. Klik switch Status pada baris `SYL2-{runId}`
25. Klik `[Activate]` pada dialog konfirmasi
26. Klik `⋯` pada baris `SYL2-{runId}`
27. Klik `Delete`
28. Klik `[Delete]` pada dialog konfirmasi

### System Log memuat keenam kejadian untuk akun milik spec ini
29. Buka Global Settings > User
30. Buka Detail User milik aktor
31. Klik tab `System Log`
32. Verifikasi kolom tabel System Log berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`
33. Verifikasi baris System Log dengan Action `Create`, Object `Chart of Accounts`, Name `SYL1-{runId}`, Field `Account Code`, Old Value `—`, dan New Value `SYL1-{runId}` tampil
34. Verifikasi baris System Log dengan Action `Edit`, Object `Chart of Accounts`, Name `SYL1-{runId}`, Field `Account Name`, Old Value `Audit Trail Cost {runId}`, dan New Value `Audit Trail Cost Revised {runId}` tampil
35. Verifikasi baris System Log dengan Action `Edit`, Object `Chart of Accounts`, Name `SYL2-{runId}`, Field `Account Code`, Old Value `SYL1-{runId}`, dan New Value `SYL2-{runId}` tampil
36. Verifikasi baris System Log dengan Action `Edit`, Object `Chart of Accounts`, Name `SYL2-{runId}`, Field `Status`, Old Value `Active`, dan New Value `Inactive` tampil
37. Verifikasi baris System Log dengan Action `Edit`, Object `Chart of Accounts`, Name `SYL2-{runId}`, Field `Status`, Old Value `Inactive`, dan New Value `Active` tampil
38. Verifikasi baris System Log dengan Action `Delete`, Object `Chart of Accounts`, Name `SYL2-{runId}`, Field `Account Code`, Old Value `SYL2-{runId}`, dan New Value `—` tampil
39. Verifikasi sesudah keenam baris tampil, jumlah baris dengan Name `SYL1-{runId}` atau `SYL2-{runId}` adalah 6, yaitu Edit tanpa perubahan tidak menulis baris
