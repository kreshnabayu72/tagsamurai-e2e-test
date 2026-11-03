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
- Guided Tooltip: flag halaman Stock List dan Approvals disetel hook `before` dan dipulihkan hook `after` spec ini (juga untuk `Fixture.hardwareStock.account.p04.createOnly.fullName` di langkah ganti akun; kemampuan disediakan tim FE/BE; lihat suite.md). Hook suite: seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
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

Tabel keputusan gagal tanpa Approval Note (langkah 57 sampai 67):

| TC | Matched Identifier | Jenis | Keputusan | Toast error |
|---|---|---|---|---|
| TC-185 | `{snFd185}` | Register Duplicate | `Approve` | `Error, failed to approve duplicate.` |
| TC-187 | `{snFd187}` | Activation Collision | `Approve` | `Error, failed to approve activation.` |

Tabel keputusan gagal dengan Approval Note (langkah 68 sampai 79):

| TC | Matched Identifier | Jenis | Keputusan | Approval Note | Toast error |
|---|---|---|---|---|---|
| TC-186 | `{snFd186}` | Register Duplicate | `Reject` | `Alasan uji` | `Error, failed to reject duplicate.` |
| TC-188 | `{snFd188}` | Activation Collision | `Reject` | `Alasan uji` | `Error, failed to reject activation.` |

## Test Steps

### TC-AC-ACHS-101: Submit manual gagal 5xx lalu retry

1. Ketik Search `{skuSfr}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuSfr}`
3. Klik opsi `Add Stock`
4. Ketik `SN-FAIL-0001-{runId}-273`
5. Pasang intercept respons Submit Add Stock dengan status 500
6. Klik `[Submit]`
7. Verifikasi toast error `Error, failed to add stock.`
8. Verifikasi form tetap terbuka
9. Verifikasi textarea masih berisi `SN-FAIL-0001-{runId}-273`
10. Verifikasi `[Submit]` aktif kembali
11. Verifikasi tidak ada unit `SN-FAIL-0001-{runId}-273` tersimpan (kemampuan baca state server)
12. Lepas intercept
13. Klik `[Submit]` lagi
14. Verifikasi toast sukses `Success, unit has been added to stock.`

### TC-AC-ACHS-102: Respons terputus setelah commit, submit ulang manual

15. Buka Hardware > Stock
16. Ketik Search `{skuSfr}`, tekan Enter
17. Klik `(⋯)` pada baris SKU `{skuSfr}`, klik opsi `Add Stock`
18. Ketik `SN-IDEM-0001-{runId}-273`
19. Pasang intercept yang meneruskan request Submit ke server lalu membuang respons
20. Klik `[Submit]`
21. Setelah error jaringan, lepas intercept lalu klik `[Submit]` lagi; tunggu aksi selesai
22. Verifikasi FE memeriksa status transaksi dengan ID transaksi sementara sebelum mengizinkan submit ulang (request pemeriksaan status transaksi teramati sebelum request submit kedua)
23. Verifikasi hanya satu unit `SN-IDEM-0001-{runId}-273` tersimpan (kemampuan baca state server)
24. Buka Hardware > Stock
25. Ketik Search `{skuSfr}`, tekan Enter
26. Klik row action `Detail` pada SKU `{skuSfr}`
27. Ketik Search `SN-IDEM-0001-{runId}-273`, tekan Enter
28. Verifikasi hasil percobaan pertama dikembalikan tanpa duplikasi: Stock Detail SKU `{skuSfr}` Tab Available memuat satu baris `SN-IDEM-0001-{runId}-273`

### TC-AC-ACHS-149: Submit Sync gagal 5xx

29. Buka Hardware > Stock
30. Ketik Search `{skuLong}`, tekan Enter
31. Klik `(⋯)` pada baris SKU `{skuLong}`, klik opsi `Add Stock`
32. Sync `SN-ZEBRA-RFD40-{runId}-273` (OK) dan `{snMatch149}` (match) lewat simulator reader USB
33. Catat jumlah unit, Subject pending, dan notifikasi approver terkait kedua Serial Number (kemampuan baca state server)
34. Pasang intercept respons Submit Sync dengan status 500
35. Klik `[Submit]`, lalu klik `[Continue]`
36. Verifikasi toast error `Error, failed to add stock.`
37. Verifikasi tidak ada unit, Subject, maupun notifikasi tersimpan: sama dengan nilai langkah 33 (atomik penuh)
38. Verifikasi Tabel Synced Units tetap berisi dua baris
39. Verifikasi `[Submit]` aktif kembali
40. Lepas intercept
41. Klik `[Cancel]` halaman
42. Verifikasi dialog `Unsaved Changes` dengan pesan `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
43. Klik `[Leave]`

### TC-AC-ACHS-164: Delete gagal server

44. Buka Hardware > Stock
45. Ketik Search `{skuLong}`, tekan Enter
46. Klik row action `Detail` pada SKU `{skuLong}`
47. Catat Summary bar (Total Registered)
48. Ketik Search `{snDel164}`, tekan Enter
49. Pasang intercept respons Delete dengan status 500
50. Klik `(⋯)` pada baris `{snDel164}`, klik `Delete`, lalu klik `[Delete]`
51. Verifikasi toast error `Error, failed to delete unit.`
52. Verifikasi unit `{snDel164}` tetap di tabel
53. Verifikasi Total Registered tidak berubah dari nilai langkah 47
54. Lepas intercept

### TC-AC-ACHS-185 dan TC-AC-ACHS-187: Keputusan Approve gagal server

55. Buka Approvals > Hardware Stock
56. Klik Tab `Active`

Untuk setiap baris tabel keputusan gagal tanpa Approval Note (TC-185, TC-187), lakukan langkah 57 sampai 67:

57. Ketik Search Matched Identifier pada baris tabel, tekan Enter
58. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
59. Pasang intercept respons keputusan Approval dengan status 500
60. Pilih radio `Approve`
61. Klik `[Submit]`
62. Verifikasi toast error sesuai kolom Toast error
63. Verifikasi dialog tetap terbuka
64. Verifikasi Subject tetap pending
65. Verifikasi radio dan `[Submit]` tetap aktif
66. Lepas intercept, lalu klik `[Cancel]`
67. Klik `(←)` pada kotak Search

### TC-AC-ACHS-186 dan TC-AC-ACHS-188: Keputusan Reject gagal server

Untuk setiap baris tabel keputusan gagal dengan Approval Note (TC-186, TC-188), lakukan langkah 68 sampai 79:

68. Ketik Search Matched Identifier pada baris tabel, tekan Enter
69. Klik row action `Review` pada Subject dengan Matched Identifier pada baris tabel
70. Pasang intercept respons keputusan Approval dengan status 500
71. Pilih radio `Reject`
72. Isi Approval Note `Alasan uji`
73. Klik `[Submit]`
74. Verifikasi toast error sesuai kolom Toast error
75. Verifikasi dialog tetap terbuka
76. Verifikasi Subject tetap pending
77. Verifikasi radio dan `[Submit]` tetap aktif
78. Lepas intercept, lalu klik `[Cancel]`
79. Klik `(←)` pada kotak Search

### TC-AC-ACHS-150: Retry Submit Sync tanpa duplikasi

80. Logout, lalu login sebagai Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName`; tunggu aksi selesai
81. Buka Hardware > Stock
82. Ketik Search `{skuLong}`, tekan Enter
83. Klik `(⋯)` pada baris SKU `{skuLong}`, klik opsi `Add Stock`
84. Sync `{snMatch150}` (match) lewat simulator reader USB
85. Catat jumlah unit, Subject pending, dan notifikasi approver terkait `{snMatch150}` (kemampuan baca state server)
86. Pasang intercept yang meneruskan request Submit ke server lalu membuang respons
87. Klik `[Submit]`, lalu klik `[Send]`
88. Lepas intercept, lalu klik `[Submit]` lagi setelah error jaringan; tunggu aksi selesai
89. Verifikasi hanya satu unit Waiting for Approval dan satu Subject pending untuk `{snMatch150}` (kemampuan baca state server)
90. Verifikasi tidak ada notifikasi ganda ke approver (jumlah notifikasi bertambah paling banyak satu dari nilai langkah 85)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-101, 102, 149, 150, 164, 185, 186, 187, 188). Tidak ada TC hanya-BE di spec ini.
- `K-1`: TC-102 dan TC-150 (idempotensi ID transaksi) tumpang tindih dengan cakupan BE; Expected hanya terobservasi di level request dan data (langkah 22 sampai 28, 89, 90), sehingga TC tetap masuk spec FE+BE menurut pengecualian K-1. Perilaku FE di luar yang tertulis di TC tidak disalin.
- Langkah 55 sampai 79: langkah 57 sampai 67 diulang dua kali (TC-185, TC-187) dan langkah 68 sampai 79 diulang dua kali (TC-186, TC-188) dengan parameter di tabel Prerequisites. Dua loop dipisah supaya langkah pengisian Approval Note tidak bersyarat (butir 8b nomor 7).
- Klausa tambahan di luar Expected TC-185 sampai TC-188 (S-03): langkah 65 dan 77 (`Verifikasi` radio dan `[Submit]` tetap aktif) dipisah dari klausa "dialog tetap terbuka" dan "Subject tetap pending" (langkah 63, 64 dan 75, 76) dan dipertahankan sebagai bukti dialog tetap interaktif sesudah kegagalan server.
- Spec ini 90 langkah dengan ekspansi sekitar 113, lebih dari sekitar 35 langkah. Alasan: semua blok kelas b (kegagalan atau pemutusan respons tulis) dengan intercept dan asersi sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 sampai 5, 15 (Buka Hardware > Stock sebelum TC-102, S-14), 17, 19, 24 (Buka Hardware > Stock sebelum Search SKU di Stock Detail, S-14), 29, 31, 33, 40, 41, 43, 44, 46, 47, 49, 54, 55, 56 (navigasi, intercept dan pelepasannya, baseline, dan klik `(⋯)` lalu `Add Stock` sesudah Search; langkah 56 `Klik Tab Active` menggantikan "Pastikan Tab `Active` aktif" TC), 81, 83, 85, 86 (langkah 44 dan 81 membuka Hardware > Stock sebelum Search dan row action pada TC-164 dan TC-150, S-14), 16, 25, 30, 45, 82 (Search baris SKU sebelum klik `(⋯)` atau row action `Detail`, R-16 dan 8b.13; langkah 25 mencari SKU `{skuSfr}` sebelum row action `Detail` pada TC-102), 26 (klik row action `Detail` pada SKU), 27 (Search Serial Number sebelum Verifikasi isi Tab Available, R-16 dan S-14), 48, 57, 68 (Search untuk menemukan baris target, R-16), 58 sampai 61 dan 66, 67 (loop pertama), 69 sampai 73 dan 78, 79 (loop kedua), 80 (ganti akun). Langkah 21 dan 88 (`[Submit]` lagi setelah error jaringan) ditutup "tunggu aksi selesai" sebelum langkah baca state server (langkah 23 dan 89, 8b.8), sehingga pembacaan state tidak mendahului respons retry.
- `P-11`: TC-149 dan TC-150 memakai simulator reader USB hanya untuk memicu Sync yang gagal atau diputus responsnya; USB (driver, cabut kabel) bukan objek asersi dan kemampuan simulator dinyatakan di Prerequisites.
- Post Condition tidak ada pada TC-101, 102, 149, 150, 164, 185 sampai 188.
- Temuan untuk QA:
  - TC-102 butir a ("FE memeriksa status transaksi dengan ID transaksi sementara") dan TC-150 butir b ("tidak ada notifikasi ganda") tidak punya langkah observasi UI; spec mengasersi pada level request dan data lewat kemampuan fixture yang tidak didefinisikan di TC, PRD, atau LLD (S-11, R-19).
  - TC-150 langkah 7 ("Klik [Submit] lagi" setelah error jaringan) tidak menyebut apakah retry `[Submit]` memunculkan dialog `[Send]` lagi, dan tidak menyebut keadaan akhir form (tetap terbuka, tertutup, atau berpindah halaman); spec tidak mengasersi keduanya dan hanya mengasersi state server (langkah 89 dan 90).
  - TC-102 butir c ("hasil percobaan pertama dikembalikan") ambigu tentang apa yang teramati; spec mengasersi satu baris unit di Tab Available.
  - TC-149, 150, 164, 185 sampai 188 memakai data Pre-setup sebagai target; spec memakai unit dan Subject milik spec (seed dan pembersihan di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD).
