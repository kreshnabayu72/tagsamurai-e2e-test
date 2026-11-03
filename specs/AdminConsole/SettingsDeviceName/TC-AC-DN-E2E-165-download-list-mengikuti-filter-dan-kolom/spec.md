---
id: TC-AC-DN-E2E-165-download-list-mengikuti-filter-dan-kolom
title: "Download List: Mengikuti Search, Filter, Sidebar, dan Kolom yang Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-370
  - TC-AC-DN-371
  - TC-AC-DN-372
  - TC-AC-DN-373
coverage:
  web: automated
---

# Download List: Mengikuti Search, Filter, Sidebar, dan Kolom yang Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #16 (`Door Antenna`, `Gate Antenna`, Category `Antenna`, Measurement `Unit`), #17 seed 120 baris, #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE): pembaca berkas CSV hasil unduhan; penghapusan preferensi Setup Column di browser di hook `after` (bagian 4). Kelas harness e: dataset 130 baris.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-372: Kolom yang disembunyikan tidak ikut diekspor
2. Klik header `⋯`, hapus centang `Measurement`
3. Verifikasi kolom Measurement hilang dari tabel
4. Klik ikon Download lalu klik `Download as CSV`
5. Verifikasi tidak ada toast atau peringatan tambahan
6. Buka file hasil unduhan dengan pembaca berkas CSV
7. Verifikasi header file memuat `Device Name`, `Category`, `Brand`, `Model/Type`, `Last Modified` dan tidak memuat `Measurement`
8. TC-AC-DN-373: Kolom yang ditampilkan kembali ikut diekspor lagi
9. Klik header `⋯`, centang `Measurement` kembali
10. Verifikasi kolom Measurement tampil lagi
11. Klik ikon Download lalu klik `Download as CSV`
12. Buka file hasil unduhan dengan pembaca berkas CSV
13. Verifikasi header file memuat `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`
14. TC-AC-DN-370: Download mengikuti Search dan Filter yang sedang aktif
15. Ketik Search `Antenna`, tekan Enter
16. Klik ikon Filter lalu klik field `Measurement`, centang `Unit`, klik `[Apply]`
17. Verifikasi List memuat 2 baris
18. Klik ikon Download lalu klik `Download as CSV`
19. Buka file hasil unduhan dengan pembaca berkas CSV
20. Verifikasi file memuat baris header ditambah 2 baris data: Door Antenna dan Gate Antenna
21. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
22. Klik `(←)` pada kotak Search
23. TC-AC-DN-371: Download mengikuti pilihan Category Sidebar
24. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
25. Klik node `Antenna` pada Category Sidebar
26. Verifikasi List memuat 2 baris
27. Klik ikon Download lalu klik `Download as CSV`
28. Buka file hasil unduhan dengan pembaca berkas CSV
29. Verifikasi file memuat baris header ditambah 2 baris data: Door Antenna dan Gate Antenna
30. Hapus pilihan node `Antenna`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): mengosongkan Search, Filter, dan pilihan node Sidebar antar-TC (S-09); membuka cabang Sidebar `Hardware` > `Smart Fixed Reader`.
- Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Langkah 5 (tidak ada toast atau peringatan tambahan) ditempatkan tepat sesudah klik `Download as CSV` sebelum berkas dibuka (bagian 8b butir 11) (S-03).
- Urutan: TC-AC-DN-372, 373, 370, 371 (sourceTc 370 sampai 373): TC kolom dijalankan lebih dulu agar List bersih dari Search, Filter, dan Sidebar (S-09, S-10).
- Temuan untuk QA:
  - TC-AC-DN-370 dan 371 mengasumsikan hanya `Door Antenna` dan `Gate Antenna` yang cocok; asumsi bergantung dataset fixture.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
