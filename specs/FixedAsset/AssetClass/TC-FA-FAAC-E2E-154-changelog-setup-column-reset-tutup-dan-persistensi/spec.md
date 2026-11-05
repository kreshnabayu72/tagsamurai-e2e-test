---
id: TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi
title: "Modal Changelog: Setup Column Reset to Default, Tutup dengan X, Satu Kolom Tersisa, dan Tidak Memengaruhi Tabel Asset Class"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-507
  - TC-FA-FAAC-508
  - TC-FA-FAAC-509
  - TC-FA-FAAC-510
coverage:
  web: automated
---

# Modal Changelog: Setup Column Reset to Default, Tutup dengan X, Satu Kolom Tersisa, dan Tidak Memengaruhi Tabel Asset Class

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Data Pre-setup 9 Asset Class contoh tersedia (nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive); dipakai pada blok TC-510 untuk memeriksa kolom tabel Asset Class.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `Reset to Default`.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAC-507: Reset to Default pada Setup Column

2. Klik ikon `⋯` pada header kolom Actions modal
3. Klik `Setup Column...`
4. Hilangkan centang `Field` dan seret `Date` ke posisi terakhir
5. Klik `Reset to Default`
6. Klik `Save`
7. Verifikasi tabel modal kembali menampilkan ketujuh kolom
8. Verifikasi urutan awal Date, Action, Class Code, Field, Old Value, New Value, Modified By

### TC-FA-FAAC-508: Tutup Setup Column dengan X membuang perubahan

9. Klik ikon `⋯` pada header kolom Actions modal
10. Klik `Setup Column...`
11. Hilangkan centang `Field`
12. Klik Close (X)
13. Verifikasi Setup Column tertutup
14. Verifikasi kolom Field tetap tampil pada tabel modal

### TC-FA-FAAC-509: Satu kolom tersisa tidak dapat disembunyikan

15. Klik ikon `⋯` pada header kolom Actions modal
16. Klik `Setup Column...`
17. Hilangkan centang kolom satu per satu hingga tersisa satu kolom
18. Arahkan kursor ke checkbox kolom yang tersisa
19. Verifikasi checkbox kolom terakhir Disabled dan tetap tampil
20. Verifikasi tooltip berbunyi `At least one column must remain visible.`
21. Klik Close (X)

### TC-FA-FAAC-510: Konfigurasi kolom modal Changelog tidak memengaruhi tabel Asset Class

22. Klik ikon `⋯` pada header kolom Actions modal
23. Klik `Setup Column...`
24. Hilangkan centang `Field`
25. Klik `Save`
26. Tutup modal Changelog dengan Close (X)
27. Verifikasi tabel Asset Class tetap menampilkan sembilan kolom bawaan Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, dan Assets

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Spec berakhir dengan kolom Field tersembunyi pada modal Changelog (TC-510 menyimpan konfigurasi); hook `after` menghapus preferensi kolom di browser (S-09, suite.md).
5. TC-509 tidak menyebut kolom mana yang tersisa; spec mengikuti TC dan menyebut checkbox kolom yang tersisa.
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 21.
