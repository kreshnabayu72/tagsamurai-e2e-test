---
id: TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman
title: "Retensi State Search, Sort, Filter, dan Halaman (Pindah Tab, F5, Sidebar, Popup Detail)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-6
  - TC-FA-FAAM-7
  - TC-FA-FAAM-8
  - TC-FA-FAAM-9
coverage:
  web: automated
---

# Retensi State Search, Sort, Filter, dan Halaman (Pindah Tab, F5, Sidebar, Popup Detail)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10), `Ergonomic Chair` (#11), dan `Seed Item 01` s.d. `Seed Item 30` (#15, UoM `Unit`, Total Asset 0) sehingga hasil Search `Seed` memuat lebih dari satu halaman. Keyword dan nilai filter: Search `Latitude`, `Seed`, `Dell`, `Chair`; Sort Code Ascending; Sort Total Asset Descending; Filter UoM `Unit`; halaman 2.
- Pemulihan preferensi: spec tidak menyimpan konfigurasi kolom. State Search, Sort, Filter, dan halaman direset oleh klik menu sidebar (langkah 8, 19, dan 27) dan oleh pembukaan halaman hook `beforeEach`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-6: Pindah tab Asset Name ke Labels lalu kembali memulihkan state Search dan Sort tab Asset Name

1. Ketik Search `Latitude`, tekan Enter
2. Klik header kolom Code satu kali (Ascending)
3. Klik tab `Labels`
4. Klik tab `Asset Name`
5. Verifikasi Search box berisi `Latitude`
6. Verifikasi hanya baris `Dell Latitude` tampil
7. Verifikasi kolom Code menampilkan indikator Ascending
8. Klik menu sidebar `Settings > Asset Master` untuk mereset Search dan Sort

### TC-FA-FAAM-7: Refresh F5 mempertahankan Search, Sort, Filter, dan halaman aktif

9. Ketik Search `Seed`, tekan Enter
10. Klik header Total Asset dua kali (Descending)
11. Buka Filter, pilih UoM `Unit`, klik `[Apply]`
12. Pindah ke halaman 2
13. Tekan F5
14. Verifikasi Search box masih berisi `Seed`
15. Verifikasi header Total Asset masih menampilkan indikator Descending
16. Verifikasi Filter UoM `Unit` masih ter-Apply (ikon Filter berbadge titik)
17. Verifikasi halaman aktif tetap halaman 2
18. Verifikasi jumlah baris per halaman tetap 10
19. Klik menu sidebar `Settings > Asset Master` untuk mereset Search, Sort, Filter, dan halaman

### TC-FA-FAAM-9: Menutup Popup Detail tidak mereset Search, Filter, Sort, dan halaman List

20. Ketik Search `Chair`, tekan Enter
21. Klik nama `Ergonomic Chair`
22. Klik icon `[✕]` Popup Detail
23. Verifikasi Popup Detail tertutup
24. Verifikasi Search box masih berisi `Chair`
25. Verifikasi hanya baris `Ergonomic Chair` tampil

### TC-FA-FAAM-8: Klik ulang menu sidebar Asset Master mereset Search dan Filter ke default

26. Ganti isi kotak search dengan `Dell`, tekan Enter
27. Klik menu sidebar `Settings > Asset Master`
28. Verifikasi Search box kosong
29. Verifikasi seluruh baris tampil kembali (baris selain `Dell Latitude` tampil)
30. Verifikasi Sort kembali ke default Asset Name A-Z

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 6, 7, 9, 8. TC-8 diletakkan terakhir karena kotak Search sudah berisi `Chair` dari TC-9, sehingga langkah 26 mengganti isi kotak (8b butir 9).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 8 dan 19 (klik menu sidebar mereset Search, Sort, Filter, dan halaman sebelum TC berikutnya, S-09; klik sidebar mereset state sesuai konvensi bagian 4).
- Langkah 1, 9, 20 mencari baris target lewat Search sesuai langkah uji TC (R-16).
- Langkah 6 dan 25 ("hanya baris ... tampil") memakai baris yang disebut sendiri sebagai pembanding positif; langkah 29 memakai baris selain `Dell Latitude` sebagai pembanding bahwa tabel tidak lagi tersaring.
- Langkah 17 (halaman 2) bergantung pada hasil Search `Seed` yang memuat 30 baris (#15) dengan ukuran halaman 10.
- Temuan untuk QA:
  - TC-8 Expected a "seluruh baris tampil" tidak menyebut jumlah; spec mengasersi bahwa baris selain `Dell Latitude` tampil kembali.
  - TC-8 judul menyebut "Search dan Filter" sedangkan Langkah uji dan Expected hanya memuat Search dan Sort; spec mengikuti Langkah uji dan Expected.
  - TC-6, 7, 8, 9 tidak menyebut sumber persistensi state; spec tidak mengasumsikan mekanisme penyimpanan (localStorage atau lainnya).
