---
id: TC-AC-ACHA-E2E-046-pencatatan-activity-log-dan-system-log
title: "Pencatatan Activity Log dan System Log per Aksi: Create, Resubmit, Edit, Approve, Reject, Cancel, Timeout, dan Entitas Target"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-370
  - TC-AC-ACHA-371
  - TC-AC-ACHA-372
  - TC-AC-ACHA-373
  - TC-AC-ACHA-374
  - TC-AC-ACHA-375
  - TC-AC-ACHA-376
  - TC-AC-ACHA-377
  - TC-AC-ACHA-378
  - TC-AC-ACHA-379
  - TC-AC-ACHA-472
  - TC-AC-ACHA-473
coverage:
  web: automated
---

# Pencatatan Activity Log dan System Log per Aksi: Create, Resubmit, Edit, Approve, Reject, Cancel, Timeout, dan Entitas Target

## Prerequisites

- Mode: FE+BE.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Env var password |
|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo (aktor hook `before`) | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `memberOnPartner2` | #47 | Siti Rahmawati (MB_P2) | `Spectra.env.AC_DA_MB_P2_PASSWORD` |
| `memberOnPartner1` | #44 | Andi Wijaya (MB_P1) | `Spectra.env.AC_DA_MB_P1_PASSWORD` |
| `totalControlPartner1` | #43 | Maya Putri | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| `totalControlPrincipal` | #21 | Admin Pratama | `Spectra.env.AC_TC_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan jam server.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #1 General Settings default (`dd/MM/yy`, 24 jam, Asia/Jakarta), #3 PT Global Distribusi dan #4 CV Mitra Solusi, #7 Client PT Sejahtera Logistik, #8 Client PT Retail Makmur, #14 dan #15 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00, #17 kantong CV Mitra Solusi saldo $2,000.00, #18 dan #19 kantong CV Karya Mandiri, #63 Approval Timeout 3 day(s).
- Data seeding milik spec (disediakan lewat fixture API tim FE/BE; salinan milik spec dari Pre-setup #49, #50, #52, #59 supaya Pre-setup bersama tidak diubah, S-06). Salinan Waiting for Approval dibuat lewat fixture tepat pada langkah pembuka tiap blok (bukan di hook `before`), sehingga waktu pembuatannya (T1) per blok dan tidak ikut terbatalkan oleh blok lain:
  - Transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00): satu salinan baru untuk tiap blok TC-AC-ACHA-372, 373, 375, 376, 377, 378. Dicatat sebagai `Allocation ID transaksi blok`.
  - Transaksi Waiting for Approval milik MB_P2 (NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT Global Distribusi (Distributor)`, Total Cost $60.00, Reserve $60.00 pada kantong A CV Karya Mandiri) untuk TC-AC-ACHA-374.
  - Transaksi Canceled milik MB_ON (BLE Gateway, Quantity 50, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch lama`) untuk TC-AC-ACHA-472; transaksi Canceled milik Hendra Wibowo untuk TC-AC-ACHA-473.
  - Saldo kantong PT Global Distribusi $20,000.00 dan Reserved awal mengikuti Pre-setup #16 (dipulihkan fixture di hook `before`).
- Pemulihan dan efek (R-08, S-06): hook `after` memulihkan seed ke 30 baris dan jam server lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec ini tidak dapat dihapus lewat UI dan audit trail (Activity Log, System Log) bertambah permanen, sehingga asersi log memakai baseline dan Allocation ID. Tidak ada Pre-setup bersama yang diubah selain jam server dan saldo/Reserve kantong PT Global Distribusi.
- Baseline log (S-12): Allocation ID transaksi yang dibuat lewat UI di spec ini baru, sehingga baseline baris log nol. Untuk transaksi hasil fixture, jumlah baris Activity Log ber-Name Allocation ID itu dicatat sebelum aksi pemicu dan asersi memakai selisih terhadap baseline. Pencarian log memakai Allocation ID, bukan posisi teratas.
- Kemampuan teknis: pergeseran jam server absolut ke `T1 + 3 hari + 1 menit` lewat fixture yang disediakan tim FE/BE (T1 = waktu terbit transaksi, dibaca lewat fixture; margin 1 menit terhadap batas 3 hari dihitung dari T1, bukan dari waktu hook); sesi UI dan API tetap valid saat jam digeser (dinyatakan di `suite.md`); jam browser tidak diubah karena Timeout dihitung murni di server dan tidak diamati lewat hitung mundur UI. Jam server dipulihkan sebelum Activity Log dibuka (S-09). Geser jam membuat job Timeout membatalkan semua transaksi Waiting for Approval yang melewati 3 hari dari waktu terbitnya, termasuk transaksi blok lain yang masih Waiting; karena itu blok TC-AC-ACHA-378 berada di akhir spec dan asersinya per Allocation ID. Menunggu satu siklus job pengecekan memakai idiom polling: muat ulang List tiap 5 detik sampai status transaksi `Canceled`, batas tunggu 2 menit.
- Suite berjalan serial (`parallel: false`): General Settings dan jam server adalah state global.

## Test Steps

### TC-AC-ACHA-370: Dokumen audit Create jalur langsung

1. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID baru dari List
2. Buka Activity Log di Admin Console dan cari Allocation ID baru
3. Verifikasi Activity Log memuat tepat satu baris: Action `Create`, Object `Device Allocation`, Name = Allocation ID baru, Field `Status`, Old Value `—`, New Value `Completed`, Modified By `Hendra Wibowo`
4. Buka System Log pada Detail User `Hendra Wibowo` (Settings > User > Detail User) dan cari Allocation ID baru
5. Verifikasi System Log aktor memuat satu baris yang sama dengan kolom Date, Action `Create`, Object `Device Allocation`, Name, Field `Status`, Old Value `—`, New Value `Completed`, tanpa kolom Modified By

### TC-AC-ACHA-473: Dokumen audit Create hasil Resubmit jalur langsung

6. Buka Activity Log, cari Allocation ID transaksi Canceled milik Hendra Wibowo, dan catat jumlah barisnya sebagai baseline transaksi lama
7. Buka Allocation > Device Allocation dan klik `Resubmit` pada transaksi Canceled itu
8. Klik `[Submit]` tanpa mengubah isian dan catat Allocation ID baru dari List
9. Buka Activity Log dan cari Allocation ID baru
10. Verifikasi Activity Log memuat tepat satu baris: Action `Create`, Object `Device Allocation`, Name = Allocation ID baru, Field `Status`, Old Value `—`, New Value `Completed`, Modified By `Hendra Wibowo`
11. Buka System Log pada Detail User `Hendra Wibowo` dan cari Allocation ID baru
12. Verifikasi System Log aktor memuat satu baris yang sama tanpa kolom Modified By
13. Buka Activity Log, cari Allocation ID transaksi lama, dan hitung barisnya
14. Verifikasi jumlah baris transaksi lama sama dengan baseline langkah 6 (tidak ada dokumen audit baru untuk transaksi lama yang Canceled)

### TC-AC-ACHA-375: Approve menulis satu dokumen audit dengan Modified By approver

15. Buat salinan transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya (`Allocation ID transaksi blok`), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline
16. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi itu, konfirmasi, lalu tunggu aksi selesai (dialog tertutup)
17. Buka Activity Log dan cari `Allocation ID transaksi blok`
18. Verifikasi Activity Log memuat tepat satu baris Approve baru terhadap baseline langkah 15: Action `Approve`, Object `Device Allocation`, Field `Status`, Old Value `Waiting for Approval`, New Value `Completed`, Modified By `Hendra Wibowo`
19. Buka System Log pada Detail User `Hendra Wibowo` dan cari `Allocation ID transaksi blok`
20. Verifikasi System Log aktor (approver) memuat satu baris Approve yang sama
21. Verifikasi System Log memuat tepat satu baris Approve untuk Allocation ID itu (tidak ada baris kedua dari modul Approvals untuk keputusan yang sama); Activity Log sudah diverifikasi tepat satu baris Approve baru pada langkah 18

### TC-AC-ACHA-376: Reject menulis baris Status dan Rejection Reason

22. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya (`Allocation ID transaksi blok`), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline
23. Buka Approvals > Device Allocation, isi Rejection Reason `Stok belum siap`, klik `[Reject]`, konfirmasi, lalu tunggu aksi selesai (dialog tertutup)
24. Buka Activity Log dan cari `Allocation ID transaksi blok`
25. Verifikasi Activity Log menambah baris baru terhadap baseline langkah 22: Field `Status` (Old Value `Waiting for Approval`, New Value `Rejected`), Modified By `Hendra Wibowo`
26. Verifikasi Activity Log menambah baris baru kedua dalam aksi Reject yang sama: Field `Rejection Reason` (Old Value `—`, New Value `Stok belum siap`), Modified By `Hendra Wibowo`, sehingga total baris baru terhadap baseline langkah 22 tepat dua

### Ganti akun ke Budi Santoso (MB_ON)

27. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-371: Dokumen audit Create jalur persetujuan

28. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID baru dari List
29. Buka Activity Log di Admin Console dan cari Allocation ID baru
30. Verifikasi Activity Log memuat tepat satu baris: Action `Create`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Budi Santoso`
31. Verifikasi tidak ada baris tambahan untuk Reserve saldo atau pengiriman ke Approvals: Allocation ID baru hanya memuat satu baris pada Activity Log

### TC-AC-ACHA-472: Dokumen audit Create hasil Resubmit jalur persetujuan

32. Buka Activity Log, cari Allocation ID transaksi Canceled milik MB_ON, dan catat jumlah barisnya sebagai baseline transaksi lama
33. Buka Allocation > Device Allocation dan klik `Resubmit` pada transaksi Canceled itu
34. Klik `[Submit]` tanpa mengubah isian dan catat Allocation ID baru dari List
35. Buka Activity Log dan cari Allocation ID baru
36. Verifikasi Activity Log memuat tepat satu baris: Action `Create`, Object `Device Allocation`, Name = Allocation ID baru, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Budi Santoso`
37. Buka System Log pada Detail User `Budi Santoso` dan cari Allocation ID baru
38. Verifikasi System Log aktor memuat satu baris yang sama tanpa kolom Modified By
39. Buka Activity Log, cari Allocation ID transaksi lama, dan hitung barisnya
40. Verifikasi jumlah baris transaksi lama sama dengan baseline langkah 32 (tidak ada dokumen audit baru untuk transaksi lama yang Canceled)

### TC-AC-ACHA-372: Edit Quantity menulis satu baris Old/New

41. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya (`Allocation ID transaksi blok`), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline
42. Buka Allocation > Device Allocation, klik `Edit` pada transaksi itu, ubah Quantity dari `100` menjadi `120`, klik `[Save]`, lalu tunggu aksi selesai (form tertutup)
43. Buka Activity Log dan cari `Allocation ID transaksi blok`
44. Verifikasi Activity Log menambah tepat satu baris terhadap baseline langkah 41: Action `Edit`, Field `Quantity`, Old Value `100`, New Value `120`, Modified By `Budi Santoso`
45. Verifikasi tidak ada baris untuk Notes atau Pay From karena nilainya tidak berubah (baris baru hanya satu, yaitu baris Quantity pada langkah 44)

### TC-AC-ACHA-373: Edit Notes menulis satu baris Old/New

46. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya (`Allocation ID transaksi blok`), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline
47. Buka Allocation > Device Allocation, klik `Edit` pada transaksi itu, ubah Notes dari `Batch uji` menjadi `Batch revisi`, klik `[Save]`, lalu tunggu aksi selesai (form tertutup)
48. Buka Activity Log dan cari `Allocation ID transaksi blok`
49. Verifikasi Activity Log menambah tepat satu baris terhadap baseline langkah 46: Action `Edit`, Field `Notes`, Old Value `Batch uji`, New Value `Batch revisi`
50. Verifikasi tidak ada baris untuk Quantity atau Pay From (baris baru hanya satu, yaitu baris Notes pada langkah 49)

### TC-AC-ACHA-377: Cancel manual menulis baris Status tanpa Cancellation Reason

51. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture dan catat Allocation ID-nya (`Allocation ID transaksi blok`), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline
52. Buka Allocation > Device Allocation, klik `Cancel Allocation` pada transaksi itu, konfirmasi di dialog, lalu tunggu aksi selesai (dialog tertutup)
53. Buka Activity Log dan cari `Allocation ID transaksi blok`
54. Verifikasi Activity Log menambah tepat satu baris terhadap baseline langkah 51: Action `Cancel`, Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, Modified By `Budi Santoso`
55. Verifikasi tidak ada baris Field `Cancellation Reason` untuk Allocation ID itu (Cancel manual tidak membawa alasan)

### Ganti akun ke Siti Rahmawati (MB_P2)

56. Logout lalu login sebagai Group Member Partner CV Karya Mandiri `memberOnPartner2` (Pre-setup #47), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-374: Edit Pay From menulis satu baris Old/New berformat Nama (Type)

57. Buka Activity Log, cari Allocation ID transaksi Waiting for Approval milik MB_P2, dan catat jumlah barisnya sebagai baseline
58. Buka Allocation > Device Allocation, klik `Edit` pada transaksi itu, ganti Pay From menjadi `PT ABC (Principal)`, klik `[Save]`, lalu tunggu aksi selesai (form tertutup)
59. Buka Activity Log dan cari Allocation ID transaksi itu
60. Verifikasi Activity Log menambah tepat satu baris terhadap baseline langkah 57: Action `Edit`, Field `Pay From`, Old Value `PT Global Distribusi (Distributor)`, New Value `PT ABC (Principal)`
61. Verifikasi format nama kantong pada Old Value dan New Value sama dengan kolom Paid From di List (Nama diikuti Type dalam kurung)

### Ganti akun ke Andi Wijaya (MB_P1) lalu Maya Putri

62. Logout lalu login sebagai Group Member Partner CV Mitra Solusi `memberOnPartner1` (Pre-setup #44), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-379: Entitas target dokumen audit adalah entitas pengirim

63. Klik `[+ Allocation]`, pilih Category `TAG - NFC`, Client `PT Retail Makmur`, isi Quantity `10`, klik `[Submit]`, lalu catat Allocation ID baru dari List
64. Logout lalu login sebagai Total Control Partner CV Mitra Solusi `totalControlPartner1` (Pre-setup #43)
65. Buka Activity Log di Admin Console dan cari Allocation ID baru
66. Verifikasi baris Create tampil pada Activity Log entitas pengirim CV Mitra Solusi dengan Name = Allocation ID baru dan Modified By `Andi Wijaya`
67. Verifikasi dokumen audit memakai entitas pengirim (From) CV Mitra Solusi sebagai entitas target: baris tampil pada Activity Log milik CV Mitra Solusi

### Ganti akun ke Admin Pratama (Principal)

68. Logout lalu login sebagai Total Control Principal `totalControlPrincipal` (Pre-setup #21)

### TC-AC-ACHA-378: Timeout Auto-Cancel: Modified By System, Cancellation Reason, tanpa System Log

69. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya (`Allocation ID transaksi blok`) dan T1 (dibaca lewat fixture), lalu buka Activity Log, cari Allocation ID itu, dan catat jumlah barisnya sebagai baseline Activity Log
70. Buka System Log pada Detail User `Budi Santoso` dan pada Detail User `Hendra Wibowo`, cari Allocation ID itu, dan catat jumlah barisnya pada masing-masing sebagai baseline System Log
71. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture
72. Buka Allocation > Device Allocation dan muat ulang List tiap 5 detik sampai status transaksi itu `Canceled` (batas tunggu 2 menit)
73. Verifikasi status transaksi `Canceled`
74. Pulihkan jam server ke waktu nyata lewat fixture
75. Buka Activity Log dan cari `Allocation ID transaksi blok`
76. Verifikasi Activity Log menambah satu dokumen Cancel terhadap baseline langkah 69 dengan baris Field `Status` (Old Value `Waiting for Approval`, New Value `Canceled`), Modified By `System`
77. Verifikasi dokumen Cancel yang sama memuat baris Field `Cancellation Reason` (Old Value `—`, New Value `approval timeout`), Modified By `System`, sehingga total baris baru terhadap baseline langkah 69 tepat dua
78. Buka System Log pada Detail User `Budi Santoso` dan `Hendra Wibowo` dan cari Allocation ID itu
79. Verifikasi System Log `Budi Santoso` (pembuat) tidak menambah baris apa pun untuk pembatalan ini: jumlah baris sama dengan baseline langkah 70
80. Verifikasi System Log `Hendra Wibowo` (approver) tidak menambah baris apa pun untuk pembatalan ini: jumlah baris sama dengan baseline langkah 70

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 5a). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC berbeda dari nomor TC: dikelompokkan per akun aktor (Hendra Wibowo, Budi Santoso, Siti Rahmawati, Andi Wijaya lalu Maya Putri, Admin Pratama) supaya ganti akun minimal; aksi yang mengubah status memakai salinan transaksi baru sehingga tidak saling bergantung (S-04, S-06).
- Langkah penghubung (S-03): langkah baca-log berpola (buka surface, cari entri) pada langkah 2, 4, 9, 11, 17, 19, 24, 29, 35, 37, 43, 48, 53, 59, 65, 75, 78; langkah baseline 6, 15, 22, 32, 41, 46, 51, 57, 69, 70; langkah 13 dan 39 (hitung ulang transaksi lama); langkah 27, 56, 62, 64, 68 (ganti akun, S-07); langkah 71 sampai 74 (geser dan pulihkan jam server, tunggu job lewat polling, S-09); langkah 73 adalah anchor status Canceled sebelum asersi log.
- Asersi tambahan di luar Expected TC: langkah 14 memakai pola TC-AC-ACHA-472 c pada TC-AC-ACHA-473 (TC-AC-ACHA-473 tidak punya butir c), dan langkah 40 adalah TC-AC-ACHA-472 c; keduanya memakai selisih terhadap baseline karena Activity Log tidak bisa dibersihkan (S-12); langkah 31, 45, 50, 55, 21, 79, 80 adalah asersi jumlah atau absence field yang menjadi bagian aksi nyata di spec ini, dengan Verifikasi anchor positif tepat sebelumnya (baris yang diharapkan), sehingga bukan asersi absence kelas g.
- P-1 (state berat) untuk langkah 79 dan 80 (TC-AC-ACHA-378 b, "tanpa baris System Log"): konteksnya bergantung pada state berat yang baru dibangun, yaitu transaksi Waiting for Approval dengan jam server digeser dan job Timeout; asersi absence tidak dipindah ke spec absence. Baseline System Log dicatat di langkah 70.
- Baris target (R-16): transaksi di List (Resubmit, Edit, Cancel) ditemukan lewat Search Allocation ID yang dicatat saat fixture sebagai langkah penghubung tanpa `Verifikasi`; langkah ini tidak diberi nomor sendiri.
- Langkah 16, 23, 42, 47, 52, dan 58 memuat "tunggu aksi selesai" sebagai penutup aksi sebelum pindah surface (bagian 8b butir 8, S-03).
- Ukuran spec: 80 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok memeriksa satu topik, dokumen audit per aksi di dua surface (Activity Log dan System Log); tiap blok memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah baca-log berpola tidak dihitung menurut bagian 3 konvensi (Smell) dan ganti akun eksplisit (S-07) menambah langkah tanpa verifikasi.
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Notes `Batch uji` dan `Batch revisi`, serta nilai `Stok belum siap`, ditulis persis seperti TC karena diasersi sebagai Old Value atau New Value; transaksi dibedakan lewat Allocation ID unik sehingga tidak bentrok antar run.
- Nama env var password per akun mengikuti daftar di `suite.md` (satu nama satu akun: `AC_DA_TC_DIST_PASSWORD`, `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD`, `AC_DA_MB_P1_PASSWORD`, `AC_DA_TC_P1_PASSWORD`, `AC_TC_PASSWORD`); Pre-setup TC tidak menyebut password per akun, sehingga nama ini didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Temuan untuk QA:
  - TC-AC-ACHA-379 b ("bukan Client penerima PT Retail Makmur") tidak punya langkah observasi pada sisi Client; precondition tidak memuat akun Client yang bisa membaca Activity Log. Spec hanya mengasersi bahwa baris tampil pada Activity Log entitas pengirim.
  - TC-AC-ACHA-378 langkah 3 menyebut System Log "milik Budi Santoso (pembuat) dan milik Hendra Wibowo" yang dibuka oleh aktor Total Control Principal; precondition tidak menyatakan Principal berhak membuka Detail User entitas Distributor. Spec mengikuti TC.
  - TC-AC-ACHA-370 langkah 3 dan TC-AC-ACHA-472/473 langkah 4 membuka System Log Detail User aktor tanpa menyebut siapa yang membuka; spec memakai aktor yang sama dengan pelaku aksi.
  - TC-AC-ACHA-376 Expected tidak menyebut Allocation ID target dan tidak menyebut baseline; spec memakai selisih terhadap baseline (S-12).
  - Post Condition TC-AC-ACHA-370, 371, 372, 373, 374, 375, 376, 377, 378, 472, 473 ("Satu dokumen audit ...") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
