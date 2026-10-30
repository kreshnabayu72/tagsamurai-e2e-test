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
- Data Dinamis (Client C, dibuat ulang lewat skrip fixture sebelum tiap TC): D-77 draft Brand 6 baris `pending` dari `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp). `brand-12.csv` (D-01, 12 baris) untuk TC-GS-IMPORT-880. General Settings Client C: format tanggal `dd/MM/yy` (TC-GS-IMPORT-878).
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

1. Muat ulang halaman Import > Brand dalam 30 detik setelah `created_at` diatur (varian 2)
2. Verifikasi Staging Table menampilkan 6 baris `pending`
3. Verifikasi Staging Metric Cards Total Rows 6 (Active)
4. Verifikasi footer `[Import (6)]` Enabled
5. Verifikasi Unsaved Banner tidak tampil
6. Verifikasi tidak ada tombol `[Discard]` di halaman

### TC-GS-IMPORT-878: Draft berumur tepat 24 jam

7. Atur ulang draft D-77 dengan `created_at` tepat 24 jam sebelum waktu server (varian 3)
8. Muat ulang halaman Import > Brand
9. Verifikasi Staging Table menampilkan 6 baris `pending`
10. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
11. Verifikasi [Date] berisi tanggal satu hari sebelum hari uji dengan format `dd/MM/yy`
12. Arahkan kursor ke `[Discard]` pada Unsaved Banner
13. Verifikasi `[Discard]` Enabled
14. Verifikasi `[Discard]` tanpa tooltip

### TC-GS-IMPORT-879: Halaman terbuka tidak menerima push saat umur melewati 24 jam

15. Atur ulang draft D-77 dengan umur 23 jam 50 menit (varian 4)
16. Muat ulang halaman Import > Brand
17. Verifikasi Staging Metric Cards Total Rows 6 (Active)
18. Verifikasi Unsaved Banner tidak tampil
19. Majukan jam server 11 menit (fixture jam server)
20. Tunggu 30 detik tanpa berinteraksi dengan halaman
21. Verifikasi footer `[Import (6)]` Enabled
22. Verifikasi Unsaved Banner tetap tidak tampil (halaman tidak menerima push saat umur draft melewati 24 jam)
23. Muat ulang halaman Import > Brand
24. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
25. Verifikasi footer `[Import (6)]` Enabled
26. Pulihkan jam server ke waktu nyata (fixture jam server)

### TC-GS-IMPORT-880: Edit baris dan Append tidak mereset umur draft

27. Atur ulang draft D-77 dengan umur 23 jam 50 menit (varian 4)
28. Muat ulang halaman Import > Brand
29. Klik `⋯` pada baris #1
30. Pilih Edit
31. Ubah Brand Name baris #1 dari `Nikon` menjadi `Nikon Corporation`
32. Klik `[Save]`
33. Verifikasi baris #1 tampil dengan Brand Name `Nikon Corporation`
34. Klik [Upload File] di toolbar
35. Pilih berkas `brand-12.csv` di file picker
36. Klik `[Append Records]`
37. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
38. Verifikasi toast sukses: "Success, row has been added."
39. Muat ulang halaman Import > Brand
40. Verifikasi Staging Metric Cards Total Rows 18 (Active)
41. Verifikasi Unsaved Banner tidak tampil karena umur draft masih kurang dari 24 jam (edit dan Append tidak mereset umur)
42. Majukan jam server 11 menit (fixture jam server)
43. Muat ulang halaman Import > Brand
44. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil (24 jam sejak `[Confirm Mapping]` pertama, bukan sejak edit atau Append)
45. Verifikasi Staging Metric Cards Total Rows 18 (Active) dan Ready to Import 18
46. Pulihkan jam server ke waktu nyata (fixture jam server) dan reset Client C ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji umur draft 24 jam sebagai batas waktu).
- Spec memuat 46 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (hook umur draft D-76 dan jam server), tiap blok memakai draft D-77 yang dibuat ulang dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 16, 23, 28, 39, 43 (muat ulang halaman); langkah 7, 15, 27 (mengatur ulang draft D-77); langkah 20 (jeda nyata 30 detik); langkah 26 dan 46 (memulihkan jam server dan draft).
- Anchor positif untuk absence (konvensi 8b butir 2, S-03): langkah 17 (Metric Cards Total Rows 6) mendahului langkah 18, langkah 21 (footer `[Import (6)]`) mendahului langkah 22, langkah 40 (Metric Cards Total Rows 18) mendahului langkah 41; langkah 5 didahului langkah 2 sampai 4.
- Pembagian TC lintas spec: TC-GS-IMPORT-881 (commit sebagian tidak mereset umur) ada di spec 053; TC-GS-IMPORT-882, 883, dan 885 (draft baru mulai dari umur 0) ada di spec 052.
- Temuan untuk QA:
  - TC-GS-IMPORT-878 tidak merujuk acuan T0 untuk "tepat 24 jam"; spec menghitung dari waktu server yang dibaca saat seeding.
  - TC-GS-IMPORT-877, 878, dan 879 tidak menyebut urutan antara `created_at` diatur dan pembacaan halaman; spec menuliskan pengaturan ulang draft sebagai langkah penghubung.
