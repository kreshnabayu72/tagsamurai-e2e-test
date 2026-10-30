---
id: TC-GS-IMPORT-E2E-201-commit-brand-measurement-position-menulis-satu-entri-ringkasan-ke
title: "Commit Brand, Measurement, Position menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log; kolom tiap surface"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-419
  - TC-GS-IMPORT-420
  - TC-GS-IMPORT-421
  - TC-GS-IMPORT-425
coverage:
  web: automated
---

# Commit Brand, Measurement, Position menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log; kolom tiap surface

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sungguhan di Client E (pembuat data, destruktif) dan menunggu worker commit nyata (batas tunggu 2 menit per commit; log ditulis maksimal dalam jendela itu) (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E; Sub-Tab Measurement dan Position dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis (draft commit Client E, disiapkan lewat skrip seed di hook `before`; Client E direset tanpa draft sebelum spec, Kontrak Fixture R1):
  - D-50: draft Brand 12 baris `pending` dari `brand-12.csv`: Acme Corp (#1), Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus; semua valid dan unik.
  - D-51: draft Measurement 6 baris `pending` dari `measurement-commit-6.csv` (kolom Unit Name; Symbol): Meter/m, Liter/l, Gram/g, Centimeter/cm, Pack/pk, Dozen/dz.
  - D-52: draft Position 6 baris `pending` dari `position-commit-6.csv`: Store Supervisor, HR Business Partner, IT Operations Lead, Warehouse Staff, Procurement Officer, Sales Executive.
  - Nama literal dipakai karena Client E khusus commit dan record hasil commit dihapus di hook `after`; asersi tidak bergantung pada nama record.
- Log (baseline S-12): jumlah total entri pada Pagination (Filter Action = `Import Brand`, `Import Measurement`, atau `Import Position`) dicatat per surface sebelum commit; asersi "bertambah tepat satu" membandingkan dengan baseline itu (0 bila yang tampil empty state). Total tidak diasersi sebagai angka absolut. Surface: Changelog Import (icon `[Changelog]` di header), System Log pada Detail User Yoga Permana (Tab System Log; hanya TC-GS-IMPORT-419), dan Activity Log (Global Settings > Activity Log, tab User Action).
- Akun tampil: Modified By `Yoga P` (Total Control Client E: Yoga Permana), format `[First Name] [Last Initial]`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh, D-47): hapus record Brand (Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus), Measurement (Meter, Liter, Gram, Centimeter, Pack, Dozen), dan Position (Store Supervisor, HR Business Partner, IT Operations Lead, Warehouse Staff, Procurement Officer, Sales Executive) hasil commit di Client E; hapus draft; reset hasil commit terakhir dan penanda Banner Hasil Commit.
- Kemampuan teknis: skrip seed draft D-50 sampai D-52; skrip reset Client E (D-47); worker commit berjalan normal.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Entri ringkasan Brand di tiga surface (TC-GS-IMPORT-419)

1. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
2. Buka System Log pada Detail User Yoga Permana (Tab System Log), terapkan Filter Action = `Import Brand`, lalu catat total entri pada Pagination sebagai baseline System Log (0 bila empty state)
3. Buka Activity Log (Global Settings > Activity Log) pada tab User Action, terapkan Filter Action = `Import Brand`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
4. Buka halaman Import > Brand
5. Klik `[Import (12)]`
6. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
7. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
8. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 1
9. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Brand` (plain text), Data `12 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
10. Buka System Log pada Detail User Yoga Permana (Tab System Log), terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
11. Verifikasi total System Log bertambah tepat satu dibanding baseline langkah 2
12. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Brand` (plain text), Object `Import`, Name `Brand`, Field `Import Summary`, Old Value `—`, New Value `12 records imported, 0 duplicates ignored, 0 errors remaining`
13. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
14. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 3
15. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Brand` (plain text), Object `Import`, Name `Brand`, Field `Import Summary`, Old Value `—`, New Value `12 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

### Kolom tiap surface (TC-GS-IMPORT-425)

16. Buka Changelog Import
17. Verifikasi header Changelog Import `Date | Action | Data | Modified By`, diikuti kolom Actions tanpa judul
18. Buka System Log pada Detail User Yoga Permana (Tab System Log)
19. Verifikasi header System Log `Date | Action | Object | Name | Field | Old Value | New Value`
20. Verifikasi header System Log tidak memuat kolom Modified By
21. Buka Activity Log (Global Settings > Activity Log)
22. Verifikasi header Activity Log `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`

### Entri ringkasan Measurement (TC-GS-IMPORT-420)

23. Buka Changelog Import, terapkan Filter Action = `Import Measurement`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
24. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Measurement`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
25. Buka halaman Import > Measurement
26. Klik `[Import (6)]`
27. Muat ulang halaman Import > Measurement setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
28. Buka Changelog Import, terapkan Filter Action = `Import Measurement`, lalu baca total entri pada Pagination
29. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 23
30. Verifikasi baris pertama tabel: Action `Import Measurement` (plain text), Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
31. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Measurement`, lalu baca total entri pada Pagination
32. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 24
33. Verifikasi baris pertama tabel: Action `Import Measurement` (plain text), Object `Import`, Name `Measurement`, Field `Import Summary`, Old Value `—`, New Value `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

### Entri ringkasan Position (TC-GS-IMPORT-421)

34. Buka Changelog Import, terapkan Filter Action = `Import Position`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
35. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Position`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
36. Buka halaman Import > Position
37. Klik `[Import (6)]`
38. Muat ulang halaman Import > Position setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
39. Buka Changelog Import, terapkan Filter Action = `Import Position`, lalu baca total entri pada Pagination
40. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 34
41. Verifikasi baris pertama tabel: Action `Import Position` (plain text), Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
42. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Position`, lalu baca total entri pada Pagination
43. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 35
44. Verifikasi baris pertama tabel: Action `Import Position` (plain text), Object `Import`, Name `Position`, Field `Import Summary`, Old Value `—`, New Value `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 44 langkah, di atas 35 langkah. Alasan: tiap blok berpola sama (catat baseline, commit, tunggu, baca log lewat tiga atau dua surface) dan berdiri sendiri; blok baca-log berpola tidak dihitung sebagai smell (bagian 3 prinsip 13). Kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok memakai Sub-Tab, draft, dan Filter Action sendiri.
- Perubahan urutan (S-05): TC-GS-IMPORT-425 ditaruh setelah TC-GS-IMPORT-419 karena Precondition c TC-425 mensyaratkan entri ringkasan commit Brand sudah tercatat di tiga surface (Dependensi 1) dan Changelog tidak menampilkan header tabel bila tidak ada entri. Dalam hal ini screening kolom bukan di awal spec.
- Langkah 6, 27, dan 38 adalah menunggu worker commit nyata (muat ulang tiap 5 detik, batas 2 menit) seperti yang tertulis di TC, bukan jeda waktu buatan.
- Langkah 1-3 mencatat baseline sebelum aksi pemicu pertama yang diasersi (S-12).
- Temuan untuk QA:
  - TC-GS-IMPORT-419 Post Condition a (draft Brand dihapus) dan b (12 record Brand tersimpan di Master Reference > Brand) tidak punya langkah observasi di TC; tidak diasersi (S-01). TC-GS-IMPORT-420, 421 Post Condition a, b, c ditangani sama.
  - TC-GS-IMPORT-425 membaca header tiga surface tanpa data yang disebut di Data Dinamis; spec bergantung pada entri commit TC-GS-IMPORT-419 di spec yang sama.
  - Jumlah record Position hasil commit TC-421 memengaruhi batas Master Data Count Limit Client E; tidak diasersi.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
