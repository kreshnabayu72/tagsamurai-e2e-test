---
id: TC-AC-DN-E2E-094-usage-setup-column-bagian-1
title: "Usage by Company: Screening Column Visibility/Setup Column, Setup Kolom, dan Kolom Tersisa Satu"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-632
  - TC-AC-DN-266
  - TC-AC-DN-616
coverage:
  web: automated
---

# Usage by Company: Screening Column Visibility/Setup Column, Setup Kolom, dan Kolom Tersisa Satu

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: konfigurasi Setup Column tabel Usage by Company tersimpan di cache browser per user (Column Visibility, urutan, dan pin). Hook `before` dan `after` spec ini memanggil kemampuan "hapus preferensi kolom Usage di browser" (`suite.md`; disediakan tim FE) sehingga spec mulai dan berakhir dari konfigurasi default. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, hover, tekan Esc, tarik-lepas (drag and drop) kolom di modal Setup Column, dan muat ulang halaman (F5).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-632: Screening Overlay Column Visibility dan modal Setup Column tabel Usage by Company

2. Hover header kolom Actions tabel Usage
3. Verifikasi tooltip `Column Visibility` tampil
4. Klik header kolom Actions tabel Usage
5. Verifikasi Overlay Column Visibility terbuka dengan daftar kolom berurutan `Company`, `Entity Type`, `Total SKU`, `Total Stock`
6. Verifikasi tiap kolom pada overlay memiliki checkbox tercentang dan enabled serta drag handle
7. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
8. Klik `Setup Column...`
9. Verifikasi header modal Setup Column: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close `(✕)`
10. Verifikasi body modal: daftar kolom `Company`, `Entity Type`, `Total SKU`, `Total Stock` dengan checkbox tercentang, drag handle, dan ikon Pin
11. Verifikasi Live Preview menampilkan urutan header yang sama
12. Verifikasi footer modal: tombol `[Reset to Default]` dan `[Save]` rata kanan, dan tidak ada tombol `[Cancel]`
13. Klik ikon close `(✕)` pada modal Setup Column

### TC-AC-DN-266: Setup Column tabel Usage menyembunyikan kolom yang dipilih

14. Klik trigger Column Visibility pada header kolom Actions tabel Usage lalu hilangkan centang kolom `Total SKU`
15. Verifikasi kolom `Total SKU` tidak tampil pada tabel Usage
16. Verifikasi kolom `Company`, `Entity Type`, dan `Total Stock` tetap tampil
17. Centang kembali kolom `Total SKU`

### TC-AC-DN-616: Setup Column tabel Usage by Company menyembunyikan dan menampilkan setiap kolom serta menjaga satu kolom tersisa

18. Klik trigger Column Visibility pada header kolom Actions tabel Usage lalu hilangkan centang kolom `Company`
19. Verifikasi kolom `Company` hilang dari header dan baris tabel Usage
20. Centang kembali kolom `Company`
21. Verifikasi kolom `Company` tampil lagi di posisi semula
22. Hilangkan centang kolom `Entity Type`
23. Verifikasi kolom `Entity Type` hilang dari header dan baris tabel Usage
24. Centang kembali kolom `Entity Type`
25. Verifikasi kolom `Entity Type` tampil lagi di posisi semula
26. Hilangkan centang kolom `Total Stock`
27. Verifikasi kolom `Total Stock` hilang dari header dan baris tabel Usage
28. Centang kembali kolom `Total Stock`
29. Verifikasi kolom `Total Stock` tampil lagi di posisi semula
30. Hilangkan centang kolom `Company`, `Entity Type`, dan `Total SKU`
31. Verifikasi hanya `Total Stock` tersisa dan checkbox `Total Stock` tetap tampil namun disabled
32. Arahkan kursor ke checkbox `Total Stock`
33. Verifikasi tooltip `At least one column must remain visible.` tampil
34. Klik checkbox `Total Stock` yang disabled
35. Verifikasi kolom `Total Stock` tidak tersembunyi
36. Centang kembali kolom `Company`, `Entity Type`, dan `Total SKU`
37. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup modal Setup Column dengan ikon close `(✕)` tanpa Save, mencentang kembali kolom yang disembunyikan agar konfigurasi Column Visibility kembali ke default sebelum blok berikutnya (S-09), dan menutup dialog Detail dengan ikon `[X]`. Overlay Column Visibility diasumsikan tetap terbuka selama beberapa centang berurutan pada blok yang sama; bila menutup sendiri sesudah satu centang, trigger dibuka kembali.
- Hook `before` dan `after` menghapus preferensi kolom Usage di browser (kemampuan `suite.md`); centang kembali antar blok menjaga default agar blok sesudahnya tetap bermakna.
- Satu pembukaan dialog Detail dipakai bersama ketiga blok TC (state dipulihkan antar blok).
- Ukuran spec (37 langkah, di atas smell 35 langkah): satu topik (Setup Column tabel Usage by Company), satu dialog, satu kelas harness; tiap blok TC membuka overlay atau modal sendiri dan memulihkan konfigurasi sebelum blok berikutnya, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition kosong (`-`) atau tanpa langkah observasi pada TC spec ini tidak diasersi (S-01).
  - TC-AC-DN-616 menutup dengan "hanya `Total Stock` tersisa" tanpa menyebut persistensi sesudah menutup dialog; spec memulihkan ketiga kolom di akhir blok.
