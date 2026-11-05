---
id: TC-FA-FAAC-E2E-176-log-edit-field-akun-dan-class-code-tiga-surface
title: "Log Edit Asset Class: Satu Baris per Field, Format Akun, dan Class Code Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-528
  - TC-FA-FAAC-529
  - TC-FA-FAAC-530
coverage:
  web: automated
---

# Log Edit Asset Class: Satu Baris per Field, Format Akun, dan Class Code Baru

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-SHARE` (Class Name `Shared Account Renamed`, dengan Description) belum dipakai aset; `B-ANCHOR` dengan Depreciation Expense `51001 – Depreciation Expense Machinery` dan akun `51002 – Depreciation Expense Other` Active; `B-RENAME` belum terkunci (belum pernah diposting) dengan satu entri Create lama di System Log dan Activity Log.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-SHARE kembali ke Class Name `Shared Account Renamed` dan Description seed; B-ANCHOR kembali ke Depreciation Expense `51001 – Depreciation Expense Machinery`; B-RENAMED dikembalikan menjadi B-RENAME dengan Class Name seed.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-528: Log Edit satu baris per field yang berubah

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Klik link Class Code `B-SHARE` di tabel
3. Ubah Class Name menjadi `Log Rename` dan Description menjadi `Log Desc`
4. Klik `Save`
5. Tunggu aksi selesai
6. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
7. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
8. Verifikasi baris Changelog: Action `Edit`, Class Code `B-SHARE`, Field `Class Name`, Old Value `Shared Account Renamed`, New Value `Log Rename`
9. Verifikasi baris Changelog: Action `Edit`, Class Code `B-SHARE`, Field `Description`, Old Value sesuai Description seed `B-SHARE`, New Value `Log Desc`
10. Tutup modal Changelog
11. Buka Global Settings > User > Detail User milik aktor > Tab System Log
12. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
13. Verifikasi dua baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `B-SHARE`, Field `Class Name` dan Field `Description`
14. Buka Activity Log FAMS
15. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
16. Verifikasi dua baris teratas Activity Log: baris yang sama dengan Object `Asset Class`, Name `B-SHARE`, Field `Class Name` dan Field `Description`

### TC-FA-FAAC-529: Log Edit akun memakai format Account Code – Account Name

17. Buka Fixed Asset > Settings > Accounting > tab Asset Class
18. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
19. Klik link Class Code `B-ANCHOR` di tabel
20. Klik tab `Accounts`
21. Ganti Depreciation Expense dari `51001 – Depreciation Expense Machinery` ke `51002 – Depreciation Expense Other`
22. Klik `Save`
23. Tunggu aksi selesai
24. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
25. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
26. Verifikasi baris teratas Changelog: Field `Depreciation Expense`, Old Value `51001 – Depreciation Expense Machinery`, New Value `51002 – Depreciation Expense Other`
27. Tutup modal Changelog

### TC-FA-FAAC-530: Log Edit yang mengubah Class Code memakai kode baru di semua baris

28. Buka Fixed Asset > Settings > Accounting > tab Asset Class
29. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
30. Klik link Class Code `B-RENAME` di tabel (belum terkunci)
31. Ubah Class Code menjadi `B-RENAMED` dan Class Name menjadi `Renamed Class`
32. Klik `Save`
33. Tunggu aksi selesai
34. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
35. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
36. Verifikasi baris Changelog: Field `Class Code`, Old Value `B-RENAME`, New Value `B-RENAMED`, kolom Class Code `B-RENAMED`
37. Verifikasi baris Changelog: Field `Class Name`, kolom Class Code `B-RENAMED`
38. Tutup modal Changelog
39. Buka Global Settings > User > Detail User milik aktor > Tab System Log
40. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
41. Verifikasi dua baris baru System Log memakai kolom Name `B-RENAMED`
42. Cari entri Create lama atas `B-RENAME` pada System Log aktor
43. Verifikasi entri Create lama tetap memakai kolom Name `B-RENAME` (tidak diperbarui)
44. Buka Activity Log FAMS
45. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
46. Verifikasi dua baris baru Activity Log memakai kolom Name `B-RENAMED`
47. Cari entri Create lama atas `B-RENAME` pada Activity Log FAMS
48. Verifikasi entri Create lama tetap memakai kolom Name `B-RENAME` (tidak diperbarui)

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 18, dan 29 (baseline log), langkah 17 dan 28 (kembali ke layar awal), serta langkah 42 dan 47 yang mencari entri Create lama atas `B-RENAME` pada log. Langkah "Tunggu aksi selesai" (5, 23, 33) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) TC-528 menulis Old Value dan New Value Description "sesuai" tanpa nilai seed Description `B-SHARE`; spec memakai nilai seed dari fixture. (b) TC-530 tidak menyebut Old Value dan New Value baris Class Name serta cara mencari entri lama di System Log dan Activity Log; langkah pencarian ditulis sebagai langkah penghubung. (c) TC-529 mengacu TC-87 untuk keadaan awal `B-ANCHOR`; nilai akun ditulis dari Expected TC-529.
