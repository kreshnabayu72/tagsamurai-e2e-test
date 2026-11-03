---
id: TC-FA-FAAM-E2E-132-setup-column-independen-filter-bertahan-dan-viewport
title: "Setup Column: Independen Antar Tabel, Filter Bertahan, dan Sel Satu Baris Saat Viewport Dipersempit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-430
  - TC-FA-FAAM-431
  - TC-FA-FAAM-669
coverage:
  web: automated
---

# Setup Column: Independen Antar Tabel, Filter Bertahan, dan Sel Satu Baris Saat Viewport Dipersempit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10) dan `Ergonomic Chair` (Pre-setup #11, UoM `Pcs`). Modal Changelog dibuka dari Table Tools (Pre-setup #28 untuk isi contoh).
- Kemampuan teknis: mengubah lebar viewport browser, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-669: Sel Code, Category, TAG Type, Total Asset, dan Last Updated tetap satu baris saat viewport dipersempit
1. Persempit lebar viewport sampai tabel dapat di-scroll horizontal
2. Verifikasi sel kolom Code baris `Dell Latitude` dan `Ergonomic Chair` satu baris tanpa wrap
3. Verifikasi sel kolom Category berupa badge satu baris tanpa wrap
4. Verifikasi sel kolom TAG Type berupa icon satu baris tanpa wrap
5. Verifikasi sel kolom Total Asset berupa angka satu baris tanpa wrap
6. Verifikasi sel kolom Last Updated berupa tanggal dan jam satu baris tanpa wrap
7. Verifikasi tinggi baris tabel konsisten antar baris
8. Pulihkan lebar viewport ke ukuran semula
### TC-FA-FAAM-431: Kolom di-hide tidak menghilangkan filter dan filter ter-Apply tetap
9. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
10. Klik header kolom Actions (⋯) untuk membuka Column Visibility
11. Uncheck kolom `UoM`
12. Tutup Column Visibility
13. Klik icon Filter
14. Verifikasi field UoM tetap ada di Filter Panel
15. Verifikasi filter ter-Apply tetap berlaku: field UoM berisi `Unit`
16. Verifikasi baris `Dell Latitude` (UoM `Unit`) tampil di tabel
17. Verifikasi baris `Ergonomic Chair` (UoM `Pcs`) tidak tampil
18. Klik `[Clear Field]`, lalu klik `[Apply]`
19. Klik header kolom Actions (⋯), lalu check kolom `UoM`
### TC-FA-FAAM-430: Konfigurasi kolom tersimpan per tabel dan independen antar tabel
20. Klik header kolom Actions (⋯), lalu `Setup Column...`
21. Sembunyikan kolom `Code`, lalu klik `[Save]`
22. Verifikasi kolom `Code` tidak tampil di tabel utama
23. Klik icon Changelog
24. Verifikasi Modal Changelog menampilkan seluruh kolomnya
25. Klik `[✕]` pada Modal Changelog
26. Verifikasi kolom `Code` tetap tersembunyi di tabel utama

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan konfigurasi kolom dan pembersihan Search, Filter, dan seleksi di antara blok (S-09).
- Urutan di spec: TC-FA-FAAM-669 (viewport) dan TC-FA-FAAM-431 lebih dulu, TC-FA-FAAM-430 terakhir karena menyimpan konfigurasi kolom dengan `[Save]` (S-10). Hook `after` menghapus preferensi kolom di browser.
- Langkah penghubung (aksi tanpa `Verifikasi`): memulihkan viewport, membuka dan menutup Column Visibility, `[Clear Field]` lalu `[Apply]`, dan menutup Modal Changelog.
- Expected b TC-FA-FAAM-430 ("cache tabel utama tidak memengaruhi tabel lain") adalah kesimpulan Expected a (Modal Changelog tetap menampilkan seluruh kolomnya); keduanya diasersi lewat satu Verifikasi (S-03) ditambah Verifikasi kolom `Code` tetap tersembunyi di tabel utama sebagai bukti konfigurasi tersimpan.
- Asersi absence baris `Ergonomic Chair` pada TC-FA-FAAM-431 beranchor Verifikasi baris `Dell Latitude` tampil pada filter yang sama (bagian 8b butir 2).
- Temuan untuk QA: TC-FA-FAAM-430 tidak menyebut daftar kolom Modal Changelog sehingga asersi "seluruh kolomnya" membandingkan dengan kolom bawaan modal; TC-FA-FAAM-669 tidak menyebut lebar viewport.
