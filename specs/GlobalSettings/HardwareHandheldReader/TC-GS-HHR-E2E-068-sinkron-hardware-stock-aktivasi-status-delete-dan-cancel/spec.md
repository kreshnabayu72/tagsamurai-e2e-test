---
id: TC-GS-HHR-E2E-068-sinkron-hardware-stock-aktivasi-status-delete-dan-cancel
title: "Sinkron Admin Console Hardware Stock: Efek Aktivasi, Mark as, Bulk, Delete, Cancel Request, dan Current Power pada Unit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-373
  - TC-GS-HHR-374
  - TC-GS-HHR-375
  - TC-GS-HHR-376
  - TC-GS-HHR-377
  - TC-GS-HHR-378
  - TC-GS-HHR-379
  - TC-GS-HHR-380
  - TC-GS-HHR-381
  - TC-GS-HHR-382
  - TC-GS-HHR-383
  - TC-GS-HHR-384
coverage:
  web: automated
---

# Sinkron Admin Console Hardware Stock: Efek Aktivasi, Mark as, Bulk, Delete, Cancel Request, dan Current Power pada Unit

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, dua sesi: Client A dan Principal di Admin Console). Blok TC-GS-HHR-373, TC-GS-HHR-374, TC-GS-HHR-375, dan TC-GS-HHR-384 juga bergantung simulator reader USB (kelas d). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `principal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

- Login Sesi A dilakukan di hook `before`; Sesi P dibuka dengan langkah ganti akun eksplisit (langkah 1) karena hasilnya diasersi di Hardware Stock. Hook `after` menutup Sesi P dan mengembalikan sesi ke akun default suite (Sesi A).
- TC tidak menyebut siapa yang membuka Admin Console > Hardware Stock; spec memakai Principal (lihat Temuan untuk QA).
- Data (Client A, plan Growth, Seed Reader A DD-01 s.d. DD-10 dari fixture BE): DD-01 (Available, Jalur A, unit `SN-HHR-00101`), DD-03 (Damaged, `SN-HHR-00103`), DD-04 (Missing, `SN-HHR-00104`), DD-07 (Available, Jalur B, `SN-HHR-00108`), DD-10 (Waiting for Approval, Jalur A, `SN-HHR-00205`). Stok Principal HS-01 `SN-HHR-00201` (Long Range, Current Power 22 dBm, Available), HS-04 `SN-HHR-00204` (aktif di Client C), serial Jalur B `SN-HHR-00302` (tidak ada di stok Principal). Katalog Device Name DN-01 s.d. DN-07 (dibaca Client read-only).
- Kemampuan teknis (disediakan tim FE/BE):
  - Konteks browser kedua untuk Sesi P.
  - Pemulihan Seed Reader A dan stok Hardware Stock ke keadaan Tabel Data Uji TC antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
  - Simulator reader USB/driver lokal untuk Sync `SN-HHR-00201`, `SN-HHR-00204`, dan `SN-HHR-00302` (mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
  - Perubahan Current Power unit `SN-HHR-00201` dari 22 dBm menjadi 18 dBm di Hardware Stock oleh Principal (blok TC-GS-HHR-384; hasilnya dipakai sebagai precondition dan tidak diasersi).
  - Pembacaan notifikasi Principal (blok TC-GS-HHR-382; hanya jumlah sebelum dan sesudah).
- Baseline: `Status` unit dan total unit Hardware Stock dicatat sebelum aksi tiap blok.
- State global yang diubah: Seed Reader A, status unit di Hardware Stock, Current Power unit `SN-HHR-00201`. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi P) dan login sebagai Principal Bambang Hartono

### Blok 1 - Mark as Damaged, Mark as Missing, Mark as Available Jalur A: TC-GS-HHR-376, TC-GS-HHR-377, TC-GS-HHR-378

Untuk setiap baris tabel "Iterasi Mark as" (langkah 2 sampai 9):

| Iterasi | TC | Aksi | Reader | Unit | Nilai `Client Reported Condition` |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-376 | `Mark as Damaged` | DD-01 | `SN-HHR-00101` | `Damaged` |
| 2 | TC-GS-HHR-377 | `Mark as Missing` | DD-01 | `SN-HHR-00101` | `Missing` |
| 3 | TC-GS-HHR-378 | `Mark as Available` | DD-03 | `SN-HHR-00103` | `Active` |

2. Pulihkan Seed Reader A ke keadaan Tabel Data Uji Dinamis TC
3. Sesi P: buka Admin Console > Hardware Stock, ketik Search unit `{Unit}`, tekan Enter, catat `Status` unit sebagai Status awal
4. Sesi A: muat ulang Handheld Reader, buka Overlay row action baris `{Reader}`, klik `{Aksi}`
5. Sesi A: klik tombol konfirmasi `[{Aksi}]` pada dialog
6. Tunggu aksi selesai
7. Sesi P: muat ulang Hardware Stock, ketik Search unit `{Unit}`, tekan Enter
8. Verifikasi field `Client Reported Condition` unit `{Unit}` menampilkan `{Nilai Client Reported Condition}`
9. Verifikasi `Status` unit `{Unit}` sama dengan Status awal (tidak berubah)

### Blok 2 - Bulk Mark as Damaged dan Bulk Mark as Available: TC-GS-HHR-379, TC-GS-HHR-380

10. Pulihkan Seed Reader A
11. Sesi P: buka Hardware Stock, catat total unit, ketik Search `SN-HHR-00101`, tekan Enter, catat `Status` unit sebagai Status awal
12. Sesi A: muat ulang Handheld Reader, centang checkbox baris DD-01 dan DD-07
13. Sesi A: klik tombol `Bulk Action`
14. Sesi A: klik `Mark as Damaged`
15. Sesi A: klik `[Mark as Damaged]` pada dialog
16. Tunggu aksi selesai
17. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00101`, tekan Enter
18. Verifikasi field `Client Reported Condition` unit `SN-HHR-00101` menampilkan `Damaged`
19. Verifikasi `Status` unit `SN-HHR-00101` sama dengan Status awal (tidak berubah)
20. Sesi P: ketik Search `SN-HHR-00108`, tekan Enter
21. Verifikasi `SN-HHR-00108` tidak ada di Hardware Stock (empty state `No results found`)
22. Verifikasi total unit Hardware Stock sama dengan total unit yang dicatat (tidak ada perubahan pada stok)
23. Pulihkan Seed Reader A
24. Sesi P: ketik Search `SN-HHR-00103`, tekan Enter, catat `Status` unit sebagai Status awal unit 1; ketik Search `SN-HHR-00104`, tekan Enter, catat `Status` unit sebagai Status awal unit 2
25. Sesi A: muat ulang Handheld Reader, centang checkbox baris DD-03 dan DD-04
26. Sesi A: klik tombol `Bulk Action`
27. Sesi A: klik `Mark as Available`
28. Sesi A: klik `[Mark as Available]` pada dialog
29. Tunggu aksi selesai
30. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00103`, tekan Enter
31. Verifikasi field `Client Reported Condition` unit `SN-HHR-00103` menampilkan `Active`
32. Verifikasi `Status` unit `SN-HHR-00103` sama dengan Status awal unit 1
33. Sesi P: ketik Search `SN-HHR-00104`, tekan Enter
34. Verifikasi field `Client Reported Condition` unit `SN-HHR-00104` menampilkan `Active`
35. Verifikasi `Status` unit `SN-HHR-00104` sama dengan Status awal unit 2

### Blok 3 - Mark as Damaged reader Jalur B dan Cancel Request: TC-GS-HHR-381, TC-GS-HHR-383

36. Pulihkan Seed Reader A
37. Sesi P: buka Hardware Stock, catat total unit
38. Sesi A: muat ulang Handheld Reader, buka Overlay row action baris DD-07, klik `Mark as Damaged`
39. Sesi A: klik `[Mark as Damaged]` pada dialog
40. Tunggu aksi selesai
41. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00108`, tekan Enter
42. Verifikasi `SN-HHR-00108` tidak ada di Hardware Stock (empty state `No results found`)
43. Verifikasi total unit Hardware Stock sama dengan total unit yang dicatat (tidak ada perubahan pada stok)
44. Pulihkan Seed Reader A
45. Sesi P: ketik Search `SN-HHR-00205`, tekan Enter, catat `Status` unit sebagai Status awal
46. Sesi A: muat ulang Handheld Reader, buka Overlay row action baris DD-10, klik `Cancel Request`
47. Sesi A: klik `[Cancel Request]` pada dialog
48. Tunggu aksi selesai
49. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00205`, tekan Enter
50. Verifikasi `Status` unit `SN-HHR-00205` sama dengan Status awal

### Blok 4 - Delete reader Jalur A: TC-GS-HHR-382

51. Pulihkan Seed Reader A
52. Sesi P: ketik Search `SN-HHR-00101`, tekan Enter, catat `Status` unit; catat jumlah notifikasi Principal sebagai baseline
53. Sesi A: muat ulang Handheld Reader, buka Overlay row action baris DD-01, klik `Delete`
54. Sesi A: klik `[Delete]` pada dialog
55. Tunggu aksi selesai
56. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00101`, tekan Enter
57. Verifikasi `Status` unit `SN-HHR-00101` berubah dari `In Use` menjadi `Available`
58. Verifikasi unit `SN-HHR-00101` tampil di Tab Available
59. Klik Tab In Use, ketik Search `SN-HHR-00101`, tekan Enter
60. Verifikasi unit `SN-HHR-00101` tidak ada di Tab In Use (empty state `No results found`)
61. Buka Changelog Hardware Stock
62. Verifikasi Changelog Hardware Stock memuat entri `Device Released` dengan Old Value `In Use` dan New Value `Available`
63. Verifikasi `Modified By` entri `Device Released` adalah nama pelaku Client (Sari Dewi)
64. Verifikasi jumlah notifikasi Principal sama dengan baseline (tidak ada notifikasi baru)

### Blok 5 - Aktivasi dan Current Power yang membaca reader USB: TC-GS-HHR-373, TC-GS-HHR-374, TC-GS-HHR-375, TC-GS-HHR-384

65. Pulihkan Seed Reader A dan stok Hardware Stock
66. Sesi P: tutup Changelog Hardware Stock, buka Tab Available, ketik Search `SN-HHR-00201`, tekan Enter, catat `Status` unit sebagai Status awal (`Available`)
67. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`
68. Sesi A: klik `Long Range` pada Overlay `Select Range Type`
69. Sesi A: klik `[Sync]` (reader USB HS-01 `SN-HHR-00201` tersambung)
70. Sesi A: klik `[Submit]`
71. Tunggu aksi selesai
72. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00201`, tekan Enter
73. Verifikasi `Status` unit `SN-HHR-00201` berubah dari `Available` menjadi `In Use`
74. Klik Tab In Use, ketik Search `SN-HHR-00201`, tekan Enter
75. Verifikasi unit `SN-HHR-00201` tampil di Tab In Use
76. Verifikasi pemakai unit `SN-HHR-00201` adalah Client A
77. Klik Tab Available, ketik Search `SN-HHR-00201`, tekan Enter
78. Verifikasi unit `SN-HHR-00201` tidak ada di Tab Available (empty state `No results found`)
79. Pulihkan Seed Reader A dan stok Hardware Stock
80. Sesi P: ketik Search `SN-HHR-00204`, tekan Enter, catat `Status` unit sebagai Status awal
81. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range`, klik `[Sync]` (reader USB HS-04 `SN-HHR-00204` tersambung, aktif di Client C), klik `[Submit]` sehingga reader menjadi Waiting for Approval
82. Tunggu aksi selesai
83. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00204`, tekan Enter
84. Verifikasi `Status` unit `SN-HHR-00204` sama dengan Status awal
85. Pulihkan Seed Reader A dan stok Hardware Stock
86. Sesi P: buka Hardware Stock, catat total unit
87. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range`, klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
88. Sesi A: pilih `Chainway C72` pada `Device Name`, isi `Brand` `Chainway`, isi `Model/Type` `C72`, klik `[Submit]`
89. Tunggu aksi selesai
90. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00302`, tekan Enter
91. Verifikasi `SN-HHR-00302` tidak ditemukan di Hardware Stock (empty state `No results found`)
92. Verifikasi total unit Hardware Stock sama dengan total unit yang dicatat
93. Pulihkan Seed Reader A dan stok Hardware Stock
94. Sesi P: ubah Current Power unit `SN-HHR-00201` dari 22 dBm menjadi 18 dBm di Hardware Stock hingga tersimpan
95. Tunggu aksi selesai
96. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, pilih `Long Range` pada Overlay `Select Range Type`
97. Sesi A: klik `[Sync]` (reader USB HS-01 `SN-HHR-00201` tersambung)
98. Verifikasi slider `Reader Power` terisi nilai awal `18 dBm`
99. Sesi A: klik `✕`, klik `[Cancel Activation]`
100. Sesi P: pulihkan Current Power unit `SN-HHR-00201` menjadi 22 dBm di Hardware Stock hingga tersimpan

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7a). Label Manual Only (b) ada pada TC-GS-HHR-373, 374, 375, dan 384 (reader USB fisik); kebutuhannya ditulis di Prerequisites.
- Urutan blok: aksi yang tidak butuh reader USB di depan, aksi yang menghapus data (Delete, blok 4) sebelum blok reader USB, blok reader USB paling akhir sehingga kegagalan simulator tidak menutupi hasil blok sebelumnya (prinsip 3 butir 5).
- Langkah 2 sampai 9 diulang tiga kali sesuai tabel "Iterasi Mark as" (bagian 8b butir 7).
- Spec melewati sekitar 35 langkah dan mencampur dua jenis harness (dua sesi dan simulator USB) sesuai pembagian topik "sinkron Hardware Stock". Tiap blok berdiri sendiri: Seed Reader A dan stok dipulihkan di awal blok (langkah 2, 10, 23, 36, 44, 51, 65, 79, 85, 93), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan Seed Reader A dan stok, muat ulang, mencatat nilai awal, berpindah sesi, Tab In Use/Available, mencari unit lewat Search, menutup Changelog. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi (bagian 8b butir 8). Langkah 99 (`✕`, `[Cancel Activation]`) menutup Popup Activate yang sudah Sync.
- Catatan pembagian: perilaku sisi Client yang sama (Mark as, Delete, Cancel Request) diasersi di spec fungsional Mark as, Delete, dan Cancel Request; spec ini hanya mengasersi efeknya di Hardware Stock.
- Temuan untuk QA:
  - TC-GS-HHR-373 sampai TC-GS-HHR-384 menulis "Buka Admin Console > Hardware Stock" tanpa menyebut akun; Total Control Client A tidak punya akses Admin Console, sehingga spec memakai Principal (Sesi P).
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00201`, `SN-HHR-00204`, `SN-HHR-00302`) tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - TC-GS-HHR-376 sampai TC-GS-HHR-380 dan TC-GS-HHR-383 menyatakan "Status unit tidak berubah" tanpa langkah mencatat Status awal; spec menambahkan langkah mencatat Status awal sebagai baseline (S-12).
  - TC-GS-HHR-382 butir c ("Tidak ada notifikasi baru ke Principal") tidak menyebut cara membaca notifikasi; spec memakai jumlah notifikasi sebelum dan sesudah dengan kemampuan baca yang disediakan tim FE.
  - TC-GS-HHR-384 precondition e menyebut Principal mengubah Current Power di Hardware Stock tanpa langkah UI; spec menaruhnya sebagai langkah Sesi P tanpa `Verifikasi`.
  - TC-GS-HHR-375 dan TC-GS-HHR-374 tidak menyebut nama kolom untuk "total unit"; spec memakai total unit yang tampil di Hardware Stock.
  - Nama tombol konfirmasi dialog Mark as Missing dan Mark as Available (`[Mark as Missing]`, `[Mark as Available]`) tidak tertulis di bagian ini; spec mengikuti pola `[Mark as Damaged]` yang tertulis di TC-GS-HHR-430.
