---
id: TC-AC-DC-E2E-001-screening-sidebar-struktur-urutan
title: "Screening Sidebar Category: Header, Body, Footer, Struktur Node Bawaan, Bold Hardcoded, dan Urutan A-Z pada Device Name dan Device SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-1
  - TC-AC-DC-2
  - TC-AC-DC-3
  - TC-AC-DC-4
  - TC-AC-DC-5
coverage:
  web: automated
---

# Screening Sidebar Category: Header, Body, Footer, Struktur Node Bawaan, Bold Hardcoded, dan Urutan A-Z pada Device Name dan Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node. Nilai literal node diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal tiap spec: halaman baru dibuka oleh hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DC-1: Screening Sidebar Category pada Settings > Device > Device Name

1. Susuri Sidebar Category dari atas ke bawah dan dari kiri ke kanan tanpa mengklik apa pun
2. Verifikasi Header: judul "Category" rata kiri pada baris 1 bersama ikon Changelog
3. Verifikasi Header baris 2: kolom pencarian tree (TreeSearchInput) sejajar dengan tombol toggle Expand/Collapse All
4. Verifikasi Header: tidak ada baris 3 berupa tombol "Category" di sidebar desktop dan tidak ada tombol silang `(X)` pada header
5. Verifikasi Body: tree dengan varian Checkbox Selection memuat baris `All Categories` paling atas, lalu node `Hardware` dan `TAG` sebagai root permanen
6. Verifikasi Body: node hardcoded tampil bold
7. Verifikasi Body: `Hardware` dan `TAG` menampilkan kotak centang
8. Verifikasi Body: `All Categories` tampil tanpa kotak centang
9. Verifikasi Body: tidak ada input inline Add/Edit yang terbuka
10. Verifikasi Footer: Floating Open/Collapse Toggle Button tampil di tepi kiri panel sidebar (state Open)

### TC-AC-DC-3: Struktur node bawaan Category dan urutan alfabetis semua level

11. Klik nama node `Hardware`
12. Klik nama node `TAG`
13. Verifikasi `Hardware` mengandung tepat 3 anak bawaan urut A-Z: `BLE Gateway`, `Handheld Reader`, `Smart Fixed Reader`
14. Verifikasi `TAG` mengandung tepat 4 anak bawaan urut A-Z: `BLE`, `GPS`, `NFC`, `RFID`
15. Verifikasi baris `All Categories` tampil paling atas, diikuti root `Hardware` lalu `TAG` urut A-Z

### TC-AC-DC-4: Node hardcoded bold dan node user-created tidak bold

16. Expand `Handheld Reader`
17. Verifikasi node hardcoded (`Hardware`, `TAG`, `Handheld Reader`) tampil bold
18. Verifikasi node user-created `Rugged Scanner` tampil tidak bold
19. Verifikasi `Handheld Reader` dan `Rugged Scanner` menampilkan kotak centang sebagai nilai filter
20. Verifikasi kotak `Hardware` dan `TAG` memilih seluruh descendant dan bukan nilai filter

### TC-AC-DC-5: Urutan A-Z case-insensitive di level yang sama, termasuk nama berawalan huruf kecil

21. Amati daftar anak `Handheld Reader`
22. Verifikasi anak `Handheld Reader` tampil berurutan A-Z tanpa membedakan huruf besar/kecil: `Barcode Handheld`, `bluetooth Reader`, `Dipakai Leaf`, `Filter Induk`, `Hapus Daun`, `Hapus Keluarga`, `Industrial Scanner`, node 120 karakter berawalan `Pemindai`, `Referensi Banyak`, dan `Rugged Scanner`
23. Verifikasi `bluetooth Reader` (berawalan huruf kecil) tampil di antara `Barcode Handheld` dan `Dipakai Leaf`, bukan di akhir daftar

### TC-AC-DC-2: Screening Sidebar Category yang sama pada Settings > Device > Device SKU

24. Pindah ke sub-tab `Device SKU`
25. Susuri Sidebar Category dari atas ke bawah dan dari kiri ke kanan tanpa mengklik apa pun
26. Verifikasi Header: judul "Category" rata kiri dan ikon Changelog pada baris 1
27. Verifikasi Header baris 2: kolom pencarian tree sejajar dengan tombol toggle Expand/Collapse All
28. Verifikasi Body: tree yang sama dengan sub-tab Device Name, yaitu `Hardware` dan `TAG` sebagai root permanen
29. Verifikasi Body: node hardcoded tampil bold
30. Verifikasi Footer: Floating Open/Collapse Toggle Button tampil di tepi kiri panel sidebar

## Notes

- Urutan TC dalam spec: TC-AC-DC-1, 3, 4, 5, lalu 2. TC-AC-DC-2 (sub-tab Device SKU) diletakkan terakhir supaya TC lain tidak bergantung pada state expand tree setelah berpindah sub-tab (S-10).
- Langkah penghubung (S-03): langkah 16 meng-expand `Handheld Reader` saja karena `Hardware` sudah ter-expand oleh langkah 11; langkah 21 hanya mengamati daftar anak yang sudah tampil; langkah 24 berpindah sub-tab untuk TC-AC-DC-2 yang precondition-nya berada di Device SKU.
- Temuan untuk QA: (1) TC-AC-DC-4 Expected c, klausa "kotak `Hardware` dan `TAG` memilih seluruh descendant dan bukan nilai filter" tidak teramati dari langkah TC (tidak ada langkah klik); perilaku itu diuji di TC-AC-DC-29. Klausa tetap ditulis sebagai Verifikasi mengikuti TC (langkah 20). (2) Node 120 karakter hanya dikenali lewat awalan `Pemindai` pada TC-AC-DC-5; asersi mengikuti teks TC.
