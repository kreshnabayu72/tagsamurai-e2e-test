---
id: TC-GS-IMPORT-E2E-051-batas-umur-draft-24-jam-23j59m-tepat-24j-halaman-terbuka-melewati-batas
title: "Batas Umur Draft 24 Jam: 23j59m, Tepat 24j, Halaman Terbuka Melewati Batas, dan Edit atau Append Tidak Mereset Umur"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-877
  - TC-GS-IMPORT-878
  - TC-GS-IMPORT-879
  - TC-GS-IMPORT-880
coverage:
  web: automated
---

# Batas Umur Draft 24 Jam: 23j59m, Tepat 24j, Halaman Terbuka Melewati Batas, dan Edit atau Append Tidak Mereset Umur

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah jam server; lihat `suite.md`.
- Akun: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client C, disiapkan oleh langkah 1, 8, 16, dan 28 lewat skrip fixture): D-77 draft Brand 6 baris `pending` dari `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp). `brand-12.csv` (D-01, 12 baris) untuk TC-GS-IMPORT-880. General Settings Client C: format tanggal `dd/MM/yy` (TC-GS-IMPORT-878).
- Hook umur draft D-76 (kemampuan teknis yang disediakan tim FE/BE; memundurkan `created_at` job lewat fixture timestamp atau memajukan jam server). Umur dihitung dari waktu server yang dibaca lewat API seeding (T0), bukan dari waktu hook:
  - Varian 2 (TC-GS-IMPORT-877): `created_at` = T0 dikurangi 23 jam 59 menit; halaman dibaca dalam 30 detik sesudahnya sehingga umur tetap di bawah 24 jam (margin 30 detik, kurang dari 5 menit).
  - Varian 3 (TC-GS-IMPORT-878): `created_at` = T0 dikurangi tepat 24 jam; pembacaan berikutnya berumur 24 jam atau lebih (tepat 24 jam sudah menampilkan banner).
  - Varian 4 (TC-GS-IMPORT-879 dan 880): `created_at` = T0 dikurangi 23 jam 50 menit; jam server dimajukan 11 menit melewati batas 24 jam.
- Jam yang diatur: jam server saja (umur draft dihitung di server dan baru terbaca saat Staging Table dibaca; tidak ada countdown UI). Jam server dipulihkan lewat langkah eksplisit sebelum blok berikutnya dan di hook `after`.
- Jeda nyata ±30 detik pada langkah menunggu TC-GS-IMPORT-879.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset (R1) di akhir tiap blok; jam server dikembalikan ke waktu nyata.

## Test Steps

### TC-GS-IMPORT-877: Draft berumur 23 jam 59 menit

1. Atur ulang draft D-77 dengan `created_at` 23 jam 59 menit sebelum waktu server (varian 2)
2. Muat ulang halaman Import > Brand dalam 30 detik setelah `created_at` diatur (varian 2)
3. Verifikasi Staging Table menampilkan 6 baris `pending`
4. Verifikasi Staging Metric Cards Total Rows 6 (Active)
5. Verifikasi footer `[Import (6)]` Enabled
6. Verifikasi Unsaved Banner tidak tampil
7. Verifikasi tidak ada tombol `[Discard]` di halaman

### TC-GS-IMPORT-878: Draft berumur tepat 24 jam

8. Atur ulang draft D-77 dengan `created_at` tepat 24 jam sebelum waktu server (varian 3)
9. Muat ulang halaman Import > Brand
10. Verifikasi Staging Table menampilkan 6 baris `pending`
11. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
12. Verifikasi [Date] berisi tanggal satu hari sebelum hari uji dengan format `dd/MM/yy`
13. Arahkan kursor ke `[Discard]` pada Unsaved Banner
14. Verifikasi `[Discard]` Enabled
15. Verifikasi `[Discard]` tanpa tooltip

### TC-GS-IMPORT-879: Halaman terbuka tidak menerima push saat umur melewati 24 jam

16. Atur ulang draft D-77 dengan umur 23 jam 50 menit (varian 4)
17. Muat ulang halaman Import > Brand
18. Verifikasi Staging Metric Cards Total Rows 6 (Active)
19. Verifikasi Unsaved Banner tidak tampil
20. Majukan jam server 11 menit (fixture jam server)
21. Tunggu 30 detik tanpa berinteraksi dengan halaman
22. Verifikasi footer `[Import (6)]` Enabled
23. Verifikasi Unsaved Banner tetap tidak tampil (halaman tidak menerima push saat umur draft melewati 24 jam)
24. Muat ulang halaman Import > Brand
25. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
26. Verifikasi footer `[Import (6)]` Enabled
27. Pulihkan jam server ke waktu nyata (fixture jam server)

### TC-GS-IMPORT-880: Edit baris dan Append tidak mereset umur draft

28. Atur ulang draft D-77 dengan umur 23 jam 50 menit (varian 4)
29. Muat ulang halaman Import > Brand
30. Klik `⋯` pada baris #1
31. Pilih Edit
32. Ubah Brand Name baris #1 dari `Nikon` menjadi `Nikon Corporation`
33. Klik `[Save]`
34. Verifikasi baris #1 tampil dengan Brand Name `Nikon Corporation`
35. Klik [Upload File] di toolbar
36. Pilih berkas `brand-12.csv` di file picker
37. Klik `[Append Records]`
38. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
39. Verifikasi toast sukses: "Success, row has been added."
40. Muat ulang halaman Import > Brand
41. Verifikasi Staging Metric Cards Total Rows 18 (Active)
42. Verifikasi Unsaved Banner tidak tampil karena umur draft masih kurang dari 24 jam (edit dan Append tidak mereset umur)
43. Majukan jam server 11 menit (fixture jam server)
44. Muat ulang halaman Import > Brand
45. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil (24 jam sejak `[Confirm Mapping]` pertama, bukan sejak edit atau Append)
46. Verifikasi Staging Metric Cards Total Rows 18 (Active) dan Ready to Import 18
47. Pulihkan jam server ke waktu nyata (fixture jam server) dan reset Client C ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji umur draft 24 jam sebagai batas waktu).
- Spec memuat 47 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (hook umur draft D-76 dan jam server), tiap blok memakai draft D-77 yang dibuat ulang dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 9, 17, 24, 29, 40, 44 (muat ulang halaman); langkah 1, 8, 16, 28 (mengatur ulang draft D-77); langkah 21 (jeda nyata 30 detik); langkah 27 dan 47 (memulihkan jam server dan draft).
- Anchor positif untuk absence (konvensi 8b butir 2, S-03): langkah 18 (Metric Cards Total Rows 6) mendahului langkah 19, langkah 22 (footer `[Import (6)]`) mendahului langkah 23, langkah 41 (Metric Cards Total Rows 18) mendahului langkah 42; langkah 6 didahului langkah 3 sampai 5.
- Pembagian TC lintas spec: TC-GS-IMPORT-881 (commit sebagian tidak mereset umur) ada di spec 053; TC-GS-IMPORT-882, 883, dan 885 (draft baru mulai dari umur 0) ada di spec 052.
- Temuan untuk QA:
  - TC-GS-IMPORT-878 tidak merujuk acuan T0 untuk "tepat 24 jam"; spec menghitung dari waktu server yang dibaca saat seeding.
  - TC-GS-IMPORT-877, 878, dan 879 tidak menyebut urutan antara `created_at` diatur dan pembacaan halaman; spec menuliskan pengaturan ulang draft sebagai langkah penghubung (langkah 1, 8, 16, 28), termasuk untuk blok pertama karena `beforeEach` suite mereset draft sebelum langkah 1.
