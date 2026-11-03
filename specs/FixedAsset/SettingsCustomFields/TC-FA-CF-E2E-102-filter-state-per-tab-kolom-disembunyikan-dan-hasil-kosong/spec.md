---
id: TC-FA-CF-E2E-102-filter-state-per-tab-kolom-disembunyikan-dan-hasil-kosong
title: "Filter: State Per Tab, Kolom Disembunyikan, dan Hasil Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-389
  - TC-FA-CF-390
  - TC-FA-CF-393
coverage:
  web: automated
---

# Filter: State Per Tab, Kolom Disembunyikan, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama dan Data Type seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral` dan `Fixture.faCustomFields.alphaPurchasing`):
  - Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12): `Asset Serial Tag` (Text, Required Yes), `Storage Capacity` (Numeric), `Equipment Class` (Dropdown), `Operating Voltage` (Text, Required Yes), `Total Cost` (Formula), `Depreciated Ratio` (Percentage), `Compliance File` (Document), `Legacy Tag` (Text).
  - Tab Purchasing Company Alpha (Pre-setup #13): `Vendor Code` (Text), `Warranty Months` (Numeric), `Rated Precision` (Numeric), `Long Option Field` (Dropdown); opsi Data Type tab ini: `Dropdown`, `Numeric`, `Text`.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan nilai field filter, opsi dropdown, dan baris hasil tabel; membuka Overlay Column Visibility dari header kolom Actions `(⋯)`.
- State global: visibilitas kolom Data Type disembunyikan pada langkah 4 dan ditampilkan kembali pada langkah 8. Hook `after` spec ini menghapus preferensi visibilitas kolom di browser sebagai cadangan (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-CF-389: Menyembunyikan kolom tidak menghilangkan field filternya dan tidak membatalkan filter ter-Apply

1. Klik ikon Filter
2. Pilih Data Type `Text`, klik `[Apply]`
3. Klik ikon Filter untuk menutup Filter Panel
4. Klik header kolom Actions `(⋯)`, hapus centang kolom `Data Type` pada Overlay Column Visibility, lalu tutup overlay
5. Klik ikon Filter untuk membuka Filter Panel
6. Verifikasi field filter `Data Type` tetap ada dengan nilai `Text`
7. Verifikasi hasil filter tetap berlaku (tabel hanya menampilkan baris `Asset Serial Tag`, `Legacy Tag`, dan `Operating Voltage`)
8. Klik header kolom Actions `(⋯)`, centang kembali kolom `Data Type` pada Overlay Column Visibility, lalu tutup overlay

### TC-FA-CF-390: Filter tiap tab terpisah dan opsi dihitung dari tab aktif

9. Klik `[Clear Field]`, pilih Data Type `Text`, klik `[Apply]`
10. Klik ikon Filter untuk menutup Filter Panel
11. Klik tab `Purchasing`
12. Klik ikon Filter untuk membuka Filter Panel
13. Verifikasi tab Purchasing tidak menerima filter tab General (field filter `Data Type` kosong)
14. Verifikasi tabel tab Purchasing menampilkan baris `Vendor Code`, `Warranty Months`, `Rated Precision`, dan `Long Option Field`
15. Buka dropdown Data Type
16. Verifikasi opsi Data Type hanya `Dropdown`, `Numeric`, dan `Text`
17. Tutup dropdown Data Type, lalu klik ikon Filter untuk menutup Filter Panel
18. Klik tab `General`
19. Klik ikon Filter untuk membuka Filter Panel
20. Verifikasi filter Data Type `Text` masih terpasang pada Filter Panel
21. Verifikasi tabel tab General hanya menampilkan baris `Asset Serial Tag`, `Legacy Tag`, dan `Operating Voltage`

### TC-FA-CF-393: Kombinasi filter tanpa hasil menampilkan empty state dan melepas satu filter memulihkan data

22. Klik `[Clear Field]`, pilih Data Type `Formula` dan Required `Yes`, klik `[Apply]`
23. Verifikasi ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.` tampil
24. Hapus filter Required (klik `✕` pada chip `Yes`), klik `[Apply]`
25. Verifikasi baris `Total Cost` tampil kembali

## Notes

- Spec memuat 25 langkah, di bawah ambang sekitar 35 langkah. Satu topik (state Filter Panel tabel utama), satu akun, dua dataset Company Alpha (tab General dan Purchasing) tanpa mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 5, 10, 12, 17, 18, dan 19 (menutup atau membuka Filter Panel dan pindah tab, karena ikon Filter membuka dan menutup panel); langkah 8 (menampilkan kembali kolom Data Type); langkah 9 dan 22 (`[Clear Field]` sebagai langkah "Bersihkan"; langkah 9 juga memastikan filter `Text` terpasang sesuai langkah TC-FA-CF-390 "Filter Data Type `Text` pada tab General").
- Asersi absence langkah 16 ("hanya") didahului langkah 15 (dropdown terbuka dengan opsi tab Purchasing tampil) sebagai anchor positif (bagian 8b butir 2); empty state langkah 23 adalah hasil Filter dan menjadi anchor positif bagi langkah 25.
- Temuan untuk QA:
  - TC-FA-CF-393 langkah "Hapus filter Required" (langkah 24 spec) tidak menyebut kontrolnya; spec memakai `✕` pada chip `Yes`.
  - TC-FA-CF-390 Expected a tidak menyebut cara memeriksa bahwa tab Purchasing "tidak menerima filter"; langkah 13 dan 14 membaca field filter dan baris tabel (keempat baris Pre-setup #13).
  - TC-FA-CF-390 Expected b menyebut "filter `Text` masih terpasang" tanpa nama baris; langkah 21 memakai nama baris Data Type `Text` dari TC-FA-CF-376 (`Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`).
  - TC-FA-CF-389 menutup dan membuka Filter Panel (langkah 3 dan 5) karena TC tidak menyatakan apakah panel tetap terbuka setelah `[Apply]`; spec mengasumsikan panel tetap terbuka setelah `[Apply]`.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
