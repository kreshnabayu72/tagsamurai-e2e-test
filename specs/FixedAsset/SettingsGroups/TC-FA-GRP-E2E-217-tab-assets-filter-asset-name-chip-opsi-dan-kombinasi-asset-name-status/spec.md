---
id: TC-FA-GRP-E2E-217-tab-assets-filter-asset-name-chip-opsi-dan-kombinasi-asset-name-status
title: "Tab Assets Filter Asset Name: Chip Opsi dan Kombinasi Asset Name + Status (AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1008
  - TC-FA-GRP-1009
  - TC-FA-GRP-1010
coverage:
  web: automated
---

# Tab Assets Filter Asset Name: Chip Opsi dan Kombinasi Asset Name + Status (AND)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Aset acuan di Warehouse A (hanya dibaca): `Laptop Dell - 1`, `Laptop Dell - 2`, `Laptop Dell - 10`, `Monitor LG - 3`. Fixture.settingsGroups.statusLaptopDell adalah satu Status yang dimiliki sebagian unit `Laptop Dell` (unit `Laptop Dell` lain berstatus berbeda, sehingga ada sedikitnya dua nilai Status distinct pada unit `Laptop Dell`).

## Test Steps

### TC-FA-GRP-1008: Chip opsi Asset Name dihapus via (X)

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Klik icon Filter
3. Buka dropdown Asset Name, centang `Laptop Dell` lalu `Monitor LG`
4. Verifikasi chip `Laptop Dell` dan chip `Monitor LG` tampil di dalam field
5. Tutup dropdown
6. Klik (X) pada chip `Laptop Dell`
7. Verifikasi chip `Laptop Dell` hilang
8. Buka dropdown Asset Name
9. Verifikasi checkbox `Laptop Dell` ter-uncheck
10. Verifikasi chip `Monitor LG` tetap ada
11. Tutup dropdown, klik [Apply]
12. Verifikasi `Monitor LG - 3` tampil
13. Verifikasi setiap baris yang tampil bernama aset `Monitor LG`

### TC-FA-GRP-1009: Chip opsi Asset Name dihapus via uncheck

14. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
15. Klik icon Filter, buka dropdown Asset Name, centang `Laptop Dell` lalu `Monitor LG`
16. Buka lagi dropdown dan uncheck `Laptop Dell`
17. Verifikasi chip `Laptop Dell` hilang dari field
18. Verifikasi chip `Monitor LG` tetap ada
19. Klik [Apply]
20. Verifikasi `Monitor LG - 3` tampil
21. Verifikasi setiap baris yang tampil bernama aset `Monitor LG`

### TC-FA-GRP-1010: Kombinasi Asset Name + Status (AND)

22. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
23. Klik icon Filter, pilih `Laptop Dell` pada Asset Name dan pilih `Fixture.settingsGroups.statusLaptopDell` pada Status, klik [Apply]
24. Verifikasi sedikitnya satu baris tampil
25. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell` dan berstatus `Fixture.settingsGroups.statusLaptopDell`
26. Verifikasi unit `Laptop Dell` berstatus lain tidak tampil
27. Verifikasi aset bernama lain (`Monitor LG - 3`) tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; menutup dropdown, [Clear Field], dan [Apply] mengosongkan Filter antar-TC (S-09); pembukaan dropdown sesudah klik (X) dipakai untuk mengamati checkbox.
- Temuan untuk QA:
  - TC-1008: Expected b ("checkbox ikut ter-uncheck") tidak punya langkah observasi eksplisit; spec membuka dropdown untuk mengamatinya.
  - TC-1010: Status "yang dimiliki sebagian unit `Laptop Dell`" tidak disebut konkret; memakai fixture dari data variasi Warehouse A.
