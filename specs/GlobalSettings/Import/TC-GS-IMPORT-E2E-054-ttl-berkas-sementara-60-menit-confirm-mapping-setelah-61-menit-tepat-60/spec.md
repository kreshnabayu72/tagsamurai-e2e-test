---
id: TC-GS-IMPORT-E2E-054-ttl-berkas-sementara-60-menit-confirm-mapping-setelah-61-menit-tepat-60
title: "TTL Berkas Sementara 60 Menit: Confirm Mapping Setelah 61 Menit atau Tepat 60 Menit Memunculkan Banner Kegagalan dan Reupload File Memulihkan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-82
  - TC-GS-IMPORT-823
coverage:
  web: automated
---

# TTL Berkas Sementara 60 Menit: Confirm Mapping Setelah 61 Menit atau Tepat 60 Menit Memunculkan Banner Kegagalan dan Reupload File Memulihkan

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah jam server; lihat `suite.md`.
- Akun: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data: `brand-12.csv` (D-01; header `Brand Name`, 12 baris). Client C tanpa draft Tab Brand sebelum tiap TC (Kontrak Fixture R1).
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi):
  - Fixture jam server (TC-GS-IMPORT-82): jam server dimajukan 61 menit sejak upload; hanya jam server karena TTL berkas sementara dihitung murni di server dan tidak diamati lewat UI. Jam dipulihkan lewat langkah eksplisit di akhir blok dan di hook `after`.
  - Hook uji umur berkas sementara (TC-GS-IMPORT-823): umur berkas sementara hasil upload diatur absolut menjadi tepat 60 menit (batas eksak, bukan geser relatif); acuan T0 dibaca dari waktu terbit berkas sementara lewat API seeding.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset (R1) setelah tiap blok; jam server dikembalikan ke waktu nyata.

## Test Steps

### TC-GS-IMPORT-82: Berkas sementara berusia lebih dari 60 menit

1. Klik [Upload File]
2. Pilih berkas `brand-12.csv` di file picker
3. Tunggu aksi selesai (permintaan mendapat respons)
4. Majukan jam server 61 menit sejak upload (fixture jam server)
5. Klik [Confirm Mapping]
6. Verifikasi Modal Column Mapping tetap terbuka
7. Verifikasi Error Banner generik dengan header "Failed to process brand-12.csv. Please try uploading again." tampil
8. Verifikasi Error Banner tanpa rincian per-rule
9. Verifikasi Error Banner tanpa link download
10. Klik [Reupload File]
11. Pilih berkas `brand-12.csv` di file picker
12. Klik [Confirm Mapping]
13. Verifikasi modal tertutup
14. Verifikasi Staging Table menampilkan 12 baris berstatus `pending`
15. Verifikasi Pagination "Showing 1 - 10 of 12 items"
16. Pulihkan jam server ke waktu nyata (fixture jam server); reset Client C ke tanpa draft Tab Brand
17. Muat ulang halaman Import > Brand

### TC-GS-IMPORT-823: Berkas sementara berusia tepat 60 menit

18. Klik [Upload File]
19. Pilih berkas `brand-12.csv` di file picker
20. Tunggu aksi selesai (permintaan mendapat respons)
21. Atur umur berkas sementara hasil upload menjadi tepat 60 menit lewat hook uji (fixture umur berkas sementara)
22. Klik [Confirm Mapping]
23. Verifikasi Modal Column Mapping tetap terbuka
24. Verifikasi Error Banner generik dengan header "Failed to process brand-12.csv. Please try uploading again." tampil
25. Verifikasi Error Banner tanpa rincian per-rule
26. Verifikasi Error Banner tanpa link download
27. Klik [Reupload File]
28. Pilih berkas `brand-12.csv` di file picker
29. Klik [Confirm Mapping]
30. Verifikasi modal tertutup
31. Verifikasi Staging Table menampilkan 12 baris berstatus `pending`
32. Verifikasi Pagination "Showing 1 - 10 of 12 items"
33. Reset Client C ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji TTL berkas sementara sebagai batas waktu).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan 33 (pemulihan jam server dan reset draft); langkah 17 (muat ulang halaman Import > Brand); langkah 3 dan 20 (Tunggu aksi selesai: menunggu unggahan diproses sebelum fixture mengubah jam server atau umur berkas; penanda permintaan mendapat respons).
- Pembersihan state antar blok (S-03): langkah 17 memuat ulang halaman sesudah fixture membuang draft (langkah 16), sehingga langkah 18 [Upload File] pada blok TC-GS-IMPORT-823 berjalan pada halaman tanpa draft (tanpa Staging Table dan tanpa dialog Append).
- Pembagian TC lintas spec: batas eksak tepat 60 menit (TC-GS-IMPORT-823) dan lebih dari 60 menit (TC-GS-IMPORT-82) berada di spec ini; tidak ada spec lain yang menguji TTL berkas sementara.
- Temuan untuk QA:
  - TC-GS-IMPORT-823 Expected a ("Modal Column Mapping tetap terbuka") dan b (Error Banner) dinomori pada langkah 4 dan 5, sedangkan TC-GS-IMPORT-82 menggabungkannya di langkah 5; spec memetakan keduanya ke langkah setelah klik [Confirm Mapping].
  - TC-GS-IMPORT-823 tidak menyebut cara membaca waktu terbit berkas sementara; spec menuliskannya sebagai kemampuan hook uji yang disediakan tim FE/BE.
  - Penanda selesai untuk langkah 3 dan 20 (sesudah pemilihan berkas `brand-12.csv`, sebelum fixture jam atau umur berkas) tidak ada di TC; spec memakai "permintaan mendapat respons" sebagai penanda tunggu tanpa hasil UI.
