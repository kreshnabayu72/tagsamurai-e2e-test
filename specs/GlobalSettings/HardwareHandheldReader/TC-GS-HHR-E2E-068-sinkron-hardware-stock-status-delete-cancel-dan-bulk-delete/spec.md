---
id: TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete
title: "Sinkron Admin Console Hardware Stock: Efek Mark as, Bulk, Delete, Bulk Delete, dan Cancel Request pada Unit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-217
  - TC-GS-HHR-376
  - TC-GS-HHR-377
  - TC-GS-HHR-378
  - TC-GS-HHR-379
  - TC-GS-HHR-380
  - TC-GS-HHR-381
  - TC-GS-HHR-382
  - TC-GS-HHR-383
coverage:
  web: automated
---

# Sinkron Admin Console Hardware Stock: Efek Mark as, Bulk, Delete, Bulk Delete, dan Cancel Request pada Unit

## Prerequisites

- Mode: FE+BE. Kelas harness tunggal: multi-konteks (kelas c, dua sesi: Client A dan Principal di Admin Console). Tidak ada TC dalam spec ini yang membutuhkan simulator reader USB. Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

- Login Sesi A dilakukan di hook `before`; Sesi P dibuka dengan langkah ganti akun eksplisit (langkah 1) karena hasilnya diasersi di Hardware Stock. Hook `after` menutup Sesi P dan mengembalikan sesi ke akun default suite (Sesi A).
- Data Dinamis (Seed Reader A, dipulihkan fixture backend; Client A, plan Growth, DD-01 s.d. DD-10): DD-01 (Available, Jalur A, unit `SN-HHR-00101`), DD-03 (Damaged, Jalur A, `SN-HHR-00103`, `In Use`), DD-04 (Missing, Jalur A, `SN-HHR-00104`, `In Use`), DD-07 (Available, Jalur B, `SN-HHR-00108`), DD-10 (Waiting for Approval, Jalur A, `SN-HHR-00205`). Nama reader bernilai literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR).
- Kemampuan teknis (disediakan tim FE/BE):
  - Konteks browser kedua untuk Sesi P.
  - Pemulihan Seed Reader A dan stok Hardware Stock ke keadaan Tabel Data Uji TC antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
  - Pembacaan jumlah notifikasi Principal di Notification Center (blok TC-GS-HHR-382; hanya jumlah sebelum dan sesudah).
- Baseline: `Status` unit dan total unit Hardware Stock dicatat sebelum aksi tiap blok.
- State global yang diubah: Seed Reader A dan status unit di Hardware Stock. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

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
52. Sesi P: ketik Search `SN-HHR-00101`, tekan Enter, catat `Status` unit
53. Sesi P: buka Notification Center, catat jumlah notifikasi sebagai baseline
54. Sesi A: muat ulang Handheld Reader, buka Overlay row action baris DD-01, klik `Delete`
55. Sesi A: klik `[Delete]` pada dialog
56. Tunggu aksi selesai
57. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00101`, tekan Enter
58. Verifikasi `Status` unit `SN-HHR-00101` berubah dari `In Use` menjadi `Available`
59. Verifikasi unit `SN-HHR-00101` tampil di Tab Available
60. Klik Tab In Use, ketik Search `SN-HHR-00101`, tekan Enter
61. Verifikasi unit `SN-HHR-00101` tidak ada di Tab In Use (empty state `No results found`)
62. Buka Changelog Hardware Stock
63. Verifikasi Changelog Hardware Stock memuat entri `Device Released` dengan Old Value `In Use` dan New Value `Available`
64. Verifikasi `Modified By` entri `Device Released` adalah nama pelaku Client (Sari Dewi)
65. Tutup Changelog Hardware Stock
66. Sesi P: buka Notification Center
67. Verifikasi jumlah notifikasi Principal sama dengan baseline (tidak ada notifikasi baru)

### Blok 5 - Bulk Delete reader Jalur A: TC-GS-HHR-217

68. Pulihkan Seed Reader A dan stok Hardware Stock
69. Sesi P: buka Hardware Stock, ketik Search `SN-HHR-00103`, tekan Enter, catat `Status` unit sebagai Status awal unit 1 (`In Use`); ketik Search `SN-HHR-00104`, tekan Enter, catat `Status` unit sebagai Status awal unit 2 (`In Use`)
70. Sesi A: muat ulang Handheld Reader, centang checkbox baris DD-03 (Damaged)
71. Sesi A: centang checkbox baris DD-04 (Missing)
72. Sesi A: klik tombol `Bulk Action`
73. Sesi A: klik `Delete`
74. Sesi A: klik `[Delete]` pada dialog
75. Verifikasi muncul toast sukses: "Success, reader has been deleted."
76. Verifikasi baris DD-03 dan DD-04 hilang dari tabel
77. Verifikasi pagination menampilkan `Showing 1 - 8 of 8 readers`
78. Verifikasi kartu `Long Range` menjadi `4 of 6`, `2 remaining`
79. Verifikasi kartu `Short Range` menjadi `4 of 8`, `4 remaining`
80. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00103`, tekan Enter
81. Verifikasi `Status` unit `SN-HHR-00103` berubah dari `In Use` (Status awal unit 1) menjadi `Available`
82. Sesi P: ketik Search `SN-HHR-00104`, tekan Enter
83. Verifikasi `Status` unit `SN-HHR-00104` berubah dari `In Use` (Status awal unit 2) menjadi `Available`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7a untuk TC-GS-HHR-376 sampai 383; section 3k untuk TC-GS-HHR-217).
- Pembagian TC lintas spec: TC-GS-HHR-217 ada di spec ini dan tidak di spec 046 (Bulk Delete Reader, TC-GS-HHR-214, 215, 216, 220). Aktivasi dan Current Power yang membaca reader USB (TC-GS-HHR-373, 374, 375, 384) ada di spec 077.
- Urutan blok: Mark as, Cancel Request, lalu aksi yang menghapus data (Delete, blok 4; Bulk Delete, blok 5) paling akhir sehingga data blok sebelumnya tidak terpengaruh (prinsip 3 butir 5).
- Langkah 2 sampai 9 diulang tiga kali sesuai tabel "Iterasi Mark as" (bagian 8b butir 7).
- Spec memuat 83 langkah nominal (99 dengan ekspansi tiga iterasi), melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (dua sesi, efek aksi Client pada Hardware Stock), tiap blok berdiri sendiri karena Seed Reader A dan stok dipulihkan di awal blok (langkah 2, 10, 23, 36, 44, 51, 68), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan Seed Reader A dan stok, muat ulang, mencatat nilai awal, berpindah sesi, Tab In Use/Available, mencari unit lewat Search, membuka dan menutup Changelog Hardware Stock dan Notification Center. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi (bagian 8b butir 8).
- Pembagian perilaku: perilaku sisi Client yang sama (Mark as, Delete, Cancel Request) diasersi di spec fungsional Mark as, Delete, dan Cancel Request; spec ini hanya mengasersi efeknya di Hardware Stock. Sisi Client TC-GS-HHR-217 (toast, baris, pagination, kartu kuota) diasersi di blok 5 karena TC-nya memuatnya.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Temuan untuk QA:
  - Nama tombol konfirmasi dialog Mark as Missing dan Mark as Available (`[Mark as Missing]`, `[Mark as Available]`) tidak tertulis di bagian ini; spec mengikuti pola `[Mark as Damaged]` yang tertulis di TC-GS-HHR-430.
  - Post Condition TC-GS-HHR-217 butir b ("Satu entri per reader pada tiga surface log") tanpa langkah observasi di TC tidak diasersi; log per reader hanya diasersi pada TC-GS-HHR-220 (spec 046).
  - TC-GS-HHR-381 dan TC-GS-HHR-379 butir b ("tidak ada perubahan pada stok") tidak menyebut langkah mencatat total unit; spec mencatat total unit Hardware Stock sebelum aksi sebagai baseline (S-12).
