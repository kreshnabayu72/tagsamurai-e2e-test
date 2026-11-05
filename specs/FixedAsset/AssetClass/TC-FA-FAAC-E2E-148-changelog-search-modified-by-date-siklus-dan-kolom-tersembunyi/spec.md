---
id: TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi
title: "Modal Changelog: Search pada Modified By, Kolom Date Tidak Dicari, Siklus Search Box, dan Kolom Field Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-481
  - TC-FA-FAAC-482
  - TC-FA-FAAC-483
  - TC-FA-FAAC-484
coverage:
  web: automated
---

# Modal Changelog: Search pada Modified By, Kolom Date Tidak Dicari, Siklus Search Box, dan Kolom Field Tersembunyi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `Reset to Default`.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog
2. Verifikasi tabel modal memuat sedikitnya satu baris entri

### TC-FA-FAAC-481: Search pada kolom Modified By

3. Ketik Search `system` di modal, tekan Enter
4. Verifikasi tabel menampilkan lima entri bertuliskan System (27/10/26 01:00, 26/10/26 02:00 dua entri, dan 01/10/26 00:05 dua entri)
5. Klik `✕` pada kotak Search di modal, tekan Enter
6. Ketik Search `budi s` di modal, tekan Enter
7. Verifikasi tabel menampilkan tujuh entri Budi S
8. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-482: Search tidak mencocokkan kolom Date

9. Ketik Search `28/10/26` di modal, tekan Enter
10. Verifikasi empty state `No results found` karena kolom Date tidak dapat dicari (penyaringan tanggal lewat Filter)
11. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-483: Siklus interaksi Search box

12. Arahkan kursor ke icon Search di modal
13. Verifikasi tooltip icon berbunyi `Search`
14. Klik icon Search di modal
15. Verifikasi Search bar melebar dengan kursor fokus
16. Ketik `budi` pada kotak Search (tanpa Enter)
17. Verifikasi icon `✕` muncul
18. Verifikasi tabel belum tersaring (entri selain Budi S masih tampil)
19. Tekan Enter
20. Verifikasi tabel menampilkan entri Budi S
21. Klik icon `✕`
22. Verifikasi teks pada kotak Search terhapus
23. Verifikasi tabel masih menampilkan hasil `budi`
24. Tekan Enter pada input kosong
25. Verifikasi semua entri kembali tampil
26. Ketik `budi`, tekan Enter
27. Klik icon `←`
28. Verifikasi kotak Search tertutup
29. Verifikasi keyword dikosongkan
30. Verifikasi tabel langsung kembali menampilkan semua entri

### TC-FA-FAAC-484: Search tidak mencari kolom Field yang disembunyikan

31. Klik ikon `⋯` pada header kolom Actions modal
32. Klik `Setup Column...`
33. Hilangkan centang `Field`
34. Klik `Save`
35. Ketik Search `declining` di modal, tekan Enter
36. Verifikasi empty state `No results found` saat kolom Field disembunyikan
37. Klik `✕` pada kotak Search di modal, tekan Enter
38. Klik ikon `⋯` pada header kolom Actions modal
39. Klik `Setup Column...`
40. Centang kembali `Field`
41. Klik `Save`
42. Ketik Search `declining` di modal, tekan Enter
43. Verifikasi tabel menampilkan entri Declining Rate IT-EQ
44. Klik `✕` pada kotak Search di modal, tekan Enter

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Anchor absence: empty state `No results found` pada TC-482 dan TC-484 adalah anchor positif hasil Search; TC-484 membuktikan kolom Field dapat dicari dengan entri Declining Rate IT-EQ setelah kolom ditampilkan kembali.
5. Langkah TC 'Arahkan kursor ke icon Search' pada TC-483 ditulis sebelum klik karena tooltip diasersi sebelum langkah yang mengubah state (bagian 8b butir 5).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 8, 11, 37, 44.
7. Alasan melebihi sekitar 35 langkah (44 langkah): semua blok membaca tab atau modal yang sama dengan data Pre-setup yang sama, tidak mengubah data, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
