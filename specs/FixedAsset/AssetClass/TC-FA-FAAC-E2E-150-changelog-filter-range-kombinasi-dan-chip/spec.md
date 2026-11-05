---
id: TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip
title: "Modal Changelog: Filter Date Range, Kombinasi AND, Logika OR, Search di Dropdown, dan Hapus Opsi lewat Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-489
  - TC-FA-FAAC-490
  - TC-FA-FAAC-491
  - TC-FA-FAAC-492
  - TC-FA-FAAC-493
  - TC-FA-FAAC-494
coverage:
  web: automated
---

# Modal Changelog: Filter Date Range, Kombinasi AND, Logika OR, Search di Dropdown, dan Hapus Opsi lewat Chip

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog
2. Klik icon Filter di modal

### TC-FA-FAAC-489: Filter date range pada kolom Date

3. Pilih Date dari 26/10/26 sampai 27/10/26
4. Klik `Apply`
5. Verifikasi tabel menampilkan tiga entri: STORAGE Last Exported Period (27/10/26 01:00), STORAGE Last Posted Period (26/10/26 02:00), dan HEAVY-EQ Last Posted Period (26/10/26 02:00)
6. Klik `Clear Field`
7. Klik `Apply`

### TC-FA-FAAC-490: Kombinasi beberapa field filter dengan logika AND

8. Klik icon Filter di modal
9. Pilih Action = Edit
10. Pilih Modified By = Budi S
11. Klik `Apply`
12. Verifikasi tabel menampilkan lima entri Edit milik Budi S (Status OFFICE-OLD dan empat entri Asset Names)
13. Tambahkan Field = Asset Names
14. Klik `Apply`
15. Verifikasi tabel menampilkan empat entri Asset Names (OFFICE-OLD, HEAVY-EQ, VEHICLES, IT-EQ)
16. Klik `Clear Field`
17. Klik `Apply`

### TC-FA-FAAC-491: Logika OR dalam satu field filter

18. Klik icon Filter di modal
19. Pilih Action = Create dan Delete
20. Klik `Apply`
21. Verifikasi tabel menampilkan tiga entri: dua entri Create (HEAVY-EQ dan IT-EQ) dan satu entri Delete (TEMP-EQ)
22. Klik `Clear Field`
23. Klik `Apply`

### TC-FA-FAAC-492: Search di dalam dropdown Class Code

24. Klik icon Filter di modal
25. Buka dropdown Class Code
26. Ketik `heavy` pada kotak search dropdown
27. Verifikasi daftar opsi menyempit menjadi `HEAVY-EQ`
28. Ketik `xyz` pada kotak search dropdown
29. Verifikasi tidak ada opsi yang cocok sehingga tidak ada opsi yang dapat dipilih
30. Tutup dropdown Class Code

### TC-FA-FAAC-493: Hapus opsi terpilih lewat ikon X pada chip

31. Klik icon Filter di modal
32. Pilih Action = Create dan Delete
33. Klik ikon X pada chip `Create`
34. Verifikasi chip `Delete` tetap ada
35. Verifikasi chip `Create` hilang
36. Buka dropdown Action
37. Verifikasi checkbox `Delete` tetap tercentang
38. Verifikasi checkbox `Create` tidak tercentang
39. Klik `Clear Field`

### TC-FA-FAAC-494: Hapus opsi terpilih lewat uncheck di dalam dropdown

40. Klik icon Filter di modal
41. Pilih Action = Create dan Delete
42. Buka dropdown Action lalu hilangkan centang `Create`
43. Verifikasi chip `Delete` tetap ada
44. Verifikasi chip `Create` hilang dari field
45. Klik `Clear Field`

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. TC-489 sampai TC-491 menutup dengan `Clear Field` dan `Apply` (langkah penghubung) agar filter tidak terbawa; TC-493 dan TC-494 hanya mengubah pilihan field tanpa `Apply`, sehingga pemulihannya cukup `Clear Field`. TC tidak menyebut `Apply` pada TC-492 sampai TC-494 dan spec mengikuti TC.
5. Anchor 'chip hilang' (TC-493 dan TC-494): didahului `Verifikasi` chip `Delete` tetap ada pada field yang sama (bagian 8b butir 2).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 6, 7, 16, 17, 22, 23, 30, 39, 45; langkah 8, 18, 24, 31, dan 40 membuka panel Filter modal sebelum tiap blok TC-490 sampai TC-494 sesuai langkah TC ('Klik icon Filter di modal'), karena panel tidak diasumsikan tetap terbuka sesudah `Apply`, `Clear Field`, atau pindah blok (R-l).
7. Alasan melebihi sekitar 35 langkah (45 langkah): semua blok membaca tab atau modal yang sama dengan data Pre-setup yang sama, tidak mengubah data, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
