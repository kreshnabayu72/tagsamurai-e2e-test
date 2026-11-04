---
id: TC-FA-TDC-E2E-206-general-settings-format-tanggal-jam-dan-zona-waktu-changelog-dan-last-updated
title: "General Settings: Format Tanggal, Jam, dan Zona Waktu pada Changelog, Date Filter, Last Updated, dan Effective From"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-779
  - TC-FA-TDC-780
  - TC-FA-TDC-781
  - TC-FA-TDC-782
  - TC-FA-TDC-783
coverage:
  web: automated
---

# General Settings: Format Tanggal, Jam, dan Zona Waktu pada Changelog, Date Filter, Last Updated, dan Effective From

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleData`, fixture belum ada): sembilan class Example Data PRD dengan tabel dalam satu halaman (9 baris, 10 baris per halaman) sehingga baris target tidak dicari lewat Search. Kondisi yang dipakai: entri Changelog Status NB-4 (seed, kunci `changelogStatusNb4`) dibuat 28 Oktober 2026 pukul 02:15 UTC dan NB-4 terakhir diubah pada waktu yang sama; NB-4 memiliki Effective From Current `Jan 2026` (TC-783). Baris entri Changelog seed dikenali lewat kolom Date dan Filter Class Code `NB-4` karena Changelog adalah audit trail permanen yang tumbuh (S-14). Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data General Settings per blok (disediakan tim FE/BE lewat seeding API, kunci `generalSettingsFormat`): TC-779, 781, 782: format tanggal `dd/MM/yy`, format jam `24-hour`, zona waktu `Asia/Jakarta UTC+07:00`; TC-780: `M/d/yy`, `12-hour hh:mm A`, `Asia/Makassar UTC+08:00`; TC-783: format tanggal awal `DD/MM/YYYY` lalu diubah lewat UI ke `MM/DD/YYYY`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding entri Changelog dengan waktu pembuatan tetap, perubahan nilai General Settings dan pemulihannya lewat API, seeding Effective From versi Current; Setup Column dengan pemulihan eksplisit (8b.14, R-24).
- State global yang diubah: General Settings company (format tanggal, jam, zona waktu) dan konfigurasi kolom tabel (kolom Last Updated ditampilkan lalu disembunyikan kembali pada langkah 14 sampai 16). Dipulihkan di langkah 37 dan di hook `after` (General Settings dikembalikan ke nilai awal company; preferensi kolom di browser dihapus).

## Test Steps

### TC-FA-TDC-779: Kolom Date pada Changelog mengikuti format General Settings

1. Seed General Settings (`dd/MM/yy`, `24-hour`, `Asia/Jakarta UTC+07:00`) dan entri Changelog Status NB-4 dibuat 28 Oktober 2026 pukul 02:15 UTC lewat seeding API, lalu muat ulang halaman
2. Klik ikon Changelog di toolbar tab Tax Depreciation Class
3. Klik ikon Filter modal Changelog
4. Isi filter Class Code `NB-4`
5. Verifikasi kolom Date pada baris Status NB-4 menampilkan `28/10/26 09:15`

### TC-FA-TDC-781: Input Date Filter Changelog menampilkan tanggal terpilih sesuai format General Settings

6. Buka date range picker Date
7. Pilih rentang 1 Oktober 2026 sampai 28 Oktober 2026
8. Verifikasi kotak input Date menampilkan teks tanggal terpilih dalam format `dd/MM/yy` (`01/10/26 - 28/10/26`)
9. Tutup modal Changelog lewat `[×]` pada header modal

### TC-FA-TDC-782: Kolom Last Updated pada tabel mengikuti format General Settings

10. Klik header Actions `⋯`
11. Centang kolom Last Updated
12. Klik `[Save]` pada overlay Setup Column
13. Verifikasi kolom Last Updated baris NB-4 menampilkan `28/10/26 09:15`
14. Klik header Actions `⋯`
15. Hilangkan centang kolom Last Updated
16. Klik `[Save]` pada overlay Setup Column

### TC-FA-TDC-780: Perubahan General Settings ke format 12 jam dan zona waktu lain tercermin di Changelog

17. Ubah General Settings (`M/d/yy`, `12-hour hh:mm A`, `Asia/Makassar UTC+08:00`) lewat seeding API, lalu muat ulang halaman
18. Klik ikon Changelog di toolbar tab Tax Depreciation Class
19. Klik ikon Filter modal Changelog
20. Isi filter Class Code `NB-4`
21. Verifikasi kolom Date pada baris Status NB-4 menampilkan `10/28/26 10:15 AM`
22. Tutup modal Changelog lewat `[×]` pada header modal

### TC-FA-TDC-783: Effective From pada tabel tetap berformat MMM YYYY walau format tanggal General Settings berubah

23. Ubah General Settings (format tanggal `DD/MM/YYYY`) dan Effective From Current NB-4 `Jan 2026` lewat seeding API, lalu muat ulang halaman
24. Verifikasi kolom Effective From baris NB-4 menampilkan `Jan 2026`
25. Buka General Settings
26. Ubah format tanggal menjadi `MM/DD/YYYY`
27. Klik `[Save]` hingga perubahan berhasil tersimpan
28. Buka Settings > Accounting > Tax Depreciation Class
29. Muat ulang halaman
30. Verifikasi kolom Effective From baris NB-4 menampilkan `Jan 2026`
31. Klik ikon Changelog di toolbar tab Tax Depreciation Class
32. Klik ikon Filter modal Changelog
33. Isi filter Class Code `NB-4`
34. Verifikasi kolom Date pada Changelog menampilkan tanggal dalam format `MM/DD/YYYY` (`10/28/2026` untuk entri yang dibuat 28 Oktober 2026)
35. Verifikasi nilai Effective From di Changelog tetap `Jan 2026`
36. Tutup modal Changelog lewat `[×]` pada header modal
37. Pulihkan General Settings ke nilai awal company lewat seeding API

## Notes

- Urutan TC di spec: 779, 781, 782, 780, 783. TC-781 dan TC-779 memakai format General Settings yang sama dan membuka modal Changelog; langkah 1 dan 2 TC-781 ("Klik ikon Changelog", "Klik ikon Filter") identik dengan langkah 2 dan 3 yang sudah dijalankan pada blok TC-779, sehingga blok TC-781 melanjutkan dari panel Filter yang terbuka. TC-782 memakai format yang sama; TC-780 dan TC-783 memakai format berbeda sehingga mengikutinya.
- Langkah penghubung (S-03): langkah 1, 17, 23, dan 37 (seeding General Settings dan entri seed, tanpa asersi), langkah 9, 22, dan 36 (menutup modal Changelog), langkah 3 dan 4, 19 dan 20, 32 dan 33 (Filter Class Code `NB-4` untuk menemukan baris seed pada audit trail yang tumbuh, R-16 dan S-14), langkah 14 sampai 16 (pemulihan Setup Column, 8b.14 dan R-24), dan langkah 28 sampai 29 (berpindah halaman lalu muat ulang tab sesuai TC-783).
- Alasan di atas ~35 langkah: semua blok satu topik (format tanggal, jam, dan zona waktu General Settings pada surface Tax Depreciation Class), tiap blok berdiri sendiri dengan nilai General Settings yang dinyatakan di Prerequisites; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-779 sampai 783 menyebut "baris Status NB-4" pada Changelog tanpa cara menemukannya; spec memakai Filter Class Code `NB-4` dan mengenali baris seed lewat kolom Date.
  - TC-783 Expected b tidak menyebut nilai persis kolom Date Changelog (format MM/DD/YYYY tanpa jam) dan tidak menyebut format jam/zona waktu pada blok itu; spec mengasersi tanggal `10/28/2026`.
  - TC-783 mengubah General Settings lewat UI tanpa menyebut jalur menu; spec menulis "Buka General Settings".
  - TC-781 Expected hanya menyebut "teks tanggal terpilih dalam format dd/MM/yy" tanpa teks lengkap input rentang; spec menulis `01/10/26 - 28/10/26` sesuai kolom Data Uji TC.
  - TC-780 Expected `10/28/26 10:15 AM` menunjukkan kolom Date memakai pemisah spasi antara tanggal dan jam; diikuti apa adanya.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
