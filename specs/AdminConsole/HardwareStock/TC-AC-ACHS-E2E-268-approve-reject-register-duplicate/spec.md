---
id: TC-AC-ACHS-E2E-268-approve-reject-register-duplicate
title: "Approve dan Reject Register Duplicate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-180
  - TC-AC-ACHS-182
  - TC-AC-ACHS-195
coverage:
  web: automated
---

# Approve dan Reject Register Duplicate

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-195): Additional Approver tanpa capability Manage hardware stock `Fixture.hardwareStock.account.p07.additionalApproverOnly.fullName` `Fixture.hardwareStock.account.p07.additionalApproverOnly.email` (Pre-setup #7, kata sandi `Spectra.env.AC_ADDITIONAL_APPROVER_ONLY_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after` (juga untuk `Fixture.hardwareStock.account.p07.additionalApproverOnly.fullName` di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup hanya dibaca: SKU `Fixture.hardwareStock.p16.a[4].sku` dan `Fixture.hardwareStock.p16.a[1].sku` (Pre-setup #16 sampai #19). Subject Pre-setup #21 tidak diputuskan oleh spec ini (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-268`): tiga Subject Register Duplicate pending beserta unit rujukannya di-seed hook `before` lewat fixture BE (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD) dan hook `after` menghapus semuanya (idempotent). Efek pada Pre-setup: hitungan Total Registered dan Available SKU `{skuLong}` dan `{skuShort}` serta isi Approvals Tab Active dan Tab History berubah selama spec berjalan; data milik spec dihapus hook `after`, sedangkan Last Updated kedua SKU berubah dan tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `skuShort` | #16, #19 (Tabel A baris ke-1) | SKU Handheld Reader Range Type Short Range, Total Registered 50 (34 Available, 16 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[1].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snRd180` | milik spec | unit Waiting for Approval pada `skuLong` sekaligus Matched Identifier Subject Register Duplicate pending (Existing Record Available, requester Distributor `Fixture.hardwareStock.p12.entityName`) untuk TC-180 | `SN-RD180-{runId}-268` |
| `snRd182` | milik spec | Matched Identifier Subject Register Duplicate pending pada `skuShort` (Existing Record Waiting for Approval) untuk TC-182 | `SN-RD182-{runId}-268` |
| `snRd195` | milik spec | Matched Identifier Subject Register Duplicate pending (Existing Record In Use, requester Distributor `Fixture.hardwareStock.p11.entityName`) untuk TC-195 | `SN-RD195-{runId}-268` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `akun additionalApproverOnlyPrincipal` | #7 | Akun Additional Approver tanpa capability Manage hardware stock | `Fixture.hardwareStock.account.p07.additionalApproverOnly.email`, `Fixture.hardwareStock.account.p07.additionalApproverOnly.fullName`, `Fixture.hardwareStock.account.p07.additionalApproverOnly.shortName` |

- Nilai baseline (Total Registered dan Available SKU `skuLong`) dibaca dari Summary bar sebelum aksi.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15; tidak ada pergeseran jam.

## Test Steps

### TC-AC-ACHS-180: Approve Register Duplicate

1. Klik row action `Detail` pada SKU `{skuLong}`
2. Catat Summary bar (Total Registered, Available) sebagai nilai awal
3. Buka Approvals > Hardware Stock
4. Klik Tab `Active`
5. Ketik Search `{snRd180}`, tekan Enter
6. Klik row action `Review` pada Subject dengan Matched Identifier `{snRd180}`
7. Pilih radio `Approve`
8. Isi Approval Note `Dokumen pengadaan sudah diperiksa`
9. Klik `[Submit]`
10. Verifikasi toast sukses `Success, duplicate has been approved.`
11. Verifikasi dialog tertutup
12. Verifikasi Tab Active di-refresh tanpa Subject `{snRd180}`
13. Buka Hardware > Stock, klik row action `Detail` pada SKU `{skuLong}`
14. Ketik Search `{snRd180}`, tekan Enter
15. Verifikasi unit `{snRd180}` berubah menjadi badge `Available`
16. Verifikasi Total Registered dan Available bertambah 1 dari nilai langkah 2
17. Buka Approvals > Hardware Stock, klik Tab `History`
18. Ketik Search `{snRd180}`, tekan Enter
19. Verifikasi baris Subject `{snRd180}` dengan Approval `Approved` (badge success)
20. Verifikasi Approver `Fixture.hardwareStock.account.p01.totalControl.shortName`
21. Verifikasi Resolved At terisi

### TC-AC-ACHS-182: Reject Register Duplicate

22. Buka Hardware > Stock, klik row action `Detail` pada SKU `{skuShort}`
23. Catat Summary bar (Total Registered) sebagai nilai awal
24. Buka Approvals > Hardware Stock
25. Klik Tab `Active`
26. Ketik Search `{snRd182}`, tekan Enter
27. Klik row action `Review` pada Subject dengan Matched Identifier `{snRd182}`
28. Pilih radio `Reject`
29. Isi Approval Note `Serial Number duplikat unit lain`
30. Klik `[Submit]`
31. Verifikasi toast sukses `Success, duplicate has been rejected.`
32. Verifikasi dialog tertutup
33. Verifikasi Subject `{snRd182}` keluar dari Tab Active
34. Buka Hardware > Stock, klik row action `Detail` pada SKU `{skuShort}`
35. Ketik Search `{snRd182}`, tekan Enter
36. Verifikasi Tab Available menampilkan empty state `No results found` (unit Rejected tidak tampil di tab manapun)
37. Verifikasi Total Registered tidak berubah dari nilai langkah 23
38. Buka Approvals > Hardware Stock, klik Tab `History`
39. Ketik Search `{snRd182}`, tekan Enter
40. Verifikasi baris Subject `{snRd182}` dengan Approval `Rejected`
41. Klik row action `Detail` pada baris itu
42. Verifikasi Approval Note berisi alasan `Serial Number duplikat unit lain`
43. Klik `[Close]`
44. Logout, lalu login sebagai `Fixture.hardwareStock.account.p07.additionalApproverOnly.fullName` (Additional Approver tanpa capability Manage hardware stock); tunggu aksi selesai

### TC-AC-ACHS-195: Additional Approver non-requester menyetujui Register Duplicate milik Distributor

45. Buka Approvals > Hardware Stock
46. Klik Tab `Active`
47. Ketik Search `{snRd195}`, tekan Enter
48. Klik row action `Review` pada Subject dengan Matched Identifier `{snRd195}`
49. Pilih radio `Approve`
50. Klik `[Submit]`
51. Verifikasi toast sukses `Success, duplicate has been approved.`
52. Klik Tab `History`
53. Ketik Search `{snRd195}`, tekan Enter
54. Verifikasi Subject `{snRd195}` pindah ke Tab History
55. Verifikasi Approver `Fixture.hardwareStock.account.p07.additionalApproverOnly.shortName`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-180, 182, 195). Tidak ada TC hanya-BE di spec ini.
- Search memakai Matched Identifier penuh milik spec (bersuffix unik, hanya satu baris yang memuatnya); tidak ada perbedaan dengan sel tabel.
- Urutan sesuai TC; ganti akun ke `Fixture.hardwareStock.account.p07.additionalApproverOnly.fullName` di akhir karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, ganti akun eksplisit). Spec ini 55 langkah, lebih dari sekitar 35 langkah; alasan: tiga TC satu topik aksi Approve dan Reject Register Duplicate, tiap TC memakai Subject milik spec sendiri, masing-masing berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 4, 13, 17, 22 sampai 25, 34, 38, 43, 45, 46, 52 (navigasi; langkah 4, 25, dan 46 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 2 dan 23 (baseline), 5, 14, 18, 26, 35, 39, 47, 53 (Search untuk menemukan baris target, R-16), 44 (ganti akun).
- Langkah 41 sampai 43 membuka Detail baris History untuk membaca Approval Note; Expected TC-182 butir e menyebut "alasan pada Approval Note" dan TC-198 menetapkan Approval Note terbaca di dialog Detail (spec 084).
- Post Condition TC-180 (kuota stok Device Allocation, notifikasi Approved ke requester, entri Activity Log `Duplicate Approved` dan Hardware Log `Hardware Approved by [PIC]`) dan Post Condition TC-182 (kuota, notifikasi Rejected, Activity Log `Duplicate Rejected`) tidak punya langkah observasi di TC dan tidak diasersi di sini; pencatatan log diuji di spec log (276, 278). Dicatat di Temuan untuk QA.
- Temuan untuk QA:
  - TC-180 mengharapkan Total Registered 26 dan Available 19; nilai ini hanya sah pada baseline Pre-setup (25 dan 18) sehingga spec membandingkan terhadap nilai awal yang dicatat.
  - TC-195 menyebut Approver `Fajar N` (format `[First Name] [Last Initial]`); spec memakai `shortName` akun Pre-setup #7. TC-195 tidak menyebut apakah akun itu melihat menu Hardware > Stock; spec hanya membuka Approvals.
  - Post Condition kuota dan notifikasi (TC-180, 182) memerlukan surface Device Allocation dan notifikasi yang tidak ditentukan langkah observasinya.
  - Seed Subject Register Duplicate dan unit rujukan milik spec serta pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
