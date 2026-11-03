---
id: TC-AC-DC-E2E-091-role-matrix-visibilitas-read-only
title: "Role Matrix: Visibilitas Aksi Node dan Kontrol Changelog untuk Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-52
  - TC-AC-DC-283
coverage:
  web: automated
---
# Role Matrix: Visibilitas Aksi Node dan Kontrol Changelog untuk Read Only

## Prerequisites

- Mode: FE+BE.
- Aktor: Read Only (Pre-setup #3); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Read Only (`Rina Wijaya`) | #3 `readOnlyDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_RO_PASSWORD` |

- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca; node `Rugged Scanner` dan `Handheld Reader` hanya di-hover, `Barcode Handheld` hanya dicentang lalu dilepas), #17 (Riwayat Changelog Uji, hanya dibaca; dipakai sebagai precondition TC-AC-DC-283). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Spec ini tidak membuat data; tidak ada seeding dan cleanup data.
- Env var `AC_DC_RO_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-52: Read Only: hanya melihat tree dan Changelog tanpa aksi mutasi

1. Verifikasi tree Category tampil penuh
2. Expand `Hardware` lalu `Handheld Reader`
3. Hover node user-created `Rugged Scanner`
4. Verifikasi `+ Subcategory`, Edit, dan Delete Hidden pada `Rugged Scanner`
5. Hover node hardcoded `Handheld Reader`
6. Verifikasi `+ Subcategory`, Edit, dan Delete Hidden pada `Handheld Reader`
7. Centang kotak `Barcode Handheld`
8. Verifikasi node selectable dapat dicentang untuk filter: kotak `Barcode Handheld` tercentang
9. Hapus centang kotak `Barcode Handheld`
10. Klik ikon Changelog pada header sidebar
11. Verifikasi modal "Changelog: Category" terbuka
12. Tutup modal Changelog

### TC-AC-DC-283: Read Only: kontrol baca modal Changelog tetap tampil dan aktif

13. Klik ikon Changelog pada header Sidebar Category
14. Verifikasi toolbar menampilkan Search, Filter, dan Download dalam keadaan aktif
15. Klik ikon Search
16. Verifikasi Search membuka kolom pencarian
17. Klik `(←)` pada kotak Search
18. Klik ikon Filter
19. Verifikasi Filter membuka Filter Panel
20. Tutup Filter Panel
21. Klik ikon Download
22. Verifikasi Download menampilkan opsi "Download as CSV" dan "Download as XLSX"
23. Tutup overlay Download
24. Verifikasi header kolom Actions menampilkan trigger Column Visibility
25. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-AC-DC-43, 50, 51, dan 56 (role dengan akses penuh atau Create-Update-Delete) ada di spec 018 (`TC-AC-DC-E2E-018-role-matrix-visibilitas-aksi-per-role`).
- Matriks visibilitas ini hanya satu role (Read Only), dua TC; keduanya memakai akun hook `before` tanpa ganti akun.
- Langkah penghubung: langkah 2 (expand tree), 7 dan 9 (mencentang dan melepas centang node selectable sebagai pembuktian "dapat dicentang untuk filter", S-09), 12 dan 25 (menutup modal Changelog), 17 (menutup kolom Search lewat `(←)`, 8b butir 9), 20 dan 23 (menutup Filter Panel dan overlay Download sebelum aksi berikutnya).
- Temuan untuk QA:
  - TC-AC-DC-52 Expected a ("node selectable dapat dicentang untuk filter") tidak menyebut node; dipilih `Barcode Handheld` (leaf Pre-setup #14) dan hanya dicentang lalu dilepas.
  - TC-AC-DC-283 memakai Pre-setup #17 sebagai precondition tanpa mengasersi isinya; dipakai sebagai precondition, tidak diasersi.
  - Post Condition TC-AC-DC-52 dan 283 ('-') tidak punya langkah observasi dan tidak diasersi.
