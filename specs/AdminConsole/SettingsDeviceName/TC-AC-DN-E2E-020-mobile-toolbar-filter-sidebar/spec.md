---
id: TC-AC-DN-E2E-020-mobile-toolbar-filter-sidebar
title: "Mobile: Toolbar, Changelog, Filter Bottom Sheet, dan Category Sidebar"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-54
  - TC-AC-DN-55
  - TC-AC-DN-56
  - TC-AC-DN-57
coverage:
  mobile: automated
---

# Mobile: Toolbar, Changelog, Filter Bottom Sheet, dan Category Sidebar

## Prerequisites

- Mode: FE+BE (mobile Android).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini pada aplikasi mobile Android; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Perangkat Android uji bersama untuk spec mobile (disediakan tim FE/BE); `parallel: false`. Aplikasi mobile Android dijalankan pada perangkat itu; kemampuan long press sekitar 500 ms dan ketuk disediakan harness mobile.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Master Brand (#15: `Brand A`), Device Name inti (#16), dan seed 120 Device Name (#17); baca-saja. Tidak ada data Dinamis dan tidak ada aksi tulis.
- State global: filter, Search, dan pilihan Sidebar dibersihkan di akhir tiap TC; state tampil Category Sidebar pada mobile dikembalikan ke tersembunyi di akhir spec.

## Test Steps

### TC-AC-DN-54: Toolbar mobile: bottom sheet titik tiga dan pencarian inline

1. Gunakan aplikasi mobile Android pada perangkat uji dan buka halaman `Settings > Device > Device Name`
2. Ketuk ikon `⋯` pada toolbar
3. Verifikasi bottom sheet `⋯` memuat opsi `Column Visibility | Filter | Download`
4. Tutup bottom sheet
5. Ketuk ikon `🔍` pada toolbar
6. Verifikasi ikon `🔍` membuka kolom pencarian inline pada toolbar
7. Verifikasi tombol `[+ Device Name]` tetap tampil di bawah toolbar di atas daftar card
8. Ketuk `(←)` pada kotak pencarian inline

### TC-AC-DN-55: Ikon Changelog tetap di header halaman pada mobile dan tidak ada di bottom sheet

9. Verifikasi ikon Changelog tampil di header halaman
10. Ketuk ikon `⋯` pada toolbar
11. Verifikasi bottom sheet `⋯` memuat opsi `Column Visibility`
12. Verifikasi bottom sheet `⋯` tidak memuat opsi Changelog
13. Tutup bottom sheet

### TC-AC-DN-56: Filter pada mobile tampil sebagai bottom sheet

14. Ketuk ikon `⋯` pada toolbar lalu pilih Filter
15. Verifikasi Filter tampil sebagai bottom sheet berjudul `Filter`
16. Verifikasi Filter bukan panel di bawah toolbar
17. Verifikasi sheet memuat field `Brand`, `Model/Type`, `Measurement`, dan `Last Modified`
18. Verifikasi sheet memuat tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
19. Pilih Brand `Brand A` pada field `Brand` (placeholder "All brands") tanpa mengetuk `[Apply]`
20. Verifikasi sebelum `[Apply]` diketuk daftar card di belakang sheet belum berubah
21. Ketuk `[Apply]`
22. Verifikasi setelah `[Apply]` sheet tertutup
23. Verifikasi setelah `[Apply]` daftar card memuat tiga Device Name berurutan: Gate Antenna, NFC Tag, RFID Reader
24. Ketuk ikon `⋯` pada toolbar lalu pilih Filter
25. Ketuk `[Clear Field]`
26. Verifikasi setelah `[Clear Field]` seluruh field pada sheet kembali kosong (placeholder "All brands", "All models/types", "All measurements", "Select date")
27. Ketuk `[Apply]`
28. Verifikasi setelah `[Apply]` kedua sheet tertutup
29. Verifikasi setelah `[Apply]` kedua daftar card kembali memuat seluruh Device Name mulai dari Barcode Station

### TC-AC-DN-57: Category Sidebar pada mobile bekerja seperti web: tersembunyi, dibuka lewat floating toggle, dan filter langsung

30. Verifikasi Category Sidebar tersembunyi sebelum toggle diklik
31. Verifikasi tidak ada bottom sheet Category sebelum toggle diklik
32. Klik floating toggle pada tepi kanan layar
33. Verifikasi setelah toggle diklik Category Sidebar terbuka seperti pada web dengan pohon Category
34. Verifikasi Category Sidebar tanpa tombol `[Clear Field]` dan `[Apply]`
35. Expand `Hardware` lalu `Smart Fixed Reader` lalu pilih node `Antenna` pada pohon Category
36. Verifikasi setelah node `Antenna` dipilih daftar card langsung memuat dua Device Name berurutan: Door Antenna, Gate Antenna
37. Klik node `Antenna` sekali lagi
38. Verifikasi setelah node `Antenna` diklik lagi tidak ada node terpilih
39. Verifikasi daftar card kembali memuat seluruh Device Name mulai dari Barcode Station
40. Klik floating toggle untuk menyembunyikan kembali Category Sidebar

## Notes

- Mode: FE+BE (mobile Android). Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. `coverage.mobile: automated` (tanpa `coverage.web`).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1: tampilan mobile diaktifkan dengan menjalankan aplikasi mobile Android; halaman dibuka hook `beforeEach` suite pada aplikasi tersebut.
- Langkah penghubung (S-03, S-09): langkah 4 dan 13 menutup bottom sheet; langkah 8 menutup pencarian inline; langkah 40 menyembunyikan kembali Category Sidebar.
- TC-AC-DN-55: `Verifikasi` bottom sheet memuat opsi `Column Visibility` ditulis sebagai anchor positif sebelum asersi absence opsi Changelog (bagian 8b butir 2); asersi tambahan ini tidak ada di Expected TC (S-03).
- Ukuran spec (40 langkah, di atas smell sekitar 35 langkah): alasan R3 (bagian 3 prinsip 13). Empat TC memakai satu topik (toolbar dan filter mobile), satu perangkat, dan satu kelas harness; tiap TC menutup bottom sheet dan membersihkan state-nya sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal. Langkah bertambah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
