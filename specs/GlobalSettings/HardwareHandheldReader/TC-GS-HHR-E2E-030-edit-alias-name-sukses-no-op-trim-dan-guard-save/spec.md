---
id: TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save
title: "Edit Alias Name Sukses: Save Tanpa Perubahan dan Kapitalisasi (No-Op), Alias Baru, Trim Spasi, Saving State, Klik Ganda Save, Search Aktif, dan Mengosongkan Alias"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-104
  - TC-GS-HHR-105
  - TC-GS-HHR-106
  - TC-GS-HHR-107
  - TC-GS-HHR-108
  - TC-GS-HHR-120
  - TC-GS-HHR-123
  - TC-GS-HHR-124
coverage:
  web: automated
---

# Edit Alias Name Sukses: Save Tanpa Perubahan dan Kapitalisasi (No-Op), Alias Baru, Trim Spasi, Saving State, Klik Ganda Save, Search Aktif, dan Mengosongkan Alias

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah alias lima reader pada Seed Reader A dan menambah entri log Client A, sehingga tidak berjalan bersamaan dengan spec lain pada Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); langkah 4 membuka layar lagi hanya sebagai kembali dari surface log.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Reader yang diedit, masing-masing milik satu blok TC: DD-01 (Serial Number `SN-HHR-00101`, TC-GS-HHR-104), DD-02 (`SN-HHR-00102`, TC-GS-HHR-106, 107, 124, 105), DD-03 (`SN-HHR-00103`, TC-GS-HHR-108), DD-04 (`SN-HHR-00104`, TC-GS-HHR-120), DD-06 (`SN-HHR-00107`, TC-GS-HHR-123). Seed Reader A bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number. Alias Name tidak wajib unik, sehingga alias uji ditulis literal sesuai TC.
- Baseline: jumlah entri total Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log Global Settings dicatat sebelum aksi pemicu pertama yang diasersi (langkah 1 sampai 3); jumlah entri Changelog dicatat lagi sebelum TC-GS-HHR-123 (langkah 53). Nilai kartu kuota `Short Range` dan `Long Range` dicatat sebelum TC-GS-HHR-104 (langkah 29).
- Cleanup: Seed Reader A dipulihkan ke kondisi awal oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE (lihat Temuan untuk QA). Entri log yang bertambah tidak dihapus (audit trail permanen).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: intercept jaringan untuk menahan respons request edit (hanya untuk mengamati saving state, dilepas segera sesudahnya); klik ganda cepat; membaca jumlah entri total pada Changelog Handheld Reader, System Log aktor, dan Activity Log; membaca kartu kuota.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite), alias Seed Reader A (dipulihkan), dan intercept penahanan respons (dilepas pada langkah 52).

## Test Steps

### Baseline log (TC-GS-HHR-106 dan 107)

1. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal
2. Buka System Log aktor Sari Dewi, catat jumlah entri total sebagai baseline System Log
3. Buka Activity Log Global Settings, catat jumlah entri total sebagai baseline Activity Log
4. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-106: Save tanpa perubahan pada Edit Alias Name

5. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
6. Klik `[Save]` tanpa mengubah `Alias Name`
7. Verifikasi tidak ada toast sukses "Success, Reader Gudang 02 has been updated."
8. Verifikasi toast netral `No changes to save.`
9. Verifikasi dialog tertutup
10. Buka ikon Changelog
11. Verifikasi jumlah entri total Changelog sama dengan baseline Changelog
12. Tutup modal Changelog, buka System Log aktor Sari Dewi
13. Verifikasi jumlah entri total System Log sama dengan baseline System Log
14. Buka Activity Log Global Settings
15. Verifikasi jumlah entri total Activity Log sama dengan baseline Activity Log
16. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-107: Save yang hanya mengubah kapitalisasi alias dianggap no-op

17. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
18. Ubah `Alias Name` menjadi `reader gudang 02`
19. Klik `[Save]`
20. Verifikasi toast netral `No changes to save.`
21. Verifikasi kolom `Alias Name` baris DD-02 tetap `Reader Gudang 02`
22. Buka ikon Changelog
23. Verifikasi jumlah entri total Changelog sama dengan jumlah yang diamati pada langkah 11
24. Tutup modal Changelog, buka System Log aktor Sari Dewi
25. Verifikasi jumlah entri total System Log sama dengan jumlah yang diamati pada langkah 13
26. Buka Activity Log Global Settings
27. Verifikasi jumlah entri total Activity Log sama dengan jumlah yang diamati pada langkah 15
28. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-104: Edit Alias Name berhasil menyimpan alias baru

29. Catat nilai kartu kuota `Short Range` dan `Long Range`
30. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
31. Isi `Alias Name` dengan `Reader Dock 01`
32. Klik `[Save]`
33. Verifikasi dialog tertutup
34. Verifikasi toast sukses "Success, Reader Dock 01 has been updated."
35. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01`
36. Verifikasi kolom `Device Name` baris DD-01 tetap `Zebra RFID Reader - 1`
37. Verifikasi kartu kuota `Short Range` dan `Long Range` sama dengan nilai yang dicatat pada langkah 29
38. Verifikasi kolom `Status` baris DD-01 tetap `Available`

### TC-GS-HHR-108: Spasi awal dan akhir alias dibuang saat Save

39. Klik `⋯` pada baris DD-03 (Serial Number `SN-HHR-00103`), pilih `Edit Alias Name`
40. Isi `Alias Name` dengan `  Reader Dock 01  ` (spasi di awal dan akhir)
41. Klik `[Save]`
42. Verifikasi kolom `Alias Name` baris DD-03 menampilkan `Reader Dock 01` tanpa spasi tepi

### TC-GS-HHR-120: Save masuk saving state selama request

43. Aktifkan penahanan respons pada request edit
44. Klik `⋯` pada baris DD-04 (Serial Number `SN-HHR-00104`), pilih `Edit Alias Name`
45. Isi `Alias Name` dengan `Reader Dock 01`
46. Klik `[Save]`
47. Verifikasi `[Save]` menampilkan spinner
48. Verifikasi `[Save]` disabled
49. Verifikasi `[Clear Field]` dinonaktifkan
50. Verifikasi `[✕]` dinonaktifkan
51. Verifikasi input `Alias Name` dinonaktifkan
52. Lepas penahanan respons dan tunggu dialog tertutup

### TC-GS-HHR-123: Klik ganda cepat pada Save hanya menyimpan satu perubahan

53. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog TC-GS-HHR-123, tutup modal
54. Klik `⋯` pada baris DD-06 (Serial Number `SN-HHR-00107`), pilih `Edit Alias Name`
55. Isi `Alias Name` dengan `Reader Dock 01`
56. Tunggu toast lama hilang otomatis
57. Klik ganda cepat `[Save]`
58. Verifikasi hanya satu toast sukses "Success, Reader Dock 01 has been updated."
59. Buka ikon Changelog
60. Verifikasi jumlah entri total Changelog bertambah tepat satu dari baseline pada langkah 53
61. Verifikasi entri baru berjenis `Edit` pada `Alias Name` untuk reader DD-06 (Serial Number `SN-HHR-00107`)
62. Tutup modal Changelog

### TC-GS-HHR-124: Edit Alias mengubah hasil Search yang sedang aktif

63. Ketik Search `Reader Gudang`, tekan Enter
64. Verifikasi tabel menampilkan tepat satu baris, yaitu baris DD-02 (`Gudang Reader - 1`)
65. Klik `⋯` pada baris DD-02, pilih `Edit Alias Name`
66. Isi `Alias Name` dengan `Dock 01`
67. Klik `[Save]`
68. Verifikasi tabel menampilkan empty state `No results found`
69. Klik `(←)` pada kotak Search

### TC-GS-HHR-105: Mengosongkan Alias Name menyimpan alias kosong

70. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
71. Kosongkan `Alias Name`
72. Klik `[Save]`
73. Verifikasi kolom `Alias Name` baris DD-02 menampilkan `—`
74. Verifikasi kolom `Device Name` baris DD-02 tetap `Gudang Reader - 1`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 106, 107, 104, 108, 120, 123, 124, 105. Urutan menyimpang dari urutan TC sumber: no-op (106, 107) tidak mengubah data dan memakai baseline log yang dicatat sebelum aksi pertama, sehingga ditaruh pertama; TC-GS-HHR-124 mengubah alias DD-02 menjadi `Dock 01` dan harus sesudah 106 dan 107 yang memakai alias awal `Reader Gudang 02`, serta sebelum 105 yang mengosongkan alias DD-02.
- Reader per blok dibedakan karena Seed Reader A hanya dipulihkan sekali sebelum spec, sedangkan tiap TC sumber mengandaikan data awal yang dipulihkan. Dibanding Data Uji TC: TC-GS-HHR-108 memakai DD-03 (TC menulis DD-01), TC-GS-HHR-120 memakai DD-04 (TC menulis DD-01), dan TC-GS-HHR-123 memakai DD-06 (TC menulis DD-01); alias awal `—` ketiganya sama dengan DD-01 sehingga objek uji (trim, saving state, klik ganda) tidak berubah. Pada TC-GS-HHR-123 Changelog diasersi untuk DD-06, bukan DD-01.
- Asersi jumlah entri (langkah 11, 13, 15, 23, 25, 27, 60) memakai baseline jumlah entri (S-12), bukan asersi absence kelas g: tiap TC memuat aksi Save nyata dan langkah catat-bandingkan di TC sumber. Baseline TC-GS-HHR-107 adalah jumlah yang diamati pada langkah 11, 13, dan 15 (setelah TC-GS-HHR-106).
- Asersi absence toast sukses pada TC-GS-HHR-106 (langkah 7) diletakkan segera sesudah pemicu `[Save]` (langkah 6) dan sebelum asersi toast netral (langkah 8), yang menjadi anchor positif (bagian 8b butir 5 dan 11); urutan ini menyimpang dari urutan Expected TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (baseline), langkah 12, 16, 24, 28 (pindah surface log dan kembali ke layar Handheld Reader), langkah 29 (mencatat kartu kuota sebagai pembanding), langkah 43 dan 52 (memasang dan melepas penahanan respons, S-09), langkah 53 (baseline Changelog), langkah 56 (menunggu toast lama hilang agar hitungan satu toast bermakna), langkah 62 (menutup modal), langkah 63 dan 69 (Search agar baris target tampil dan menutup input Search).
- Jumlah pembukaan dialog Edit Alias Name: 8 (langkah 5, 17, 30, 39, 44, 54, 65, 70); jumlah penutupan: 8 (semua lewat Save atau penutupan otomatis sesudah Save).
- Spec melewati sekitar 35 langkah (74 langkah). Seluruhnya satu topik dan satu kelas (Edit Alias Name yang berhasil atau no-op), satu akun, tanpa harness eksternal; penahanan respons pada langkah 43 hanya untuk mengamati saving state dan dilepas pada langkah 52. Tiap blok TC memakai reader sendiri dan memulai dari dialog yang baru dibuka, sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan dialog. Sekitar 18 langkah adalah blok baca-log berpola (buka surface, bandingkan jumlah).
- Pembagian TC lintas spec: TC-GS-HHR-103, 109 sampai 114, dan 462 ada di spec 029; TC-GS-HHR-115 sampai 119 ada di spec 031; TC-GS-HHR-121 dan 122 ada di spec 026. Spec absence 065 tidak memuat TC-GS-HHR-106 dan 107.
- Temuan untuk QA:
  - TC-GS-HHR-106 dan 107 menyebut System Log aktor dan Activity Log tanpa menyebut jalur navigasi surface atau cara membaca jumlah entri; spec membaca jumlah entri total tiap surface dan jalur navigasinya mengikuti TC section 5.
  - TC-GS-HHR-104 Expected d ("Kartu kuota dan `Status` tidak berubah") tidak menyebut nilai; spec membandingkan kartu dengan nilai yang dicatat sebelum Save dan `Status` `Available` sesuai Seed Reader A.
  - TC-GS-HHR-105 tidak menyebut toast; spec hanya mengasersi Expected a dan b.
  - TC-GS-HHR-120 dan 123 menyebut DD-01 sedangkan Seed Reader A tidak dipulihkan antar blok dalam spec; spec memakai reader lain (lihat Notes di atas).
  - TC-GS-HHR-124 Expected a ("hanya DD-02 yang cocok") diasersi sebagai tepat satu baris DD-02 pada hasil Search `Reader Gudang`.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Post Condition tanpa langkah observasi di TC dan tidak diasersi: TC-GS-HHR-104 ("Alias Name DD-01 tersimpan" dan "Tiga surface log (TC section 5)").
