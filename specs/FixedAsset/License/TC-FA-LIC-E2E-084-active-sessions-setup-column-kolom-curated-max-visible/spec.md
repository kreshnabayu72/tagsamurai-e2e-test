---
id: TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible
title: "Active Sessions: Setup Column Ceklis, Geser, dan Pin Kolom Curated Hidden Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-287
  - TC-FA-LIC-288
  - TC-FA-LIC-289
coverage:
  web: automated
---

# Active Sessions: Setup Column Ceklis, Geser, dan Pin Kolom Curated Hidden Default

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Kolom Curated Hidden secara default. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.sesiTabel` (berkas fixture belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Curated Hidden default" (parameter langkah 2 sampai 12, 13 sampai 20, dan 23 sampai 31): `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser. Tiap iterasi memulihkan kolom ke Hidden, langkah 21 memulihkan urutan kolom hasil seretan lewat `[Reset to Default]` lalu `[Save]`, dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom. Kemampuan teknis: seret-dan-lepas item daftar kolom, mengatur lebar viewport agar tabel dapat digeser horizontal, membaca isi Live Preview dan urutan kolom tabel.
- State yang diubah dan dipulihkan: viewport browser disempitkan pada langkah 22 agar tabel dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 32.

## Test Steps

### TC-FA-LIC-287: Ceklis dan unceklis kolom Curated Hidden default

1. Klik tab Concurrent User
2. Untuk setiap kolom pada tabel "Kolom Curated Hidden default" (langkah 2 sampai 12): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
3. Centang kolom itu, klik `[Save]`, lalu buka kembali Popup Setup Column
4. Hilangkan centang kolom itu
5. Verifikasi kolom itu hilang dari Live Preview
6. Klik `[Save]`
7. Verifikasi kolom itu hilang dari tabel setelah Save
8. Muat ulang halaman (F5)
9. Verifikasi kolom itu tetap hilang setelah F5
10. Buka Popup Setup Column, lalu centang kolom itu
11. Verifikasi kolom itu kembali tampil di Live Preview
12. Klik `[Save]`, lalu buka Popup Setup Column, hilangkan centang kolom itu, dan klik `[Save]`

### TC-FA-LIC-288: Geser (drag) kolom Curated Hidden default

13. Untuk setiap kolom pada tabel "Kolom Curated Hidden default" (langkah 13 sampai 20): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
14. Centang kolom itu, lalu seret kolom itu ke posisi pertama
15. Verifikasi urutan kolom di Live Preview berubah sesuai seretan: kolom itu di posisi pertama
16. Klik `[Save]`
17. Verifikasi urutan kolom di tabel berubah sesuai seretan: kolom itu di posisi pertama
18. Muat ulang halaman (F5)
19. Verifikasi urutan kolom di tabel bertahan setelah F5: kolom itu di posisi pertama
20. Buka Popup Setup Column, hilangkan centang kolom itu, dan klik `[Save]`
21. Buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-LIC-289: Pin dan Unpin kolom Curated Hidden default

22. Sempitkan viewport browser sehingga tabel dapat digeser horizontal
23. Untuk setiap kolom pada tabel "Kolom Curated Hidden default" (langkah 23 sampai 31): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
24. Centang kolom itu, klik ikon Pin kolom itu, lalu klik `[Save]`
25. Geser tabel secara horizontal
26. Verifikasi kolom itu membeku (sticky) di kiri saat scroll horizontal
27. Muat ulang halaman (F5), lalu geser tabel secara horizontal
28. Verifikasi kolom itu tetap membeku (sticky) di kiri setelah F5
29. Buka Popup Setup Column, klik ikon Pin kolom itu untuk Unpin, lalu klik `[Save]`
30. Verifikasi kolom itu tidak lagi membeku (sticky) setelah Unpin
31. Buka Popup Setup Column, hilangkan centang kolom itu, dan klik `[Save]`
32. Pulihkan viewport browser ke ukuran semula

## Notes

- Langkah penghubung tanpa `Verifikasi`: mencentang dan menyimpan kolom Curated di awal iterasi, memulihkan kolom ke Hidden, urutan, dan Pin di akhir iterasi (S-09), langkah 21 memulihkan urutan kolom hasil seretan di akhir blok TC-FA-LIC-288 lewat `[Reset to Default]` lalu `[Save]` (bagian 8b butir 14), serta menyempitkan viewport (langkah 22) dan memulihkannya (langkah 32) agar tabel dapat digeser horizontal pada TC-FA-LIC-289 (S-14). Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: ketiga blok (langkah 2 sampai 12, 13 sampai 20, dan 23 sampai 31) dijalankan 4 kali masing-masing. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah Setup Column kolom Curated pada satu tabel dengan satu dataset dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: TC-FA-LIC-287 menyebut "hilangkan centang lalu Save" untuk kolom yang Hidden secara default, dan TC-FA-LIC-288 dan TC-FA-LIC-289 menyeret dan mem-Pin kolom itu tanpa menyebut langkah menampilkannya; spec mencentang kolom itu lebih dulu. Urutan kolom hasil seretan TC-FA-LIC-288 tidak dipulihkan antar iterasi selain kolom Curated disembunyikan kembali; pemulihan urutan dilakukan sekali di akhir blok (langkah 21).
