---
id: TC-GS-IMPORT-E2E-053-commit-sebagian-tidak-mereset-umur-draft-job-kembali-draft-banner
title: "Commit Sebagian Tidak Mereset Umur Draft (Job Kembali Draft, Banner Tampil 24 Jam sejak Confirm Mapping Pertama)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-881
coverage:
  web: automated
---

# Commit Sebagian Tidak Mereset Umur Draft (Job Kembali Draft, Banner Tampil 24 Jam sejak Confirm Mapping Pertama)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec menjalankan commit nyata dan mengubah jam server; lihat `suite.md`.
- Akun: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client E, direset sebelum TC sesuai Kontrak Fixture R1): D-58 draft Brand 15 baris dari `brand-partial-15.csv`: #1-#9 `Nikon`, `Pentax`, `Olympus`, `Fujifilm`, `Leica`, `Sigma`, `Tamron`, `Hasselblad`, `Ricoh` (`pending`); #10 dan #11 `Brand Kembar` (`duplicate` antar-baris); #12 `Brand Kembar` (`pending`); #13 `Samsung` (`duplicate` terhadap sistem); #14 Brand Name 121 karakter huruf `A` dan #15 121 karakter huruf `B` (`error`). Hook umur draft D-76 varian 4: `created_at` = waktu server (dibaca lewat API seeding) dikurangi 23 jam 50 menit.
- Kemampuan teknis yang disediakan tim FE/BE: fixture jam server (jam server dimajukan 11 menit; hanya jam server karena umur draft dihitung di server dan dibaca saat Staging Table dibaca, tanpa countdown UI) dan hook umur draft. Commit dijalankan nyata di Client E.
- State global yang diubah dan dipulihkan: jam server (dipulihkan lewat langkah eksplisit dan hook `after`); hasil commit di Client E (hapus Brand hasil commit, hapus draft, reset penanda Banner Hasil Commit sesuai D-47).
- Menunggu: polling muat ulang tiap 5 detik dengan batas tunggu 2 menit, sesuai TC.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

1. Muat ulang halaman Import > Brand
2. Klik [Import (10)]
3. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
4. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
5. Verifikasi Staging Metric Cards: Total Rows 2, Ready to Import 0 (Disabled), Errors 2, Duplicates 0 (Disabled)
6. Verifikasi Unsaved Banner tidak tampil (job kembali `draft`, umur draft masih kurang dari 24 jam; commit sebagian tidak mereset umur)
7. Majukan jam server 11 menit (fixture jam server)
8. Muat ulang halaman Import > Brand
9. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
10. Verifikasi Staging Metric Cards tetap Total Rows 2
11. Pulihkan jam server ke waktu nyata (fixture jam server); reset Client E sesuai D-47

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji umur draft sebagai batas waktu dan job latar commit).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 3, 8 (muat ulang halaman); langkah 7 dan 11 (jam server).
- Langkah 6 (absence Unsaved Banner) memakai Banner Hasil Commit langkah 4 sebagai anchor positif.
- Pembagian TC lintas spec: TC-GS-IMPORT-877 sampai 880 ada di spec 051; TC-GS-IMPORT-882, 883, 885 di spec 052.
- Temuan untuk QA:
  - TC-GS-IMPORT-881 Expected c ("di bawah Banner Hasil Commit bila banner itu belum ditutup") bersyarat; spec menulis `Verifikasi` Unsaved Banner tampil tanpa langkah menutup Banner Hasil Commit, mengikuti alur TC.
  - Post Condition "entri ringkasan job tercatat di Changelog Import" tidak punya langkah observasi di TC; tidak diasersi.
