---
id: TC-GS-BRAND-E2E-040-setup-column-tabel-brand-screening-hide-dan-tutup
title: "Setup Column Tabel Brand: Screening, Hide, dan Tutup Modal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-154
  - TC-GS-BRAND-155
  - TC-GS-BRAND-156
  - TC-GS-BRAND-157
  - TC-GS-BRAND-161
  - TC-GS-BRAND-162
coverage:
  web: automated
---

# Setup Column Tabel Brand: Screening, Hide, dan Tutup Modal

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API daftar Brand dan daftar Changelog di-mock, tanpa backend nyata).
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - Endpoint daftar Brand mengembalikan 12 brand Pre-setup Client A (Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp) beserta Used By (Items) dan Last Updated.
  - Endpoint daftar Changelog Brand mengembalikan beberapa baris dengan seluruh 7 kolom default Modal Changelog.
- Preferensi kolom tabel (visibilitas, urutan, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD brand.md §4.2h; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Brand dikembalikan ke default (Brand Name, Used By (Items), Last Updated, semuanya tampil, tanpa pin) lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Brand.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Brand dan daftar Changelog; mengarahkan kursor ke checkbox disabled untuk membaca tooltip; membaca dan menghapus key `localStorage` browser.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-154: Screening Overlay Column Visibility tabel Brand

2. Klik header Column Visibility (⋯)
3. Verifikasi overlay berisi `Brand Name`, `Used By (Items)`, `Last Updated` tercentang (Hideable, enabled) dengan drag handle
4. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-BRAND-156: Screening Modal Setup Column tabel Brand

5. Klik item `Setup Column...` pada overlay yang terbuka
6. Verifikasi **Header**: Title `Setup Column`, `[✕]`, subtitle `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
7. Verifikasi **Body**: search `Search column name...`; daftar `Brand Name`, `Used By (Items)`, `Last Updated` dengan drag handle, checkbox, icon Pin
8. Verifikasi **Footer**: `[Reset to Default]` (text, primary) dan `[Save]`; tidak ada `[Cancel]`
9. Klik `[✕]` untuk menutup modal tanpa perubahan

### TC-GS-BRAND-155: Overlay Column Visibility: uncheck kolom langsung diterapkan

10. Klik header Column Visibility (⋯)
11. Uncheck `Last Updated`
12. Verifikasi kolom Last Updated langsung hilang tanpa tombol Save
13. Muat ulang halaman
14. Verifikasi kolom Last Updated tetap hilang
15. Buka Overlay Column Visibility, lalu centang kembali `Last Updated`

### TC-GS-BRAND-157: Modal Setup Column: hide/unhide kelas kolom Hideable lalu Save

16. Buka Overlay Column Visibility, lalu klik `Setup Column...`
17. Uncheck `Brand Name`
18. Verifikasi preview menghilangkan kolom Brand Name
19. Uncheck `Used By (Items)`
20. Verifikasi preview menghilangkan kolom Used By (Items)
21. Arahkan kursor ke checkbox `Last Updated` (kolom terakhir yang tersisa)
22. Verifikasi checkbox `Last Updated` disabled dengan tooltip `At least one column must remain visible.`
23. Centang kembali `Brand Name` saja (`Used By (Items)` tetap hidden)
24. Klik `[Save]`
25. Muat ulang halaman
26. Verifikasi konfigurasi bertahan setelah muat ulang: hanya kolom Brand Name dan Last Updated yang tampil, `Used By (Items)` tetap hidden
27. Buka Overlay Column Visibility, lalu centang kembali `Used By (Items)`

### TC-GS-BRAND-161: Tutup Modal Setup Column lewat [✕] membuang perubahan

28. Buka Overlay Column Visibility, lalu klik `Setup Column...`
29. Uncheck `Used By (Items)`
30. Klik `[✕]`
31. Verifikasi tabel tetap menampilkan kolom Used By (Items)

### TC-GS-BRAND-162: Konfigurasi kolom tabel Brand tidak memengaruhi Modal Changelog

32. Buka Overlay Column Visibility, lalu uncheck `Used By (Items)` (hide di tabel Brand)
33. Buka Changelog
34. Verifikasi Modal Changelog tetap menampilkan seluruh 7 kolom default
35. Tutup Modal Changelog
36. Buka Overlay Column Visibility, lalu centang kembali `Used By (Items)`

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: 154, 156, 155, 157, 161, 162. Dua TC screening (154, 156) ditaruh di awal sebelum aksi yang mengubah konfigurasi kolom (prinsip 2 konvensi bagian 3); kasus tutup modal (161) dan efek ke Changelog (162) di akhir.
- Langkah penghubung: langkah 9 (menutup Modal Setup Column setelah screening) dan langkah 15, 27, 36 (mencentang kembali kolom yang di-hide, supaya TC berikutnya mulai dari konfigurasi default). Pembagian TC Setup Column dengan reorder, pin, dan reset ada di spec `TC-GS-BRAND-E2E-041-setup-column-tabel-brand-reorder-pin-dan-reset`.
- TC-GS-BRAND-157: ketiga kolom di-uncheck satu per satu hingga tersisa satu (Last Updated); kolom terakhir tidak bisa di-uncheck (checkbox disabled), sehingga langkah dituliskan sebagai uncheck dua kolom lalu verifikasi checkbox kolom ketiga disabled.
- Kebutuhan pada Prerequisites (mock daftar Brand dan Changelog, pembacaan `localStorage`) dicatat sebagai kebutuhan tim FE.
