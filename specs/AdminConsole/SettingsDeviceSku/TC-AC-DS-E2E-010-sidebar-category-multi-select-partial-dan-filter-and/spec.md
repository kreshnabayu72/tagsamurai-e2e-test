---
id: TC-AC-DS-E2E-010-sidebar-category-multi-select-partial-dan-filter-and
title: "Sidebar Category: Multi-select, Parent Partial dan Full Check, serta Gabungan dengan Filter Hardware Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-39
  - TC-AC-DS-40
  - TC-AC-DS-575
coverage:
  web: automated
---

# Sidebar Category: Multi-select, Parent Partial dan Full Check, serta Gabungan dengan Filter Hardware Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25, SKU inti #29 (`HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`, `SFR-VEL-4P`) dan seed #30. Dirujuk lewat `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`, disediakan tim FE, belum ada).
- Data hierarki mendalam Pre-setup #42 (data khusus TC-39 dan TC-575): Subcategory `UHF Handheld Gudang` (tingkat ke-4) dan `UHF Handheld Lapangan` (tingkat ke-4, tanpa Device Name dan tanpa SKU) di bawah `UHF Handheld`; Device Name `Pemindai Gudang` (Category `UHF Handheld Gudang`); SKU `HHR-GDG-01` (Device Name `Pemindai Gudang`, Brand `Arcturus`, Model/Type `PG-1`, Range Type `Long Range`, stok 0, 1 foto); SKU `HHR-PRT-01` (Device Name `Pemindai Ujung` pada Category `Handheld Reader`, Brand `Kinetia`, Model/Type `PU-1`, Range Type `Short Range`, stok 0, 1 foto). Disiapkan lewat fixture BE pada langkah 11 dan dihapus oleh hook `after` lewat fixture BE yang disediakan tim BE/FE; seeding idempotent (dilewati bila sudah ada) dan cleanup hanya menghapus yang dibuat spec ini.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini mengubah data Category dan SKU bersama (hierarki #42) sehingga pemulihannya dijamin hook `after`.

## Test Steps

### TC-AC-DS-40: Sidebar Category digabung dengan filter Hardware Type secara AND

1. Klik tombol Expand/Collapse All pada Sidebar Category
2. Klik node `Handheld Reader` pada Sidebar Category
3. Klik ikon Filter
4. Pilih Hardware Type `Handheld Reader` pada Filter Panel lalu klik `[Apply]`
5. Verifikasi List memuat SKU Handheld Reader (`HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`)
6. Klik ikon Filter
7. Pilih Hardware Type `Smart Fixed Reader` saja dengan menghapus `Handheld Reader`, lalu klik `[Apply]`
8. Verifikasi List kosong dengan "No results found" karena irisan AND antara Sidebar `Handheld Reader` dan Hardware Type `Smart Fixed Reader`
9. Bersihkan Filter Hardware Type lewat Filter Panel
10. Klik node `Handheld Reader` untuk membatalkan pilihan

### Persiapan data hierarki mendalam

11. Siapkan data hierarki mendalam Pre-setup #42 lewat fixture BE hingga Subcategory, Device Name, dan SKU tersimpan
12. Muat ulang halaman `Settings > Device > Device SKU`
13. Klik tombol Expand/Collapse All pada Sidebar Category

### TC-AC-DS-39: Multi-select dan parent partial-check

14. Centang node `UHF Handheld Gudang` pada Sidebar Category
15. Verifikasi List hanya memuat SKU `HHR-GDG-01` (berkategori `UHF Handheld Gudang`)
16. Verifikasi SKU `HHR-ARC-100` dan `HHR-ARC-200` (Category `UHF Handheld`) serta `HHR-PRT-01` (Category `Handheld Reader`) tidak tampil pada List
17. Centang node `Portal Reader` pada Sidebar Category
18. Verifikasi List memuat `HHR-GDG-01` dan `SFR-VEL-4P` (berkategori `Portal Reader`)
19. Hilangkan centang node `Portal Reader` dan `UHF Handheld Gudang`

### TC-AC-DS-575: Parent tercentang penuh karena seluruh descendant dipilih satu per satu

20. Centang node `UHF Handheld Gudang` pada Sidebar Category
21. Centang node `UHF Handheld` pada Sidebar Category
22. Verifikasi List memuat `HHR-ARC-100`, `HHR-ARC-200`, dan `HHR-GDG-01`
23. Verifikasi `HHR-PRT-01` dan `HHR-BIG-01` tidak tampil pada List
24. Centang node `Barcode Handheld` dan `Perangkat Pemindai Kode Batang Industri` pada Sidebar Category
25. Verifikasi node `Handheld Reader` berstatus tercentang penuh
26. Verifikasi List memuat `HHR-PRT-01`, `HHR-ARC-100`, `HHR-ARC-200`, `HHR-GDG-01`, dan `HHR-BIG-01`
27. Hilangkan seluruh centang node pada Sidebar Category

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-40, persiapan data hierarki #42, TC-39, TC-575. TC-40 diletakkan pertama karena tidak membutuhkan data #42 dan hasilnya tidak bergantung pada SKU tambahan (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 13 (membuka semua node agar pohon terlihat; TC-43 menyatakan klik Expand/Collapse All pertama membuka semua node), 2 sampai 4 dan 6 sampai 7 (memilih node dan Filter yang hasilnya diasersi pada langkah 5 dan 8), 9 dan 10 (membersihkan Filter dan pilihan node, S-09), 11 dan 12 (seeding dan memuat ulang), 14, 17, 20, 21, 24 (mencentang node yang hasilnya diasersi), 19 dan 27 (membersihkan centang, S-09).
- Langkah 16 dan 23 (absence) didahului langkah 15 dan 22 (baris lain tampil sebagai anchor positif pada List yang sama).
- Langkah 4 dan 7 mengikuti TC (pilih Hardware Type lalu `[Apply]`); label tombol Filter Panel `[Apply]` mengikuti TC.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25, #29, dan #30 sesuai pengecualian S-12 A-11 (`suite.md`). Data hierarki mendalam Pre-setup #42 (Subcategory `UHF Handheld Gudang` dan `UHF Handheld Lapangan`, Device Name `Pemindai Gudang`, SKU `HHR-GDG-01` dan `HHR-PRT-01`) tidak tercantum di A-11; seeding #42 memakai nama literal (idempotent, serial, cleanup hanya yang dibuat spec) mengikuti TC dan butuh keputusan pengecualian.
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 dan hierarki #42 di environment belum diverifikasi.
  - TC-39 langkah 2 dan TC-575 langkah 2 sampai 3 menyebut status parent `partial` pada langkah, tetapi Expected hanya mengasersi isi List; spec tidak mengasersi status partial itu. Status `Handheld Reader` tercentang penuh (TC-575 Expected c) diasersi pada langkah 25, sebelum isi List pada langkah 26.
  - TC-40 tidak menyebut cara membersihkan Filter Hardware Type sesudah uji; langkah 9 ditulis sebagai langkah penghubung.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
