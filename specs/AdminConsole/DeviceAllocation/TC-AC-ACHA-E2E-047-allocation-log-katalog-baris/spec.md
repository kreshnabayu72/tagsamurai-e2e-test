---
id: TC-AC-ACHA-E2E-047-allocation-log-katalog-baris
title: "Allocation Log: Katalog Entri per Kejadian dan Baris Description"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-380
  - TC-AC-ACHA-381
  - TC-AC-ACHA-382
  - TC-AC-ACHA-383
  - TC-AC-ACHA-384
  - TC-AC-ACHA-385
  - TC-AC-ACHA-386
  - TC-AC-ACHA-387
  - TC-AC-ACHA-388
  - TC-AC-ACHA-490
coverage:
  web: automated
---

# Allocation Log: Katalog Entri per Kejadian dan Baris Description

## Prerequisites

- Mode: FE+BE.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var):

| Alias | Pre-setup | Nama pengguna | Env var password |
|---|---|---|---|
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON, aktor hook `before`) | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `totalControlDistributor` | #27 | Hendra Wibowo | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnPrincipal` | #24 | Dewi Lestari (MB_PRIN) | `Spectra.env.AC_DA_MB_PRIN_PASSWORD` |
| `memberOnPartner1` | #44 | Andi Wijaya (MB_P1) | `Spectra.env.AC_DA_MB_P1_PASSWORD` |

- Login akun pertama (Budi Santoso) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan jam server.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #1 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Asia/Jakarta), #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00, #63 Approval Timeout 3 day(s).
- Data seeding milik spec (fixture API tim FE/BE; salinan milik spec dari Pre-setup #49, #51, #56, #59; Allocation ID ditangkap saat runtime):
  - Transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00): satu salinan baru untuk tiap blok TC-AC-ACHA-380 (dipakai juga oleh TC-AC-ACHA-383 pada transaksi yang sama), 490, 387, 384, 386, 388, dibuat lewat fixture tepat pada langkah pembuka tiap blok (bukan di hook `before`), sehingga waktu pembuatan (T1) per blok.
  - Transaksi Waiting for Approval milik MB_PRIN (Handheld Reader Long Range, Quantity 10, Client PT Manufaktur Unggul, Payment Free, tanpa Notes) untuk TC-AC-ACHA-381, dan milik MB_P1 (NFC, Quantity 10, Client PT Retail Makmur, Pay From `PT Global Distribusi (Distributor)`, tanpa Notes, Total Cost $15.00) untuk TC-AC-ACHA-382, dibuat di hook `before`; transaksi Completed jalur langsung milik Hendra Wibowo untuk TC-AC-ACHA-385. Ketiganya tidak terpengaruh geser jam karena TC-AC-ACHA-388 berada di akhir spec.
- Kemampuan teknis: pergeseran jam server absolut ke `T1 + 3 hari + 1 menit` lewat fixture yang disediakan tim FE/BE (T1 = waktu terbit transaksi, dibaca lewat fixture; margin 1 menit dihitung dari T1); sesi UI dan API tetap valid saat jam digeser (dinyatakan di `suite.md`); jam browser tidak diubah karena Timeout dihitung di server dan tidak diamati lewat hitung mundur UI. Tunggu satu siklus job memakai polling: muat ulang halaman tiap 5 detik sampai status transaksi `Canceled`, batas tunggu 2 menit. Jam server dipulihkan sesudah polling dan sebelum Allocation Log dibuka.
- Efek samping geser jam: job Timeout membatalkan semua transaksi Waiting for Approval yang melewati 3 hari dari waktu terbitnya, termasuk transaksi blok lain yang masih Waiting. Karena itu blok TC-AC-ACHA-388 berada di akhir spec dan semua asersi memakai Allocation ID transaksi blok masing-masing.
- Pemulihan (R-08): hook `after` memulihkan seed ke 30 baris dan jam server lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec tidak dapat dihapus lewat UI dan audit trail bertambah permanen. Pre-setup bersama tidak diubah selain jam server dan saldo/Reserve kantong PT Global Distribusi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACHA-380: Entri `Allocation created` dengan Description lengkap

1. Buat salinan transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya, muat ulang halaman (F5), buka menu row action `⋯` pada transaksi itu dan klik `Allocation Log`
2. Verifikasi modal Allocation Log memuat tepat satu entri
3. Verifikasi entri teratas berjudul `Allocation created by Budi S`
4. Verifikasi Date & Time di bawah judul sesuai General Settings (Date Format `dd/MM/yy`, Time Format 24 jam)
5. Verifikasi baris Description berurutan: `Category: RFID`, `Type: Object TAG`, `Quantity: 100`, `From: PT Global Distribusi`, `Notes: Batch uji`, `Cost: $250.00`
6. Verifikasi tidak ada baris `Resubmitted From`
7. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-383: Entri `Allocation edited` memuat nilai setelah Edit

8. Klik `Edit` pada transaksi itu, ubah Quantity menjadi `120` dan Notes menjadi `Batch revisi`, lalu klik `[Save]`
9. Buka menu row action `⋯` pada transaksi dan klik `Allocation Log`
10. Verifikasi entri teratas berjudul `Allocation edited by Budi S`
11. Verifikasi Description entri teratas memuat nilai setelah Edit: `Category: RFID`, `Type: Object TAG`, `Quantity: 120`, `From: PT Global Distribusi`, `Notes: Batch revisi`, `Cost: $300.00` (120 x $2.50 dari snapshot)
12. Verifikasi tidak ada baris `Resubmitted From`
13. Verifikasi entri `Allocation created by Budi S` di bawahnya tetap berisi `Quantity: 100`, `Notes: Batch uji`, dan `Cost: $250.00`
14. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-490: Edit yang mengosongkan Notes

15. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya, muat ulang halaman (F5), buka menu row action `⋯` pada transaksi itu, klik `Edit`, kosongkan Notes (`Batch uji` menjadi kosong) tanpa mengubah field lain, lalu klik `[Save]`
16. Buka menu row action `⋯` pada transaksi dan klik `Allocation Log`
17. Verifikasi entri teratas berjudul `Allocation edited by Budi S`
18. Verifikasi Description entri teratas: `Category: RFID`, `Type: Object TAG`, `Quantity: 100`, `From: PT Global Distribusi`, `Notes: —`, `Cost: $250.00`
19. Verifikasi baris `Notes` tetap tampil walau kosong
20. Verifikasi entri `Allocation created by Budi S` di bawahnya tetap berisi `Notes: Batch uji`
21. Tutup modal Allocation Log dengan `[×]`
22. Buka Activity Log di Admin Console dan cari Allocation ID transaksi itu
23. Verifikasi Activity Log memuat tepat satu baris Edit baru: Action `Edit`, Field `Notes`, Old Value `Batch uji`, New Value `—`
24. Verifikasi tidak ada baris untuk Quantity atau Pay From (baris Edit hanya satu, yaitu baris Notes pada langkah 23)

### TC-AC-ACHA-387: Entri `Allocation canceled` tanpa Description

25. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya, muat ulang halaman (F5), buka menu row action `⋯` pada transaksi itu, klik `Cancel Allocation`, lalu konfirmasi di dialog
26. Buka menu row action `⋯` pada transaksi dan klik `Allocation Log`
27. Verifikasi entri teratas berjudul `Allocation canceled by Budi S`
28. Verifikasi entri teratas memuat Date & Time
29. Verifikasi entri teratas tidak memuat baris Description (tidak ada alasan)
30. Tutup modal Allocation Log dengan `[×]`

### Ganti akun ke Hendra Wibowo (Total Control Distributor)

31. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-384: Entri `Allocation approved` tanpa Description

32. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya, buka Approvals > Device Allocation, klik `[Approve]` pada transaksi itu, lalu konfirmasi sampai toast sukses
33. Buka Allocation > Device Allocation, buka menu row action `⋯` pada transaksi itu, dan klik `Allocation Log`
34. Verifikasi entri teratas berjudul `Allocation approved by Hendra W`
35. Verifikasi entri teratas memuat Date & Time
36. Verifikasi entri teratas tidak memuat baris Description
37. Verifikasi entri `Allocation created by Budi S` tetap ada di bawahnya
38. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-386: Entri `Allocation rejected` memuat Rejection Reason

39. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya, buka Approvals > Device Allocation, isi Rejection Reason `Stok belum siap` pada transaksi itu, klik `[Reject]`, lalu konfirmasi sampai toast sukses
40. Buka Allocation > Device Allocation, buka menu row action `⋯` pada transaksi itu, dan klik `Allocation Log`
41. Verifikasi entri teratas berjudul `Allocation rejected by Hendra W`
42. Verifikasi entri teratas memuat Description `Rejection Reason: Stok belum siap`
43. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-385: Jalur langsung hanya punya entri created

44. Buka menu row action `⋯` pada transaksi Completed jalur langsung milik Hendra Wibowo dan klik `Allocation Log`
45. Verifikasi modal Allocation Log tampil memuat tepat satu entri `Allocation created by Hendra W`
46. Verifikasi tidak ada entri `Allocation approved` karena jalur langsung tidak melewati persetujuan
47. Tutup modal Allocation Log dengan `[×]`

### Ganti akun ke Dewi Lestari (Principal)

48. Logout lalu login sebagai Group Member Principal `memberOnPrincipal` (Pre-setup #24), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-381: Baris Description kosong tidak ditampilkan: Notes dan Cost Principal

49. Buka menu row action `⋯` pada transaksi Waiting for Approval milik MB_PRIN (Handheld Reader Long Range, Quantity 10) dan klik `Allocation Log`
50. Verifikasi judul entri `Allocation created by Dewi L`
51. Verifikasi baris Description: `Category: Handheld Reader`, `Type: Long Range`, `Quantity: 10`, `From: PT ABC`
52. Verifikasi tidak ada baris `Notes` (kosong tidak ditampilkan)
53. Verifikasi tidak ada baris `Cost` (pengirim Principal tanpa biaya)
54. Tutup modal Allocation Log dengan `[×]`

### Ganti akun ke Andi Wijaya (Partner)

55. Logout lalu login sebagai Group Member Partner CV Mitra Solusi `memberOnPartner1` (Pre-setup #44), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-382: Category tanpa Type tidak menampilkan baris Type

56. Buka menu row action `⋯` pada transaksi Waiting for Approval milik MB_P1 (NFC, Quantity 10) dan klik `Allocation Log`
57. Verifikasi judul entri `Allocation created by Andi W`
58. Verifikasi baris Description: `Category: NFC`, `Quantity: 10`, `From: CV Mitra Solusi`, `Cost: $15.00`
59. Verifikasi tidak ada baris `Type` (Category tanpa Type)
60. Verifikasi tidak ada baris `Notes`
61. Tutup modal Allocation Log dengan `[×]`

### Ganti akun ke Budi Santoso (blok geser jam di akhir spec)

62. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-388: Entri `Allocation auto-canceled` memuat Reason

63. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya dan T1 (dibaca lewat fixture), lalu muat ulang halaman (F5)
64. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture untuk transaksi itu
65. Muat ulang halaman tiap 5 detik sampai status transaksi itu `Canceled` (batas tunggu 2 menit)
66. Verifikasi status transaksi itu `Canceled`
67. Pulihkan jam server ke waktu nyata lewat fixture
68. Buka menu row action `⋯` pada transaksi itu dan klik `Allocation Log`
69. Verifikasi entri teratas berjudul `Allocation auto-canceled` tanpa `by` dan tanpa nama pelaku
70. Verifikasi entri teratas memuat Description `Reason: Approval timeout`
71. Tutup modal Allocation Log dengan `[×]`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 5b). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC dikelompokkan per akun aktor (Budi Santoso, Hendra Wibowo, Dewi Lestari, Andi Wijaya) dan TC-AC-ACHA-383 ditaruh sebelum TC-AC-ACHA-490, 387 supaya entri `Allocation edited` mengikuti transaksi yang sama dengan blok awal; TC-AC-ACHA-388 (geser jam server) ditaruh paling akhir dengan ganti akun kembali ke Budi Santoso, supaya pembatalan Timeout global tidak membatalkan transaksi Waiting for Approval blok lain sebelum dibaca (S-09). Tiap aksi yang mengubah status memakai salinan transaksi baru (S-04, S-06).
- Langkah penghubung (S-03): langkah 7, 14, 21, 30, 38, 43, 47, 54, 61, 71 (tutup modal Allocation Log); langkah 15, 25, 32, 39 (aksi pemicu bersama pembuatan salinan yang hasilnya diasersi di Allocation Log); langkah 63 sampai 65 dan 67 (salinan, geser jam, polling job, pulihkan jam); langkah 31, 48, 55, 62 (ganti akun, S-07); langkah 1, 9, 16, 26, 33, 40, 44, 49, 56, 68 (buka modal).
- Baris target (R-16): transaksi milik spec ditemukan lewat Search Allocation ID yang dicatat saat fixture sebagai langkah penghubung tanpa `Verifikasi` sebelum aksi baris; langkah ini tidak diberi nomor sendiri, dan Search dikosongkan lewat klik `(←)` pada kotak Search sebelum blok berikutnya.
- Ukuran spec: 71 langkah (melewati sekitar 35 langkah). Alasan: semua blok satu topik, entri Allocation Log per kejadian, dan tiap blok memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun (S-07) dan penutupan modal menambah langkah tanpa verifikasi.
- Asersi tambahan di luar Expected TC: langkah 66 (anchor status Canceled sebelum membuka Allocation Log); langkah 24 (jumlah baris Edit pada Activity Log, anchor positif langkah 23).
- Pengecualian S-12 nama literal (Lampiran A butir A-11): Notes `Batch uji`, `Batch revisi`, dan `Stok belum siap` ditulis persis seperti TC karena diasersi pada Description Allocation Log; transaksi dibedakan lewat Allocation ID unik.
- Temuan untuk QA:
  - TC-AC-ACHA-380 menyebut Date & Time "sesuai General Settings" tanpa menulis nilai persisnya; spec mengasersi format `dd/MM/yy` dan 24 jam dari Pre-setup #1 tanpa nilai tanggal absolut.
  - TC-AC-ACHA-490 langkah 3 membuka Activity Log tanpa menyebut siapa yang membuka; spec memakai aktor yang sama dengan pelaku Edit (Budi Santoso).
  - TC-AC-ACHA-384, 386, 387, 388 tidak menyebut Date & Time tertentu; hanya keberadaan Date & Time yang diasersi pada TC-AC-ACHA-384 dan 387.
  - Post Condition TC-AC-ACHA-383 ("Satu entri `Allocation edited` ditambahkan") dan TC-AC-ACHA-490 tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
