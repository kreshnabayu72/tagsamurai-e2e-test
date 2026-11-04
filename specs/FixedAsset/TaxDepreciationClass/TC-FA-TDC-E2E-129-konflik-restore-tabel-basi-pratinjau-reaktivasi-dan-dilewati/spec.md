---
id: TC-FA-TDC-E2E-129-konflik-restore-tabel-basi-pratinjau-reaktivasi-dan-dilewati
title: "Konflik Restore Default Classes: Tabel Basi, Pratinjau Reaktivasi dan Dilewati, serta Nilai Tidak Ditimpa"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-320
  - TC-FA-TDC-325
  - TC-FA-TDC-326
coverage:
  web: automated
---

# Konflik Restore Default Classes: Tabel Basi, Pratinjau Reaktivasi dan Dilewati, serta Nilai Tidak Ditimpa

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk tabel tanpa class sama sekali pada company/state yang disediakan tim FE khusus automation), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (dikondisikan di hook `before` lewat API; class buatan spec dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `tabelKosong` | seluruh class | tabel tanpa class sama sekali (ketujuh seed sudah dihapus), Empty State tampil |
| `seedNb1` | `NB-1` | Class Name `Bukan bangunan – Kelompok 1` (nilai seed), Active |
| `seedNb2` | `NB-2` | Class Name `Bukan bangunan – Kelompok 2`; pada TC-FA-TDC-325 Useful Life `9` (Non-building, Straight Line), Inactive |
| `kustomNb1` | `NB-1` | Active, Class Name `Kelompok satu kustom`, Useful Life `5`, Allowed Methods `Straight Line` |
| `seedLain` | `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, `LAND` | dibuat oleh `Restore default classes` dengan nilai seed: `NB-3` `Bukan bangunan – Kelompok 3`, `NB-4` `Bukan bangunan – Kelompok 4`, `BLD-P` `Bangunan permanen`, `BLD-NP` `Bangunan tidak permanen`, `LAND` `Tanah` |

- Tabel dikembalikan ke keadaan tanpa class di antara blok (langkah 9 dan 23) karena tiap blok menghasilkan class.
- Suite berjalan serial (`parallel: false`) karena tabel tanpa class adalah state company dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-320: Pratinjau D-12 memuat tiga bagian saat data tabel usang

1. Verifikasi Empty State tabel tampil
2. Sesi B (sesi API): buat `NB-1` (Active), buat `NB-2` (Active) lalu nonaktifkan `NB-2` hingga status Inactive tersimpan
3. Sesi A: klik `Restore default classes`
4. Verifikasi bagian "To be created" memuat "• NB-3 – Bukan bangunan – Kelompok 3", "• NB-4 – Bukan bangunan – Kelompok 4", "• BLD-P – Bangunan permanen", "• BLD-NP – Bangunan tidak permanen", dan "• LAND – Tanah"
5. Verifikasi bagian "To be reactivated" memuat "• NB-2 – Bukan bangunan – Kelompok 2"
6. Verifikasi bagian "Skipped, already exists" memuat "• NB-1 – Bukan bangunan – Kelompok 1"
7. Verifikasi tombol `[Cancel]` dan `[Restore]` tampil, `[Restore]` enabled
8. Klik `[Cancel]`

### TC-FA-TDC-325: Restore mengaktifkan kembali seed Inactive tanpa mengembalikan nilai yang sudah diubah

9. Pulihkan tabel ke keadaan tanpa class lewat seeding API
10. Muat ulang halaman (F5)
11. Verifikasi Empty State tabel tampil
12. Sesi B (sesi API): buat `NB-2` dengan Useful Life `9` (Non-building, Straight Line), lalu nonaktifkan hingga status Inactive tersimpan
13. Sesi A: klik `Restore default classes`
14. Klik `[Restore]`
15. Verifikasi muncul toast sukses: `Success, default classes have been restored.`
16. Ketik Search `NB-2`, tekan Enter
17. Verifikasi baris `NB-2` berstatus Active = On
18. Klik link Class Code `NB-2`
19. Verifikasi Useful Life `9` (nilai seed `8` tidak menimpa)
20. Klik ikon ✕ pada Drawer
21. Klik `(←)` pada kotak Search
22. Verifikasi tabel memuat enam class seed lainnya (`NB-1`, `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, `LAND`) dengan nilai seed

### TC-FA-TDC-326: Restore melewati seed berkode sama yang Active dengan nilai berbeda tanpa menimpa

23. Pulihkan tabel ke keadaan tanpa class lewat seeding API
24. Muat ulang halaman (F5)
25. Verifikasi Empty State tabel tampil
26. Sesi B (sesi API): buat `NB-1` Active dengan Class Name `Kelompok satu kustom`, Useful Life `5`, dan Allowed Methods `Straight Line` hingga class tersimpan
27. Sesi A: klik `Restore default classes`
28. Verifikasi bagian "Skipped, already exists" memuat bullet "• NB-1 – Kelompok satu kustom"
29. Verifikasi `NB-1` tidak ada pada bagian "To be created"
30. Klik `[Restore]`
31. Verifikasi muncul toast sukses: `Success, default classes have been restored.`
32. Ketik Search `NB-1`, tekan Enter
33. Klik link Class Code `NB-1`
34. Verifikasi Useful Life `5`
35. Verifikasi Allowed Methods `Straight Line`
36. Klik ikon ✕ pada Drawer
37. Verifikasi tabel hanya memuat satu baris `NB-1`
38. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 8 (menutup dialog D-12 dengan `[Cancel]`), langkah 9 dan 23 (membentuk precondition tabel tanpa class), langkah 10 dan 24 (memuat ulang halaman agar Empty State tampil), langkah 16 dan 32 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 20 dan 36 (menutup Drawer yang bersih), langkah 21 dan 38 (mengosongkan Search). Langkah 1, 11, dan 25 mengamati keadaan awal "Empty State tampil" yang dinyatakan langkah TC.
- Langkah 2, 12, dan 26 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tidak memuat ulang tabel sebelum klik `Restore default classes` sehingga data tabel basi (langkah 3, 13, 27).
- Langkah 29 (absence): bagian "Skipped, already exists" langkah 28 menjadi anchor positif pada dialog yang sama (8b.2). Langkah 37 (hanya satu `NB-1`): baris `NB-1` ditemukan lewat Search langkah 32 dan seluruh baris hasil Search diasersi.
- Alasan spec melewati sekitar 35 langkah (38 langkah): ketiga blok adalah kelas c pada dialog Restore default classes, masing-masing membentuk state sendiri dari tabel kosong dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-1`, `NB-2`, dan class seed lain ditulis literal tanpa suffix `{runId}-<NNN>`; kode seed bawaan dipakai TC apa adanya (S-12), dan Lampiran A konvensi belum memuat pengecualian untuk modul ini. Tabel tanpa class sama sekali disediakan tim FE pada company/state khusus automation.
  - TC-FA-TDC-325 Post Condition (satu entri L-04 untuk `NB-2` dan enam entri L-01) dan TC-FA-TDC-326 Post Condition (tidak ada entri log untuk `NB-1`) tidak punya langkah observasi di TC; tidak diasersi (S-01, S-05).
  - TC-FA-TDC-325 Expected c ("enam class seed lainnya dibuat dengan nilai seed") tidak merinci nilai seed; spec mengasersi keberadaan keenam class dengan nilai seed (PRD §4.1.5) lewat fixture.
  - TC-FA-TDC-320 langkah 4 hanya menyebut "Amati dialog dari atas ke bawah"; spec memetakan Expected a, b, c, d ke langkah 4 sampai 7.
