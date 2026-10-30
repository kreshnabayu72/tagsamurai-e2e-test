---
id: TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi
title: "Bulk Action Bar: Screening, Checkbox Header, Select All Lintas Halaman, Unselect All, dan Retensi Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-109
  - TC-GS-UOM-110
  - TC-GS-UOM-111
  - TC-GS-UOM-274
  - TC-GS-UOM-275
  - TC-GS-UOM-276
  - TC-GS-UOM-277
  - TC-GS-UOM-279
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Checkbox Header, Select All Lintas Halaman, Unselect All, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE. Spec hanya memilih baris dan membaca; tidak ada data dibuat, diubah, atau dihapus (tidak ada aksi `Delete` yang dikonfirmasi).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca): `Box`, `Dozen`, `Gram`, `Kilogram`, `Liter`, `Meter`, `Pack`, `Pieces`.
- Data dinamis: Population D-01 (12 unit, nama literal tanpa suffix; pengecualian S-12): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Di-seed idempotent oleh hook `before` (dilewati bila sudah ada, cleanup hanya menghapus yang dibuat spec ini). Total baris tabel N = 20 diturunkan dari seeding (8 Pre-setup + 12 Population, butir 10 bagian 8b); hook suite membersihkan sisa unit non-Population hasil run sebelumnya.
- Nilai turunan: Search `kilo` menghasilkan M = 1 baris (`Kilogram`) pada baseline 20 unit, dihitung dari seeding.
- Cleanup: hook `after` mengosongkan seleksi dan state tabel (Search, Sort, Filter) ke default.
- Kemampuan teknis: klik header kolom untuk sort; pengisian Filter Last Updated; pembacaan state indeterminate checkbox header.
- State global yang diubah: tidak ada. Pre-setup lebih lama dari 01 Jan 2020 (Last Updated), prasyarat TC-279.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-109: Screening Bulk Action Bar saat satu baris dicentang

1. Centang baris `Meter`
2. Verifikasi Bulk Action Bar muncul rata kiri sejajar Table Tools
3. Verifikasi urutan elemen pada bar: tombol `Bulk Action`, teks `1 unit selected`, tombol `Select All (20 records)`, icon `✕`
4. Verifikasi baris `Meter` berlatar terpilih
5. Klik `Bulk Action`
6. Verifikasi overlay `Bulk Action` memuat aksi `Delete` (icon DeleteBin6Line, severity danger)
7. Tekan Esc (menutup overlay tanpa memilih aksi)

### TC-GS-UOM-110: Counter live plural dan clear lewat X

8. Klik `[✕]` pada bar (membersihkan seleksi Meter dari TC-109)
9. Centang `Meter` dan `Liter`
10. Ketik Search `Pack`, tekan Enter
11. Centang `Pack`
12. Klik `(←)` pada kotak Search
13. Verifikasi counter `3 units selected`
14. Uncheck `Pack`
15. Verifikasi counter `2 units selected`
16. Klik `[✕]` pada bar
17. Verifikasi seleksi kosong
18. Verifikasi Bulk Action Bar hilang

### TC-GS-UOM-111: Checkbox header select-all, deselect-all, dan indeterminate

19. Centang satu baris (`Meter`)
20. Verifikasi checkbox header indeterminate `[-]`
21. Klik checkbox header
22. Verifikasi seluruh baris halaman 1 tercentang
23. Klik checkbox header lagi
24. Verifikasi seleksi kosong
25. Verifikasi Bulk Action Bar hilang

### TC-GS-UOM-274: Select All (N records) memilih seluruh baris lintas halaman

26. Centang satu baris di halaman 1
27. Klik tombol `Select All (20 records)` pada Bulk Action Bar
28. Pindah ke halaman 2
29. Verifikasi counter `20 units selected`
30. Verifikasi seluruh baris halaman 2 tercentang
31. Verifikasi tombol `Select All (20 records)` berubah menjadi `Unselect All`

### TC-GS-UOM-276: Unselect All membatalkan seluruh seleksi lintas halaman

32. Klik `Unselect All` (melanjutkan seleksi 100% dari langkah 27)
33. Verifikasi seluruh checkbox baris halaman 2 tidak tercentang
34. Pindah ke halaman 1
35. Verifikasi seluruh checkbox baris halaman 1 tidak tercentang
36. Verifikasi Bulk Action Bar hilang

### TC-GS-UOM-277: Uncheck satu baris dari kondisi 100% terpilih mengembalikan tombol Select All

37. Centang satu baris, klik `Select All (20 records)`
38. Uncheck baris `Box`
39. Verifikasi counter `19 units selected`
40. Verifikasi Bulk Action Bar tetap tampil
41. Verifikasi tombol `Unselect All` berubah kembali menjadi `Select All (20 records)`
42. Klik `[✕]` pada bar

### TC-GS-UOM-275: Centang manual seluruh baris hasil Search mengubah tombol menjadi Unselect All

43. Ketik Search `kilo`, tekan Enter
44. Verifikasi baris `Kilogram` tampil sebagai hasil (M = 1)
45. Centang seluruh baris hasil Search (satu baris)
46. Verifikasi counter `1 unit selected`
47. Verifikasi tombol `Select All (1 record)` berubah menjadi `Unselect All`
48. Klik `[✕]` pada bar
49. Klik `(←)` pada kotak Search

### TC-GS-UOM-279: Seleksi dipertahankan saat pindah halaman, Search, Filter, dan Sort

50. Centang `Box` dan `Dozen`
51. Pindah ke halaman 2 lalu kembali ke halaman 1
52. Verifikasi counter `2 units selected`
53. Verifikasi `Box` dan `Dozen` tetap tercentang
54. Ketik Search `Gram`, tekan Enter
55. Verifikasi counter `2 units selected`
56. Klik `(←)` pada kotak Search
57. Verifikasi counter `2 units selected`
58. Verifikasi `Box` dan `Dozen` tetap tercentang
59. Klik header Unit Name hingga descending
60. Verifikasi counter `2 units selected`
61. Buka Filter, isi Last Updated 01 Jan 2020 sampai hari ini, klik [Apply]
62. Verifikasi counter `2 units selected`
63. Buka Filter, klik [Clear Field], klik [Apply]
64. Verifikasi counter `2 units selected`
65. Klik header Unit Name hingga kembali netral
66. Verifikasi `Box` dan `Dozen` tetap tercentang
67. Klik `[✕]` pada bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 67.
- Urutan TC dalam spec: 109, 110, 111, 274, 276, 277, 275, 279 (urutan sumber 109, 110, 111, 274, 275, 276, 277, 279). TC-276 melanjutkan seleksi 100% dari TC-274 (langkah 1 dan 2 TC-276 "centang 1 baris, klik Select All" sudah dipenuhi langkah 26 dan 27); TC-277 membuat ulang kondisi 100% (langkah 37) sebelum uncheck. TC-275 (Search) ditaruh sesudahnya karena membutuhkan state tabel bersih dari seleksi.
- Spec ini sekitar 67 langkah (di atas batas 35 langkah); alasan pertahanan: seluruh TC satu kelas dan satu dataset (Bulk Action Bar pada tabel baseline 20 unit) dan tidak ada aksi yang mengubah atau menghapus data. Blok diawali pembersihan seleksi, kecuali satu rantai: TC-276 melanjutkan TC-274 (langkah 32 memakai seleksi 100% dari langkah 27), sehingga kegagalan TC-274 membuat TC-276 kehilangan makna; blok lain berdiri sendiri. Delapan TC dipetakan ke satu spec karena kondisi data identik.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup overlay `Bulk Action`), 8, 42, 48, 67 (membersihkan seleksi, S-09), langkah 10 dan 12 (Search `Pack` membawa baris `Pack` ke halaman 1 untuk dicentang, lalu `(←)` mengosongkannya; S-14), 49 dan 56 (mengosongkan Search lewat `(←)`), langkah 65 (reset Sort ke netral), dan langkah 63 (membersihkan Filter yang merupakan bagian langkah 5 TC-279). Langkah 51 sampai 66 menyertai Verifikasi "tetap tercentang" hanya pada saat baris `Box` dan `Dozen` tampil di halaman aktif (langkah 53, 58, 66); sesudah sort descending kedua baris berada di halaman lain sehingga hanya counter yang diasersi (langkah 60, 62, 64).
- TC-GS-UOM-275: pada baseline 20 unit, Search `kilo` menghasilkan satu baris (M = 1, `Kilogram`); Expected TC menyebut `1 unit selected` bila M = 1 dan tombol `Select All (M records)` berubah menjadi `Unselect All`. Langkah 44 adalah `Verifikasi` pembanding (bagian 8b butir 2) bahwa baris `Kilogram` (M = 1) tampil sebagai hasil Search, bukan dari Expected TC; langkah 46 dan 47 mengasersi kondisi setelah baris dicentang.
- TC-GS-UOM-279 butir a ("counter tetap setelah tiap langkah") dipecah per langkah: 52, 55, 57, 60, 62, 64.
- Temuan untuk QA:
  - TC-GS-UOM-275 memakai Search `kilo` (data uji TC) yang pada baseline 20 unit hanya cocok dengan `Kilogram`, sehingga skenario "centang seluruh M baris satu per satu" tidak menguji beberapa baris; perlu data uji dengan M lebih dari 1 bila QA ingin kasus beberapa baris. Teks tombol pada M = 1 ditulis `Select All (1 record)` mengikuti bentuk tunggal di prd-conventions §8; Expected TC-GS-UOM-275 tidak menyebut bentuk tunggal itu.
  - TC-GS-UOM-279 langkah 5 menyebut Filter Last Updated "01 Jan 2020 sampai hari ini" tanpa format tanggal; spec mengikuti Format Tanggal General Settings default environment.
