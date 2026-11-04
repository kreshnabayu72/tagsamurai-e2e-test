---
id: TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom
title: "Active Sessions: Screening Column Visibility dan Setup Column, serta Ceklis, Unceklis, dan Geser Kolom Hideable Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-282
  - TC-FA-LIC-283
  - TC-FA-LIC-284
  - TC-FA-LIC-285
coverage:
  web: automated
---

# Active Sessions: Screening Column Visibility dan Setup Column, serta Ceklis, Unceklis, dan Geser Kolom Hideable Visible

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.*` (berkas fixture belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Hideable Visible default" (parameter langkah 21 sampai 32 dan 33 sampai 39): `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser. Konfigurasi dikembalikan ke default oleh langkah spec di akhir tiap iterasi (kolom dicentang kembali) dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom. Kemampuan teknis: seret-dan-lepas item daftar kolom pada Popup Setup Column dan membaca isi Live Preview Setup Column dan urutan kolom tabel.

## Test Steps

### TC-FA-LIC-282: Screening Overlay Column Visibility

1. Klik tab Concurrent User
2. Klik header kolom Actions `⋯`
3. Verifikasi overlay (Quick Panel) menampilkan daftar kolom berurutan: `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`
4. Verifikasi tiap kolom pada daftar overlay memiliki checkbox
5. Verifikasi tiap kolom pada daftar overlay memiliki drag handle
6. Verifikasi kolom tercentang: `User Name`, `Email`, `Position`, `Division`, `IP Address`, `Device / OS`, `Browser`, `Login Time`, `Last Activity`
7. Verifikasi kolom tidak tercentang: `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`
8. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-FA-LIC-283: Screening Popup Setup Column tiga zona

9. Klik item `Setup Column...` pada overlay yang terbuka
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi Header: tombol `(×)`
13. Verifikasi Body: daftar kolom dengan checkbox
14. Verifikasi Body: daftar kolom dengan drag handle
15. Verifikasi Body: daftar kolom dengan ikon Pin
16. Verifikasi Body: Live Preview tabel
17. Verifikasi Footer: tombol `[Reset to Default]`
18. Verifikasi Footer: tombol `[Save]`
19. Verifikasi tidak ada tombol `[Cancel]`
20. Klik `(×)` untuk menutup popup tanpa perubahan

### TC-FA-LIC-284: Ceklis dan unceklis per kelas kolom Hideable Visible default

21. Untuk setiap kolom pada tabel "Kolom Hideable Visible default" (langkah 21 sampai 32): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
22. Hilangkan centang kolom itu
23. Verifikasi kolom itu hilang dari Live Preview
24. Klik `[Save]`
25. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
26. Verifikasi kolom itu hilang dari tabel setelah Save
27. Muat ulang halaman (F5)
28. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
29. Verifikasi kolom itu tetap hilang setelah F5
30. Buka Popup Setup Column, lalu centang kembali kolom itu
31. Verifikasi kolom itu kembali tampil di Live Preview
32. Klik `[Save]`

### TC-FA-LIC-285: Geser (drag) per kelas kolom Hideable Visible default

33. Untuk setiap kolom pada tabel "Kolom Hideable Visible default" (langkah 33 sampai 39): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
34. Seret kolom itu ke posisi pertama
35. Verifikasi urutan kolom di Live Preview berubah sesuai seretan: kolom itu di posisi pertama
36. Klik `[Save]`
37. Verifikasi urutan kolom di tabel berubah sesuai seretan: kolom itu di posisi pertama
38. Muat ulang halaman (F5)
39. Verifikasi urutan kolom di tabel bertahan setelah F5: kolom itu di posisi pertama
40. Buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup popup dengan `(×)` pada TC-FA-LIC-283 dan `[Save]` penutup iterasi (langkah 32) yang memulihkan konfigurasi kolom serta `[Reset to Default]` lalu `[Save]` di akhir TC-FA-LIC-285 yang mengembalikan urutan kolom (S-09). Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: langkah 21 sampai 32 dan langkah 33 sampai 39 masing-masing dijalankan 9 kali; urutan hasil iterasi TC-FA-LIC-285 tidak dipulihkan antar iterasi karena asersi hanya memeriksa kolom yang baru diseret berada di posisi pertama. Spec di atas 35 langkah (40 langkah nominal; 192 langkah setelah ekspansi). Alasan: semua blok memakai satu popup Setup Column pada satu tabel dengan satu dataset, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Asersi di luar Expected TC (S-03; 8b.2): `Verifikasi` "sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel" pada langkah 25 dan 28 mendahului asersi kolom hilang (anchor positif supaya tabel yang belum termuat tidak meloloskan absence).
- Temuan untuk QA: TC-FA-LIC-285 meminta menyeret kolom `User Name` ke posisi pertama padahal kolom itu sudah pertama; untuk iterasi itu seretan tidak mengubah urutan sehingga klausa "urutan berubah sesuai seretan" tidak memiliki perubahan yang teramati. TC-FA-LIC-285 tidak menyebut urutan kolom lain selain posisi pertama; spec tidak mengasersi urutan kolom lainnya. Pada TC-FA-LIC-284 Expected "kembali tampil saat dicentang ulang" tidak menyebut apakah diasersi di Live Preview atau tabel; spec mengasersi di Live Preview lalu menyimpan untuk memulihkan konfigurasi.
