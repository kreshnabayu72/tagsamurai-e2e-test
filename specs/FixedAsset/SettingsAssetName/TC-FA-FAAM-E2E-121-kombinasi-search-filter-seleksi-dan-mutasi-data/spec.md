---
id: TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data
title: "Kombinasi: Tanpa Hasil Pulih, Seleksi Bertahan, serta Create dan Edit yang Tidak Cocok Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-385
  - TC-FA-FAAM-386
  - TC-FA-FAAM-387
  - TC-FA-FAAM-388
coverage:
  web: automated
---

# Kombinasi: Tanpa Hasil Pulih, Seleksi Bertahan, serta Create dan Edit yang Tidak Cocok Filter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10), `Ergonomic Chair` (Pre-setup #11), `Seed Item 01` (Pre-setup #15, UoM `Unit`).
- Data Dinamis: seed API di hook `before` untuk Asset Name `Edit Target Item {runId}-121` (salinan Pre-setup #13d, Code diisi seed); Asset Name `Pcs Filter Item {runId}-121` dibuat oleh TC-FA-FAAM-387 dengan Category `IT Equipment` (leaf lewat `[Select Category]`), TAG Type `QR`, Brand `Dell`, UoM `Pcs` (isian field wajib mengikuti TC-FA-FAAM-143). Hook `after` menghapus kedua Asset Name (nama hasil rename `Renamed Out {runId}-121` ikut dihapus).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-385: Kombinasi Search dan Filter tanpa hasil pulih saat salah satu dilepas
1. Ketik Search `Dell`, tekan Enter
2. Klik icon Filter, pilih UoM `Pcs`, lalu klik `[Apply]`
3. Verifikasi tabel kosong dengan `No results found`
4. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
5. Verifikasi tabel pulih menampilkan `Dell Latitude`
6. Klik `(←)` pada kotak Search
### TC-FA-FAAM-386: Seleksi checkbox bertahan saat Search dan Filter dibersihkan
7. Centang baris `Dell Latitude`
8. Ketik Search `Chair`, tekan Enter
9. Klik `(←)` pada kotak Search
10. Verifikasi baris `Dell Latitude` masih tercentang
11. Klik icon `×` pada Bulk Action Bar
### TC-FA-FAAM-388: Edit yang membuat record tidak cocok dengan Search aktif menghilangkannya dari tampilan
12. Ketik Search `Edit Target Item {runId}-121`, tekan Enter
13. Verifikasi baris `Edit Target Item {runId}-121` tampil di tabel
14. Klik `⋯` baris `Edit Target Item {runId}-121`, lalu klik `Edit`
15. Ubah Asset Name menjadi `Renamed Out {runId}-121`
16. Klik `[Save]`
17. Verifikasi toast `Success, asset name has been updated.`
18. Verifikasi baris `Renamed Out {runId}-121` tidak tampil di tabel karena tidak cocok dengan keyword Search
19. Klik `(←)` pada kotak Search
### TC-FA-FAAM-387: Create record yang tidak cocok dengan filter aktif tidak muncul di tabel terfilter
20. Klik icon Filter, pilih UoM `Unit`, lalu klik `[Apply]`
21. Verifikasi baris `Dell Latitude` (UoM `Unit`) tampil di tabel
22. Klik `[+ Asset Name]`
23. Isi Asset Name `Pcs Filter Item {runId}-121`
24. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
25. Pilih TAG Type `QR`
26. Pilih Brand `Dell`
27. Pilih UoM `Pcs`
28. Klik `[Submit]`
29. Verifikasi toast `Success, asset name has been created.`
30. Verifikasi baris `Pcs Filter Item {runId}-121` tidak tampil di tabel terfilter
31. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Urutan di spec: TC-FA-FAAM-385, 386, 388, lalu 387; blok yang mengubah data (Edit dan Create) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` pada Search, klik icon `×` pada Bulk Action Bar (seleksi satu baris tidak memunculkan `Unselect All`, hanya `Select All` dan icon `×`; langkah 11), serta `[Clear Field]` lalu `[Apply]` untuk membersihkan state antar blok (S-09).
- Search untuk menemukan baris target `Edit Target Item {runId}-121` dicatat sebagai langkah penghubung (R-16); TC memakai keyword `Edit Target`, spec memakai nama bersuffix yang memuat keyword itu supaya tidak menyentuh baris milik spec lain.
- Verifikasi toast `Success, asset name has been updated.` dan `Success, asset name has been created.` bukan Expected TC; keduanya anchor positif untuk asersi absence baris (bagian 8b butir 2) dan dicatat di sini (S-03).
- Verifikasi tabel kosong `No results found` pada TC-FA-FAAM-385 adalah anchor bahwa kombinasi menghasilkan 0 baris sebelum filter dilepas (S-03; TC menyebut "sehingga 0 hasil" pada langkah).
- Temuan untuk QA: nama literal `Pcs Filter Item` dan `Renamed Out` pada TC diberi suffix `{runId}-121` (S-12); field wajib Create selain UoM tidak disebut TC-FA-FAAM-387 sehingga spec memakai isian TC-FA-FAAM-143.
