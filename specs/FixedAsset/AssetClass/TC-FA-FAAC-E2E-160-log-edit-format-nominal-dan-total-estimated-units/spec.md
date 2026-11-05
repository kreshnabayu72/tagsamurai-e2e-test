---
id: TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units
title: "Log Edit: Format Angka Nominal, Desimal, Persen, dan Total Estimated Units"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-711
  - TC-FA-FAAC-713
  - TC-FA-FAAC-715
  - TC-FA-FAAC-717
coverage:
  web: automated
---

# Log Edit: Format Angka Nominal, Desimal, Persen, dan Total Estimated Units

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-LOGDEC` belum dipakai aset dengan Residual Value unit Amount 1000.25 dan Capitalization Threshold 1500.99; `B-LOGZERO` belum dipakai aset dengan Residual Value unit Amount 1500.5 dan Capitalization Threshold 1500.5; `B-LOGRATE` belum dipakai aset dengan Method Declining Balance, Declining Rate 25.5, dan Residual Value 33.3 unit Percent; `B-LOGUNITS` belum dipakai aset dengan Method Units of Production, Total Estimated Units 80000, dan Unit Type Hour meter.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: keempat Asset Class kembali ke nilai seed.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-711: Log Edit Capitalization Threshold dan Residual Value Amount menampilkan angka tersimpan polos

1. Buka Fixed Asset > Settings > Accounting > tab Asset Class
2. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
3. Klik link Class Code `B-LOGDEC` di tabel
4. Klik tab `Depreciation`
5. Ubah Residual Value (unit Amount) menjadi `2500000.75` dan Capitalization Threshold menjadi `3000000.75` lalu klik `Save`
6. Tunggu aksi selesai
7. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
8. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
9. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGDEC`, Field `Residual Value`, Old Value `1000.25`, New Value `2500000.75` (angka polos tanpa pemisah ribuan dan tanpa simbol mata uang, bukan `2,500,000.75`; desimal sebagaimana tersimpan)
10. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGDEC`, Field `Capitalization Threshold`, Old Value `1500.99`, New Value `3000000.75` (angka polos tanpa pemisah ribuan dan tanpa simbol mata uang, bukan `3,000,000.75`; desimal sebagaimana tersimpan)
11. Tutup modal Changelog

### TC-FA-FAAC-713: Log Edit Capitalization Threshold dan Residual Value Amount menghilangkan bagian desimal nol

12. Buka Fixed Asset > Settings > Accounting > tab Asset Class
13. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
14. Klik link Class Code `B-LOGZERO` di tabel
15. Klik tab `Depreciation`
16. Ubah Residual Value (unit Amount) menjadi `3000000.00` dan Capitalization Threshold menjadi `3000000.00` lalu klik `Save`
17. Tunggu aksi selesai
18. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
19. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
20. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGZERO`, Field `Residual Value`, Old Value `1500.5`, New Value `3000000` (satu digit desimal ditulis apa adanya, bukan `1500.50`; bagian desimal nol dihilangkan, bukan `3000000.00`; tanpa pemisah ribuan)
21. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGZERO`, Field `Capitalization Threshold`, Old Value `1500.5`, New Value `3000000` (satu digit desimal ditulis apa adanya, bukan `1500.50`; bagian desimal nol dihilangkan, bukan `3000000.00`; tanpa pemisah ribuan)
22. Tutup modal Changelog

### TC-FA-FAAC-715: Log Edit Declining Rate dan Residual Value Percent menghilangkan bagian desimal nol

23. Buka Fixed Asset > Settings > Accounting > tab Asset Class
24. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
25. Klik link Class Code `B-LOGRATE` di tabel
26. Klik tab `Depreciation`
27. Ubah Declining Rate menjadi `40.00` dan Residual Value (unit Percent) menjadi `12.5` lalu klik `Save`
28. Tunggu aksi selesai
29. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
30. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
31. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGRATE`, Field `Declining Rate`, Old Value `25.5`, New Value `40` (satu digit desimal ditulis apa adanya, bukan `25.50`; bagian desimal nol dihilangkan, bukan `40.00`)
32. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGRATE`, Field `Residual Value`, Old Value `33.3%`, New Value `12.5%` (satu digit desimal ditulis apa adanya, bukan `33.30%`; unit Percent tetap ditulis sebagai `%`)
33. Tutup modal Changelog

### TC-FA-FAAC-717: Log Edit Total Estimated Units menulis pemisah ribuan koma

34. Buka Fixed Asset > Settings > Accounting > tab Asset Class
35. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
36. Klik link Class Code `B-LOGUNITS` di tabel
37. Klik tab `Depreciation`
38. Ubah Total Estimated Units menjadi `125000` lalu klik `Save`
39. Tunggu aksi selesai
40. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
41. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
42. Verifikasi baris Changelog: Action `Edit`, Class Code `B-LOGUNITS`, Field `Total Estimated Units`, Old Value `80,000`, New Value `125,000` (pemisah ribuan koma seperti tampilan kolom tabel, bukan `80000` dan bukan `125000`)
43. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): baseline log di awal tiap TC (langkah 2 dan langkah serupa di awal tiap blok TC) dan langkah kembali ke layar awal sebelum TC berikutnya. Langkah "Tunggu aksi selesai" (6, 17, 28, 39) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: Expected TC-711, 713, dan 715 memuat klausa pembanding dalam kurung (bukan ...); spec menyalinnya ke dalam `Verifikasi` baris log yang sama karena kurung hanya memperjelas format nilai yang sama.
