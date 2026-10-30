---
id: TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power
title: "Aktivasi Jalur A (Official): Hasil Sync, Submit Long Range dan Short Range, Default Reader Power 30 dBm, Reader Power Disesuaikan, dan Alias Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-63
  - TC-GS-HHR-64
  - TC-GS-HHR-65
  - TC-GS-HHR-66
  - TC-GS-HHR-67
  - TC-GS-HHR-68
coverage:
  web: automated
---

# Aktivasi Jalur A (Official): Hasil Sync, Submit Long Range dan Short Range, Default Reader Power 30 dBm, Reader Power Disesuaikan, dan Alias Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat reader di Client A, mengonsumsi kuota dan stok Principal, dan memulihkan state di tengah spec; tidak boleh paralel dengan spec lain yang memakai Client A, Seed Reader A, atau simulator USB.
- Aktor: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`): Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (`Short Range` `5 of 8`, `Long Range` `5 of 6`, pagination `Showing 1 - 10 of 10 readers`), format tanggal default General Settings. Hardware Stock Principal (status `Available`):

  | ID | Serial Number | Range Type | Brand / Model | Current Power | Device Name bawaan | Dipakai di |
  |---|---|---|---|---|---|---|
  | HS-01 | `SN-HHR-00201` | Long Range | Zebra / RFD40 | 22 dBm | `Zebra RFID Reader - 2` | TC-GS-HHR-63, TC-GS-HHR-64, TC-GS-HHR-67, TC-GS-HHR-68 |
  | HS-02 | `SN-HHR-00202` | Short Range | Chainway / C66 | tidak ada | `Gudang Reader - 3` | TC-GS-HHR-65 |
  | HS-05 | `SN-HHR-00206` | Long Range | Zebra / RFD40 | tidak tersedia | (tidak dikirim) | TC-GS-HHR-66 |

- Data Dinamis: Alias Name `Reader Dock 01 {runId}-017` (TC-GS-HHR-68).
- Pemulihan state di tengah spec: `SN-HHR-00201` dipakai tiga kali (TC-GS-HHR-67, TC-GS-HHR-64, TC-GS-HHR-68) dan kuota `Long Range` hanya 5 dari 6, sehingga tiap aktivasi sukses berikutnya membutuhkan state awal. Langkah 26 dan 54 memulihkan Seed Reader A (menghapus reader hasil aktivasi), status unit HS-01 ke `Available`, dan kartu kuota `Short Range` `5 of 8` serta `Long Range` `5 of 6` lewat reset fixture backend (Catatan TC: "mutasi TC sebelumnya tidak dibawa ke TC berikutnya"); mekanisme disediakan tim FE/BE.
- Kemampuan teknis: simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00206`, `SN-HHR-00201`, `SN-HHR-00202`) dan Current Power dari stok (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); TC-GS-HHR-63 sampai TC-GS-HHR-68 berlabel Manual Only (b) di TC sumber. Reset fixture backend (di atas). Pembacaan nilai slider dan preview nilai saat digeser.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan Seed Reader A, stok HS-01 dan HS-02, kuota Client A, dan simulator; tutup popup yang masih terbuka.

## Test Steps

### TC-GS-HHR-66: Current Power tidak tersedia di stok, slider memakai default 30 dBm

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader dengan Serial Number `SN-HHR-00206` (HS-05, tanpa Current Power) lewat simulator reader USB
4. Klik `[Sync]`
5. Verifikasi slider `Reader Power` terisi nilai awal `30 dBm`
6. Klik `[✕]` di header popup, lalu klik `[Cancel Activation]` pada dialog

### TC-GS-HHR-63: Hasil Sync serial milik stok Principal

7. Klik `[+ Activate Reader]`
8. Klik `Long Range` pada Overlay `Select Range Type`
9. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01, Current Power 22 dBm) lewat simulator reader USB
10. Klik `[Sync]`
11. Verifikasi `Serial Number` read-only terisi `SN-HHR-00201`
12. Verifikasi label `Official` tampil
13. Verifikasi field `Brand` terisi `Zebra` dan `Model/Type` terisi `RFD40` dari stok
14. Verifikasi field `Brand` dan `Model/Type` terkunci (tidak dapat diubah)
15. Verifikasi slider `Reader Power` tampil dengan nilai awal `22 dBm`
16. Verifikasi slider `Reader Power` dapat digeser
17. Verifikasi field `Alias Name` opsional dengan placeholder `Enter alias name` dan kosong
18. Verifikasi `[Submit]` enabled
19. Verifikasi pemilih `Device Name` dan `SKU` Jalur B tidak tampil

### TC-GS-HHR-67: Reader Power disesuaikan pengguna sebelum Submit tersimpan

20. Geser slider `Reader Power` ke 15 dBm
21. Verifikasi preview nilai pada slider menampilkan `15 dBm`
22. Klik `[Submit]`
23. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
24. Verifikasi baris `Zebra RFID Reader - 2` menampilkan `Reader Power` `15 dBm`
25. Klik `(←)` pada kotak Search
26. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 `Available`, kuota `Long Range` `5 of 6`)
27. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-64: Submit aktivasi Jalur A Long Range berhasil dengan status Available

28. Klik `[+ Activate Reader]`
29. Klik `Long Range` pada Overlay `Select Range Type`
30. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
31. Klik `[Sync]`
32. Klik `[Submit]`
33. Verifikasi muncul toast sukses: "Success, Zebra RFID Reader - 2 has been activated."
34. Verifikasi Popup `Activate Handheld Reader` tertutup
35. Verifikasi kartu `Long Range` menampilkan `6 of 6`
36. Verifikasi kartu `Long Range` menampilkan `0 remaining`
37. Verifikasi kartu `Short Range` tetap `5 of 8`
38. Verifikasi kartu `Short Range` menampilkan `3 remaining`
39. Verifikasi pagination `Showing 1 - 10 of 11 readers`
40. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
41. Verifikasi baris baru: `Device Name` `Zebra RFID Reader - 2`, `Serial Number` `SN-HHR-00201`, `SKU` `SKU-HHR-01`, `Range Type` `Long Range`, `Reader Power` `22 dBm`, `Source` `Official`, `Status` `Available`
42. Klik `(←)` pada kotak Search

### TC-GS-HHR-65: Submit aktivasi Jalur A Short Range berhasil tanpa Reader Power

43. Klik `[+ Activate Reader]`
44. Klik `Short Range` pada Overlay `Select Range Type`
45. Sambungkan reader dengan Serial Number `SN-HHR-00202` (HS-02) lewat simulator reader USB
46. Klik `[Sync]`
47. Klik `[Submit]`
48. Verifikasi muncul toast sukses: "Success, Gudang Reader - 3 has been activated."
49. Verifikasi kartu `Short Range` menampilkan `6 of 8`
50. Verifikasi kartu `Short Range` menampilkan `2 remaining`
51. Ketik Search `Gudang Reader - 3`, tekan Enter
52. Verifikasi baris baru `Gudang Reader - 3`: `Range Type` `Short Range`, `Reader Power` `—`, `Source` `Official`, `Status` `Available`
53. Klik `(←)` pada kotak Search
54. Pulihkan state awal lewat reset fixture backend (Seed Reader A, status unit HS-01 dan HS-02 `Available`, kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`)
55. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-68: Alias Name opsional diisi saat aktivasi

56. Klik `[+ Activate Reader]`
57. Klik `Long Range` pada Overlay `Select Range Type`
58. Sambungkan reader dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
59. Klik `[Sync]`
60. Isi `Alias Name` dengan `Reader Dock 01 {runId}-017`
61. Klik `[Submit]`
62. Verifikasi muncul toast sukses: "Success, Reader Dock 01 {runId}-017 has been activated."
63. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
64. Verifikasi baris baru menampilkan `Device Name` `Zebra RFID Reader - 2`
65. Verifikasi baris baru menampilkan `Alias Name` `Reader Dock 01 {runId}-017`
66. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (aktivasi Jalur A), satu akun, satu harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-66 dan TC-GS-HHR-63 (tanpa Submit, screening) lebih dulu; TC-GS-HHR-67 (Submit pertama, kuota `Long Range` masih `5 of 6`) berikutnya; TC-GS-HHR-64 dan TC-GS-HHR-65 sesudah pemulihan state; TC-GS-HHR-68 terakhir sesudah pemulihan kedua. TC-GS-HHR-63 dan TC-GS-HHR-67 berbagi satu popup (satu Sync `SN-HHR-00201`) karena TC-GS-HHR-67 melanjutkan dari hasil Sync yang diamati TC-GS-HHR-63. TC-GS-HHR-65 berjalan tanpa pemulihan sesudah TC-GS-HHR-64 karena kuota `Short Range` tidak terpengaruh aktivasi `Long Range`; nilai kartu `Short Range` `6 of 8` pada langkah 49 bergantung pada urutan itu.
- Spec melewati sekitar 35 langkah (66 langkah). Alasan: 27 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01), dan tiap aktivasi sukses mengulang prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]` (empat langkah per blok) serta Search; semua blok satu kelas harness (simulator USB), satu topik, dan tiap blok sukses dimulai dari state hasil reset (langkah 26 dan 54), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 9, 30, 45, 58 (menyiapkan reader di simulator); langkah 6 (menutup popup yang sudah berisi hasil Sync); langkah 23, 40, 51, 63 (Search untuk menemukan baris target) dan langkah 25, 42, 53, 66 (mengosongkan Search); langkah 26, 27, 54, 55 (pemulihan state dan muat ulang). Pagination (langkah 39) diasersi sebelum Search karena Search mengubah jumlah baris tampil.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-68 ditulis bersuffix per run (`Reader Dock 01 {runId}-017`) mengikuti S-12.
- Asersi baris baru (langkah 41, 52) menyatukan kolom satu baris yang disebut utuh pada Expected TC. Tidak ada asersi absence.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB dan pembacaan Current Power dari stok tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - Mekanisme reset fixture backend di tengah spec (langkah 26 dan 54) tidak didefinisikan; TC hanya menyatakan reset antar TC. `SN-HHR-00201` dan kuota `Long Range` tidak cukup untuk TC-GS-HHR-64, TC-GS-HHR-67, dan TC-GS-HHR-68 dalam satu spec tanpa pemulihan; QA/tim FE perlu menyediakan reset atau unit stok tambahan.
  - TC-GS-HHR-64 tidak menyatakan kolom mana yang tampil secara default (`Serial Number`, `SKU`, `Alias Name`); spec mengasersi kolom seperti di Expected TC dan membutuhkan kolom tampil, tanpa langkah Column Visibility.
  - Post Condition TC-GS-HHR-64 (record baru Jalur A, pencatatan 3 surface log dan Event Log Activate, perubahan unit HS-01 di Hardware Stock) tidak punya langkah observasi di TC dan tidak diasersi (S-01); pencatatan log diasersi di spec lain pada TC section 5.
  - TC-GS-HHR-67 Expected a ("secara real-time saat digeser") diasersi sebagai nilai preview setelah slider digeser ke 15 dBm (langkah 21); pengamatan selama penggeseran bergantung pada kemampuan simulator input.
  - TC-GS-HHR-66 hanya mengamati nilai awal slider tanpa Submit; spec menutup popup tanpa menyimpan, sehingga HS-05 tidak berubah.
  - Judul dan isi dialog yang memuat `[Cancel Activation]` (langkah 6) tidak tertulis di TC sumber slice ini; langkah dibuat tanpa `Verifikasi` dialog.
