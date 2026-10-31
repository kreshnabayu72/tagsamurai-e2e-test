---
id: TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power
title: "Aktivasi Jalur A (Official): Hasil Sync, Submit Long Range dan Short Range, Default Reader Power 30 dBm, Reader Power Disesuaikan, Alias Name, dan Aktivasi oleh Manage hardware Create"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-42
  - TC-GS-HHR-63
  - TC-GS-HHR-64
  - TC-GS-HHR-65
  - TC-GS-HHR-66
  - TC-GS-HHR-67
  - TC-GS-HHR-68
coverage:
  web: automated
---

# Aktivasi Jalur A (Official): Hasil Sync, Submit Long Range dan Short Range, Default Reader Power 30 dBm, Reader Power Disesuaikan, Alias Name, dan Aktivasi oleh Manage hardware Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat reader di Client A, mengonsumsi kuota dan stok Principal, dan memulihkan state di tengah spec; tidak boleh paralel dengan spec lain yang memakai Client A, Seed Reader A, atau simulator USB.
- Aktor blok TC-GS-HHR-66 sampai TC-GS-HHR-68: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader.
- Aktor blok TC-GS-HHR-42 (blok terakhir): Manage hardware (Create) Rina Lestari (Client A) `manageHardwareCreate_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup #4), password `Spectra.env.GS_HW_CREATE_PASSWORD`; login lewat langkah ganti akun eksplisit. Karena spec berakhir di akun Manage hardware (Create), hook `after` mengembalikan sesi ke akun default suite (Total Control Sari Dewi, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`), termasuk akun Manage hardware (Create).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`): Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (`Short Range` `5 of 8`, `Long Range` `5 of 6`, pagination `Showing 1 - 10 of 10 readers`), format tanggal default General Settings. Hardware Stock Principal (status `Available`):

  | ID | Serial Number | Range Type | Brand / Model | Current Power | Device Name bawaan | Dipakai di |
  |---|---|---|---|---|---|---|
  | HS-01 | `SN-HHR-00201` | Long Range | Zebra / RFD40 | 22 dBm | `Zebra RFID Reader - 2` | TC-GS-HHR-63, TC-GS-HHR-64, TC-GS-HHR-67, TC-GS-HHR-68, TC-GS-HHR-42 |
  | HS-02 | `SN-HHR-00202` | Short Range | Chainway / C66 | tidak ada | `Gudang Reader - 3` | TC-GS-HHR-65 |
  | HS-05 | `SN-HHR-00206` | Long Range | Zebra / RFD40 | tidak tersedia | (tidak dikirim) | TC-GS-HHR-66 |

- Data Dinamis: Alias Name `Reader Dock 01-{runId}-017` (TC-GS-HHR-68).
- Pemulihan state di tengah spec: `SN-HHR-00201` dipakai empat kali (TC-GS-HHR-67, TC-GS-HHR-64, TC-GS-HHR-68, TC-GS-HHR-42) dan kuota `Long Range` hanya 5 dari 6, sehingga tiap aktivasi sukses berikutnya membutuhkan state awal. Langkah 29, 66, dan 79 memulihkan Seed Reader A (menghapus reader hasil aktivasi), status unit HS-01 (dan HS-02) ke `Available`, kartu kuota `Short Range` `5 of 8` serta `Long Range` `5 of 6`, dan counter `N` Device Name `Zebra RFID Reader` lewat reset fixture backend (Catatan TC: "mutasi TC sebelumnya tidak dibawa ke TC berikutnya"); mekanisme disediakan tim FE/BE.
- Kemampuan teknis: simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00206`, `SN-HHR-00201`, `SN-HHR-00202`) dan Current Power dari stok (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); TC-GS-HHR-63 sampai TC-GS-HHR-68 dan TC-GS-HHR-42 berlabel Manual Only (b) di TC sumber. Reset fixture backend (di atas). Pembacaan nilai slider dan preview nilai saat digeser.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Seed Reader A, stok HS-01 dan HS-02, kuota Client A, dan simulator; tutup popup yang masih terbuka.

## Test Steps

### TC-GS-HHR-66: Current Power tidak tersedia di stok, slider memakai default 30 dBm

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader dengan Serial Number `SN-HHR-00206` (HS-05, tanpa Current Power) lewat simulator reader USB
4. Klik `[Sync]`
5. Verifikasi slider `Reader Power` terisi nilai awal `30 dBm`
6. Klik `[✕]` di header popup
7. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
8. Klik `[Cancel Activation]`

### TC-GS-HHR-63: Hasil Sync serial milik stok Principal

9. Klik `[+ Activate Reader]`
10. Klik `Long Range` pada Overlay `Select Range Type`
11. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01, Current Power 22 dBm) lewat simulator reader USB
12. Klik `[Sync]`
13. Verifikasi `Serial Number` read-only terisi `SN-HHR-00201`
14. Verifikasi label `Official` tampil
15. Verifikasi field `Brand` terisi `Zebra` dan `Model/Type` terisi `RFD40` dari stok
16. Verifikasi field `Brand` dan `Model/Type` terkunci (tidak dapat diubah)
17. Verifikasi slider `Reader Power` tampil dengan nilai awal `22 dBm`
18. Verifikasi slider `Reader Power` dapat digeser
19. Verifikasi field `Alias Name` opsional dengan placeholder `Enter alias name` dan kosong
20. Verifikasi `[Submit]` enabled
21. Verifikasi pemilih `Device Name` dan `SKU` Jalur B tidak tampil

### TC-GS-HHR-67: Reader Power disesuaikan pengguna sebelum Submit tersimpan

22. Geser slider `Reader Power` ke 15 dBm
23. Verifikasi preview nilai pada slider menampilkan `15 dBm`
24. Klik `[Submit]`
25. Tunggu aksi selesai (Popup `Activate Handheld Reader` tertutup)
26. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
27. Verifikasi baris `Zebra RFID Reader - 2` menampilkan `Reader Power` `15 dBm`
28. Klik `(←)` pada kotak Search
29. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`)
30. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-64: Submit aktivasi Jalur A Long Range berhasil dengan status Available

31. Klik `[+ Activate Reader]`
32. Klik `Long Range` pada Overlay `Select Range Type`
33. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
34. Klik `[Sync]`
35. Klik `[Submit]`
36. Verifikasi muncul toast sukses: "Success, Zebra RFID Reader - 2 has been activated."
37. Verifikasi Popup `Activate Handheld Reader` tertutup
38. Verifikasi kartu `Long Range` menampilkan `6 of 6`
39. Verifikasi kartu `Long Range` menampilkan `0 remaining`
40. Verifikasi kartu `Short Range` tetap `5 of 8`
41. Verifikasi kartu `Short Range` menampilkan `3 remaining`
42. Verifikasi pagination `Showing 1 - 10 of 11 readers`
43. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
44. Verifikasi baris baru menampilkan `Device Name` `Zebra RFID Reader - 2`
45. Verifikasi baris baru menampilkan `Serial Number` `SN-HHR-00201`
46. Verifikasi baris baru menampilkan `SKU` `SKU-HHR-01`
47. Verifikasi baris baru menampilkan `Range Type` `Long Range`
48. Verifikasi baris baru menampilkan `Reader Power` `22 dBm`
49. Verifikasi baris baru menampilkan `Source` `Official`
50. Verifikasi baris baru menampilkan `Status` `Available`
51. Klik `(←)` pada kotak Search

### TC-GS-HHR-65: Submit aktivasi Jalur A Short Range berhasil tanpa Reader Power

52. Klik `[+ Activate Reader]`
53. Klik `Short Range` pada Overlay `Select Range Type`
54. Sambungkan reader dengan Serial Number `SN-HHR-00202` (HS-02) lewat simulator reader USB
55. Klik `[Sync]`
56. Klik `[Submit]`
57. Verifikasi muncul toast sukses: "Success, Gudang Reader - 3 has been activated."
58. Verifikasi kartu `Short Range` menampilkan `6 of 8`
59. Verifikasi kartu `Short Range` menampilkan `2 remaining`
60. Ketik Search `Gudang Reader - 3`, tekan Enter
61. Verifikasi baris baru `Gudang Reader - 3` menampilkan `Range Type` `Short Range`
62. Verifikasi baris baru `Gudang Reader - 3` menampilkan `Reader Power` `—`
63. Verifikasi baris baru `Gudang Reader - 3` menampilkan `Source` `Official`
64. Verifikasi baris baru `Gudang Reader - 3` menampilkan `Status` `Available`
65. Klik `(←)` pada kotak Search
66. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 dan HS-02 `Available`, kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`)
67. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-68: Alias Name opsional diisi saat aktivasi

68. Klik `[+ Activate Reader]`
69. Klik `Long Range` pada Overlay `Select Range Type`
70. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
71. Klik `[Sync]`
72. Isi `Alias Name` dengan `Reader Dock 01-{runId}-017`
73. Klik `[Submit]`
74. Verifikasi muncul toast sukses: "Success, Reader Dock 01-{runId}-017 has been activated."
75. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
76. Verifikasi baris baru menampilkan `Device Name` `Zebra RFID Reader - 2`
77. Verifikasi baris baru menampilkan `Alias Name` `Reader Dock 01-{runId}-017`
78. Klik `(←)` pada kotak Search

### TC-GS-HHR-42: Aktor Manage hardware (Create) menyelesaikan aktivasi Jalur A

79. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`, counter `N` Device Name `Zebra RFID Reader`)
80. Ganti akun: logout, lalu login sebagai Rina Lestari (Manage hardware level Create)
81. Buka Global Settings > Hardware > Handheld Reader
82. Klik `[+ Activate Reader]`
83. Klik `Long Range` pada Overlay `Select Range Type`
84. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
85. Klik `[Sync]`
86. Klik `[Submit]`
87. Verifikasi muncul toast sukses: "Success, Zebra RFID Reader - 2 has been activated."
88. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
89. Verifikasi baris `Zebra RFID Reader - 2` tampil dengan Status `Available`
90. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (aktivasi Jalur A), satu harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Blok TC-GS-HHR-42 (aktor Manage hardware level Create) berada paling akhir dengan Step ganti akun eksplisit (langkah 80). Dua akun dipertahankan dalam satu spec karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (bagian 3 "Pisahkan spec hanya jika ada pemisah nyata", butir b; state dipulihkan di langkah 79) dan seluruh blok satu kelas harness (simulator USB). Hook `after` mengembalikan sesi ke Total Control.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-66 dan TC-GS-HHR-63 (tanpa Submit, screening) lebih dulu; TC-GS-HHR-67 (Submit pertama, kuota `Long Range` masih `5 of 6`) berikutnya; TC-GS-HHR-64 dan TC-GS-HHR-65 sesudah pemulihan state; TC-GS-HHR-68 sesudah pemulihan kedua; TC-GS-HHR-42 terakhir sesudah pemulihan ketiga dan ganti akun. TC-GS-HHR-63 dan TC-GS-HHR-67 berbagi satu popup (satu Sync `SN-HHR-00201`) karena TC-GS-HHR-67 melanjutkan dari hasil Sync yang diamati TC-GS-HHR-63. TC-GS-HHR-65 berjalan tanpa pemulihan sesudah TC-GS-HHR-64 karena kuota `Short Range` tidak terpengaruh aktivasi `Long Range`; nilai kartu `Short Range` `6 of 8` pada langkah 58 bergantung pada urutan itu.
- Spec melewati sekitar 35 langkah (90 langkah nominal). Alasan: 39 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01), dan tiap aktivasi sukses mengulang prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]` (empat langkah per blok) serta Search; semua blok satu kelas harness (simulator USB), satu topik, dan tiap blok sukses dimulai dari state hasil reset (langkah 29, 66, 79), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 11, 33, 54, 70, 84 (menyiapkan reader di simulator); langkah 8 (menutup popup yang sudah berisi hasil Sync lewat dialog `Cancel Activation`, S-08); langkah 25 (Tunggu aksi selesai: hasil Submit TC-GS-HHR-67 tidak diasersi sebelum Search); langkah 26, 43, 60, 75, 88 (Search untuk menemukan baris target) dan langkah 28, 51, 65, 78, 90 (mengosongkan Search); langkah 29, 30, 66, 67, 79 (pemulihan state dan muat ulang); langkah 80 dan 81 (ganti akun dan membuka halaman). Pagination (langkah 42) diasersi sebelum Search karena Search mengubah jumlah baris tampil.
- Teks dialog `Cancel Activation` (langkah 7) mengikuti Expected TC-GS-HHR-89; TC-GS-HHR-66 sendiri tidak memuatnya.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-68 ditulis bersuffix per run (`Reader Dock 01-{runId}-017`) mengikuti S-12.
- Asersi baris baru (langkah 44 sampai 50 dan 61 sampai 64) dipecah satu `Verifikasi` per kolom. Tidak ada asersi absence.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB dan pembacaan Current Power dari stok tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - Mekanisme reset fixture backend di tengah spec (langkah 29, 66, dan 79) tidak didefinisikan; TC hanya menyatakan reset antar TC. `SN-HHR-00201` dan kuota `Long Range` tidak cukup untuk TC-GS-HHR-64, TC-GS-HHR-67, TC-GS-HHR-68, dan TC-GS-HHR-42 dalam satu spec tanpa pemulihan; QA/tim FE perlu menyediakan reset atau unit stok tambahan.
  - TC-GS-HHR-42 menetapkan Device Name bawaan `Zebra RFID Reader - 2` yang bergantung pada counter `N` Device Name `Zebra RFID Reader`; TC tidak menyebut mekanisme reset counter. Seed Reader A memuat `Zebra RFID Reader - 1` (DD-01 dan DD-06).
  - TC-GS-HHR-42 tidak menyatakan cara mengamati baris `Zebra RFID Reader - 2` pada daftar 11 reader (halaman pertama memuat 10); spec memakai Search (langkah 88) sebagai langkah penghubung.
  - TC-GS-HHR-64 tidak menyatakan kolom mana yang tampil secara default (`Serial Number`, `SKU`, `Alias Name`); spec mengasersi kolom seperti di Expected TC dan membutuhkan kolom tampil, tanpa langkah Column Visibility.
  - Post Condition TC-GS-HHR-64 (record baru Jalur A, pencatatan 3 surface log dan Event Log Activate, perubahan unit HS-01 di Hardware Stock) tidak punya langkah observasi di TC dan tidak diasersi (S-01); pencatatan log diasersi di spec lain pada TC section 5.
  - TC-GS-HHR-67 Expected a ("secara real-time saat digeser") diasersi sebagai nilai preview setelah slider digeser ke 15 dBm (langkah 23); pengamatan selama penggeseran bergantung pada kemampuan simulator input.
  - TC-GS-HHR-66 hanya mengamati nilai awal slider tanpa Submit; spec menutup popup lewat dialog `Cancel Activation` tanpa menyimpan, sehingga HS-05 tidak berubah.
