---
id: TC-AC-ACHS-E2E-264-dialog-dan-sukses-delete-unit
title: "Dialog dan Sukses Delete Unit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-161
  - TC-AC-ACHS-162
  - TC-AC-ACHS-163
  - TC-AC-ACHS-167
  - TC-AC-ACHS-172
  - TC-AC-ACHS-173
  - TC-AC-ACHS-174
coverage:
  web: automated
---

# Dialog dan Sukses Delete Unit

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #20; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup hanya dibaca (SKU dan Summary bar): SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #16 sampai #18) dan SKU `Fixture.hardwareStock.p16.a[3].sku` (Pre-setup #16, #27). Spec tidak menghapus atau mengubah unit Pre-setup (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-264`): seed di hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD) dan hook `after` menghapus semuanya (idempotent, juga bila spec gagal di tengah). Urutan seed di `before`: unit TC-162, TC-163, TC-167, TC-174, SKU TC-173, lalu unit TC-172 paling akhir sehingga unit itu menjadi unit Available bernomor tertinggi pada SKU `{skuLong}`. Data bersuffix `SN-ZEBRA-RFD40-{runId}-264` dibuat langkah TC-172 dan dihapus hook `after`.
- Efek pada Pre-setup: hitungan Total Registered dan Available SKU `{skuLong}` dan `{skuSfr}` berubah selama spec berjalan (unit milik spec ditambah di `before` dan dihapus di `after`); hitungan dipulihkan, sedangkan Last Updated kedua SKU berubah dan tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snDel162` | milik spec | unit Available pada `skuLong`, dibuka dialog Delete lalu dibatalkan (TC-161) dan dihapus (TC-162) | `SN-DEL162-{runId}-264` |
| `snDel163` | milik spec | unit Available pada `skuLong` untuk Cancel, Esc, dan klik backdrop (TC-163); tidak dihapus oleh langkah | `SN-DEL163-{runId}-264` |
| `snDel167` | milik spec | unit Available pada `skuLong` untuk klik ganda `[Delete]` (TC-167) | `SN-DEL167-{runId}-264` |
| `snDel172` | milik spec | unit Available pada `skuLong`, dibuat paling akhir di `before` sehingga bernomor tertinggi (TC-172) | `SN-DEL172-{runId}-264` |
| `snDel174` | milik spec | unit Available pada `skuSfr` yang menjadi Existing Record Subject Register Duplicate pending milik spec (seed sesaat setara Pre-setup #21b; Matched Identifier Subject = nilai ini) | `SN-DEL174-{runId}-264` |
| `skuDel173` | milik spec | SKU Smart Fixed Reader milik spec dengan satu unit Available `SN-DEL173-{runId}-264` (TC-173) | `SKU-DEL173-{runId}-264` |
| `snSync172` | milik spec | Serial Number baru yang di-Sync pada TC-172 | `SN-ZEBRA-RFD40-{runId}-264` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Kemampuan teknis (disediakan tim FE/BE): simulator reader USB Handheld Reader (service driver mock Pre-setup #25) hanya sebagai pemicu Add Stock Sync pada TC-172; seed unit, SKU, dan Subject milik spec serta pembersihannya di `after`; Search Serial Number pada Tab Available.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15; tidak ada pergeseran jam.

## Test Steps

### Persiapan baseline

1. Ketik Search `{skuLong}`, tekan Enter
2. Catat baris SKU `{skuLong}` di Stock List (Total Registered, Available, In Use, Last Updated)

### TC-AC-ACHS-161: Dialog konfirmasi Delete Unit

3. Klik row action `Detail` pada SKU `{skuLong}`
4. Klik Tab `Available`
5. Ketik Search `{snDel162}`, tekan Enter
6. Klik `(⋯)` pada baris `{snDel162}`
7. Klik `Delete`
8. Verifikasi dialog tampil dengan Title `Delete Unit`, Body bullet `• {snDel162}`, dan teks `This action cannot be undone. Are you sure you want to delete it?`
9. Verifikasi dialog memuat tombol `[Cancel]` dan `[Delete]`
10. Klik `[Cancel]`
11. Verifikasi belum ada unit yang terhapus: baris `{snDel162}` masih tampil di Tab Available

### TC-AC-ACHS-163: Cancel, Esc, dan klik backdrop pada dialog Delete

12. Ganti isi kotak search dengan `{snDel163}`, tekan Enter
13. Klik `(⋯)` pada baris `{snDel163}`
14. Klik `Delete`
15. Klik `[Cancel]`
16. Verifikasi dialog tertutup
17. Verifikasi unit `{snDel163}` tetap tampil di tabel
18. Klik `(⋯)` pada baris `{snDel163}`, klik `Delete`
19. Tekan Esc
20. Verifikasi Esc menutup dialog setara `[Cancel]`
21. Verifikasi unit `{snDel163}` tetap tampil di tabel
22. Klik `(⋯)` pada baris `{snDel163}`, klik `Delete`
23. Klik area backdrop di luar dialog
24. Verifikasi klik backdrop tidak menutup dialog (dialog tetap tampil)
25. Klik `[Cancel]`

### TC-AC-ACHS-162: Konfirmasi Delete unit Available

26. Catat Summary bar (Total Registered, Available, In Use)
27. Ganti isi kotak search dengan `{snDel162}`, tekan Enter
28. Klik `(⋯)` pada baris `{snDel162}`, klik `Delete`, lalu klik `[Delete]` pada dialog
29. Verifikasi toast sukses `Success, unit has been deleted.`
30. Verifikasi baris `{snDel162}` hilang dari Tab Available
31. Verifikasi Total Registered dan Available pada Summary bar berkurang 1 dari nilai langkah 26
32. Verifikasi In Use pada Summary bar tidak berubah dari nilai langkah 26
33. Klik segmen breadcrumb `Stock`
34. Verifikasi baris SKU `{skuLong}` di Stock List: Total Registered dan Available berkurang 1 dari nilai langkah 2
35. Verifikasi kolom Last Updated baris SKU `{skuLong}` berubah dari nilai langkah 2

### TC-AC-ACHS-167: Klik ganda cepat pada [Delete]

36. Ganti isi kotak search dengan `{skuLong}`, tekan Enter
37. Klik row action `Detail` pada SKU `{skuLong}`
38. Tunggu toast lama hilang otomatis, lalu catat Summary bar (Total Registered)
39. Ketik Search `{snDel167}`, tekan Enter
40. Klik `(⋯)` pada baris `{snDel167}`, klik `Delete`
41. Klik `[Delete]` dua kali cepat
42. Verifikasi hanya satu toast sukses `Success, unit has been deleted.` tampil
43. Verifikasi Total Registered berkurang tepat 1 dari nilai langkah 38

### TC-AC-ACHS-172: Nomor unit tidak dipakai ulang

44. Ganti isi kotak search dengan `{snDel172}`, tekan Enter
45. Catat nomor unit pada Device Name baris `{snDel172}` sebagai nomor unit Available tertinggi
46. Klik `(⋯)` pada baris `{snDel172}`, klik `Delete`, lalu klik `[Delete]`
47. Verifikasi toast sukses `Success, unit has been deleted.`
48. Klik `[Add Stock]` pada toolbar Tab Available
49. Sync satu Serial Number baru `{snSync172}` lewat simulator reader USB
50. Klik `[Submit]`
51. Tunggu aksi selesai dan kembali ke Stock Detail SKU `{skuLong}` Tab Available
52. Ketik Search `{snSync172}`, tekan Enter
53. Verifikasi unit baru menerima nomor lebih besar dari nomor tertinggi yang dicatat pada langkah 45
54. Verifikasi nomor unit yang dihapus pada langkah 46 tidak dipakai ulang

### TC-AC-ACHS-174: Delete unit yang menjadi Existing Record Subject pending

55. Klik segmen breadcrumb `Stock`
56. Ganti isi kotak search dengan `{skuSfr}`, tekan Enter
57. Klik row action `Detail` pada SKU `{skuSfr}`
58. Ketik Search `{snDel174}`, tekan Enter
59. Klik `(⋯)` pada baris unit `{snDel174}`, klik `Delete`, lalu klik `[Delete]`
60. Verifikasi toast sukses `Success, unit has been deleted.`
61. Buka Approvals > Hardware Stock, klik Tab `Active`
62. Ketik Search `{snDel174}`, tekan Enter
63. Verifikasi kolom Existing Record pada Subject dengan Matched Identifier `{snDel174}` tetap menampilkan snapshot Status, Registrant, Registered by, Registered at
64. Klik row action `Review` pada Subject itu
65. Verifikasi blok Existing Record di dialog tetap menampilkan snapshot Status, Registrant, Registered by, Registered at
66. Klik `[Cancel]`

### TC-AC-ACHS-173: Menghapus unit Available terakhir SKU

67. Klik sidebar Hardware > Stock
68. Ketik Search `{skuDel173}`, tekan Enter
69. Klik row action `Detail` pada SKU `{skuDel173}`
70. Klik `(⋯)` pada satu-satunya unit, klik `Delete`, lalu klik `[Delete]`
71. Verifikasi toast sukses `Success, unit has been deleted.`
72. Verifikasi Tab Available menampilkan empty state `No available hardware units`
73. Verifikasi Summary bar `0 | 0 | 0`
74. Klik segmen breadcrumb `Stock`
75. Ketik Search `{skuDel173}`, tekan Enter
76. Verifikasi baris SKU `{skuDel173}` di Stock List menjadi `0 | 0 | 0`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-161, 162, 163, 167, 172, 173, 174). Tidak ada TC hanya-BE di spec ini.
- Search memakai nilai penuh Serial Number atau SKU milik spec (bersuffix unik, hanya satu baris yang memuatnya); tidak ada perbedaan dengan sel tabel.
- Urutan menyimpang dari TC: TC-161 dan TC-163 (tanpa penghapusan) di awal; TC-162, 167, 172, 174, 173 (menghapus data) di akhir, TC-173 paling akhir (prinsip 3 butir 5 dan 2).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2, 26, 38, dan 45 (mencatat baseline), 10, 15, 25, 66 (menutup dialog), 33, 55, 67, 74 (navigasi kembali), 4 (`Klik Tab Available`, pengganti "Pastikan Tab `Available` aktif" TC), 61 (Tab `Active`), 1, 5, 12, 27, 36, 39, 44, 52, 56, 58, 62, 68, 75 (Search untuk menemukan baris target, R-16; langkah 1, 36, dan 56 mencari baris SKU di Stock List sebelum row action `Detail` atau pencatatan baris, 8b.13), 51 (tunggu aksi selesai, butir 8b nomor 8).
- Langkah 8 (Title dan Body dialog) ditulis satu `Verifikasi` karena Expected TC-161 butir a menyebutnya sebagai satu butir dialog konfirmasi (S-01).
- Spec ini 76 langkah, lebih dari sekitar 35 langkah. Alasan: tujuh TC satu topik aksi Delete Unit, satu kelas fungsional, berbagi dataset SKU RFD40, dan bagian sesudah tiap TC tidak bergantung pada hasil TC sebelumnya (tiap blok memakai unit milik spec berbeda); memisahkan menambah login dan hook tanpa pemisah nyata (prinsip 1).
- `P-11`: TC-172 memakai simulator reader USB (langkah 49) hanya sebagai pemicu penambahan unit baru; TC-172 adalah satu-satunya TC kelas d di spec ini, objek asersinya nomor unit (USB bukan objek asersi), dan kemampuan simulator dinyatakan di Prerequisites.
- TC-173 dan TC-174 memakai SKU, unit, dan Subject milik spec yang di-seed hook `before`; Subject seed tidak diasersi selain Existing Record yang diuji.
- Post Condition TC-162 (Hardware Log unit hilang, entri Activity Log `Delete`, satu sesi `Delete Stock` di Event Log) tidak memiliki langkah observasi di TC; tidak diasersi di sini dan diuji di spec log (Activity Log dan Event Log).
- Temuan untuk QA:
  - TC-172 menyebut "hapus unit bernomor tertinggi" tanpa menyatakan apakah unit Waiting for Approval termasuk; spec memakai unit Available milik spec yang dibuat terakhir (bernomor tertinggi) karena unit Waiting for Approval tidak ada di daftar Delete.
  - TC-167 butir a ("satu toast sukses dan satu entri log"): hanya klausa toast yang diasersi (langkah 42); TC tidak menyebut surface log yang diamati. Selisih satu entri `Delete` untuk hapus tunggal diuji di spec Activity Log (TC-534); kasus klik ganda pada TC-167 tidak diuji di spec manapun.
  - Seed unit, SKU Smart Fixed Reader beserta satu unit, dan Subject milik spec (padanan Pre-setup #21b) serta pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
  - TC-162 dan TC-173 menyebut Last Updated "berubah" tanpa nilai persis; spec membandingkan terhadap nilai baseline.
