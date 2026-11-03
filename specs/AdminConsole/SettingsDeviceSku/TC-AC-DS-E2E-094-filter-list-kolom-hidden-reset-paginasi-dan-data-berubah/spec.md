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
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti, termasuk `BLE-KIN-GW1` Brand `Kinetia`, `HHR-ARC-200` Model/Type `H200`, `SFR-VEL-4P`, `SFR-ZERO-01`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Pohon Category, Device Name, dan Brand (#25, #26, #27) dibaca untuk form Register. File foto `foto-a.jpg` (#37).
- Data Dinamis milik spec (S-06, S-12), dibuat dan dihapus oleh spec ini:
  - SKU hasil Register di langkah 18: `FLT-NEW-01-{runId}-094` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-F1`, foto `foto-a.jpg`). Device Name tidak disebut TC; nilai `Asset TAG` dipilih dari Pre-setup #26 (lihat Temuan untuk QA).
  - SKU target Edit: `EDT-094-{runId}`, di-seed lewat API di hook `before` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `H200`, 1 foto).
- Preferensi kolom List: langkah 1 dan 5 mengubah visibilitas kolom (tersimpan di cache browser). Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Hook `after` menghapus kedua SKU milik spec lewat API tanpa mengasumsikan seeding atau Register berhasil penuh. Pemulihan jumlah SKU (129) dan Changelog (35 entri) ke keadaan awal dilakukan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
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

26. Ketik Search `H200`, tekan Enter
27. Verifikasi baris `HHR-ARC-200` dan `EDT-094-{runId}` tampil (Model/Type `H200`)
28. Klik `⋯` baris `EDT-094-{runId}`, pilih `Edit`, ubah Model/Type menjadi `H250`, lalu klik `[Save]`
29. Verifikasi muncul toast sukses: "Success, device SKU has been updated."
30. Verifikasi baris `EDT-094-{runId}` hilang dari tampilan karena Model/Type baru tidak cocok dengan kata kunci `H200`
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09, R-16): langkah 9, 15, dan 22 melepas filter; langkah 23 mencari baris `FLT-NEW-01-{runId}-094` karena tabel memuat lebih dari satu halaman; langkah 25 dan 31 menutup Search; tanpa asersi tambahan.
- Asersi tambahan (S-03): langkah 20 dan 27 membuktikan baris pembanding tampil pada surface yang sama sebagai anchor positif absence di langkah 21 dan 30; bukan Expected TC.
- Data Edit TC-AC-DS-334 memakai SKU milik spec (`EDT-094-{runId}`) dan bukan `HHR-ARC-200`, agar data Pre-setup bersama tidak berubah (S-06); asersi tetap atas Model/Type `H200` menjadi `H250`.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `BLE-KIN-GW1`, `SFR-VEL-4P`, Brand `Kinetia`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal dan suffix `{runId}` untuk kode SKU hasil Register masih terbuka (aturan panjang dan format kode SKU tidak diketahui spec).
  - TC-AC-DS-333 tidak menyebut Device Name SKU yang didaftarkan; spec memakai `Asset TAG` dari Pre-setup #26. TC-AC-DS-334 menyebut `HHR-ARC-200` (data Pre-setup); spec memakai SKU milik spec.
  - TC-AC-DS-325 langkah 7 "buka Filter Panel" tidak menyatakan apakah panel masih terbuka setelah `[Apply]`; spec menutup lalu membuka panel di langkah 6.
  - Pemulihan Changelog 35 entri dan total 129 SKU setelah Register, Edit, dan hapus oleh spec ini bergantung pada baseline data uji (kemampuan disediakan tim FE/BE, belum tertulis di suite).
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
