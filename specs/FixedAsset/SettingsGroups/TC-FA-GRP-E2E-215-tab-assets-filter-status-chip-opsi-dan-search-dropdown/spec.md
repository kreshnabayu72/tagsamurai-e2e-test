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

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Klik icon Filter
3. Buka dropdown Status
4. Ketik `Fixture.settingsGroups.statusSearchKecil` di kotak search dropdown
5. Verifikasi sedikitnya satu opsi tampil
6. Verifikasi setiap opsi yang tampil mengandung substring `Fixture.settingsGroups.statusSearchKecil` (case-insensitive)
7. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.statusTanpaMatch`
8. Verifikasi daftar opsi kosong dengan teks "No results found"
9. Verifikasi tidak ada ilustrasi pada daftar opsi kosong

### TC-FA-GRP-688: Chip opsi dihapus via (X)

10. Hapus isi kotak search dropdown, tutup dropdown Status, klik [Clear Field] (langkah penghubung)
11. Buka dropdown Status, centang opsi `Fixture.settingsGroups.statusA` lalu opsi `Fixture.settingsGroups.statusB`
12. Verifikasi chip `Fixture.settingsGroups.statusA` dan chip `Fixture.settingsGroups.statusB` tampil di dalam field dan chip `Fixture.settingsGroups.statusB` tidak menggantikan chip `Fixture.settingsGroups.statusA`
13. Tutup dropdown
14. Klik (X) pada chip `Fixture.settingsGroups.statusA`
15. Verifikasi chip `Fixture.settingsGroups.statusA` hilang
16. Buka dropdown Status
17. Verifikasi checkbox `Fixture.settingsGroups.statusA` ter-uncheck
18. Verifikasi chip `Fixture.settingsGroups.statusB` tetap ada
19. Tutup dropdown, klik [Apply]
20. Verifikasi sedikitnya satu baris tampil
21. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`

### TC-FA-GRP-689: Chip opsi dihapus via uncheck di dropdown

22. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
23. Klik icon Filter, buka dropdown Status, centang opsi `Fixture.settingsGroups.statusA` lalu opsi `Fixture.settingsGroups.statusB`
24. Buka lagi dropdown Status dan uncheck opsi `Fixture.settingsGroups.statusA` dari dalam dropdown
25. Verifikasi chip `Fixture.settingsGroups.statusA` hilang dari field
26. Verifikasi chip `Fixture.settingsGroups.statusB` tetap ada
27. Klik [Apply]
28. Verifikasi sedikitnya satu baris tampil
29. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusB`

## Notes

- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; langkah yang menghapus isi search dropdown, menutup dropdown, dan menekan [Clear Field] atau [Apply] mengosongkan Filter antar-TC (S-09); pembukaan dropdown pada TC-688 sesudah klik (X) dipakai untuk mengamati checkbox.
- Temuan untuk QA:
  - TC-688/689: nilai opsi Status A dan B tidak disebut konkret; memakai fixture dari data variasi Warehouse A.
  - TC-687: Expected "teks saja, tanpa ilustrasi" ditulis sebagai dua Verifikasi (teks tampil, ilustrasi tidak ada; anchor positif teks "No results found").
