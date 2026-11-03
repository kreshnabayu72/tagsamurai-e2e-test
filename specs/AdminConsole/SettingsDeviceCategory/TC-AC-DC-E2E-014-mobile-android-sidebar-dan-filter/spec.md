---
id: TC-AC-DC-E2E-014-mobile-android-sidebar-dan-filter
title: "Mobile Android: Sidebar Category Tampil lewat Floating Toggle, Aksi per Node, Filter Langsung Berlaku, All Categories, dan Changelog sebagai Bottom Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-37
  - TC-AC-DC-38
  - TC-AC-DC-41
  - TC-AC-DC-40
coverage:
  mobile: automated
---

# Mobile Android: Sidebar Category Tampil lewat Floating Toggle, Aksi per Node, Filter Langsung Berlaku, All Categories, dan Changelog sebagai Bottom Sheet

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6 Mobile Layout); data Device Name tampil sebagai Card List.
- Perangkat atau emulator Android dengan aplikasi TAG Samurai Admin Console terpasang (perangkat uji tidak disebut di Pre-setup TC; disediakan tim FE), serta kemampuan mengetuk elemen UI, menampilkan aksi node pada baris tree, dan membaca isi Card List. `parallel: false` untuk perangkat fisik bersama.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori), #15 (Device Name `FN-1`), dan #17 (Riwayat Changelog) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dan riwayat Changelog #17 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah dan dipulihkan: state Open atau Collapsed sidebar per user dan per halaman, serta pilihan filter Category. Hook `before` dan `after` menghapus preferensi sidebar tersimpan akun aktor (kemampuan disediakan tim FE) supaya sidebar tersembunyi pada kunjungan pertama.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-37: Mobile: Sidebar Category tampil dan pilihan filter langsung berlaku tanpa Apply

1. Catat jumlah total Device Name pada Card List (tanpa filter Category)
2. Verifikasi Sidebar Category tersembunyi sebelum floating toggle diklik
3. Klik floating toggle pada tepi kanan layar
4. Verifikasi Sidebar Category tampil dengan judul "Category", ikon Changelog, kolom pencarian tree (TreeSearchInput), toggle Expand/Collapse All, dan baris `All Categories` di atas `Hardware` dan `TAG`
5. Verifikasi data Device Name tampil sebagai Card List
6. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
7. Klik node `Filter Anak 1`
8. Verifikasi Card List langsung menampilkan `FN-1`
9. Verifikasi tidak ada tombol `[Apply]`
10. Klik baris `All Categories`

### TC-AC-DC-38: Mobile: aksi per node hanya tampil pada node yang punya minimal satu aksi diizinkan

11. Munculkan aksi node pada baris `Hardware` dan `TAG`
12. Verifikasi `Hardware` dan `TAG` tidak memiliki aksi
13. Munculkan aksi node pada baris `Handheld Reader`
14. Verifikasi `Handheld Reader` hanya memiliki aksi `+ Subcategory`
15. Munculkan aksi node pada baris `Rugged Scanner`
16. Verifikasi `Rugged Scanner` memiliki aksi `+ Subcategory`, Edit, dan Delete

### TC-AC-DC-41: Mobile: klik All Categories langsung melepas pilihan filter

17. Klik node `Filter Anak 1`
18. Klik baris `All Categories`
19. Verifikasi Card List langsung menampilkan seluruh Device Name (jumlah total sama dengan catatan langkah 1)
20. Verifikasi tidak ada tombol `[Apply]`
21. Verifikasi tidak ada node berstatus tercentang atau partial-check

### TC-AC-DC-40: Mobile: Changelog dibuka lewat ikon di header Sidebar Category dan tampil sebagai bottom sheet

22. Klik ikon Changelog pada header Sidebar Category
23. Verifikasi modal "Changelog: Category" terbuka dari ikon header Sidebar Category
24. Verifikasi modal tampil sebagai bottom sheet (bukan dialog di tengah layar)
25. Verifikasi isi riwayat ditampilkan dalam Card List (bukan tabel)
26. Tutup modal Changelog dengan `[×]`

## Notes

- Urutan TC dalam spec: TC-AC-DC-37, 38, 41, 40. TC-AC-DC-37 dijalankan pertama karena mengasersi sidebar tersembunyi pada kunjungan pertama; TC-AC-DC-38 memakai tree yang sudah ter-expand dari TC-AC-DC-37 (`Hardware` dan `Handheld Reader`).
- Langkah penghubung (S-03): langkah 1 mencatat baseline Card List untuk langkah 19; `All Categories` (langkah 10) melepas pilihan filter (S-09); langkah 26 menutup modal Changelog.
- Temuan untuk QA: (1) TC-AC-DC-37 sampai 42 menyebut "aplikasi mobile Android" tanpa menyatakan apakah dijalankan lewat viewport mobile web atau aplikasi Android nyata, dan tanpa nama perangkat uji. (2) TC-AC-DC-38 dan 39 tidak menyatakan cara memunculkan aksi node pada mobile ("munculkan aksi node"); gesture atau ketukan ditentukan tim FE. (3) TC-AC-DC-40 tidak menyatakan cara menutup modal Changelog pada mobile; spec memakai `[×]`. (4) Ukuran halaman default Card List tidak ditulis; asersi "seluruh Device Name" memakai jumlah total yang dicatat.
