---
id: TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select
title: "Modal Changelog: Struktur Filter Panel, Isi Opsi Dropdown, Opsi Field 24 Nilai, dan Filter Tunggal Multi-Select"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-485
  - TC-FA-FAAC-486
  - TC-FA-FAAC-487
  - TC-FA-FAAC-488
sourceRules: ["§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r32", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r33", "§4.1.1#r34", "§4.1.1#r35", "§4.1.1#r38", "§4.1.1#r40", "§4.1.1#r42", "§4.1.1#r43", "§4.1.1#r44", "§5#b3", "§4.1.1#r36", "§4.1.1#r37", "§4.1.1#r39", "§8#r3", "§4.1.1#b5"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r26": [3, 4]
  "§4.1.1#r27": [3, 5, 11]
  "§4.1.1#r28": [3, 6, 13]
  "§4.1.1#r29": [3, 7]
  "§4.1.1#r32": [3, 8, 15]
  "§4.1.1#r30": 9
  "§4.1.1#r31": 9
  "§4.1.1#r33": [13, 15]
  "§4.1.1#r34": [13, 15, 19]
  "§4.1.1#r35": [13, 15, 24, 34]
  "§4.1.1#r38": [13, 34]
  "§4.1.1#r40": 13
  "§4.1.1#r42": [13, 29]
  "§4.1.1#r43": [13, 29]
  "§4.1.1#r44": 13
  "§5#b3": 19
  "§4.1.1#r36": [24, 34]
  "§4.1.1#r37": 34
  "§4.1.1#r39": 34
  "§8#r3": 42
  "§4.1.1#b5": 42
anchor: [16]
coverage:
  web: automated
---

# Modal Changelog: Struktur Filter Panel, Isi Opsi Dropdown, Opsi Field 24 Nilai, dan Filter Tunggal Multi-Select

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Data Changelog khusus blok TC-487: Changelog hanya memuat entri Create untuk Field Class Code (tidak ada baris untuk 23 Field lainnya), dikondisikan lewat fixture BE di akhir spec dan dipulihkan ke 19 entri Pre-setup sesudahnya.
- Kemampuan teknis: fixture BE yang mengubah isi Changelog Asset Class client hingga tersimpan dan memulihkannya ke 19 entri Pre-setup disediakan tim FE/BE; pemulihan juga dijalankan di hook `after`. Suite berjalan serial karena spec ini mengubah state Changelog bersama.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog
2. Klik icon Filter di modal

### TC-FA-FAAC-485: Screening struktur Filter Panel

3. Verifikasi Filter Panel memuat lima field berurutan Date, Action, Class Code, Field, dan Modified By
4. Verifikasi field Date berupa date range dengan placeholder `Select date`
5. Verifikasi field Action berupa multi-select searchable dengan placeholder `All actions`
6. Verifikasi field Class Code berupa multi-select searchable dengan placeholder `All asset classes`
7. Verifikasi field Field berupa multi-select searchable dengan placeholder `All fields`
8. Verifikasi field Modified By berupa multi-select searchable dengan placeholder `All users`
9. Verifikasi tidak ada field filter untuk Old Value maupun New Value

### TC-FA-FAAC-486: Isi opsi dropdown Filter hanya dari entri yang tampil

10. Buka dropdown Action
11. Verifikasi opsi Action `Create`, `Edit`, dan `Delete`
12. Buka dropdown Class Code
13. Verifikasi opsi Class Code `HEAVY-EQ`, `IT-EQ`, `MACHINERY`, `OFFICE-NEW`, `OFFICE-OLD`, `STORAGE`, `TEMP-EQ`, dan `VEHICLES`
14. Buka dropdown Modified By
15. Verifikasi opsi Modified By `Rina P`, `Budi S`, dan `System`
16. Verifikasi tidak ada opsi `None` atau opsi nilai kosong pada ketiga dropdown

### TC-FA-FAAC-488: Filter tunggal pada field multi-select

17. Pilih Action = Delete
18. Klik `Apply`
19. Verifikasi tabel hanya memuat entri Delete TEMP-EQ, sedangkan entri Create dan Edit tidak tampil
20. Klik `Clear Field`
21. Klik `Apply`
22. Pilih Class Code = STORAGE
23. Klik `Apply`
24. Verifikasi tabel menampilkan dua entri STORAGE (Last Posted Period dan Last Exported Period)
25. Klik `Clear Field`
26. Klik `Apply`
27. Pilih Field = Status
28. Klik `Apply`
29. Verifikasi tabel menampilkan entri Status OFFICE-NEW dan OFFICE-OLD
30. Klik `Clear Field`
31. Klik `Apply`
32. Pilih Modified By = System
33. Klik `Apply`
34. Verifikasi tabel menampilkan lima entri System
35. Klik `Clear Field`
36. Klik `Apply`

### TC-FA-FAAC-487: Opsi Field pada Filter selalu memuat 24 nilai

37. Tutup modal Changelog dengan Close (X)
38. Kondisikan Changelog hanya memuat entri Create untuk Field Class Code lewat fixture BE hingga tersimpan
39. Klik icon Changelog
40. Klik icon Filter di modal
41. Buka dropdown Field
42. Verifikasi opsi Field memuat seluruh 24 nilai enum: Class Code, Class Name, Description, Status, Method, Useful Life, Declining Rate, Total Estimated Units, Unit Type, Residual Value, Depreciation Start Convention, Tax Depreciation Class, Tax Method, Tax Depreciation Start Rule, Capitalization Threshold, Asset Cost, Accumulated Depreciation, Depreciation Expense, Gain on Disposal, Loss on Disposal, Asset Names, Scheduled Version, Last Posted Period, Last Exported Period
43. Tutup modal Changelog dengan Close (X)
44. Pulihkan 19 entri Changelog Pre-setup lewat fixture BE hingga tersimpan

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Perubahan urutan TC: TC-488 ditulis sebelum TC-487 karena TC-487 membutuhkan state Changelog berbeda lewat fixture BE (state berat di akhir spec) dan dipulihkan sesudahnya.
4. TC-486 mengasersi bahwa tidak ada opsi `None` atau opsi kosong; anchor positifnya adalah `Verifikasi` opsi pada dropdown yang sama.
5. Langkah `Clear Field` lalu `Apply` pada TC-488 mengembalikan filter sebelum field berikutnya dipilih (langkah TC, S-09).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 37, 38, 43, 44.
7. Alasan melebihi sekitar 35 langkah (44 langkah): empat blok membaca Filter modal Changelog yang sama dengan data Pre-setup yang sama dan tiap blok berdiri sendiri; satu-satunya blok yang mengubah state (TC-487, fixture BE) ditaruh di akhir dan dipulihkan sesudahnya, sehingga kegagalannya tidak menutupi blok lain.
