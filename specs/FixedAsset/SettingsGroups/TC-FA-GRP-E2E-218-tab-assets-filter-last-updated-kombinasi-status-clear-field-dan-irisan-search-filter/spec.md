---
id: TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter
title: "Tab Assets Filter Last Updated, Kombinasi Status + Last Updated (AND), [Clear Field], dan Search lalu Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-690
  - TC-FA-GRP-691
  - TC-FA-GRP-692
  - TC-FA-GRP-693
coverage:
  web: automated
---

# Tab Assets Filter Last Updated, Kombinasi Status + Last Updated (AND), [Clear Field], dan Search lalu Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Rentang tanggal Last Updated: Fixture.settingsGroups.lastUpdatedAwal dan Fixture.settingsGroups.lastUpdatedAkhir (rentang yang memuat sebagian baris Warehouse A dan tidak memuat sebagian lain); Fixture.settingsGroups.lastUpdatedHari adalah satu tanggal yang memuat sedikitnya satu baris dan tidak memuat baris lain. Format teks tanggal mengikuti Date Format General Settings client (tidak diubah spec ini).
- Status filter Fixture.settingsGroups.statusA; Search keyword Fixture.settingsGroups.searchKeywordIrisan dan Fixture.settingsGroups.irisanSemuaField (nilai tiap field Filter Panel yang beririsan dengan baris sasaran Fixture.settingsGroups.irisanBaris; nilai kolom bergerbang yang diisi mengikuti hak Total Control).

## Test Steps

### TC-FA-GRP-690: Filter Last Updated rentang tanggal

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Catat jumlah baris tabel Tab Assets sebelum Filter dipasang
4. Klik icon Filter
5. Buka date range picker Last Updated, pilih tanggal awal `Fixture.settingsGroups.lastUpdatedAwal` dan tanggal akhir `Fixture.settingsGroups.lastUpdatedAkhir`
6. Verifikasi teks tanggal di input mengikuti Date Format General Settings
7. Klik [Apply]
8. Verifikasi sedikitnya satu baris tampil
9. Verifikasi setiap baris yang tampil memiliki Last Updated dalam rentang (inklusif)
10. Klik icon Filter, buka date range picker Last Updated, pilih tanggal awal dan tanggal akhir `Fixture.settingsGroups.lastUpdatedHari`, klik [Apply]
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi setiap baris yang tampil memiliki Last Updated pada hari itu saja

### TC-FA-GRP-691: Kombinasi Status + Last Updated (AND)

13. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
14. Klik icon Filter, isi Status `Fixture.settingsGroups.statusA` dan Last Updated `Fixture.settingsGroups.lastUpdatedAwal` sampai `Fixture.settingsGroups.lastUpdatedAkhir`, klik [Apply]
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusA` dan Last Updated dalam rentang (kedua kriteria terpenuhi)

### TC-FA-GRP-692: [Clear Field] mengosongkan seluruh field

17. Klik icon Filter, isi Status dan Last Updated, klik [Apply]
18. Klik icon Filter, klik [Clear Field]
19. Verifikasi field Status dan Last Updated kembali kosong dengan placeholder
20. Klik [Apply]
21. Verifikasi tabel kembali menampilkan seluruh data (jumlah baris sama dengan jumlah baris yang dicatat sebelum Filter dipasang)

### TC-FA-GRP-693: Search lalu Filter (irisan)

22. Ketik Search `Fixture.settingsGroups.searchKeywordIrisan`, tekan Enter
23. Klik icon Filter, isi seluruh field Filter Panel dengan nilai `Fixture.settingsGroups.irisanSemuaField` yang beririsan dengan baris sasaran, klik [Apply]
24. Verifikasi sedikitnya satu baris tampil
25. Verifikasi setiap baris yang tampil memenuhi Search dan Filter (irisan)
26. Verifikasi keyword `Fixture.settingsGroups.searchKeywordIrisan` tetap terpasang di kotak Search

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; [Clear Field] dan [Apply] mengosongkan Filter antar-TC (S-09). Search TC-693 memakai idiom "Ketik Search, tekan Enter" (8b butir 9).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-690: "tanggal awal = tanggal akhir menampilkan baris pada hari itu saja" memerlukan baris dengan Last Updated pada hari yang berbeda; Last Updated aset Warehouse A bergantung data seed.
  - TC-693: "isi semua field filter yang tersedia dengan nilai yang beririsan" tidak merinci nilai per field; sejumlah field (TAG, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry) tidak punya data yang dijamin di Warehouse A. Nilai dibaca dari fixture yang disediakan tim FE/BE.
  - TC-693 b: keyword tetap terpasang tidak memberi asersi tabel; diasersi lewat isi kotak Search.
