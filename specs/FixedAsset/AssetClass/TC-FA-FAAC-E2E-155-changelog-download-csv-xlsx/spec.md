---
id: TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx
title: "Modal Changelog: Isi Berkas Download CSV dan XLSX serta Pengikutan Search, Filter, dan Kolom"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-679
  - TC-FA-FAAC-680
  - TC-FA-FAAC-681
  - TC-FA-FAAC-718
sourceRules: ["§4.1.1#p10", "§5#b8", "R-15", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r32", "§4.1.1#p11", "§4.1.1#r51", "§4.1.1#r34", "§4.1.1#r49", "§4.1.1#r35", "§4.1.1#r48", "§4.1.1#r38", "§4.1.1#r39", "§4.1.1#r50"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p10": [3, 8, 19, 35, 36, 45]
  "§5#b8": [5, 12, 13, 21, 23, 37]
  "R-15": [7, 18, 44]
  "§4.1.1#r26": [10, 22]
  "§4.1.1#r27": [10, 22, 35]
  "§4.1.1#r28": [10, 22]
  "§4.1.1#r29": [10, 22]
  "§4.1.1#r30": [10, 22, 37, 47]
  "§4.1.1#r31": [10, 22, 37, 47]
  "§4.1.1#r32": [10, 14, 15, 22, 24]
  "§4.1.1#p11": 11
  "§4.1.1#r51": [12, 23]
  "§4.1.1#r34": 13
  "§4.1.1#r49": [14, 24, 35]
  "§4.1.1#r35": 15
  "§4.1.1#r48": 35
  "§4.1.1#r38": 35
  "§4.1.1#r39": 35
  "§4.1.1#r50": 36
anchor: [48]
coverage:
  web: automated
---

# Modal Changelog: Isi Berkas Download CSV dan XLSX serta Pengikutan Search, Filter, dan Kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri pada langkah 50 dan di hook `after` (blok TC-718 menambah satu entri); suite berjalan serial.
- Kemampuan teknis: pembaca berkas unduhan CSV dan XLSX (nilai sel, nama sheet, kutip ganda) disediakan tim FE; berkas diunduh ke folder unduhan browser uji.
- Data Changelog khusus blok TC-718: entri Edit Total Estimated Units untuk Asset Class `B-LOGUNITS` dengan Old Value `80,000` dan New Value `125,000` ditanam lewat fixture BE (hasil TC-FA-FAAC-717) di akhir spec; tidak bergantung pada hasil spec lain.
- Kemampuan teknis: fixture BE yang mengubah isi Changelog Asset Class client hingga tersimpan dan memulihkannya ke 19 entri Pre-setup disediakan tim FE/BE; pemulihan juga dijalankan di hook `after`. Suite berjalan serial karena spec ini mengubah state Changelog bersama.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `Reset to Default`.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAC-679: Download as CSV memberi nama berkas Changelog-Asset-Class.csv dan memuat kolom serta nilai entri

2. Arahkan kursor ke icon Download pada toolbar modal
3. Verifikasi tooltip icon berbunyi `Download`
4. Klik icon Download pada toolbar modal
5. Verifikasi menu memuat `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas terunduh dengan nama `Changelog-Asset-Class.csv`
9. Buka berkas yang terunduh
10. Verifikasi baris header memuat tujuh kolom berurutan Date, Action, Class Code, Field, Old Value, New Value, Modified By
11. Verifikasi berkas memuat 19 baris data
12. Verifikasi baris Create HEAVY-EQ: Old Value `-` (hyphen tunggal, bukan `—`)
13. Verifikasi baris Delete TEMP-EQ: New Value `-`
14. Verifikasi baris Edit IT-EQ Class Name (12/08/26 08:45): Old Value `IT Equipments`, New Value `IT Equipment`, Modified By `Rina Pratiwi` (nama lengkap utuh, bukan `Rina P`)
15. Verifikasi baris entri tanpa user aktor: Modified By `System`

### TC-FA-FAAC-680: Download as XLSX memberi nama berkas Changelog-Asset-Class.xlsx dan memuat satu sheet Sheet1

16. Klik icon Download pada toolbar modal
17. Pilih `Download as XLSX`
18. Verifikasi tidak ada toast sukses
19. Verifikasi berkas terunduh dengan nama `Changelog-Asset-Class.xlsx`
20. Buka berkas yang terunduh
21. Verifikasi berkas memiliki satu sheet bernama `Sheet1`
22. Verifikasi baris header memuat tujuh kolom berurutan Date, Action, Class Code, Field, Old Value, New Value, Modified By
23. Verifikasi baris Create HEAVY-EQ: Old Value `-`
24. Verifikasi baris Edit IT-EQ Class Name (12/08/26 08:45): Modified By `Rina Pratiwi` (nama lengkap utuh, bukan `Rina P`)

### TC-FA-FAAC-681: Download mengikuti Search, Filter, dan kolom yang sedang tampil

25. Ketik Search `IT-EQ` di modal, tekan Enter
26. Klik icon Filter di modal
27. Pilih Action = Edit
28. Klik `Apply`
29. Klik ikon `⋯` pada header kolom Actions modal
30. Klik `Setup Column...`
31. Hilangkan centang `Old Value` dan `New Value`
32. Klik `Save`
33. Klik icon Download pada toolbar modal
34. Pilih `Download as CSV`
35. Verifikasi berkas hanya memuat empat baris data IT-EQ dengan Action Edit: Class Name (12/08/26), Asset Names (19/08/26), Useful Life dan Declining Rate (01/10/26)
36. Verifikasi baris Create IT-EQ dan entri Asset Class lain tidak ada pada berkas
37. Verifikasi baris header hanya memuat lima kolom Date, Action, Class Code, Field, dan Modified By (Old Value dan New Value tidak ikut)
38. Tampilkan kembali `Old Value` dan `New Value` lewat Setup Column lalu klik `Save`

### TC-FA-FAAC-718: Download as CSV menulis Old Value dan New Value Total Estimated Units sama dengan teks sel modal

39. Tutup modal Changelog dengan Close (X)
40. Tanamkan entri Changelog Edit Total Estimated Units B-LOGUNITS (80,000 menjadi 125,000) lewat fixture BE hingga tersimpan
41. Klik icon Changelog
42. Klik icon Download pada toolbar modal
43. Pilih `Download as CSV`
44. Verifikasi tidak ada toast sukses
45. Verifikasi berkas terunduh dengan nama `Changelog-Asset-Class.csv`
46. Buka berkas yang terunduh lalu baca sel Old Value dan New Value baris Edit B-LOGUNITS dengan Field `Total Estimated Units`
47. Verifikasi Old Value `80,000` dan New Value `125,000` (sama dengan teks sel modal, bukan `80000` dan bukan `125000`)
48. Verifikasi kedua nilai dibungkus tanda kutip ganda karena memuat koma
49. Tutup modal Changelog dengan Close (X)
50. Pulihkan 19 entri Changelog Pre-setup lewat fixture BE hingga tersimpan

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Temuan untuk QA: precondition TC-718 menyebut Asset Class `B-LOGUNITS` sudah diedit pada TC-FA-FAAC-717 (hasil TC lain); spec tidak menumpang hasil spec lain (S-06) dan menanam entri itu lewat fixture BE di akhir spec. Entri itu menambah baris Changelog di atas 19 entri Pre-setup yang diasersi TC-679 (19 baris data), sehingga TC-718 ditulis paling akhir.
4. Perubahan urutan TC: TC-718 ditulis paling akhir karena membutuhkan state Changelog tambahan lewat fixture BE (state berat) dan dipulihkan sesudahnya.
5. Asersi 'tidak ada toast sukses' diletakkan tepat sesudah pemicu (langkah 7, 18, dan 44) dan sebelum asersi berkas terunduh (langkah 8, 19, dan 45); berkas terunduh menjadi anchor positif sesudahnya (bagian 8b butir 11).
6. Kolom Old Value dan New Value pada TC-681 disembunyikan lewat Setup Column modal dan dipulihkan sebagai langkah penghubung; hook `after` menghapus preferensi kolom di browser.
7. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 38 sampai 40, 49, 50.
8. Alasan melebihi sekitar 35 langkah (50 langkah): seluruh blok berkelas sama (isi berkas hasil unduh dari modal Changelog yang sama), tiap blok berdiri sendiri, dan TC-FA-FAAC-681 serta TC-FA-FAAC-718 membutuhkan Search, Filter, atau state Changelog yang tidak dapat digabung ke blok lain tanpa mencampur kelas.
- P-10 (isi berkas pada spec fungsional): TC-FA-FAAC-679 memuat klausa UI (tooltip icon Download dan isi menu, langkah 3 dan 5) dan klausa isi berkas dalam satu alur; klausa UI diletakkan lebih dulu, klausa isi berkas sesudahnya, satu `Verifikasi` per klausa. Alur unduh tidak dapat dipisah dari asersi isi berkas karena berkas hanya ada sesudah menu dibuka dan format dipilih. TC-FA-FAAC-680, 681, dan 718 hanya memuat isi berkas (kelas f).
