---
id: TC-FA-GRP-E2E-242-tab-assets-category-sort-dan-setup-column-centang-serta-geser
title: "Tab Assets Kolom Category: Sort dan Setup Column (Centang Kolom Curated, Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1165
  - TC-FA-GRP-1166
  - TC-FA-GRP-1167
coverage:
  web: automated
---

# Tab Assets Kolom Category: Sort dan Setup Column (Centang Kolom Curated, Geser)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan Category bervariasi (huruf besar/kecil, angka; sedikitnya dua nilai Category distinct, S-11).
- Kolom curated Category tersembunyi secara default dan ditampilkan oleh TC-FA-GRP-1166 dalam spec ini (precondition d TC-FA-GRP-1165).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE); membaca data aset Warehouse A (tim FE/BE).
- State global: konfigurasi kolom Setup Column akun Total Control disimpan oleh TC-FA-GRP-1166 dan TC-FA-GRP-1167. Pemulihan preferensi kolom Setup Column: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`.

## Test Steps

### Langkah penghubung

1. Buka Detail Warehouse A (Tab Assets)

### TC-FA-GRP-1166: Setup Column: centang kolom curated Category

2. Buka Popup Setup Column
3. Centang Category
4. Verifikasi Live Preview langsung menampilkan kolom Category
5. Klik [Save]
6. Verifikasi kolom Category tampil di tabel
7. Refresh F5
8. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
9. Verifikasi kolom Category tampil di tabel (konfigurasi bertahan setelah F5)

### TC-FA-GRP-1165: Sort Tab Assets by kolom Category: siklus Asc, Desc, Netral

10. Klik header Category 1×
11. Verifikasi urutan Ascending A→Z case-insensitive berdasarkan teks badge
12. Klik header 2×
13. Verifikasi urutan Descending Z→A
14. Klik header 3×
15. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1167: Setup Column: geser (drag) kolom Category

16. Hapus preferensi kolom Setup Column di browser lalu muat ulang halaman (langkah penghubung)
17. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
18. Verifikasi kolom Name tampil di tabel
19. Verifikasi kolom Category tidak tampil di tabel
20. Buka Popup Setup Column
21. Centang Category
22. Drag Category ke posisi lain (posisi paling atas daftar kolom)
23. Verifikasi urutan Live Preview mengikuti posisi baru
24. Klik [Save]
25. Verifikasi urutan kolom tabel berubah sesuai posisi baru
26. Refresh F5
27. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
28. Verifikasi urutan kolom tabel tetap sesuai posisi baru

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: TC-FA-GRP-1166, TC-FA-GRP-1165, TC-FA-GRP-1167. TC-FA-GRP-1166 memuat aksi yang membentuk precondition d (kolom Category ditampilkan) yang dibutuhkan TC-FA-GRP-1165 (S-10).
- Langkah penghubung (S-03): "Hapus preferensi kolom Setup Column di browser lalu muat ulang halaman" mengembalikan kolom Category ke tersembunyi sebelum TC-FA-GRP-1167 (S-09); pemulihan akhir lewat hook `after`.
- Temuan untuk QA:
  - TC-FA-GRP-1167: "drag Category ke posisi lain" tidak menyebut posisi tujuan; spec memakai posisi paling atas daftar kolom.
  - TC-FA-GRP-1166 dan TC-FA-GRP-1167: TC tidak menyatakan apakah Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A sebagai langkah penghubung.
  - TC-FA-GRP-1165: precondition d (kolom Category sudah ditampilkan) dibentuk oleh TC-FA-GRP-1166 karena kolom tersembunyi secara default.
