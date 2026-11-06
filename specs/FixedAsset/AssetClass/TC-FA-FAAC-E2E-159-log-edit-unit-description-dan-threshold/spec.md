---
id: TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold
title: "Log Edit: Unit Residual Value, Useful Life Berlaku Langsung, Description, dan Capitalization Threshold"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-531
  - TC-FA-FAAC-532
  - TC-FA-FAAC-675
  - TC-FA-FAAC-676
  - TC-FA-FAAC-677
  - TC-FA-FAAC-678
coverage:
  web: automated
---

# Log Edit: Unit Residual Value, Useful Life Berlaku Langsung, Description, dan Capitalization Threshold

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-RESU` belum dipakai aset dengan Residual Value 10 Percent; `B-ASSETS2` dipakai aset dengan Useful Life 60; `B-DESCCLR` belum dipakai aset dengan Description `Desc To Clear`; `B-DESCFILL` belum dipakai aset tanpa Description; `B-THRCLR` belum dipakai aset dengan Capitalization Threshold 5000000; `B-THRFILL` belum dipakai aset tanpa Capitalization Threshold (tampil Default).
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-RESU kembali ke Residual Value 10 Percent; B-ASSETS2 kembali ke Useful Life 60 (versi baru dihapus); B-DESCCLR, B-DESCFILL, B-THRCLR, dan B-THRFILL kembali ke nilai seed.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-531: Perubahan unit Residual Value saja dicatat sebagai perubahan

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Klik link Class Code `B-RESU` di tabel
3. Klik tab `Depreciation`
4. Ganti unit Residual Value dari `Percent` menjadi `Amount` dengan nilai `10`
5. Klik `Save`
6. Tunggu aksi selesai
7. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
8. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc (Save tidak dianggap No-Op)
9. Verifikasi baris teratas Changelog: Field `Residual Value`, Old Value `10%`, New Value `10`
10. Tutup modal Changelog

### TC-FA-FAAC-532: Log versi estimasi yang berlaku langsung memakai user aktor

11. Buka Fixed Asset > Settings > Accounting > tab Asset Class
12. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
13. Klik link Class Code `B-ASSETS2` di tabel
14. Klik tab `Depreciation`
15. Ubah Useful Life menjadi `36`
16. Klik `Save`
17. Pada dialog `Apply Changes` pertahankan Effective From bulan berjalan, lalu klik `Apply`
18. Tunggu aksi selesai
19. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
20. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
21. Verifikasi baris teratas Changelog: Action `Edit`, Field `Useful Life`, Old Value `60`, New Value `36` (jumlah bulan tanpa satuan, bukan `5 yrs` dan `3 yrs`), Modified By `Rina W`
22. Tutup modal Changelog
23. Buka Global Settings > User > Detail User milik aktor > Tab System Log
24. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
25. Verifikasi baris teratas System Log aktor memuat entri yang sama: Action `Edit`, Object `Asset Class`, Name `B-ASSETS2`, Field `Useful Life`, Old Value `60`, New Value `36`

### TC-FA-FAAC-675: Log Edit Description dikosongkan menampilkan New Value —

26. Buka Fixed Asset > Settings > Accounting > tab Asset Class
27. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
28. Klik link Class Code `B-DESCCLR` di tabel
29. Kosongkan field Description lalu klik `Save`
30. Tunggu aksi selesai
31. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
32. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
33. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-DESCCLR`, Field `Description`, Old Value `Desc To Clear`, New Value `—`
34. Tutup modal Changelog

### TC-FA-FAAC-676: Log Edit Description diisi dari kosong menampilkan Old Value —

35. Buka Fixed Asset > Settings > Accounting > tab Asset Class
36. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
37. Klik link Class Code `B-DESCFILL` di tabel
38. Isi field Description dengan `Filled Desc` lalu klik `Save`
39. Tunggu aksi selesai
40. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
41. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
42. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-DESCFILL`, Field `Description`, Old Value `—`, New Value `Filled Desc`
43. Tutup modal Changelog

### TC-FA-FAAC-677: Log Edit Capitalization Threshold dikosongkan menampilkan New Value Default

44. Buka Fixed Asset > Settings > Accounting > tab Asset Class
45. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
46. Klik link Class Code `B-THRCLR` di tabel
47. Klik tab `Depreciation`
48. Kosongkan field Capitalization Threshold lalu klik `Save`
49. Tunggu aksi selesai
50. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
51. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
52. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-THRCLR`, Field `Capitalization Threshold`, Old Value `5000000` (angka polos tanpa pemisah ribuan, bukan `5,000,000`), New Value `Default`
53. Tutup modal Changelog

### TC-FA-FAAC-678: Log Edit Capitalization Threshold diisi dari kosong menampilkan Old Value Default

54. Buka Fixed Asset > Settings > Accounting > tab Asset Class
55. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
56. Klik link Class Code `B-THRFILL` di tabel
57. Klik tab `Depreciation`
58. Isi field Capitalization Threshold dengan `7500000` lalu klik `Save`
59. Tunggu aksi selesai
60. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
61. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
62. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-THRFILL`, Field `Capitalization Threshold`, Old Value `Default`, New Value `7500000` (angka polos tanpa pemisah ribuan, bukan `7,500,000`)
63. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): baseline log di awal tiap TC (langkah 1 dan langkah serupa di awal tiap blok TC) dan langkah kembali ke layar awal sebelum TC berikutnya. Langkah "Tunggu aksi selesai" (6, 18, 30, 39, 49, 59) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) TC-675 sampai TC-678 tidak menyebut dialog `Apply Changes`; Asset Class di TC itu belum dipakai aset sehingga spec tidak menulis dialog. (b) TC-532 menyebut "Apply dengan Effective From bulan berjalan" tanpa label tombol; spec memakai `Apply` seperti spec Apply Changes lain di suite ini. (c) TC-531 tidak menyebut tab Depreciation; Residual Value diasumsikan ada di tab itu seperti pada TC-532.
