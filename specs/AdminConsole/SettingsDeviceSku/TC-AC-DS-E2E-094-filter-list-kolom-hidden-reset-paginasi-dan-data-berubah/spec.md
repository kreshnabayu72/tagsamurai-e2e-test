---
id: TC-AC-DS-E2E-094-filter-list-kolom-hidden-reset-paginasi-dan-data-berubah
title: "Filter List: Kolom Hidden, Reset Paginasi, serta Register dan Edit saat Filter atau Search Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-325
  - TC-AC-DS-326
  - TC-AC-DS-333
  - TC-AC-DS-334
coverage:
  web: automated
---

# Filter List: Kolom Hidden, Reset Paginasi, serta Register dan Edit saat Filter atau Search Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti, termasuk `BLE-KIN-GW1` Brand `Kinetia`, `HHR-ARC-200` Model/Type `H200`, `SFR-VEL-4P`, `SFR-ZERO-01`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Data khusus TC #44: SKU `SCH-334-01` (Device Name `Asset TAG`, Category `Asset TAG`, Brand `Arcturus`, Model/Type `H334`, stok 0, 1 foto) dipakai TC-AC-DS-334 dan ditulis literal sesuai TC (pengecualian S-12 A-11); Edit di langkah 28 mengubah Model/Type-nya menjadi `H335`, dan SKU itu dipulihkan atau dihapus oleh automation baseline (seed atau fixture BE disediakan tim FE/BE) sesuai tabel Pre-setup TC. Pohon Category, Device Name, dan Brand (#25, #26, #27) dibaca untuk form Register. File foto `foto-a.jpg` (#37).
- Data Dinamis milik spec (S-06, S-12), dibuat dan dihapus oleh spec ini:
  - SKU hasil Register di langkah 18: `FLT-NEW-01-{runId}-094` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-F1`, foto `foto-a.jpg`). Device Name `Asset TAG` disebut eksplisit oleh TC-AC-DS-333 (Pre-setup #26).
- Preferensi kolom List: langkah 1 dan 5 mengubah visibilitas kolom (tersimpan di cache browser). Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Hook `after` menghapus SKU hasil Register milik spec lewat API tanpa mengasumsikan Register berhasil penuh. Pemulihan jumlah SKU (129), Model/Type `SCH-334-01` (`H334`), dan entri Changelog buatan spec ke keadaan awal dilakukan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.

## Test Steps

### TC-AC-DS-325: Filter pada kolom Hidden

1. Klik header kolom Actions (⋯), lalu centang `Hardware Type` pada Overlay Column Visibility
2. Klik ikon Filter
3. Pada field Hardware Type pilih `Smart Fixed Reader`
4. Klik `[Apply]`
5. Klik header kolom Actions (⋯), lalu hilangkan centang `Hardware Type` pada Overlay Column Visibility
6. Klik ikon Filter sehingga panel tertutup, lalu klik ikon Filter lagi sehingga panel terbuka
7. Verifikasi field Hardware Type tetap ada di Filter Panel walau kolomnya Hidden
8. Verifikasi filter ter-Apply tetap berlaku: tabel memuat `SFR-VEL-4P` dan `SFR-ZERO-01`
9. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-326: Apply Filter dari halaman lebih dari 1

10. Klik nomor halaman 3
11. Pada field Brand pilih `Arcturus`
12. Klik `[Apply]`
13. Verifikasi hasil filter tampil pada halaman 1
14. Verifikasi indikator halaman menunjukkan 1
15. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-333: Register SKU yang tidak cocok dengan filter aktif

16. Pada field Brand pilih `Kinetia`
17. Klik `[Apply]`
18. Klik `[+ SKU]`, isi Category `Asset TAG`, Device Name `Asset TAG`, SKU `FLT-NEW-01-{runId}-094`, Brand `Arcturus`, Model/Type `T-F1`, unggah foto `foto-a.jpg`, lalu klik `[Submit]`
19. Verifikasi muncul toast sukses: "Success, device SKU has been registered."
20. Verifikasi baris `BLE-KIN-GW1` (Brand `Kinetia`) tetap tampil pada tabel yang sedang difilter
21. Verifikasi baris `FLT-NEW-01-{runId}-094` tidak muncul pada tabel yang sedang difilter Brand `Kinetia`
22. Klik `[Clear Field]`, lalu `[Apply]`
23. Ketik Search `FLT-NEW-01-{runId}-094`, tekan Enter
24. Verifikasi baris `FLT-NEW-01-{runId}-094` tampil setelah filter dilepas
25. Klik `(←)` pada kotak Search

### TC-AC-DS-334: Edit yang membuat baris tidak cocok dengan Search aktif

26. Ketik Search `H334`, tekan Enter
27. Verifikasi baris `SCH-334-01` tampil (Model/Type `H334`)
28. Klik `⋯` baris `SCH-334-01`, pilih `Edit`, ubah Model/Type menjadi `H335`, lalu klik `[Save]`
29. Verifikasi muncul toast sukses: "Success, device SKU has been updated."
30. Verifikasi baris `SCH-334-01` hilang dari tampilan karena Model/Type baru `H335` tidak cocok dengan kata kunci `H334`
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09, R-16): langkah 9, 15, dan 22 melepas filter; langkah 23 mencari baris `FLT-NEW-01-{runId}-094` karena tabel memuat lebih dari satu halaman; langkah 25 dan 31 menutup Search; tanpa asersi tambahan.
- Asersi tambahan (S-03): langkah 20 membuktikan baris pembanding tampil pada surface yang sama sebagai anchor positif absence di langkah 21; langkah 27 membuktikan baris target tampil sebelum Edit dan toast sukses langkah 29 menjadi anchor absence di langkah 30; bukan Expected TC.
- Data Edit TC-AC-DS-334 memakai SKU data khusus TC `SCH-334-01` (Pre-setup #44), bukan SKU inti #29, sehingga data Pre-setup bersama tidak berubah; asersi atas Model/Type `H334` menjadi `H335` sesuai TC.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `BLE-KIN-GW1`, `SFR-VEL-4P`, Brand `Kinetia`). Pengecualian S-12 A-11 (`suite.md`) berlaku untuk nama literal Pre-setup; spec mengikuti TC dengan seeding idempoten dan suite serial, dan kode SKU hasil Register diberi suffix `{runId}-094`.
  - TC-AC-DS-325 langkah 7 "buka Filter Panel" tidak menyatakan apakah panel masih terbuka setelah `[Apply]`; spec menutup lalu membuka panel di langkah 6.
  - Pemulihan entri Changelog buatan spec, total 129 SKU, dan Model/Type `SCH-334-01` setelah Register, Edit, dan hapus oleh spec ini bergantung pada baseline data uji (kemampuan disediakan tim FE/BE, belum tertulis di suite).
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
