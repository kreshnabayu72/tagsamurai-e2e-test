---
id: TC-FA-GRP-E2E-215-tab-assets-filter-status-chip-opsi-dan-search-dropdown
title: "Tab Assets Filter Status: Search Dropdown dan Chip Opsi (Hapus via X dan Uncheck)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-687
  - TC-FA-GRP-688
  - TC-FA-GRP-689
coverage:
  web: automated
---

# Tab Assets Filter Status: Search Dropdown dan Chip Opsi (Hapus via X dan Uncheck)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Opsi Status: Fixture.settingsGroups.statusA dan Fixture.settingsGroups.statusB adalah dua nilai Status distinct yang dimiliki baris Warehouse A; Fixture.settingsGroups.statusSearchKecil adalah potongan huruf kecil nama opsi Status; Fixture.settingsGroups.statusTanpaMatch adalah teks yang tidak ada di opsi mana pun.

## Test Steps

### TC-FA-GRP-687: Search internal dropdown Filter Status

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Klik icon Filter
4. Buka dropdown Status
5. Ketik `Fixture.settingsGroups.statusSearchKecil` di kotak search dropdown
6. Verifikasi sedikitnya satu opsi tampil
7. Verifikasi setiap opsi yang tampil mengandung substring `Fixture.settingsGroups.statusSearchKecil` (case-insensitive)
8. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.statusTanpaMatch`
9. Verifikasi daftar opsi kosong dengan teks "No results found"
10. Verifikasi tidak ada ilustrasi pada daftar opsi kosong

### TC-FA-GRP-688: Chip opsi dihapus via (X)

11. Hapus isi kotak search dropdown, tutup dropdown Status, klik [Clear Field] (langkah penghubung)
12. Buka dropdown Status, centang opsi `Fixture.settingsGroups.statusA` lalu opsi `Fixture.settingsGroups.statusB`
13. Verifikasi chip `Fixture.settingsGroups.statusA` dan chip `Fixture.settingsGroups.statusB` tampil di dalam field dan chip `Fixture.settingsGroups.statusB` tidak menggantikan chip `Fixture.settingsGroups.statusA`
14. Tutup dropdown
15. Klik (X) pada chip `Fixture.settingsGroups.statusA`
16. Verifikasi chip `Fixture.settingsGroups.statusA` hilang
17. Buka dropdown Status
18. Verifikasi checkbox `Fixture.settingsGroups.statusA` ter-uncheck
19. Verifikasi chip `Fixture.settingsGroups.statusB` tetap ada
20. Tutup dropdown, klik [Apply]
21. Verifikasi sedikitnya satu baris tampil
22. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`

### TC-FA-GRP-689: Chip opsi dihapus via uncheck di dropdown

23. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
24. Klik icon Filter, buka dropdown Status, centang opsi `Fixture.settingsGroups.statusA` lalu opsi `Fixture.settingsGroups.statusB`
25. Buka lagi dropdown Status dan uncheck opsi `Fixture.settingsGroups.statusA` dari dalam dropdown
26. Verifikasi chip `Fixture.settingsGroups.statusA` hilang dari field
27. Verifikasi chip `Fixture.settingsGroups.statusB` tetap ada
28. Klik [Apply]
29. Verifikasi sedikitnya satu baris tampil
30. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; langkah yang menghapus isi search dropdown, menutup dropdown, dan menekan [Clear Field] atau [Apply] mengosongkan Filter antar-TC (S-09); pembukaan dropdown pada TC-688 sesudah klik (X) dipakai untuk mengamati checkbox.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-688/689: nilai opsi Status A dan B tidak disebut konkret; memakai fixture dari data variasi Warehouse A.
  - TC-687: Expected "teks saja, tanpa ilustrasi" ditulis sebagai dua Verifikasi (teks tampil, ilustrasi tidak ada; anchor positif teks "No results found").
