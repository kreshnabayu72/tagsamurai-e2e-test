---
id: TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available
title: "Bulk Mark as Damaged, Missing, dan Available: Dialog, Cancel, Esc, Eksekusi, Dialog Tunggal, Pencatatan Log per Reader, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-207
  - TC-GS-HHR-208
  - TC-GS-HHR-209
  - TC-GS-HHR-210
  - TC-GS-HHR-211
  - TC-GS-HHR-212
  - TC-GS-HHR-213
  - TC-GS-HHR-218
  - TC-GS-HHR-219
  - TC-GS-HHR-461
coverage:
  web: automated
---

# Bulk Mark as Damaged, Missing, dan Available: Dialog, Cancel, Esc, Eksekusi, Dialog Tunggal, Pencatatan Log per Reader, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini mengubah status reader Seed Reader A dan memulihkannya (lihat butir pemulihan).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman) atau pembacaan log (kembali ke halaman).
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SKU-HHR-01, Available), DD-07 (`Honeywell CK65 - 1`, Available), DD-03 (`Zebra Mobile Reader - 1`, Damaged), dan DD-04 (`Gudang Reader - 2`, Missing). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya; urutan bullet dialog mengikuti urutan baris tabel.
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya pada langkah pertama tiap iterasi eksekusi dan sebelum TC-GS-HHR-219, 213, dan 461 lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" yang disediakan tim FE/BE tanpa endpoint yang dikarang, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log (dibaca TC-GS-HHR-219): Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (tab `User Action`, dibuka lewat Global Settings > Activity Log). Baseline jumlah entri dicatat per surface sebelum aksi pemicu.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus dialog bulk Mark as" (parameter langkah 1 sampai 12):

| TC | Reader 1 | Reader 2 | Aksi (Judul dialog) | Bullet Body (berurutan) | Kalimat penutup Body | Status awal |
|---|---|---|---|---|---|---|
| TC-GS-HHR-207 | DD-01 | DD-07 | `Mark as Damaged` | `Honeywell CK65 - 1` lalu `Zebra RFID Reader - 1` | `Are you sure you want to mark them as damaged?` | `Available` |
| TC-GS-HHR-209 | DD-01 | DD-07 | `Mark as Missing` | `Honeywell CK65 - 1` lalu `Zebra RFID Reader - 1` | `Are you sure you want to mark them as missing?` | `Available` |
| TC-GS-HHR-211 | DD-03 | DD-04 | `Mark as Available` | `Gudang Reader - 2` lalu `Zebra Mobile Reader - 1` | `Are you sure you want to mark them as available?` | DD-03 `Damaged`, DD-04 `Missing` |

- Tabel "Kasus bulk Mark as berhasil" (parameter langkah 24 sampai 34):

| TC | Reader 1 | Reader 2 | Aksi | Toast sukses | Status baru |
|---|---|---|---|---|---|
| TC-GS-HHR-212 | DD-03 | DD-04 | `Mark as Available` | "Success, reader has been marked as available." | `Available` |
| TC-GS-HHR-210 | DD-01 | DD-07 | `Mark as Missing` | "Success, reader has been marked as missing." | `Missing` |

- Kemampuan teknis: klik ganda cepat pada `[Mark as Damaged]` (TC-GS-HHR-461); penekanan tombol `Esc`; pembacaan dialog, kartu kuota, dan tiga surface log (jumlah dan isi entri); pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain status Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-207, 209, 211: Screening dialog bulk Mark as dan Cancel mempertahankan seleksi

Untuk setiap baris tabel "Kasus dialog bulk Mark as" (langkah 1 sampai 12):

1. Centang checkbox baris {Reader 1}
2. Centang checkbox baris {Reader 2}
3. Klik tombol `Bulk Action`
4. Klik `{Aksi}`
5. Verifikasi dialog tampil utuh: Judul `{Aksi}`, Body berisi bullet {Bullet Body}, kalimat penutup `{Kalimat penutup Body}`, Footer `[Cancel]` dan `[{Aksi}]`
6. Klik `[Cancel]`
7. Verifikasi tidak ada toast
8. Verifikasi dialog tertutup
9. Verifikasi baris {Reader 1} dan {Reader 2} tetap tercentang
10. Verifikasi Bulk Action Bar tetap tampil
11. Verifikasi `Status` {Reader 1} dan {Reader 2} tidak berubah ({Status awal})
12. Klik ikon `×`

### TC-GS-HHR-218: Esc pada dialog bulk setara Cancel dan mempertahankan seleksi

13. Centang checkbox baris DD-01
14. Centang checkbox baris DD-07
15. Klik tombol `Bulk Action`
16. Klik `Mark as Damaged`
17. Tekan `Esc`
18. Verifikasi tidak ada toast
19. Verifikasi dialog tertutup
20. Verifikasi `Status` DD-01 dan DD-07 tidak berubah (`Available`)
21. Verifikasi baris DD-01 dan DD-07 tetap tercentang
22. Verifikasi Bulk Action Bar tetap tampil
23. Klik ikon `×`

### TC-GS-HHR-212 dan TC-GS-HHR-210: Bulk Mark as Available dan Mark as Missing mengubah status seluruh reader terpilih

Untuk setiap baris tabel "Kasus bulk Mark as berhasil" (langkah 24 sampai 34):

24. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
25. Centang checkbox baris {Reader 1}
26. Centang checkbox baris {Reader 2}
27. Klik tombol `Bulk Action`
28. Klik `{Aksi}`
29. Klik `[{Aksi}]` pada dialog
30. Verifikasi muncul toast sukses: "{Toast sukses}"
31. Verifikasi Badge `Status` baris {Reader 1} dan {Reader 2} menjadi `{Status baru}`
32. Verifikasi Bulk Action Bar hilang
33. Verifikasi seluruh checkbox tidak tercentang
34. Verifikasi kartu kuota tidak berubah: `Short Range` `5 of 8` dan `Long Range` `5 of 6`

### TC-GS-HHR-208 dan TC-GS-HHR-219: Bulk Mark as Damaged mengubah status dan menulis satu entri per reader pada tiga surface log

35. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
36. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
37. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
38. Catat baseline Activity Log (tab `User Action`): buka Global Settings > Activity Log > tab User Action, catat jumlah entri
39. Buka Global Settings > Hardware > Handheld Reader
40. Centang checkbox baris DD-01
41. Centang checkbox baris DD-07
42. Klik tombol `Bulk Action`
43. Klik `Mark as Damaged`
44. Klik `[Mark as Damaged]` pada dialog
45. Verifikasi muncul toast sukses: "Success, reader has been marked as damaged."
46. Verifikasi Badge `Status` baris DD-01 dan DD-07 menjadi `Damaged`
47. Verifikasi Bulk Action Bar hilang
48. Verifikasi seluruh checkbox tidak tercentang
49. Verifikasi kartu kuota tidak berubah: `Short Range` `5 of 8` dan `Long Range` `5 of 6`
50. Buka ikon Changelog
51. Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 36
52. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru, masing-masing Action `Edit`, Field `Status`, Old Value `Available`, New Value `Damaged`, untuk `Zebra RFID Reader - 1 (SKU-HHR-01)` dan `Honeywell CK65 - 1`, Modified By `Sari D`
53. Tutup Modal Changelog dengan `✕`
54. Buka Global Settings > User > Detail akun aktor > tab System Log
55. Verifikasi jumlah entri System Log aktor bertambah tepat 2 dibanding baseline langkah 37
56. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru, satu per reader (`Zebra RFID Reader - 1 (SKU-HHR-01)` dan `Honeywell CK65 - 1`)
57. Buka Activity Log (tab `User Action`) lewat Global Settings > Activity Log > tab User Action
58. Verifikasi jumlah entri Activity Log (tab `User Action`) bertambah tepat 2 dibanding baseline langkah 38
59. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru dengan Action `Mark as Damaged`, satu per reader
60. Verifikasi tidak ada entri gabungan satu baris untuk dua reader

### TC-GS-HHR-213: Seleksi satu reader memakai dialog single dan toast bulk generik

61. Buka Global Settings > Hardware > Handheld Reader
62. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
63. Centang checkbox baris DD-01
64. Klik tombol `Bulk Action`
65. Klik `Mark as Damaged`
66. Verifikasi dialog tampil: Judul `Mark as Damaged`, Body berisi bullet `Zebra RFID Reader - 1` lalu kalimat penutup bentuk tunggal `Are you sure you want to mark it as damaged?`
67. Klik `[Mark as Damaged]` pada dialog
68. Verifikasi muncul toast sukses: "Success, reader has been marked as damaged."
69. Verifikasi Badge `Status` baris DD-01 menjadi `Damaged`

### TC-GS-HHR-461: Klik ganda cepat pada konfirmasi bulk Mark as Damaged hanya memproses satu permintaan

70. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
71. Tunggu toast lama hilang otomatis
72. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
73. Centang checkbox baris DD-01
74. Centang checkbox baris DD-07
75. Klik tombol `Bulk Action`
76. Klik `Mark as Damaged`
77. Klik ganda cepat `[Mark as Damaged]` pada dialog
78. Verifikasi hanya satu toast sukses yang tampil: "Success, reader has been marked as damaged."
79. Verifikasi toast tidak memuat kalimat `Some items were skipped.`
80. Buka ikon Changelog
81. Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 72
82. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru: `Edit` `Status` `Available` ke `Damaged`, satu untuk DD-01 dan satu untuk DD-07
83. Tutup Modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 1 sampai 12 diulang tiga kali dan langkah 24 sampai 34 diulang dua kali, sehingga ekspansi spec 36 + 11 + 22 + 26 + 9 + 14 = 118 langkah.
- Urutan TC di spec: 207, 209, 211, 218 (screening dan batal, tidak mengubah data), lalu 212 dan 210 (eksekusi pada pasangan reader yang terpisah), lalu 208 dan 219 (satu eksekusi), 213, dan 461. Menyimpang dari urutan nomor TC sumber. TC-GS-HHR-208 dan 219 memuat aksi yang sama persis (bulk Mark as Damaged atas DD-01 dan DD-07) sehingga digabung dalam satu eksekusi; Expected 208 (toast, Badge, Bar, kartu) ada di langkah 45 sampai 49 dan Expected 219 (tiga surface log) di langkah 50 sampai 60. TC-GS-HHR-210, 213, dan 461 memakai DD-01 yang berstatus Available pada precondition TC sehingga Seed Reader A dipulihkan sebelum tiap eksekusi. Langkah pemulihan pada iterasi pertama tidak mengubah apa pun dan dipertahankan agar iterasi seragam tanpa langkah bersyarat.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 23 (mengosongkan seleksi lewat `×`), langkah 24, 35, 62, dan 70 (pemulihan dan muat ulang), langkah 36 sampai 38, dan 72 (baseline jumlah entri sebelum aksi pemicu; S-12), langkah 39 dan 61 (kembali ke halaman Handheld Reader), langkah 53 dan 83 (menutup Modal Changelog), langkah 50, 54, 57, dan 80 (membuka surface log untuk dibaca), serta langkah 71 (menunggu toast lama hilang otomatis sebelum hitungan toast TC-GS-HHR-461; R-12).
- Pada TC-GS-HHR-207 sampai 218 asersi tidak ada toast (langkah 7 dan 18) diletakkan segera sesudah `[Cancel]` atau `Esc` karena toast adalah state sementara. Pada TC-GS-HHR-461 langkah 78 dan 79 diletakkan segera sesudah klik ganda dan sebelum membuka Changelog; hitungan "satu toast" didahului muat ulang halaman pada langkah 70 dan langkah 71 (menunggu toast lama hilang otomatis).
- Langkah 60 (tidak ada entri gabungan) didahului langkah 59 yang membuktikan dua entri per reader tampil pada surface yang sama (8b butir 2). Asersi jumlah entri memakai selisih terhadap baseline (S-12). Entri baru pada Changelog, System Log aktor, dan Activity Log (tab `User Action`) dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya (S-14). Tab `User Action` dipilih karena PRD Activity Log memisahkannya dari tab `Session`.
- Pengecualian alasan di atas sekitar 35 langkah (ekspansi 118): seluruh blok satu kelas (aksi bulk Mark as atas Seed Reader A), tiap eksekusi memakai pemulihan Seed Reader A sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, langkah 1 sampai 12 dan 24 sampai 34 hanya diulang per baris data, dan blok log (langkah 36 sampai 60) adalah blok baca-log berpola.
- Opsi bulk per status (TC-GS-HHR-196 sampai 200) ada di spec 044; Bulk Delete (TC-GS-HHR-214 sampai 217, 220) di spec 046; resilience 5xx bulk (TC-GS-HHR-225 dan 226) di spec 027; pencatatan log per aksi single dan sinkronisasi Hardware Stock Client Reported Condition (TC-GS-HHR-379 dan 380) tidak diasersi di spec ini.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix reader Pre-setup DD-01, DD-03, DD-04, dan DD-07 Client A karena asersi bergantung pada nama dan status persis; pemulihan ke keadaan awal lewat fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok (langkah 24, 35, 62, dan 70), dinyatakan di `suite.md` dan Prerequisites; suite serial.
- Temuan untuk QA:
  - Post Condition TC-GS-HHR-208, 210, dan 212 ("Satu entri per reader pada tiga surface log (TC section 5)"; "Hardware Stock Jalur A (TC section 7)") tidak punya langkah observasi untuk Hardware Stock di TC ini; surface log hanya diasersi untuk TC-GS-HHR-219 yang punya langkah observasinya. Hardware Stock tidak diasersi.
  - TC-GS-HHR-219 Expected b dan c tidak menyebut isi kolom entri System Log aktor selain "satu per reader" dan "Action `Mark as Damaged`" untuk Activity Log; spec mengasersi nama reader dan Action tersebut sesuai TC.
  - TC-GS-HHR-461 Expected b ("tepat dua entri") tidak menyebut cara menemukan entri di Changelog kumulatif; spec memakai selisih jumlah entri terhadap baseline.
  - TC-GS-HHR-207, 209, dan 211 Expected a.ii menulis urutan bullet "mengikuti urutan baris tabel" sehingga `Honeywell CK65 - 1` mendahului `Zebra RFID Reader - 1` (DD-07 di atas DD-01 pada tabel); `Gudang Reader - 2` mendahului `Zebra Mobile Reader - 1`. Spec mengikuti urutan itu.
  - TC-GS-HHR-218 Expected a tidak menyebut Bulk Action Bar secara terpisah dari seleksi; spec mengasersi keduanya sebagai dua klausa.
