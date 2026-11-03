---
id: TC-AC-ACHS-E2E-273-resilience-tulis-add-stock-delete-approve-reject
title: "Resilience Tulis: Add Stock, Delete, Approve, dan Reject"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-101
  - TC-AC-ACHS-102
  - TC-AC-ACHS-149
  - TC-AC-ACHS-150
  - TC-AC-ACHS-164
  - TC-AC-ACHS-185
  - TC-AC-ACHS-186
  - TC-AC-ACHS-187
  - TC-AC-ACHS-188
coverage:
  web: automated
---

# Resilience Tulis: Add Stock, Delete, Approve, dan Reject

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada respons tulis; asersi state server lewat kemampuan baca disediakan tim BE/FE).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-150): Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName` `Fixture.hardwareStock.account.p04.createOnly.email` (Pre-setup #4, `Spectra.env.AC_CREATE_ONLY_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after` (juga untuk `Fixture.hardwareStock.account.p04.createOnly.fullName` di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` untuk memaksa respons HTTP 500 pada request Submit Add Stock, Submit Sync, Delete, dan keputusan Approval, dan untuk meneruskan request lalu membuang respons (TC-102 dan TC-150); melepas intercept segera setelah asersi tiap blok (S-09); hook `after` melepas intercept yang tersisa. Simulator reader USB Handheld Reader (service driver mock, Pre-setup #25) untuk TC-149 dan TC-150.
- Kemampuan baca state server (disediakan tim BE/FE, tanpa endpoint di spec): jumlah unit per Serial Number, jumlah Subject pending, dan jumlah notifikasi ke approver sebelum dan sesudah aksi.
- Data Pre-setup hanya dibaca: SKU `Fixture.hardwareStock.p16.a[3].sku` (Pre-setup #16, #27) dan SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #16 sampai #18). Spec tidak mengubah atau menghapus unit dan Subject Pre-setup (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-273`): unit Available `SN-DEL164-{runId}-273` pada `skuLong` (target Delete TC-164), unit Available `SN-MATCH149-{runId}-273` dan `SN-MATCH150-{runId}-273` pada `skuSfr` (unit yang cocok pada Sync TC-149 dan TC-150), dan empat Subject pending pada tabel di bawah di-seed hook `before` lewat fixture BE (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Data Dinamis yang dibuat langkah: `SN-FAIL-0001-{runId}-273` (TC-101), `SN-IDEM-0001-{runId}-273` (TC-102), `SN-ZEBRA-RFD40-{runId}-273` (unit Sync OK TC-149, tidak tersimpan), serta unit Waiting for Approval dan Subject pending hasil Sync `SN-MATCH150-{runId}-273` (TC-150). Hook `after` menghapus semua data bersuffix `-273` yang masih ada (idempotent, juga bila spec gagal di tengah). Efek pada Pre-setup: hitungan unit SKU `skuSfr` dan `skuLong` serta isi Approvals Tab Active berubah selama spec berjalan; hitungan dipulihkan hook `after`, Last Updated SKU tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snDel164` | milik spec | unit Available pada `skuLong` yang gagal dihapus (TC-164) | `SN-DEL164-{runId}-273` |
| `snMatch149` | milik spec | unit Available pada `skuSfr` yang cocok dengan Serial Number Sync TC-149 | `SN-MATCH149-{runId}-273` |
| `snMatch150` | milik spec | unit Available pada `skuSfr` yang cocok dengan Serial Number Sync TC-150 | `SN-MATCH150-{runId}-273` |
| `snFd185` | milik spec | Matched Identifier Subject Register Duplicate pending untuk TC-185 | `SN-FD185-{runId}-273` |
| `snFd186` | milik spec | Matched Identifier Subject Register Duplicate pending untuk TC-186 | `SN-FD186-{runId}-273` |
| `snFd187` | milik spec | Matched Identifier Subject Activation Collision pending untuk TC-187 | `SN-FD187-{runId}-273` |
| `snFd188` | milik spec | Matched Identifier Subject Activation Collision pending untuk TC-188 | `SN-FD188-{runId}-273` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun createOnlyPrincipal` | #4 | Akun Principal Create-Only | `Fixture.hardwareStock.account.p04.createOnly.email`, `Fixture.hardwareStock.account.p04.createOnly.fullName` |

Tabel keputusan gagal tanpa Approval Note (langkah 47 sampai 55):

| TC | Matched Identifier | Jenis | Keputusan | Toast error |
|---|---|---|---|---|
| TC-185 | `{snFd185}` | Register Duplicate | `Approve` | `Error, failed to approve duplicate.` |
| TC-187 | `{snFd187}` | Activation Collision | `Approve` | `Error, failed to approve activation.` |

Tabel keputusan gagal dengan Approval Note (langkah 56 sampai 65):

| TC | Matched Identifier | Jenis | Keputusan | Approval Note | Toast error |
|---|---|---|---|---|---|
| TC-186 | `{snFd186}` | Register Duplicate | `Reject` | `Alasan uji` | `Error, failed to reject duplicate.` |
| TC-188 | `{snFd188}` | Activation Collision | `Reject` | `Alasan uji` | `Error, failed to reject activation.` |

## Test Steps

### TC-AC-ACHS-101: Submit manual gagal 5xx lalu retry

1. Klik `(⋯)` pada baris SKU `{skuSfr}`
2. Klik opsi `Add Stock`
3. Ketik `SN-FAIL-0001-{runId}-273`
4. Pasang intercept respons Submit Add Stock dengan status 500
5. Klik `[Submit]`
6. Verifikasi toast error `Error, failed to add stock.`
7. Verifikasi form tetap terbuka
8. Verifikasi textarea masih berisi `SN-FAIL-0001-{runId}-273`
9. Verifikasi `[Submit]` aktif kembali
10. Verifikasi tidak ada unit `SN-FAIL-0001-{runId}-273` tersimpan (kemampuan baca state server)
11. Lepas intercept
12. Klik `[Submit]` lagi
13. Verifikasi toast sukses `Success, unit has been added to stock.`

### TC-AC-ACHS-102: Respons terputus setelah commit, submit ulang manual

14. Buka Hardware > Stock
15. Klik `(⋯)` pada baris SKU `{skuSfr}`, klik opsi `Add Stock`
16. Ketik `SN-IDEM-0001-{runId}-273`
17. Pasang intercept yang meneruskan request Submit ke server lalu membuang respons
18. Klik `[Submit]`
19. Setelah error jaringan, lepas intercept lalu klik `[Submit]` lagi
20. Verifikasi FE memeriksa status transaksi dengan ID transaksi sementara sebelum mengizinkan submit ulang (request pemeriksaan status transaksi teramati sebelum request submit kedua)
21. Verifikasi hanya satu unit `SN-IDEM-0001-{runId}-273` tersimpan (kemampuan baca state server)
22. Verifikasi hasil percobaan pertama dikembalikan tanpa duplikasi: Stock Detail SKU `{skuSfr}` Tab Available memuat satu baris `SN-IDEM-0001-{runId}-273`

### TC-AC-ACHS-149: Submit Sync gagal 5xx

23. Buka Hardware > Stock, klik `(⋯)` pada baris SKU `{skuLong}`, klik opsi `Add Stock`
24. Sync `SN-ZEBRA-RFD40-{runId}-273` (OK) dan `{snMatch149}` (match) lewat simulator reader USB
25. Catat jumlah unit, Subject pending, dan notifikasi approver terkait kedua Serial Number (kemampuan baca state server)
26. Pasang intercept respons Submit Sync dengan status 500
27. Klik `[Submit]`, lalu klik `[Continue]`
28. Verifikasi toast error `Error, failed to add stock.`
29. Verifikasi tidak ada unit, Subject, maupun notifikasi tersimpan: sama dengan nilai langkah 25 (atomik penuh)
30. Verifikasi Tabel Synced Units tetap berisi dua baris
31. Verifikasi `[Submit]` aktif kembali
32. Lepas intercept
33. Klik `[Cancel]` halaman
34. Verifikasi dialog `Unsaved Changes` dengan pesan `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
35. Klik `[Leave]`

### TC-AC-ACHS-164: Delete gagal server

36. Klik row action `Detail` pada SKU `{skuLong}`
37. Catat Summary bar (Total Registered)
38. Ketik Search `{snDel164}`, tekan Enter
39. Pasang intercept respons Delete dengan status 500
40. Klik `(⋯)` pada baris `{snDel164}`, klik `Delete`, lalu klik `[Delete]`
41. Verifikasi toast error `Error, failed to delete unit.`
42. Verifikasi unit `{snDel164}` tetap di tabel
43. Verifikasi Total Registered tidak berubah dari nilai langkah 37
44. Lepas intercept

### TC-AC-ACHS-185 dan TC-AC-ACHS-187: Keputusan Approve gagal server

45. Buka Approvals > Hardware Stock
46. Klik Tab `Active`

Untuk setiap baris tabel keputusan gagal tanpa Approval Note (TC-185, TC-187), lakukan langkah 47 sampai 55:

47. Ketik Search Matched Identifier pada baris tabel, tekan Enter
48. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
49. Pasang intercept respons keputusan Approval dengan status 500
50. Pilih radio `Approve`
51. Klik `[Submit]`
52. Verifikasi toast error sesuai kolom Toast error
53. Verifikasi dialog tetap terbuka dan Subject tetap pending: radio dan `[Submit]` tetap aktif
54. Lepas intercept, lalu klik `[Cancel]`
55. Klik `(←)` pada kotak Search

### TC-AC-ACHS-186 dan TC-AC-ACHS-188: Keputusan Reject gagal server

Untuk setiap baris tabel keputusan gagal dengan Approval Note (TC-186, TC-188), lakukan langkah 56 sampai 65:

56. Ketik Search Matched Identifier pada baris tabel, tekan Enter
57. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
58. Pasang intercept respons keputusan Approval dengan status 500
59. Pilih radio `Reject`
60. Isi Approval Note `Alasan uji`
61. Klik `[Submit]`
62. Verifikasi toast error sesuai kolom Toast error
63. Verifikasi dialog tetap terbuka dan Subject tetap pending: radio dan `[Submit]` tetap aktif
64. Lepas intercept, lalu klik `[Cancel]`
65. Klik `(←)` pada kotak Search

### TC-AC-ACHS-150: Retry Submit Sync tanpa duplikasi

66. Logout, lalu login sebagai Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName`; tunggu aksi selesai
67. Buka Hardware > Stock, klik `(⋯)` pada baris SKU `{skuLong}`, klik opsi `Add Stock`
68. Sync `{snMatch150}` (match) lewat simulator reader USB
69. Catat jumlah unit, Subject pending, dan notifikasi approver terkait `{snMatch150}` (kemampuan baca state server)
70. Pasang intercept yang meneruskan request Submit ke server lalu membuang respons
71. Klik `[Submit]`, lalu klik `[Send]`
72. Lepas intercept, lalu klik `[Submit]` lagi setelah error jaringan
73. Verifikasi hanya satu unit Waiting for Approval dan satu Subject pending untuk `{snMatch150}` (kemampuan baca state server)
74. Verifikasi tidak ada notifikasi ganda ke approver (jumlah notifikasi bertambah paling banyak satu dari nilai langkah 69)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-101, 102, 149, 150, 164, 185, 186, 187, 188). Tidak ada TC hanya-BE di spec ini.
- `K-1`: TC-102 dan TC-150 (idempotensi ID transaksi) tumpang tindih dengan cakupan BE; Expected hanya terobservasi di level request dan data (langkah 20 sampai 22, 73, 74), sehingga TC tetap masuk spec FE+BE menurut pengecualian K-1. Perilaku FE di luar yang tertulis di TC tidak disalin.
- Langkah 45 sampai 65: langkah 47 sampai 55 diulang dua kali (TC-185, TC-187) dan langkah 56 sampai 65 diulang dua kali (TC-186, TC-188) dengan parameter di tabel Prerequisites. Dua loop dipisah supaya langkah pengisian Approval Note tidak bersyarat (butir 8b nomor 7).
- Spec ini 74 langkah dengan ekspansi sekitar 93, lebih dari sekitar 35 langkah. Alasan: semua blok kelas b (kegagalan atau pemutusan respons tulis) dengan intercept dan asersi sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 4, 14 (Buka Hardware > Stock sebelum TC-102, S-14), 15, 17, 23, 25, 32, 33, 35, 36, 37, 39, 44, 45, 46 (navigasi, intercept dan pelepasannya, baseline; langkah 46 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 38, 47, 56 (Search untuk menemukan baris target, R-16), 48 sampai 51 dan 54, 55 (loop pertama), 57 sampai 61 dan 64, 65 (loop kedua), 66 (ganti akun), 69, 70.
- `P-11`: TC-149 dan TC-150 memakai simulator reader USB hanya untuk memicu Sync yang gagal atau diputus responsnya; USB (driver, cabut kabel) bukan objek asersi dan kemampuan simulator dinyatakan di Prerequisites.
- Post Condition tidak ada pada TC-101, 102, 149, 150, 164, 185 sampai 188.
- Temuan untuk QA:
  - TC-102 butir a ("FE memeriksa status transaksi dengan ID transaksi sementara") dan TC-150 butir b ("tidak ada notifikasi ganda") tidak punya langkah observasi UI; spec mengasersi pada level request dan data lewat kemampuan fixture yang tidak didefinisikan di TC, PRD, atau LLD (S-11, R-19).
  - TC-102 butir c ("hasil percobaan pertama dikembalikan") ambigu tentang apa yang teramati; spec mengasersi satu baris unit di Tab Available.
  - TC-149, 150, 164, 185 sampai 188 memakai data Pre-setup sebagai target; spec memakai unit dan Subject milik spec (seed dan pembersihan di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD).
