---
id: TC-FA-FACO-E2E-094-activity-log-dep-activity-log
title: "Aksi akun tercatat di Activity Log"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§8#r2", "§8.3#p1"]
smoke: []
dependsOn: ["Activity Log (FAMS): daftar Activity Log"]
trace:
  "§8#r2": [32, 33, 34, 35, 36, 37]
  "§8.3#p1": [19, 31, 32, 33, 34, 35, 36, 37, 38]
coverage:
  web: automated
---
# Aksi akun tercatat di Activity Log

## Prerequisites
- Aktor: Admin dengan role Total Control. Nama aktor tampil pada Modified By dengan format `[First Name] [Last Initial]`.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-094-1: Account Code `ACL1-{runId}`, Account Name `Activity Trail Cost {runId}`, Account Function `Asset Cost`, dibuat oleh spec ini lewat `[+ Account]`, belum pernah diekspor, Used By `0`.
  - DU-094-2: Account Name baru `Activity Trail Cost Revised {runId}`.
  - DU-094-3: Account Code baru `ACL2-{runId}`.
  - Akun DU-094-1 dengan Account Code `ACL2-{runId}` adalah satu-satunya akun milik spec ini; seluruh aksinya dilakukan oleh aktor di atas.
- Kondisi:
  - Entri Activity Log ditulis sesudah commit secara best-effort, sehingga setiap baris diamati paling lambat 30 detik sesudah aksi pemicunya selesai; data akun itu sendiri sudah tersimpan saat commit.

## Test Steps

### Akun dibuat, diubah, tanpa perubahan, dinonaktifkan, diaktifkan, dan dihapus di tab Chart of Accounts
1. Klik `[+ Account]`
2. Isi Account Code `ACL1-{runId}`
3. Isi Account Name `Activity Trail Cost {runId}`
4. Pilih `Asset Cost` pada field Account Function
5. Klik `[Submit]`
6. Ketik Search `ACL1-{runId}`, tekan Enter
7. Klik `⋯` pada baris `ACL1-{runId}`
8. Klik `Edit`
9. Ganti isi field Account Name dengan `Activity Trail Cost Revised {runId}`
10. Klik `[Save]`
11. Klik `⋯` pada baris `ACL1-{runId}`
12. Klik `Edit`
13. Ganti isi field Account Code dengan `ACL2-{runId}`
14. Klik `[Save]`
15. Ketik Search `ACL2-{runId}`, tekan Enter
16. Klik `⋯` pada baris `ACL2-{runId}`
17. Klik `Edit`
18. Klik `[Save]` tanpa mengubah nilai apa pun
19. Verifikasi toast netral `No changes to save.` tampil sebagai penanda Edit tanpa perubahan nilai yang tidak menulis baris Activity Log
20. Muat ulang halaman
21. Ketik Search `ACL2-{runId}`, tekan Enter
22. Klik switch Status pada baris `ACL2-{runId}`
23. Klik `[Deactivate]` pada dialog konfirmasi
24. Klik switch Status pada baris `ACL2-{runId}`
25. Klik `[Activate]` pada dialog konfirmasi
26. Klik `⋯` pada baris `ACL2-{runId}`
27. Klik `Delete`
28. Klik `[Delete]` pada dialog konfirmasi

### Activity Log memuat keenam kejadian untuk akun milik spec ini
29. Buka halaman Activity Log FAMS
30. Cari baris Activity Log dengan Name `ACL1-{runId}` atau `ACL2-{runId}`
31. Verifikasi kolom tabel Activity Log berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`
32. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Create`, Object `Chart of Accounts`, Name `ACL1-{runId}`, Field `Account Code`, Old Value `—`, dan New Value `ACL1-{runId}` tampil; Modified By pada baris itu adalah nama aktor
33. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Edit`, Object `Chart of Accounts`, Name `ACL1-{runId}`, Field `Account Name`, Old Value `Activity Trail Cost {runId}`, dan New Value `Activity Trail Cost Revised {runId}` tampil; Modified By pada baris itu adalah nama aktor
34. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Edit`, Object `Chart of Accounts`, Name `ACL2-{runId}`, Field `Account Code`, Old Value `ACL1-{runId}`, dan New Value `ACL2-{runId}` tampil; Modified By pada baris itu adalah nama aktor
35. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Edit`, Object `Chart of Accounts`, Name `ACL2-{runId}`, Field `Status`, Old Value `Active`, dan New Value `Inactive` tampil; Modified By pada baris itu adalah nama aktor
36. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Edit`, Object `Chart of Accounts`, Name `ACL2-{runId}`, Field `Status`, Old Value `Inactive`, dan New Value `Active` tampil; Modified By pada baris itu adalah nama aktor
37. Verifikasi paling lambat 30 detik sesudah aksinya selesai, baris Activity Log dengan Action `Delete`, Object `Chart of Accounts`, Name `ACL2-{runId}`, Field `Account Code`, Old Value `ACL2-{runId}`, dan New Value `—` tampil; Modified By pada baris itu adalah nama aktor
38. Verifikasi sesudah 30 detik sejak aksi terakhir selesai, jumlah baris dengan Name `ACL1-{runId}` atau `ACL2-{runId}` adalah 6, yaitu Edit tanpa perubahan tidak menulis baris
