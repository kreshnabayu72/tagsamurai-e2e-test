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

1. Ketik Search `Warehouse A`, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)

### TC-FA-GRP-1166: Setup Column: centang kolom curated Category

3. Buka Popup Setup Column
4. Centang Category
5. Verifikasi Live Preview langsung menampilkan kolom Category
6. Klik [Save]
7. Verifikasi kolom Category tampil di tabel
8. Refresh F5
9. Ketik Search `Warehouse A`, tekan Enter
10. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
11. Verifikasi kolom Category tampil di tabel (konfigurasi bertahan setelah F5)

### TC-FA-GRP-1165: Sort Tab Assets by kolom Category: siklus Asc, Desc, Netral

12. Klik header Category 1×
13. Verifikasi urutan Ascending A→Z case-insensitive berdasarkan teks badge
14. Klik header 2×
15. Verifikasi urutan Descending Z→A
16. Klik header 3×
17. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1167: Setup Column: geser (drag) kolom Category

18. Hapus preferensi kolom Setup Column di browser lalu muat ulang halaman (langkah penghubung)
19. Ketik Search `Warehouse A`, tekan Enter
20. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
21. Verifikasi kolom Name tampil di tabel
22. Verifikasi kolom Category tidak tampil di tabel
23. Buka Popup Setup Column
24. Centang Category
25. Drag Category ke posisi lain (posisi paling atas daftar kolom)
26. Verifikasi urutan Live Preview mengikuti posisi baru
27. Klik [Save]
28. Verifikasi urutan kolom tabel berubah sesuai posisi baru
29. Refresh F5
30. Ketik Search `Warehouse A`, tekan Enter
31. Buka Detail Warehouse A (Tab Assets) (langkah penghubung)
32. Verifikasi urutan kolom tabel tetap sesuai posisi baru

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: TC-FA-GRP-1166, TC-FA-GRP-1165, TC-FA-GRP-1167. TC-FA-GRP-1166 memuat aksi yang membentuk precondition d (kolom Category ditampilkan) yang dibutuhkan TC-FA-GRP-1165 (S-10).
- Langkah penghubung (S-03): "Hapus preferensi kolom Setup Column di browser lalu muat ulang halaman" mengembalikan kolom Category ke tersembunyi sebelum TC-FA-GRP-1167 (S-09); pemulihan akhir lewat hook `after`.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1167: "drag Category ke posisi lain" tidak menyebut posisi tujuan; spec memakai posisi paling atas daftar kolom.
  - TC-FA-GRP-1166 dan TC-FA-GRP-1167: TC tidak menyatakan apakah Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A sebagai langkah penghubung.
  - TC-FA-GRP-1165: precondition d (kolom Category sudah ditampilkan) dibentuk oleh TC-FA-GRP-1166 karena kolom tersembunyi secara default.
