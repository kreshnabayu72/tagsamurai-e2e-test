---
id: TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated
title: "Filter: Kelas TAG Type, Default Addon, Default Label, Total Asset, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-363
  - TC-FA-FAAM-364
  - TC-FA-FAAM-365
  - TC-FA-FAAM-366
  - TC-FA-FAAM-367
coverage:
  web: automated
---

# Filter: Kelas TAG Type, Default Addon, Default Label, Total Asset, dan Last Updated

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Total Asset 42), `MacBook Pro` (Pre-setup #12, Total Asset 15), `Ergonomic Chair` (Pre-setup #11, Total Asset 120), `Service Vehicle` (Pre-setup #14), `Warehouse Pallet` (Pre-setup #13, Default Label `Fragile`). Opsi dropdown TAG Type dirujuk lewat `Fixture.faSettingsAssetName.baselineList.tagTypeOptions` (fixture baru belum ada).
- Date Format General Settings dibaca dari pengaturan client sebelum langkah.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-363: Filter kelas TAG Type
1. Klik icon Filter
2. Buka dropdown TAG Type
3. Verifikasi opsi berasal dari tipe TAG yang muncul di tabel (`Fixture.faSettingsAssetName.baselineList.tagTypeOptions`)
4. Pilih `RFID`
5. Klik `[Apply]`
6. Verifikasi tabel menampilkan baris yang memiliki tipe `RFID` (`Dell Latitude`, `Service Vehicle`)
### TC-FA-FAAM-364: Filter kelas Default Addon
7. Klik icon Filter, lalu klik `[Clear Field]`
8. Buka dropdown Default Addon
9. Verifikasi opsi berurutan mengikuti enum tetap `Audit`, `Maintenance`, `Tracking`, `Maps` (hanya yang muncul di tabel)
10. Pilih `Tracking`
11. Klik `[Apply]`
12. Verifikasi tabel menampilkan baris ber-addon `Tracking` (`Service Vehicle`, `Ergonomic Chair`)
### TC-FA-FAAM-365: Filter kelas Default Label
13. Klik icon Filter, lalu klik `[Clear Field]`
14. Buka dropdown Default Label
15. Verifikasi opsi label tampil berbadge warna aslinya
16. Pilih `Fragile`
17. Klik `[Apply]`
18. Verifikasi tabel menampilkan baris ber-label `Fragile` (`Warehouse Pallet`)
### TC-FA-FAAM-366: Filter kelas Total Asset (range Min-Max)
19. Klik icon Filter, lalu klik `[Clear Field]`
20. Verifikasi placeholder input `Min` dan `Max`
21. Isi `Min` 10 dan `Max` 50, lalu klik `[Apply]`
22. Verifikasi baris `MacBook Pro` (15) dan `Dell Latitude` (42) tampil di tabel
23. Verifikasi seluruh baris yang tampil ber-Total Asset 15 atau 42 (Min dan Max inklusif)
24. Klik icon Filter, kosongkan `Max`, ganti `Min` menjadi 100, lalu klik `[Apply]`
25. Verifikasi tabel menampilkan `Ergonomic Chair` (120)
### TC-FA-FAAM-367: Filter kelas Last Updated (date range picker)
26. Catat tanggal Last Updated baris `Dell Latitude` dari tabel
27. Klik icon Filter, lalu klik `[Clear Field]`
28. Buka field Last Updated (placeholder `Select date`)
29. Pilih rentang yang hanya mencakup satu hari tanggal pembaruan `Dell Latitude` (Start = End)
30. Klik `[Apply]`
31. Verifikasi tabel menampilkan baris yang diperbarui pada hari itu (`Dell Latitude`)
32. Klik icon Filter
33. Verifikasi tanggal pada input Last Updated mengikuti Date Format General Settings
34. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): klik `[Clear Field]` di awal tiap blok (S-09), pencatatan tanggal Last Updated sebelum membuka Filter pada TC-FA-FAAM-367, dan `[Clear Field]` lalu `[Apply]` terakhir.
- Asersi "seluruh baris yang tampil ber-Total Asset 15 atau 42" pada TC-FA-FAAM-366 didahului Verifikasi dua baris pembanding tampil (bagian 8b butir 2).
- Temuan untuk QA: nama Asset Name keenam (Total Asset 3) tidak tertulis di Pre-setup; TC-FA-FAAM-366 menyatakan rentang Min 10 Max 50 hanya memuat Total Asset 15 dan 42, yang konsisten dengan nilai 0, 3, 8, 15, 42, 120 pada TC-FA-FAAM-394.
