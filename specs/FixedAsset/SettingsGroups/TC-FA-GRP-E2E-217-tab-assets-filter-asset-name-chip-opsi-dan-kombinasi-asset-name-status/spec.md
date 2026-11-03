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

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Klik icon Filter
4. Buka dropdown Asset Name, centang `Laptop Dell` lalu `Monitor LG`
5. Verifikasi chip `Laptop Dell` dan chip `Monitor LG` tampil di dalam field
6. Tutup dropdown
7. Klik (X) pada chip `Laptop Dell`
8. Verifikasi chip `Laptop Dell` hilang
9. Buka dropdown Asset Name
10. Verifikasi checkbox `Laptop Dell` ter-uncheck
11. Verifikasi chip `Monitor LG` tetap ada
12. Tutup dropdown, klik [Apply]
13. Verifikasi `Monitor LG - 3` tampil
14. Verifikasi setiap baris yang tampil bernama aset `Monitor LG`

### TC-FA-GRP-1009: Chip opsi Asset Name dihapus via uncheck

15. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
16. Klik icon Filter, buka dropdown Asset Name, centang `Laptop Dell` lalu `Monitor LG`
17. Buka lagi dropdown dan uncheck `Laptop Dell`
18. Verifikasi chip `Laptop Dell` hilang dari field
19. Verifikasi chip `Monitor LG` tetap ada
20. Klik [Apply]
21. Verifikasi `Monitor LG - 3` tampil
22. Verifikasi setiap baris yang tampil bernama aset `Monitor LG`

### TC-FA-GRP-1010: Kombinasi Asset Name + Status (AND)

23. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
24. Klik icon Filter, pilih `Laptop Dell` pada Asset Name dan pilih `Fixture.settingsGroups.statusLaptopDell` pada Status, klik [Apply]
25. Verifikasi sedikitnya satu baris tampil
26. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell` dan berstatus `Fixture.settingsGroups.statusLaptopDell`
27. Verifikasi unit `Laptop Dell` berstatus lain tidak tampil
28. Verifikasi aset bernama lain (`Monitor LG - 3`) tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; menutup dropdown, [Clear Field], dan [Apply] mengosongkan Filter antar-TC (S-09); pembukaan dropdown sesudah klik (X) dipakai untuk mengamati checkbox.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-1008: Expected b ("checkbox ikut ter-uncheck") tidak punya langkah observasi eksplisit; spec membuka dropdown untuk mengamatinya.
  - TC-1010: Status "yang dimiliki sebagian unit `Laptop Dell`" tidak disebut konkret; memakai fixture dari data variasi Warehouse A.
