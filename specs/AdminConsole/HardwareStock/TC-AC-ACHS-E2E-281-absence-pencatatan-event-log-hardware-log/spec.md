---
id: TC-AC-ACHS-E2E-281-absence-pencatatan-event-log-hardware-log
title: "Absence Pencatatan Event Log dan Hardware Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-519
  - TC-AC-ACHS-551
  - TC-AC-ACHS-558
  - TC-AC-ACHS-594
  - TC-AC-ACHS-595
  - TC-AC-ACHS-596
coverage:
  web: automated
---

# Absence Pencatatan Event Log dan Hardware Log

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22 dan #27; suite serial `parallel: false` (lihat suite.md).
- Pemicu (`P-5` butir a, tiap TC punya baseline sendiri): Approve Register Duplicate `{snApr}` (TC-519), Reject Register Duplicate `{snRej}` dan Delete unit `{snDel}` (TC-551), Add Stock Sync yang ditolak atau dibatalkan (TC-594), pemicu Client yang menghapus atau mengganti perangkat BLE Gateway (TC-558, lewat sesi API Client; kemampuan disediakan tim BE/FE), serta request langsung Add Stock manual dan Submit Add Stock Sync di atas limit yang ditolak (TC-595 dan TC-596). Keputusan, Delete, dan request langsung dijalankan lewat klien HTTP dengan token sesi API aktor Total Control (login API password, token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, bukan konteks kedua). Add Stock Sync memakai simulator reader USB Handheld Reader (service driver mock, Pre-setup #25, kemampuan disediakan tim FE); simulator hanya memicu keadaan dan bukan objek asersi (`P-11`, TC-594).
- Data seed milik spec (S-06; hook `before` spec ini lewat sesi API aktor Total Control, kemampuan seed disediakan tim BE/FE): unit Waiting for Approval `{snApr}` dengan Subject Register Duplicate pending (target Approve TC-519), Subject Register Duplicate pending `{snRej}` (target Reject TC-551), unit Available `{snDel}` pada SKU `{skuLong}` (target Delete TC-551), dan perangkat BLE Gateway In Use `BLE-{runId}-281` pada SKU `{skuBle}` milik Client `Fixture.hardwareStock.p23.client[4].name` (pemicu TC-558). Hook `after` menghapus keempat data seed itu dan unit lain yang dibuat spec ini (idempotent, dilewati bila sudah tidak ada; R-08).
- State global yang diubah (R-08): System Limit `register_asset_bulk_limit` (Pre-setup #26) diubah ke 100 untuk TC-595 dan TC-596 oleh pelaku yang disediakan tim FE/BE, dipulihkan ke 1.000 di langkah penghubung (langkah 50) dan di hook `after`. Suite berjalan serial.
- Kemampuan baca state server (disediakan tim BE/FE, tanpa endpoint di spec): jumlah unit per Serial Number.
- Data Dinamis (S-12, suffix `{runId}-281`): `SN-APR-{runId}-281`, `SN-REJ-{runId}-281`, `SN-DEL-{runId}-281` (seed), `SN-ZEBRA-RFD40-{runId}-281a` dan `SN-ZEBRA-RFD40-{runId}-281b` (TC-594), `SN-DIR-{runId}-281-0001` sampai `SN-DIR-{runId}-281-0101` (TC-595), dan `SN-DIRS-{runId}-281-0001` sampai `SN-DIRS-{runId}-281-0101` (TC-596), dan `BLE-{runId}-281` (seed TC-558).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai (hanya dibaca): SKU `Fixture.hardwareStock.p16.a[4].sku` dengan unit Available `Fixture.hardwareStock.p17.e[19].serialNumber` (Pre-setup #17), SKU `Fixture.hardwareStock.p16.a[3].sku` (Pre-setup #16), SKU `Fixture.hardwareStock.p16.a[5].sku` (Pre-setup #16, #27); `Fixture.hardwareStock.p27.fx[1].serialNumber` (Pre-setup #27, dipakai sebagai Serial Number yang cocok dengan unit Available SKU lain untuk menghasilkan Waiting for Approval).

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `skuFx` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuBle` | #16, #27 (Tabel A baris ke-5) | SKU BLE Gateway dengan 5 unit (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
| `client4` | #23 (urutan penulisan daftar Client, butir ke-4) | Nama Client ke-4 pada daftar Client Pre-setup #23, pemilik perangkat BLE Gateway seed TC-558 | `Fixture.hardwareStock.p23.client[4].name` |
| `snE19` | #17 (Tabel E baris N = 19) | Serial Number unit `unitE19` | `Fixture.hardwareStock.p17.e[19].serialNumber` |
| `snFx1` | #27 | Serial Number unit Available ke-1 pada `skuSfr` (urutan Serial Number naik), milik Distributor #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |

Parameter `{snApr}`, `{snRej}`, `{snDel}` adalah data seed milik spec (bukan Pre-setup bersama) bernilai `SN-APR-{runId}-281`, `SN-REJ-{runId}-281`, dan `SN-DEL-{runId}-281`.

## Test Steps

### TC-AC-ACHS-519: Event Log tidak memuat keputusan

1. Approve Register Duplicate `{snApr}` lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
2. Klik menu Hardware > Stock di sidebar, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
3. Klik Tab `Available`
4. Klik icon `[Event Log]` di toolbar
5. Verifikasi sedikitnya satu sesi `Add Stock` atau `Delete Stock` tampil di popup Event Log (pembanding)
6. Ketik Search `Approve`, tekan Enter
7. Verifikasi popup menampilkan `No results found` (tidak ada baris keputusan Duplicate Identifier)
8. Klik `(←)` pada kotak Search
9. Klik icon Filter, lalu buka filter Activity
10. Verifikasi opsi filter Activity hanya `Add Stock` dan `Delete Stock`
11. Tutup popup Event Log

### TC-AC-ACHS-594: Event Log tidak mencatat Add Stock yang ditolak atau dibatalkan

12. Klik icon `[Event Log]` dan catat info jumlah entri pada footer, lalu tutup popup
13. Klik opsi `Add Stock` pada toolbar Tab Available
14. Sync `Fixture.hardwareStock.p17.e[19].serialNumber` (unit Available SKU yang sama) dan `SN-ZEBRA-RFD40-{runId}-281a` (OK) lewat simulator reader USB
15. Klik `[Submit]`, lalu klik `[Continue]`
16. Verifikasi Submit pertama ditolak dengan error banner `Serial number Fixture.hardwareStock.p17.e[19].serialNumber already exists in the system`
17. Verifikasi tidak ada unit `SN-ZEBRA-RFD40-{runId}-281a` tersimpan (kemampuan baca state server)
18. Klik `[Cancel]` halaman
19. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`
21. Klik opsi `Add Stock` lagi
22. Sync `Fixture.hardwareStock.p27.fx[1].serialNumber` (Waiting for Approval) dan `SN-ZEBRA-RFD40-{runId}-281b` (OK) lewat simulator reader USB
23. Klik `[Submit]`, lalu klik `[Cancel]` pada dialog D-02
24. Verifikasi dialog D-02 tertutup dan halaman Add Stock masih terbuka (Submit kedua dibatalkan lewat `[Cancel]` pada D-02)
25. Verifikasi tidak ada unit `SN-ZEBRA-RFD40-{runId}-281b` tersimpan (kemampuan baca state server)
26. Klik `[Cancel]` halaman
27. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Leave]`
29. Klik icon `[Event Log]`
30. Verifikasi info jumlah entri pada footer sama dengan jumlah yang dicatat pada langkah 12 (anchor: footer info tampil)
31. Verifikasi tidak ada sesi `Add Stock` baru
32. Tutup popup Event Log

### TC-AC-ACHS-595: Event Log tidak mencatat request Add Stock manual di atas limit yang ditolak

33. Ubah System Limit `register_asset_bulk_limit` menjadi 100 lewat pelaku yang disediakan tim FE/BE; tunggu aksi selesai
34. Klik menu Hardware > Stock di sidebar, lalu klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[3].sku` dan klik row action `Detail`
35. Klik icon `[Event Log]` dan catat info jumlah entri pada footer sebagai baseline, lalu tutup popup
36. Kirim request langsung Add Stock manual untuk SKU `Fixture.hardwareStock.p16.a[3].sku` dengan 101 Serial Number `SN-DIR-{runId}-281-0001` sampai `SN-DIR-{runId}-281-0101` memakai token sesi API Total Control hingga respons diterima; tunggu aksi selesai
37. Verifikasi respons menolak seluruh request dengan error validasi V-03 (pemicu ditolak, anchor absence)
38. Klik icon `[Event Log]`
39. Verifikasi info jumlah entri pada footer sama dengan baseline langkah 35 (anchor: footer info tampil)
40. Verifikasi tidak ada sesi Event Log baru
41. Tutup popup Event Log

### TC-AC-ACHS-596: Event Log tidak mencatat request Submit Add Stock Sync di atas limit yang ditolak

42. Klik segmen breadcrumb `Stock`, lalu klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[4].sku` dan klik row action `Detail`
43. Klik icon `[Event Log]` dan catat info jumlah entri pada footer sebagai baseline, lalu tutup popup
44. Kirim request langsung Submit Add Stock Sync untuk SKU `Fixture.hardwareStock.p16.a[4].sku` dengan 101 unit `SN-DIRS-{runId}-281-0001` sampai `SN-DIRS-{runId}-281-0101` beserta nilai Min/Max/Current Power memakai token sesi API Total Control hingga respons diterima; tunggu aksi selesai
45. Verifikasi respons menolak seluruh request dengan error validasi V-18 (pemicu ditolak, anchor absence)
46. Klik icon `[Event Log]`
47. Verifikasi info jumlah entri pada footer sama dengan baseline langkah 43 (anchor: footer info tampil)
48. Verifikasi tidak ada sesi Event Log baru
49. Tutup popup Event Log
50. Pulihkan System Limit `register_asset_bulk_limit` ke 1.000 lewat pelaku yang disediakan tim FE/BE; tunggu aksi selesai

### TC-AC-ACHS-551: Keputusan Reject dan unit dihapus tidak punya Hardware Log

51. Reject Register Duplicate `{snRej}` lewat sesi API hingga keputusan tersimpan, lalu hapus unit `{snDel}` lewat sesi API hingga tersimpan; tunggu aksi selesai
52. Muat ulang halaman (F5)
53. Verifikasi sedikitnya satu unit tampil di Tab Available (pembanding)
54. Ketik Search `{snRej}`, tekan Enter
55. Verifikasi Tab Available menampilkan `No results found`
56. Ganti isi kotak search dengan `{snDel}`, tekan Enter
57. Verifikasi Tab Available menampilkan `No results found`: tidak ada unit dengan Hardware Log yang bisa dibuka
58. Klik `(←)` pada kotak Search
59. Buka Approvals > Hardware Stock, lalu klik Tab `History`
60. Ketik Search `{snRej}`, tekan Enter
61. Verifikasi Subject `{snRej}` tampil dengan Approval `Rejected` (keputusan Reject terlihat di Tab History Approvals)
62. Klik `(←)` pada kotak Search

### TC-AC-ACHS-558: Activity Log tidak mencatat Device Released untuk perangkat BLE Gateway yang dihapus Client

63. Buka Admin Console > Activity Log, lalu terapkan Filter Object = `Hardware`
64. Catat jumlah entri `Device Released` sebagai baseline TC-558
65. Client menghapus atau mengganti perangkat BLE Gateway `BLE-{runId}-281` di Global Settings lewat sesi API hingga respons diterima; tunggu aksi selesai
66. Verifikasi respons menunjukkan penghapusan atau penggantian perangkat BLE Gateway tersimpan (pemicu diterima, anchor absence)
67. Muat ulang halaman (F5), lalu terapkan Filter Object = `Hardware`
68. Verifikasi sedikitnya satu entri Object `Hardware` tampil di tabel Activity Log (pembanding, anchor absence)
69. Verifikasi jumlah entri `Device Released` sama dengan baseline langkah 64: tidak ada entri `Device Released` baru untuk `BLE-{runId}-281`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-519, 551, 594, 595, 596). Tidak ada TC hanya-BE di spec ini. Spec kelas g (absence); pemicu kelas lain memakai `P-5` butir a; pemicu bersifat pembentuk kondisi dan bukan objek uji.
- `P-11`: TC-594 memakai simulator reader USB hanya untuk memicu Add Stock yang ditolak atau dibatalkan; USB bukan objek asersi.
- `S-05`: TC-595 dan TC-596 terbelah antara presence dan absence. Spec asal TC-AC-ACHS-E2E-243 mengasersi Expected a dan b (respons ditolak, tidak ada unit tersimpan); spec ini memuat Expected c (tidak ada sesi Event Log baru) dengan pemicu request ditolak (`P-5` butir a), user dan baseline sendiri (S-12). Id kedua TC ada di `sourceTc` kedua spec (konvensi §8 pengecualian 2026-11-02).
- TC-595 dan TC-596 hanya memuat Expected c (tidak ada sesi Event Log baru) di spec ini; Expected a dan b (respons ditolak seluruhnya, tidak ada unit tersimpan) diasersi di spec 243. Respons ditolak pada langkah 37 dan 45 adalah anchor positif yang terhubung ke pemicu, bukan objek uji (butir 8b nomor 1 dan 2).
- `S-05`: TC-558 terbelah antara presence dan absence. Spec asal TC-AC-ACHS-E2E-279 mengasersi Expected a dan b (unit BLE tetap In Use, tidak berpindah ke Tab Available); spec ini memuat Expected c (tidak ada entri Activity Log `Device Released`) dengan pemicu Client menghapus atau mengganti perangkat BLE Gateway (`P-5` butir a), user dan baseline sendiri (S-12). Id TC-AC-ACHS-558 ada di `sourceTc` kedua spec (keputusan 2026-11-02; konvensi §8 pengecualian 2026-11-02).
- Konfirmasi keyword Search terhadap nilai penuh data seed (#8): Search `{snRej}` dan `{snDel}` memakai Serial Number seed penuh milik spec; Search `Approve` adalah istilah Action dari TC, bukan nilai seed. Tidak ada perbedaan.
- Urutan: TC-519 (Approve), TC-594 (memakai unit `Fixture.hardwareStock.p17.e[19].serialNumber` yang tetap ada), TC-595 dan TC-596 (pemicu request ditolak, tanpa mengubah data), TC-551 (Reject dan Delete, menghapus data), lalu TC-558 (pemicu Client pada data BLE seed milik spec) di akhir.
- Baseline Event Log (S-12): TC-594, TC-595, dan TC-596 masing-masing mencatat jumlah entri footer Event Log sendiri sebelum pemicu (langkah 12, 35, dan 43) dan mengasersi selisih nol; TC-558 mencatat jumlah entri Activity Log `Device Released` sendiri (langkah 64) dan mengasersi selisih nol (langkah 69); tidak ada total absolut.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 36, 44, 51 (pemicu lewat sesi API, "Tunggu aksi selesai", R-20), 33 dan 50 (mengubah dan memulihkan System Limit, state global), 2, 3, 4, 11, 12, 13, 21, 29, 32, 34, 35, 38, 41, 42, 43, 46, 49, 59 (navigasi dan membuka/menutup popup), 6, 54, 56, 60 (Search untuk menemukan baris target, R-16), 8, 58, 62 (mengosongkan Search lewat `(←)`), 18, 26 (`[Cancel]` halaman) dan 20, 28 (`[Leave]`; dialog `Unsaved Changes` diverifikasi pada langkah 19 dan 27), 52, 67 (memuat ulang), 63, 64, 65 (membuka Activity Log dengan Filter, baseline, dan pemicu Client lewat sesi API, "Tunggu aksi selesai", R-20). Klik `[Cancel]` pada dialog D-02 (langkah 23) adalah bagian aksi TC.
- Anchor positif asersi absence (butir 8b nomor 2): langkah 5 untuk langkah 7, langkah 53 untuk langkah 55 dan 57, langkah 30 untuk langkah 31, langkah 39 untuk langkah 40, langkah 47 untuk langkah 48, langkah 66 dan 68 untuk langkah 69; Expected b TC-551 diasersi pada langkah 61 (keputusan Reject terlihat di Tab History). Activity Log diperiksa di spec ini hanya untuk TC-558 (langkah 63 sampai 69); isi entri Activity Log diuji di spec 276.
- Langkah 24 menambah `Verifikasi` dialog D-02 tertutup dan halaman Add Stock masih terbuka sebagai hasil teramati dari `[Cancel]` pada D-02 (TC hanya menulis "dibatalkan lewat `[Cancel]` pada D-02"; S-03).
- Spec ini 69 langkah, di atas sekitar 35 langkah. Alasan: enam TC satu kelas g (absence) yang masing-masing butuh pemicu, anchor positif, dan baseline sendiri; semua blok satu kelas dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-594 memakai `SN-ZEBRA-RFD40-000010` sebagai unit Available SKU yang sama; spec memakai `Fixture.hardwareStock.p17.e[19].serialNumber` karena target Delete TC-551 kini data seed milik spec (`{snDel}`) dan unit Pre-setup tetap tidak berubah.
  - TC-551 mencari unit hasil Reject (SKU TC52) pada Tab Available SKU RFD40 (langkah TC 2 sampai 3) dan unit yang dihapus bernama literal Pre-setup; spec mengikuti langkah TC memakai data seed bersuffix milik spec dan menambah pembanding positif.
  - Expected butir b TC-551 ("keputusan Reject hanya terlihat di Tab History Approvals dan Activity Log") tidak punya langkah observasi Activity Log; spec hanya mengasersi Tab History.
  - TC-595 dan TC-596 Precondition menyebut Register Asset Bulk Limit = 100 (Pre-setup #26, default 1.000); pelaku yang mengubah limit tidak disebut TC, sehingga disediakan tim FE/BE. TC-595 dan TC-596 Langkah 2 membuka popup Event Log tanpa mencatat jumlah entri awal; spec mencatat baseline sendiri (S-12).
