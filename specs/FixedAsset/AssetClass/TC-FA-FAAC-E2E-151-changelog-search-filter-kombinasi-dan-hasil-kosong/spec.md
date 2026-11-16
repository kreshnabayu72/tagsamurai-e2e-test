---
id: TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong
title: "Modal Changelog: Kombinasi Search dan Filter, Hasil Kosong Pulih, dan Kombinasi Search, Filter, Sort, serta Ukuran Halaman"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-495
  - TC-FA-FAAC-496
  - TC-FA-FAAC-497
  - TC-FA-FAAC-498
sourceRules: ["§4.1.1#r27", "§4.1.1#r32", "§4.1.1#p10", "ST-27", "§4.1.1#r26", "§5#b5", "§4.1.1#r49"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r27": [6, 15, 16, 36]
  "§4.1.1#r32": [6, 15, 27, 35, 36]
  "§4.1.1#p10": [7, 16, 35]
  "ST-27": 24
  "§4.1.1#r26": [35, 37]
  "§5#b5": 35
  "§4.1.1#r49": 37
coverage:
  web: automated
---

# Modal Changelog: Kombinasi Search dan Filter, Hasil Kosong Pulih, dan Kombinasi Search, Filter, Sort, serta Ukuran Halaman

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

### TC-FA-FAAC-495: Search lalu Filter

2. Ketik Search `budi` di modal, tekan Enter
3. Klik icon Filter di modal
4. Pilih Action = Edit
5. Klik `Apply`
6. Verifikasi tabel menampilkan lima entri Edit milik Budi S
7. Verifikasi keyword `budi` tetap terisi pada kotak Search
8. Klik `Clear Field`
9. Klik `Apply`
10. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-496: Filter lalu Search

11. Klik icon Filter di modal
12. Pilih Action = Edit
13. Klik `Apply`
14. Ketik Search `budi` di modal, tekan Enter
15. Verifikasi tabel menampilkan lima entri Edit milik Budi S
16. Verifikasi filter Action = Edit tetap aktif
17. Klik `✕` pada kotak Search di modal, tekan Enter
18. Klik `Clear Field`
19. Klik `Apply`

### TC-FA-FAAC-497: Hasil kosong pulih saat salah satu saringan dilepas

20. Ketik Search `rina` di modal, tekan Enter
21. Klik icon Filter di modal
22. Pilih Modified By = Budi S
23. Klik `Apply`
24. Verifikasi empty state menampilkan `No results found` dan `Try adjusting your search or filter.`
25. Klik `Clear Field`
26. Klik `Apply`
27. Verifikasi tabel pulih menampilkan tujuh entri Rina P
28. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-498: Kombinasi Search, Filter, Sort, dan ukuran halaman

29. Ketik Search `edit` di modal, tekan Enter
30. Klik icon Filter di modal
31. Pilih Modified By = Rina P
32. Klik `Apply`
33. Klik header Date satu kali
34. Ubah ukuran halaman ke 25
35. Verifikasi keempat kontrol (Search `edit`, Filter Modified By = Rina P, sort Date, ukuran halaman 25) berlaku bersamaan
36. Verifikasi tabel menampilkan enam entri Edit milik Rina P
37. Verifikasi urutan Oldest First dimulai dari Class Name IT-EQ 12/08/26

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Pemulihan antar blok: `Clear Field` + `Apply` dan `✕` + Enter mengembalikan Filter dan Search ke kosong sebelum blok berikutnya (S-09); blok terakhir tidak memerlukan pemulihan karena state modal hilang saat modal ditutup hook `beforeEach`.
5. Anchor 'hasil kosong' (TC-497): empty state `No results found` adalah anchor positif hasil Search dan Filter; pemulihan dibuktikan dengan tujuh entri Rina P.
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 8 sampai 10, 17 sampai 19, 28.
7. Alasan melebihi sekitar 35 langkah (37 langkah): semua blok membaca tab atau modal yang sama dengan data Pre-setup yang sama, tidak mengubah data, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
