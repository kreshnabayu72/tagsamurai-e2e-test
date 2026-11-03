---
id: TC-FA-FAAM-E2E-115-filter-screening-opsi-distinct-dan-kelas-category
title: "Filter: Screening Panel, Opsi DISTINCT Brand UoM Modified By, dan Kelas Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-360
  - TC-FA-FAAM-361
  - TC-FA-FAAM-362
coverage:
  web: automated
---

# Filter: Screening Panel, Opsi DISTINCT Brand UoM Modified By, dan Kelas Category

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Opsi dropdown yang diamati dirujuk lewat `Fixture.faSettingsAssetName.baselineList.brandOptions`, `.categoryOptions`, dan `.modifiedByOptions` (daftar nilai distinct pada data tabel; fixture baru belum ada). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Brand `Dell`, UoM `Unit`, Modified By `Sarah Johnson`), `Warehouse Pallet` (Pre-setup #13, Category `Logistics`).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-360: Screening Filter Panel tabel utama
1. Arahkan kursor ke icon Filter
2. Verifikasi tooltip `Filter` tampil
3. Klik icon Filter
4. Verifikasi icon Filter menjadi gelap saat panel terbuka
5. Verifikasi field berurutan: `Category` `All categories`, `TAG Type` `All TAG types`, `Brand` `All brands`, `Default Addon` `All addons`, `Default Label` `All labels`, `UoM` `All units`, `Total Asset` `Min` / `Max`, `Modified By` `All users`, `Last Updated` `Select date`
6. Verifikasi maksimal 4 field per baris
7. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
8. Verifikasi tidak ada field filter untuk Asset Name, Code, dan Model/Type
### TC-FA-FAAM-361: Filter kelas Brand, UoM, Modified By: opsi DISTINCT dan penyaringan
9. Buka dropdown Brand
10. Verifikasi opsi Brand hanya Brand yang muncul di data tabel saat ini (`Fixture.faSettingsAssetName.baselineList.brandOptions`)
11. Pilih Brand `Dell`
12. Buka dropdown UoM
13. Verifikasi opsi UoM hanya `Pcs`, `Set`, `Unit`
14. Pilih UoM `Unit`
15. Buka dropdown Modified By
16. Verifikasi opsi Modified By hanya user yang pernah memodifikasi (`Fixture.faSettingsAssetName.baselineList.modifiedByOptions`)
17. Pilih Modified By `Sarah Johnson`
18. Klik `[Apply]`
19. Verifikasi sedikitnya satu baris tampil di tabel
20. Verifikasi tabel hanya menampilkan baris yang memenuhi ketiga kriteria (AND antar-field): baris `Dell Latitude` tampil
21. Verifikasi icon Filter menampilkan badge titik
### TC-FA-FAAM-362: Filter kelas Category
22. Klik icon Filter, lalu klik `[Clear Field]`
23. Buka dropdown Category
24. Verifikasi opsi Category berasal dari Category yang muncul di tabel (`Fixture.faSettingsAssetName.baselineList.categoryOptions`)
25. Pilih Category `IT Equipment` dan `Logistics`
26. Klik `[Apply]`
27. Verifikasi tabel menampilkan baris Category `IT Equipment` (`Dell Latitude`) dan baris Category `Logistics` (`Warehouse Pallet`) sebagai OR dalam satu field
28. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): klik `[Clear Field]` dan `[Apply]` untuk membersihkan filter sebelum dan sesudah blok TC-FA-FAAM-362 (S-09).
- Opsi dropdown diasersi terhadap daftar fixture karena TC menyebut "hanya Brand yang muncul di data tabel" dan "hanya user yang pernah memodifikasi" tanpa menyebut nilainya.
- Temuan untuk QA: TC-FA-FAAM-361 tidak menyebut nilai opsi Brand dan Modified By; daftar nilai distinct perlu ditetapkan di Pre-setup agar asersi dapat dibandingkan.
