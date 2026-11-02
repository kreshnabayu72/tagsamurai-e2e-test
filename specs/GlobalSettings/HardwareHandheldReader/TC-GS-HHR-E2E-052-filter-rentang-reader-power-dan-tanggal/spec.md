---
id: TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal
title: "Filter Rentang Daftar Reader Handheld Reader: Reader Power Min/Max Inklusif, Last Scanned, dan Activated At"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-243
  - TC-GS-HHR-244
  - TC-GS-HHR-245
  - TC-GS-HHR-246
  - TC-GS-HHR-247
  - TC-GS-HHR-248
  - TC-GS-HHR-249
coverage:
  web: automated
---

# Filter Rentang Daftar Reader Handheld Reader: Reader Power Min/Max Inklusif, Last Scanned, dan Activated At

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps`.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini). Asersi tanggal mengikuti format ini; jam server dan jam browser tidak diatur karena data tanggal berasal dari seeding tetap.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): 10 reader DD-01 sampai DD-10, dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Nama dan tanggal literal tanpa suffix `{runId}` karena asersi bergantung pada rentang tanggal dan nilai Reader Power (pengecualian S-12 Population Seed Reader A HHR, A-5; lihat Notes). Spec hanya membaca daftar. Baris dikenali lewat Serial Number. Kolom `Last Scanned` dan `Activated At` dipakai sebagai data filter (kolom `Last Scanned` dan `Activated At` memuat dua nilai atau lebih yang distinct pada tanggal berbeda):

| ID | Device Name | Serial Number | Reader Power | Last Scanned | Activated At |
|---|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | SN-HHR-00101 | 30 dBm | 21/06/26 10:15 | 21/06/26 08:00 |
| DD-02 | Gudang Reader - 1 | SN-HHR-00102 | — | 20/06/26 09:40 | 11/06/26 08:30 |
| DD-03 | Zebra Mobile Reader - 1 | SN-HHR-00103 | 25 dBm | 17/06/26 16:05 | 12/06/26 09:00 |
| DD-04 | Gudang Reader - 2 | SN-HHR-00104 | — | — | 01/06/26 07:45 |
| DD-05 | Chainway C72 - 1 | SN-HHR-00105 | 30 dBm | — | 20/06/26 11:10 |
| DD-06 | Zebra RFID Reader - 1 | SN-HHR-00107 | — | 19/06/26 13:20 | 18/06/26 15:30 |
| DD-07 | Honeywell CK65 - 1 | SN-HHR-00108 | 30 dBm | — | 22/06/26 10:00 |
| DD-08 | Unitech EA520 - 1 | SN-HHR-00109 | — | — | 23/06/26 10:30 |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | SN-HHR-00110 | 30 dBm | — | 24/06/26 09:15 |
| DD-10 | Gudang Reader - 4 | SN-HHR-00205 | — | — | 25/06/26 14:00 |

- Kemampuan teknis: pengisian field `Reader Power` (dua input `Min` dan `Max`) dan pemilihan rentang tanggal pada date range picker `Last Scanned` dan `Activated At`; pembacaan teks field date range picker.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap blok TC membuka panel sendiri, membersihkan filter dengan `[Clear Field]` lalu `[Apply]`, dan menutup panel (lihat "Temuan untuk QA").

## Test Steps

### TC-GS-HHR-243: Reader Power Min dan Max inklusif

1. Klik ikon Filter untuk membuka panel
2. Isi `Min` 25 dan `Max` 30 pada field `Reader Power`
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan 5 baris DD-01, DD-03, DD-05, DD-07, DD-09
5. Verifikasi baris batas dengan Reader Power `25 dBm` dan `30 dBm` termasuk dalam hasil
6. Verifikasi tidak ada reader Short Range (Reader Power `—`) di tabel
7. Klik `[Clear Field]`
8. Klik `[Apply]`
9. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-244: Reader Power hanya Min

10. Klik ikon Filter untuk membuka panel
11. Isi `Min` 26 dan kosongkan `Max` pada field `Reader Power`
12. Klik `[Apply]`
13. Verifikasi tabel menampilkan 4 baris DD-01, DD-05, DD-07, DD-09 (30 dBm)
14. Klik `[Clear Field]`
15. Klik `[Apply]`
16. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-245: Reader Power hanya Max

17. Klik ikon Filter untuk membuka panel
18. Isi `Max` 25 dan kosongkan `Min` pada field `Reader Power`
19. Klik `[Apply]`
20. Verifikasi tabel menampilkan 1 baris DD-03 (25 dBm)
21. Klik `[Clear Field]`
22. Klik `[Apply]`
23. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-246: Reader Power Min sama dengan Max

24. Klik ikon Filter untuk membuka panel
25. Isi `Min` 25 dan `Max` 25 pada field `Reader Power`
26. Klik `[Apply]`
27. Verifikasi tabel menampilkan 1 baris DD-03
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-247: Last Scanned rentang tanggal inklusif

31. Klik ikon Filter untuk membuka panel
32. Pilih rentang `19/06/26` sampai `21/06/26` pada field `Last Scanned`
33. Verifikasi teks field `Last Scanned` menampilkan tanggal dalam format `dd/MM/yy`
34. Klik `[Apply]`
35. Verifikasi tabel menampilkan 3 baris DD-01 (21/06), DD-02 (20/06), DD-06 (19/06)
36. Verifikasi reader yang belum pernah dipindai tidak tampil di tabel
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-248: Last Scanned satu hari (Start sama dengan End)

40. Klik ikon Filter untuk membuka panel
41. Pilih rentang `20/06/26` sampai `20/06/26` pada field `Last Scanned`
42. Klik `[Apply]`
43. Verifikasi tabel menampilkan 1 baris DD-02
44. Klik `[Clear Field]`
45. Klik `[Apply]`
46. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-249: Activated At rentang tanggal inklusif

47. Klik ikon Filter untuk membuka panel
48. Pilih rentang `11/06/26` sampai `12/06/26` pada field `Activated At`
49. Klik `[Apply]`
50. Verifikasi tabel menampilkan 2 baris DD-02 (11/06) dan DD-03 (12/06), kedua batas termasuk
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Klik ikon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti urutan TC sumber (243 sampai 249); semua blok hanya membaca dan tidak mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, serta `[Clear Field]` lalu `[Apply]` di akhir tiap blok untuk membersihkan filter sebelum blok berikutnya.
- Anchor asersi universal dan absence: pada TC-GS-HHR-243 `Verifikasi` 5 baris (termasuk batas) mendahului `Verifikasi` tidak ada reader Short Range; pada TC-GS-HHR-247 `Verifikasi` 3 baris hasil mendahului `Verifikasi` reader yang belum pernah dipindai tidak tampil. Asersi baris batas `25 dBm` dan `30 dBm` pada TC-GS-HHR-243 adalah cara mengamati klausa Expected "batas 25 dan 30 termasuk".
- Spec memuat 53 langkah (di atas smell sekitar 35 langkah, tanpa ekspansi). Alasan: seluruhnya satu kelas harness (Filter rentang daftar reader), satu akun, satu dataset, tanpa aksi yang mengubah data; tiap blok membuka panel sendiri, membersihkan filter, dan menutup panel, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Filter multi-select, chip, dan kombinasi AND ada di spec 051; kombinasi Search, Filter, dan Sort ada di spec 054.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix Seed Reader A Client A karena asersi bergantung pada rentang tanggal tetap dan nilai Reader Power; pemulihan antar TC dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di `suite.md`; spec ini hanya membaca daftar sehingga tidak ada langkah pemulihan; suite serial.
- Alasan pemisahan dari spec 050 (Search) dan 053 (Sort): ketiganya membaca dataset Seed Reader A yang sama, tetapi digabung akan melewati sekitar 170 langkah dan tiap aksi punya keadaan UI sendiri yang dibersihkan (Search ditutup, filter di-clear, sort di-reset), sehingga kegagalan satu aksi tidak menghilangkan makna aksi lain.
- Temuan untuk QA:
  - TC-GS-HHR-247 dan 248 tidak menyatakan apakah batas akhir rentang mencakup jam sehari penuh (mis. DD-01 `21/06/26 10:15` pada batas akhir `21/06/26`); spec mengikuti Expected TC (DD-01 termasuk).
  - TC-GS-HHR-247 menyebut "teks field menampilkan tanggal dalam format `dd/MM/yy`" tanpa menyebut pemisah antar tanggal rentang; spec mengasersi format tanggal, bukan teks lengkap field.
  - TC-GS-HHR-243 sampai 249: TC tidak menyatakan keadaan Filter Panel sesudah `[Apply]` (tetap terbuka atau menutup); model "tetap terbuka, ditutup dengan klik ikon Filter" diambil dari TC-GS-HHR-258 dan diterapkan sebagai langkah penghubung.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.
