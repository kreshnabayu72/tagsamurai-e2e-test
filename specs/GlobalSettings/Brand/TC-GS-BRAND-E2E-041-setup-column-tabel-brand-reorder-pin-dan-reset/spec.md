---
id: TC-GS-BRAND-E2E-041-setup-column-tabel-brand-reorder-pin-dan-reset
title: "Setup Column Tabel Brand: Reorder, Pin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-158
  - TC-GS-BRAND-159
  - TC-GS-BRAND-160
coverage:
  web: automated
---

# Setup Column Tabel Brand: Reorder, Pin, dan Reset to Default

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API daftar Brand di-mock, tanpa backend nyata).
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (endpoint dan respons yang dipaksa): endpoint daftar Brand mengembalikan 12 brand Pre-setup Client A beserta Used By (Items) dan Last Updated.
- Lebar konten tabel Brand melebihi lebar viewport 1024px (overflow horizontal), karena TC-GS-BRAND-159 hanya bermakna bila scroll horizontal teramati. Kebutuhan lingkungan uji: kontainer tabel dilebarkan atau data mock memaksa overflow; asersi tidak diubah.
- Preferensi kolom tabel (urutan, visibilitas, pin) disimpan di `localStorage` browser dengan key unik per tabel (PRD brand.md §4.2h; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Brand dikembalikan ke default (urutan Brand Name, Used By (Items), Last Updated, semua tampil, tanpa pin) lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Brand; viewport dikembalikan ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Brand; drag and drop elemen; mengatur viewport 1024px; scroll horizontal tabel; membaca dan menghapus key `localStorage` browser.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-158: Modal Setup Column: drag reorder lalu Save

2. Buka Overlay Column Visibility, lalu klik `Setup Column...`
3. Drag `Last Updated` ke posisi pertama
4. Drag `Used By (Items)` ke posisi kedua
5. Verifikasi preview Modal Setup Column berurutan: Last Updated, Used By (Items), Brand Name
6. Klik `[Save]`
7. Verifikasi kolom tabel berurutan: Last Updated, Used By (Items), Brand Name
8. Muat ulang halaman
9. Verifikasi urutan kolom Last Updated, Used By (Items), Brand Name bertahan setelah muat ulang

### TC-GS-BRAND-159: Modal Setup Column: pin kolom lalu scroll horizontal

10. Atur viewport 1024px
11. Buka Overlay Column Visibility, lalu klik `Setup Column...`
12. Pin `Brand Name`
13. Klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom Brand Name tetap di tempat saat scroll
16. Muat ulang halaman
17. Verifikasi pin kolom Brand Name bertahan setelah muat ulang
18. Kembalikan viewport ke ukuran awal

### TC-GS-BRAND-160: Reset to Default mengembalikan konfigurasi default

19. Buka Overlay Column Visibility, lalu klik `Setup Column...`
20. Ubah urutan kolom dengan drag `Used By (Items)` ke posisi terakhir
21. Uncheck `Used By (Items)`
22. Klik `[Save]`
23. Buka kembali Modal Setup Column
24. Klik `[Reset to Default]`
25. Klik `[Save]`
26. Verifikasi kolom kembali berurutan Brand Name, Used By (Items), Last Updated dan semuanya tampil

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec mengikuti TC sumber (158, 159, 160); TC-GS-BRAND-160 di akhir karena reset mengembalikan konfigurasi yang diubah dua TC sebelumnya (sekaligus menjadi pemulihan state).
- Langkah penghubung: langkah 18 (mengembalikan viewport ke ukuran awal setelah TC-GS-BRAND-159, hook `after` sebagai cadangan).
- Pembagian TC Setup Column dengan screening, hide, dan tutup modal ada di spec `TC-GS-BRAND-E2E-040-setup-column-tabel-brand-screening-hide-dan-tutup`.
