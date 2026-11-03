---
id: TC-AC-DC-E2E-003-screening-sidebar-all-categories-dan-tooltip
title: "Screening Sidebar Category: Baris All Categories dan Tooltip Aksi Node serta Ikon Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-286
  - TC-AC-DC-287
  - TC-AC-DC-11
coverage:
  web: automated
---

# Screening Sidebar Category: Baris All Categories dan Tooltip Aksi Node serta Ikon Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-286: All Categories tampil sebagai baris pertama di atas Hardware dan TAG tanpa kotak centang dan tanpa aksi

1. Perhatikan urutan baris tree dari atas
2. Verifikasi baris pertama tree adalah `All Categories`, diikuti `Hardware` lalu `TAG`
3. Verifikasi `All Categories` tidak memiliki kotak centang
4. Hover baris `All Categories`
5. Verifikasi tidak ada aksi `+ Subcategory`, Edit, atau Delete pada `All Categories`

### TC-AC-DC-287: All Categories tidak tersaring pencarian tree dan tidak terpengaruh Expand/Collapse All

6. Ketik Search `Rugged` pada kolom pencarian tree, tekan Enter
7. Verifikasi baris `All Categories` tetap tampil sebagai baris pertama
8. Kosongkan isi kotak pencarian tree, tekan Enter
9. Klik tombol toggle Expand/Collapse All
10. Klik tombol toggle Expand/Collapse All
11. Verifikasi baris `All Categories` tetap tampil di posisi yang sama dan tidak berubah state

### TC-AC-DC-11: Tooltip aksi node dan ikon Changelog pada header sidebar

12. Hover ikon Changelog pada header sidebar
13. Verifikasi tooltip ikon Changelog berisi "Changelog"
14. Expand `Hardware`
15. Expand `Handheld Reader`
16. Hover node `Rugged Scanner`
17. Verifikasi aksi per node tampil sebagai ikon langsung pada baris node saat hover (desktop)
18. Hover aksi `+ Subcategory` pada `Rugged Scanner`
19. Verifikasi tooltip aksi berisi "+ Subcategory"
20. Hover aksi Edit pada `Rugged Scanner`
21. Verifikasi tooltip aksi berisi "Edit"
22. Hover aksi Delete pada `Rugged Scanner`
23. Verifikasi tooltip aksi berisi "Delete"

## Notes

- Langkah penghubung (S-03): langkah 8 mengosongkan Search sesuai TC-AC-DC-287 langkah 3; langkah 14 dan 15 meng-expand `Hardware` dan `Handheld Reader` supaya `Rugged Scanner` terlihat sebelum di-hover (TC-AC-DC-11 menyebut tree tampil tanpa langkah expand); setelah langkah 10 tree berada dalam keadaan collapse.
- Temuan untuk QA: (1) Urutan Expected TC-AC-DC-11 (a: ikon langsung, b: tooltip Changelog, c: tooltip aksi) disesuaikan dengan urutan state (8b butir 5): tooltip Changelog diasersi pertama karena di-hover sebelum node. (2) TC-AC-DC-287 tidak menyatakan state `All Categories` sebelum Expand/Collapse All; "tidak berubah state" diasersi sebagai tetap tanpa kotak centang dan tetap tampil di baris pertama.
