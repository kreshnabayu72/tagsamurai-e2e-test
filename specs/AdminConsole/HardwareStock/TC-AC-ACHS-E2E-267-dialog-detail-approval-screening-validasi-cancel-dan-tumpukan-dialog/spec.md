---
id: TC-AC-ACHS-E2E-267-dialog-detail-approval-screening-validasi-cancel-dan-tumpukan-dialog
title: "Dialog Detail Approval: Screening, Validasi, Cancel, dan Tumpukan Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-175
  - TC-AC-ACHS-176
  - TC-AC-ACHS-177
  - TC-AC-ACHS-178
  - TC-AC-ACHS-179
  - TC-AC-ACHS-189
  - TC-AC-ACHS-582
coverage:
  web: automated
---

# Dialog Detail Approval: Screening, Validasi, Cancel, dan Tumpukan Dialog

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai hanya dibaca atau dibatalkan (dialog dibuka lalu `[Cancel]`, `[Esc]`, atau `[Leave]`; tidak ada keputusan atau penghapusan yang disimpan, sehingga Pre-setup tidak berubah, S-06): Subject pending Approvals Tab Active (Pre-setup #21, Tabel C): Register Duplicate `Fixture.hardwareStock.p17.e[28].serialNumber` (Existing Record Available, Registrant `Fixture.hardwareStock.p12.entityName`; requester `Fixture.hardwareStock.p12.entityName` Distributor), Activation Collision `Fixture.hardwareStock.p21.c[11].matchedIdentifier` (Existing Record Active, Client `Fixture.hardwareStock.p23.client[1].name`; requester `Fixture.hardwareStock.p23.client[2].name`). SKU `Fixture.hardwareStock.p16.a[4].sku` dengan unit `Fixture.hardwareStock.p17.e[12].deviceName` (Pre-setup #17).

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `distC` | #12 | Nama entitas Distributor akun #12 | `Fixture.hardwareStock.p12.entityName` |
| `dnHh (1)` | #16 (Tabel A) | Device Name SKU Handheld Reader (sama untuk `skuLong`, `skuShort`, `skuEda`) | `Fixture.hardwareStock.p16.a[1].deviceName` |
| `skuShort` | #16, #19 (Tabel A baris ke-1) | SKU Handheld Reader Range Type Short Range, Total Registered 50 (34 Available, 16 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[1].sku` |
| `dnHh (4)` | #16 (Tabel A) | Device Name SKU Handheld Reader (sama untuk `skuLong`, `skuShort`, `skuEda`) | `Fixture.hardwareStock.p16.a[4].deviceName` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `unitE12` | #17 (Tabel E baris N = 12) | Device Name unit Available pada `skuLong` | `Fixture.hardwareStock.p17.e[12].deviceName` |
| `snWfa` | #17 (Tabel E baris N = 28), #21 (Tabel C baris ke-10) | Serial Number unit `unitWfa`; sekaligus Matched Identifier Subject Register Duplicate pending (Existing Record Available, Registrant dan requester Distributor #12) | `Fixture.hardwareStock.p17.e[28].serialNumber` |
| `snD05` | milik spec | Matched Identifier Subject Register Duplicate pending milik spec yang diputuskan sesi lain (TC-582) | `SN-D05-{runId}-267` |
| `snAcTc52` | #21 (Tabel C baris ke-11) | Matched Identifier Subject Activation Collision pending pada `skuShort` (Existing Record Active Client ke-1 Pre-setup #23, requester Client ke-2) | `Fixture.hardwareStock.p21.c[11].matchedIdentifier` |
| `client1` | #23 (urutan penulisan daftar Client, butir ke-1) | Nama Client ke-1 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[1].name` |
| `client2` | #23 (urutan penulisan daftar Client, butir ke-2) | Nama Client ke-2 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[2].name` |
| `snFx1` | #27 | Serial Number unit Available ke-1 pada `skuSfr` (urutan Serial Number naik), milik Distributor #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |

- Data milik spec (S-06, S-12; suffix `{runId}-267`): Subject Register Duplicate pending `{snD05}` (dengan unit rujukannya) di-seed hook `before` lewat fixture BE (kemampuan seed disediakan tim FE/BE; jenis Subject tidak ditentukan TC, lihat Temuan untuk QA), diputuskan sesi lain pada langkah 73, dan dihapus hook `after` (idempotent). Subject Pre-setup tidak diputuskan oleh spec ini.
- Data Dinamis bersuffix: `SN-ZEBRA-RFD40-{runId}-267` (unit Sync OK pada TC-582, tidak tersimpan karena form dibatalkan; menggantikan Serial Number literal dari Tabel Data Uji Dinamis). Panjang karakter 360 dan 361 (TC-179) mengikuti TC; tidak ada nilai lain yang dipilih spec.
- Kemampuan teknis (disediakan tim BE/FE): simulator reader USB Handheld Reader (service driver mock, Pre-setup #25) untuk TC-582; sesi API pelaku kedua Total Control lain `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2, kata sandi `Spectra.env.AC_DEFAULT_USER_PASSWORD`, nama ditetapkan tim FE) yang memutuskan Subject sampai tersimpan.

## Test Steps

### TC-AC-ACHS-175: Screening Dialog Detail Approval Register Duplicate

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber`
4. Verifikasi Header: Title `Duplicate Identifier Review`
5. Verifikasi Header: Device Name (SKU) `Fixture.hardwareStock.p16.a[4].deviceName (Fixture.hardwareStock.p16.a[4].sku)`
6. Verifikasi Header: badge `Handheld Reader - Long Range`
7. Verifikasi Header: Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber`
8. Verifikasi Header: badge `Register Duplicate`
9. Verifikasi Body, Existing Record (di atas): Status `Available` (Registrant: `Fixture.hardwareStock.p12.entityName`), Registered by, Registered at
10. Verifikasi Body, New Request - Register Duplicate (di bawah): Entitas `Fixture.hardwareStock.p12.entityName (Distributor)`, Synced by, Synced at
11. Verifikasi Body: RadioGroup horizontal `Approve | Reject` tanpa pilihan awal
12. Verifikasi Body: Approval Note berupa textarea yang selalu tampil dengan placeholder `Enter approval note`
13. Verifikasi Footer: `[Cancel]` (text, contrast)
14. Verifikasi Footer: `[Submit]` (filled, success) disabled sampai radio dipilih
15. Klik `[Cancel]`

### TC-AC-ACHS-176: Screening Dialog Detail Approval Activation Collision

16. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p21.c[11].matchedIdentifier`
17. Verifikasi Header: Title `Duplicate Identifier Review`
18. Verifikasi Header: Device Name (SKU) `Fixture.hardwareStock.p16.a[1].deviceName (Fixture.hardwareStock.p16.a[1].sku)`
19. Verifikasi Header: badge `Handheld Reader - Short Range`
20. Verifikasi Header: Matched Identifier `Fixture.hardwareStock.p21.c[11].matchedIdentifier`
21. Verifikasi Header: badge `Activation Collision`
22. Verifikasi Body, Existing Record (di atas): Client `Fixture.hardwareStock.p23.client[1].name`, Subscription, Activated at
23. Verifikasi Body, New Activation (di bawah): Client `Fixture.hardwareStock.p23.client[2].name`, Subscription, Requested at
24. Verifikasi Body: RadioGroup `Approve | Reject` tanpa pilihan awal
25. Verifikasi Body: Approval Note berupa textarea
26. Verifikasi Footer: `[Cancel]` dan `[Submit]` (disabled sampai radio dipilih)
27. Klik `[Cancel]`

### TC-AC-ACHS-177: Submit disabled sampai radio dipilih

28. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber`
29. Verifikasi `[Submit]` disabled saat radio belum dipilih
30. Pilih radio `Approve` tanpa mengisi Approval Note
31. Verifikasi `[Submit]` enabled dengan `Approve` dan Approval Note kosong
32. Pilih radio `Reject`
33. Verifikasi Approval Note tetap satu field tunggal dengan nama yang sama seperti saat `Approve` dipilih

### TC-AC-ACHS-178: Reject tanpa Approval Note

34. Biarkan radio `Reject` terpilih dan Approval Note kosong
35. Klik `[Submit]`
36. Verifikasi error inline `Reason is required to reject this request`
37. Verifikasi dialog tetap terbuka
38. Klik `[Cancel]`
39. Verifikasi Subject dengan Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber` tetap pending di Tab Active

### TC-AC-ACHS-179: Approval Note maksimum 360 karakter

40. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber`
41. Pilih radio `Approve`
42. Tempel 360 karakter pada Approval Note
43. Verifikasi tidak ada error pada Approval Note dengan 360 karakter
44. Tambahkan 1 karakter (361)
45. Verifikasi error inline `Max. 360 characters` muncul langsung saat melebihi
46. Klik `[Cancel]`

### TC-AC-ACHS-189: Cancel menutup dialog tanpa commit

47. Klik row action `Review` pada Subject dengan Matched Identifier `Fixture.hardwareStock.p17.e[28].serialNumber`
48. Pilih radio `Approve` dan isi Approval Note `Catatan uji batal`
49. Klik `[Cancel]`
50. Verifikasi dialog tertutup
51. Verifikasi Subject `Fixture.hardwareStock.p17.e[28].serialNumber` tetap pending di Tab Active
52. Klik row action `Review` pada Subject yang sama
53. Verifikasi dialog yang dibuka ulang tanpa pilihan radio
54. Verifikasi Approval Note kosong
55. Klik `[Cancel]`

### TC-AC-ACHS-582: Dialog D-01, D-02, dan D-05 bertumpuk

56. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
57. Pada Tab `Available` klik `(⋯)` baris `Fixture.hardwareStock.p17.e[12].deviceName`, klik `Delete` sehingga dialog D-01 tampil
58. Tekan Esc
59. Verifikasi Esc pada D-01 setara `[Cancel]`: dialog tertutup
60. Verifikasi unit `Fixture.hardwareStock.p17.e[12].deviceName` tetap ada di Tab Available
61. Klik opsi `Add Stock` pada toolbar Tab Available
62. Sync `SN-ZEBRA-RFD40-{runId}-267` (OK) dan `Fixture.hardwareStock.p27.fx[1].serialNumber` (Waiting for Approval) lewat simulator reader USB
63. Klik `[Submit]` sehingga dialog D-02 tampil
64. Klik backdrop di luar dialog D-02
65. Verifikasi klik backdrop tidak menutup D-02 (D-02 tetap tampil)
66. Klik `[Cancel]` pada D-02
67. Klik `[Cancel]` halaman
68. Verifikasi dialog `Unsaved Changes` dengan pesan `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
69. Klik `[Leave]`
70. Buka Approvals > Hardware Stock
71. Ketik Search `{snD05}`, tekan Enter
72. Klik row action `Review` pada Subject `{snD05}`
73. `Fixture.hardwareStock.account.p02.defaultUser.fullName` memutuskan Subject `{snD05}` lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
74. Pilih radio `Approve`, klik `[Submit]` sehingga D-05 tampil di atas Detail Approval
75. Tekan Esc
76. Verifikasi Esc pada D-05 hanya menutup D-05 (lapisan teratas)
77. Verifikasi dialog Detail Approval tetap terbuka
78. Klik `[Cancel]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-175, 176, 177, 178, 179, 189, 582). Tidak ada TC hanya-BE di spec ini.
- Urutan menyimpang dari TC: TC-582 di akhir karena memutuskan Subject lewat sesi lain (mengubah baseline) dan memakai simulator USB; TC-178 melanjutkan dialog TC-177 (radio `Reject` sudah terpilih) untuk menghemat satu pembukaan dialog.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 3 (langkah 2 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 15, 27, 38, 46, 49, 55, 78 (membuka dan menutup dialog), 56, 70 (navigasi), 61 sampai 63, 66, 67, 69, 72 (aksi alur TC-582), 71 (Search untuk menemukan baris target, R-16), dan 73 (pelaku kedua lewat sesi API; "Tunggu aksi selesai", R-20).
- Spec ini 78 langkah, lebih dari sekitar 35 langkah. Alasan: seluruh blok membahas satu dialog Detail Approval dengan dataset Subject yang sama dan masing-masing berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-582 memuat simulator reader USB (kelas d) dan pelaku kedua; pelaku kedua lewat sesi API bukan konteks kedua. Penempatan TC-582 di spec fungsional mengikuti pengelompokan yang disepakati dan tidak diklaim sebagai pengecualian bernomor; lihat Temuan untuk QA.
- Pasangan judul dan severity serta pasangan tombol footer dipecah per elemen mengikuti Expected TC yang membedakan `[Cancel]` dan `[Submit]` pada langkah 13 dan 14 (Activation Collision pada langkah 26 menyebutnya dalam satu butir Footer sehingga satu `Verifikasi`).
- Post Condition TC-582 ("Subject sudah diputuskan sesi B (Tab History)") tidak punya langkah observasi di TC dan tidak diasersi; dicatat di Temuan untuk QA.
- Temuan untuk QA:
  - TC-582 menggabungkan simulator USB (kelas d), dua sesi (kelas c), dan tiga dialog; keputusan pengelompokan ke spec fungsional perlu dikonfirmasi.
  - TC-582 menyebut Subject pending `SN-ZEBRA-RFD40-000005` yang tidak ada di Tabel C Pre-setup #21 dan tidak menyebut jenisnya; spec memakai Subject Register Duplicate milik spec `{snD05}` (seed dan pembersihannya disediakan tim FE/BE).
  - TC-175 menulis Existing Record sebagai satu blok (Status, Registrant, Registered by, Registered at) tanpa nilai Registered by dan Registered at; spec mengasersi keberadaan nilai tanpa angka persis.
  - Kolom Subscription pada TC-176 tidak disebut nilainya di TC.
