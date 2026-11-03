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
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
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
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |

- Kemampuan teknis (disediakan tim FE/BE): simulator reader USB Handheld Reader (service driver mock Pre-setup #25) hanya sebagai pemicu Add Stock Sync pada TC-172; seed unit, SKU, dan Subject milik spec serta pembersihannya di `after`; Search Serial Number pada Tab Available.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15; tidak ada pergeseran jam.

## Test Steps

### Persiapan baseline

1. Catat baris SKU `{skuLong}` di Stock List (Total Registered, Available, In Use, Last Updated)

### TC-AC-ACHS-161: Dialog konfirmasi Delete Unit

2. Klik row action `Detail` pada SKU `{skuLong}`
3. Klik Tab `Available`
4. Ketik Search `{snDel162}`, tekan Enter
5. Klik `(⋯)` pada baris `{snDel162}`
6. Klik `Delete`
7. Verifikasi dialog tampil dengan Title `Delete Unit`, Body bullet `• {snDel162}`, dan teks `This action cannot be undone. Are you sure you want to delete it?`
8. Verifikasi dialog memuat tombol `[Cancel]` dan `[Delete]`
9. Klik `[Cancel]`
10. Verifikasi belum ada unit yang terhapus: baris `{snDel162}` masih tampil di Tab Available

### TC-AC-ACHS-163: Cancel, Esc, dan klik backdrop pada dialog Delete

11. Ganti isi kotak search dengan `{snDel163}`, tekan Enter
12. Klik `(⋯)` pada baris `{snDel163}`
13. Klik `Delete`
14. Klik `[Cancel]`
15. Verifikasi dialog tertutup
16. Verifikasi unit `{snDel163}` tetap tampil di tabel
17. Klik `(⋯)` pada baris `{snDel163}`, klik `Delete`
18. Tekan Esc
19. Verifikasi Esc menutup dialog setara `[Cancel]`
20. Verifikasi unit `{snDel163}` tetap tampil di tabel
21. Klik `(⋯)` pada baris `{snDel163}`, klik `Delete`
22. Klik area backdrop di luar dialog
23. Verifikasi klik backdrop tidak menutup dialog (dialog tetap tampil)
24. Klik `[Cancel]`

### TC-AC-ACHS-162: Konfirmasi Delete unit Available

25. Catat Summary bar (Total Registered, Available, In Use)
26. Ganti isi kotak search dengan `{snDel162}`, tekan Enter
27. Klik `(⋯)` pada baris `{snDel162}`, klik `Delete`, lalu klik `[Delete]` pada dialog
28. Verifikasi toast sukses `Success, unit has been deleted.`
29. Verifikasi baris `{snDel162}` hilang dari Tab Available
30. Verifikasi Total Registered dan Available pada Summary bar berkurang 1 dari nilai langkah 25
31. Verifikasi In Use pada Summary bar tidak berubah dari nilai langkah 25
32. Klik segmen breadcrumb `Stock`
33. Verifikasi baris SKU `{skuLong}` di Stock List: Total Registered dan Available berkurang 1 dari nilai langkah 1
34. Verifikasi kolom Last Updated baris SKU `{skuLong}` berubah dari nilai langkah 1

### TC-AC-ACHS-167: Klik ganda cepat pada [Delete]

35. Klik row action `Detail` pada SKU `{skuLong}`
36. Tunggu toast lama hilang otomatis, lalu catat Summary bar (Total Registered)
37. Ketik Search `{snDel167}`, tekan Enter
38. Klik `(⋯)` pada baris `{snDel167}`, klik `Delete`
39. Klik `[Delete]` dua kali cepat
40. Verifikasi hanya satu toast sukses `Success, unit has been deleted.` tampil
41. Verifikasi Total Registered berkurang tepat 1 dari nilai langkah 36

### TC-AC-ACHS-172: Nomor unit tidak dipakai ulang

42. Ganti isi kotak search dengan `{snDel172}`, tekan Enter
43. Catat nomor unit pada Device Name baris `{snDel172}` sebagai nomor unit Available tertinggi
44. Klik `(⋯)` pada baris `{snDel172}`, klik `Delete`, lalu klik `[Delete]`
45. Verifikasi toast sukses `Success, unit has been deleted.`
46. Klik `[Add Stock]` pada toolbar Tab Available
47. Sync satu Serial Number baru `{snSync172}` lewat simulator reader USB
48. Klik `[Submit]`
49. Tunggu aksi selesai dan kembali ke Stock Detail SKU `{skuLong}` Tab Available
50. Ketik Search `{snSync172}`, tekan Enter
51. Verifikasi unit baru menerima nomor lebih besar dari nomor tertinggi yang dicatat pada langkah 43
52. Verifikasi nomor unit yang dihapus pada langkah 44 tidak dipakai ulang

### TC-AC-ACHS-174: Delete unit yang menjadi Existing Record Subject pending

53. Klik segmen breadcrumb `Stock`, lalu klik row action `Detail` pada SKU `{skuSfr}`
54. Ketik Search `{snDel174}`, tekan Enter
55. Klik `(⋯)` pada baris unit `{snDel174}`, klik `Delete`, lalu klik `[Delete]`
56. Verifikasi toast sukses `Success, unit has been deleted.`
57. Buka Approvals > Hardware Stock, klik Tab `Active`
58. Ketik Search `{snDel174}`, tekan Enter
59. Verifikasi kolom Existing Record pada Subject dengan Matched Identifier `{snDel174}` tetap menampilkan snapshot Status, Registrant, Registered by, Registered at
60. Klik row action `Review` pada Subject itu
61. Verifikasi blok Existing Record di dialog tetap menampilkan snapshot Status, Registrant, Registered by, Registered at
62. Klik `[Cancel]`

### TC-AC-ACHS-173: Menghapus unit Available terakhir SKU

63. Klik sidebar Hardware > Stock
64. Ketik Search `{skuDel173}`, tekan Enter
65. Klik row action `Detail` pada SKU `{skuDel173}`
66. Klik `(⋯)` pada satu-satunya unit, klik `Delete`, lalu klik `[Delete]`
67. Verifikasi toast sukses `Success, unit has been deleted.`
68. Verifikasi Tab Available menampilkan empty state `No available hardware units`
69. Verifikasi Summary bar `0 | 0 | 0`
70. Klik segmen breadcrumb `Stock`
71. Ketik Search `{skuDel173}`, tekan Enter
72. Verifikasi baris SKU `{skuDel173}` di Stock List menjadi `0 | 0 | 0`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-161, 162, 163, 167, 172, 173, 174). Tidak ada TC hanya-BE di spec ini.
- Search memakai nilai penuh Serial Number atau SKU milik spec (bersuffix unik, hanya satu baris yang memuatnya); tidak ada perbedaan dengan sel tabel.
- Urutan menyimpang dari TC: TC-161 dan TC-163 (tanpa penghapusan) di awal; TC-162, 167, 172, 174, 173 (menghapus data) di akhir, TC-173 paling akhir (prinsip 3 butir 5 dan 2).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 25, 36, dan 43 (mencatat baseline), 9, 14, 24, 62 (menutup dialog), 32, 53, 63, 70 (navigasi kembali), 3 (`Klik Tab Available`, pengganti "Pastikan Tab `Available` aktif" TC), 57 (Tab `Active`), 4, 11, 26, 37, 42, 50, 54, 58, 64, 71 (Search untuk menemukan baris target, R-16), 49 (tunggu aksi selesai, butir 8b nomor 8).
- Langkah 7 (Title dan Body dialog) ditulis satu `Verifikasi` karena Expected TC-161 butir a menyebutnya sebagai satu butir dialog konfirmasi (S-01).
- Spec ini 72 langkah, lebih dari sekitar 35 langkah. Alasan: tujuh TC satu topik aksi Delete Unit, satu kelas fungsional, berbagi dataset SKU RFD40, dan bagian sesudah tiap TC tidak bergantung pada hasil TC sebelumnya (tiap blok memakai unit milik spec berbeda); memisahkan menambah login dan hook tanpa pemisah nyata (prinsip 1).
- TC-172 memakai simulator reader USB (langkah 47) hanya sebagai pemicu penambahan unit baru, objek ujinya nomor unit; dicatat di Temuan untuk QA karena kelas d dan TC-172 di spec fungsional.
- TC-173 dan TC-174 memakai SKU, unit, dan Subject milik spec yang di-seed hook `before`; Subject seed tidak diasersi selain Existing Record yang diuji.
- Post Condition TC-162 (Hardware Log unit hilang, entri Activity Log `Delete`, satu sesi `Delete Stock` di Event Log) tidak memiliki langkah observasi di TC; tidak diasersi di sini dan diuji di spec log (Activity Log dan Event Log).
- Temuan untuk QA:
  - TC-172 menyebut "hapus unit bernomor tertinggi" tanpa menyatakan apakah unit Waiting for Approval termasuk; spec memakai unit Available milik spec yang dibuat terakhir (bernomor tertinggi) karena unit Waiting for Approval tidak ada di daftar Delete.
  - TC-172 meminta Sync (kelas d, simulator USB) tetapi objek ujinya penomoran unit; perlu diputuskan apakah dipindah ke spec kelas d.
  - TC-167 butir a ("satu toast sukses dan satu entri log"): hanya klausa toast yang diasersi (langkah 40); TC tidak menyebut surface log yang diamati. Selisih satu entri `Delete` per unit diuji di spec Activity Log (TC-534).
  - Seed unit, SKU Smart Fixed Reader beserta satu unit, dan Subject milik spec (padanan Pre-setup #21b) serta pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
  - TC-162 dan TC-173 menyebut Last Updated "berubah" tanpa nilai persis; spec membandingkan terhadap nilai baseline.
