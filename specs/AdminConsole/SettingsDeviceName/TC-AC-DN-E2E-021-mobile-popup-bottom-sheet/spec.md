---
id: TC-AC-DN-E2E-021-mobile-popup-bottom-sheet
title: "Mobile: Popup Create, Edit, Changelog, Delete, Blok, dan Unsaved Changes sebagai Bottom Sheet"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-599
  - TC-AC-DN-619
  - TC-AC-DN-620
coverage:
  mobile: automated
---

# Mobile: Popup Create, Edit, Changelog, Delete, Blok, dan Unsaved Changes sebagai Bottom Sheet

## Prerequisites

- Mode: FE+BE (mobile Android).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini pada aplikasi mobile Android; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Perangkat Android uji bersama untuk spec mobile (disediakan tim FE/BE); `parallel: false`. Aplikasi mobile Android dijalankan pada perangkat itu; kemampuan long press sekitar 500 ms dan ketuk disediakan harness mobile.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16: `Door Antenna`, `Cable Tester`, `RFID Reader` dengan SKU yang memblok Delete), unit BYO dan relasi SKU sesuai fixture (#22), serta Riwayat Changelog Uji (#19); baca-saja. Tidak ada data Dinamis; dialog Delete dibatalkan dan tidak ada record yang diubah atau dihapus.
- Teks "Draft Gateway" yang diketik pada form Create hanya membuat form dirty dan tidak pernah disimpan; form dirty ditutup lewat `[Leave]`.

## Test Steps

### TC-AC-DN-599: Mobile: popup Create Device Name tampil sebagai bottom sheet

1. Gunakan aplikasi mobile Android pada perangkat uji dan buka halaman `Settings > Device > Device Name`
2. Klik tombol `+ Device Name` pada toolbar mobile
3. Verifikasi form Create tampil sebagai bottom sheet berjudul "Create Device Name"
4. Verifikasi form Create memuat field Device Name, Measurement, dan Category
5. Verifikasi form Create memuat checkbox `Stay on this form after submitting`
6. Verifikasi form Create memuat tombol `[Clear Field]` dan `[Submit]`
7. Ketuk icon close `[✕]` pada form Create

### TC-AC-DN-619: Mobile: popup Edit dan modal Changelog tampil sebagai bottom sheet

8. Buka menu aksi pada card `Door Antenna` lalu pilih `Edit`
9. Verifikasi form Edit tampil sebagai bottom sheet berjudul "Edit Device Name"
10. Verifikasi field Device Name berisi `Door Antenna`, Measurement `Unit`, Category `Antenna`
11. Verifikasi form Edit memuat tombol `[Clear Field]` dan `[Save]`
12. Verifikasi form Edit tanpa checkbox `Stay on this form after submitting`
13. Verifikasi form Edit tidak tampil sebagai dialog di tengah layar
14. Ketuk icon close `[✕]` pada form Edit
15. Ketuk ikon Changelog di header halaman
16. Verifikasi modal Changelog tampil sebagai bottom sheet berjudul "Changelog: Device Name" dengan tabel Changelog
17. Verifikasi modal Changelog tidak tampil sebagai dialog di tengah layar
18. Tutup modal Changelog

### TC-AC-DN-620: Mobile: dialog Delete, dialog blok, dan dialog Unsaved Changes tampil sebagai bottom sheet

19. Long press selama sekitar 500 ms pada card `Cable Tester`
20. Ketuk tombol `[Delete]` pada Bulk Bar
21. Verifikasi dialog Delete tampil sebagai bottom sheet berjudul "Delete Device Name" dengan bullet `Cable Tester` serta tombol `[Cancel]` dan `[Delete]`
22. Verifikasi dialog Delete tidak tampil sebagai dialog di tengah layar
23. Ketuk `[Cancel]`
24. Ketuk tombol tutup `[✕]` pada Bulk Bar
25. Long press selama sekitar 500 ms pada card `RFID Reader`
26. Ketuk tombol `[Delete]` pada Bulk Bar
27. Verifikasi dialog blok tampil sebagai bottom sheet berjudul "Cannot Delete Device Name" dengan bullet `RFID Reader`, pesan "This device name still has SKUs.", dan tombol `[OK]`
28. Verifikasi dialog blok tidak tampil sebagai dialog di tengah layar
29. Ketuk `[OK]`
30. Ketuk tombol tutup `[✕]` pada Bulk Bar
31. Ketuk tombol `+ Device Name`
32. Ketik "Draft Gateway" pada field Device Name
33. Ketuk icon close `[✕]`
34. Verifikasi dialog Unsaved Changes tampil sebagai bottom sheet dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
35. Verifikasi dialog Unsaved Changes tidak tampil sebagai dialog di tengah layar
36. Ketuk `[Leave]`

## Notes

- Mode: FE+BE (mobile Android). Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. `coverage.mobile: automated` (tanpa `coverage.web`).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1: tampilan mobile diaktifkan dengan menjalankan aplikasi mobile Android; halaman dibuka hook `beforeEach` suite pada aplikasi tersebut.
- Langkah penghubung (S-03, S-08, S-09): langkah 7 menutup form Create yang belum diubah; langkah 18 menutup modal Changelog; langkah 30 mengakhiri mode seleksi sebelum membuka form Create; langkah 36 menutup form dirty secara deterministik (dialog `Unsaved Changes` lalu `[Leave]`).
- TC-AC-DN-620: TC tidak menyatakan keadaan mode seleksi sesudah `[OK]` pada dialog blok; langkah 30 mengakhirinya sebelum langkah berikutnya (lihat Temuan untuk QA). Expected butir d ("tidak tampil sebagai dialog di tengah layar") diasersi tepat sesudah masing-masing dialog.
- TC-AC-DN-619: Expected butir c ("Keduanya tidak tampil sebagai dialog di tengah layar") diasersi sesudah form Edit dan sesudah modal Changelog.
- Ukuran spec (36 langkah, di atas smell sekitar 35 langkah): alasan R3 (bagian 3 prinsip 13). Tiga TC memakai satu topik (popup dan dialog sebagai bottom sheet), satu perangkat, dan satu kelas harness; tiap TC menutup popup atau dialognya sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal. Langkah bertambah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-DN-620 langkah 8 sampai 9 tidak menyatakan apakah mode seleksi berakhir sesudah `[OK]` pada dialog blok; spec mengetuk `[✕]` pada Bulk Bar sebelum membuka form Create.
  - TC-AC-DN-620 berlabel kelas b pada indeks (dialog blok) hanya karena kata kunci; pemicunya Pre-setup `RFID Reader` yang ber-SKU dan bukan kegagalan yang dipaksakan, sehingga tetap di spec fungsional ini.
