---
id: TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog
title: "Resilience Baca: Error Load List, Popup Detail, Changelog, dan Baca Setelah Tulis"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-35
  - TC-FA-FAAM-314
  - TC-FA-FAAM-468
  - TC-FA-FAAM-644
coverage:
  web: automated
---

# Resilience Baca: Error Load List, Popup Detail, Changelog, dan Baca Setelah Tulis

## Prerequisites

- Mode: FE+BE (backend nyata). Respons dipaksa gagal 5xx lewat `Spectra.intercept()` di atas backend nyata (intercept parsial, bukan mock seluruh API); asersi menyangkut state UI dan record yang dibuat di server (langkah 26 dan 27).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `MacBook Pro` (#12) sebagai satu-satunya Asset Name Category Locked pada client utama (hitungan Needs Update 1); `Dell Latitude` (#10, Total Asset 42, 3 Linked Custom Fields dari #26 dan #27); Changelog berisi entri contoh PRD §4.1 Modal Changelog Example Data (#28).
- Data Dinamis (suffix `{runId}-017`): Asset Name `Resilience Item {runId}-017` dibuat TC-FA-FAAM-644 (langkah 26) dengan Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit` (master data Pre-setup #22 s.d. #24); dihapus hook `after` lewat seed API.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx pada request list Asset Name (langkah 1 dan 28), data tab Total Assets Popup Detail (langkah 12), dan Changelog (langkah 18). Intercept dilepas segera sesudah pemicu (langkah 6, 16, 22, 31, S-09); hook `after` melepas intercept yang tersisa.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-35: Gagal memuat list menampilkan alert error load dan bukan empty state

1. Paksa respons list gagal 5xx lewat intercept jaringan
2. Buka tab Asset Name lewat klik menu sidebar `Settings > Asset Master`
3. Verifikasi Alert `Unable to load this data.` dengan tombol `[Try Again]` tampil
4. Verifikasi empty state tidak tampil
5. Verifikasi Notice Category Locked tidak tampil selama Error Load
6. Hapus intercept respons list
7. Klik `[Try Again]`
8. Verifikasi baris data tampil pada tabel
9. Verifikasi notice `1 asset name needs a category update.` tampil

### TC-FA-FAAM-314: Popup Detail gagal memuat tab menampilkan alert inline dengan header dan close tetap

10. Ketik Search `Dell Latitude`, tekan Enter
11. Klik nama `Dell Latitude`
12. Paksa respons data tab Total Assets gagal lewat intercept
13. Klik tab `Total Assets (42)`
14. Verifikasi Alert `Unable to load this data.` dengan `[Try Again]` tampil inline
15. Verifikasi header dan `[✕]` Popup Detail tetap
16. Hapus intercept data tab Total Assets
17. Klik `[✕]` pada Popup Detail

### TC-FA-FAAM-468: Gagal memuat Changelog menampilkan alert inline dengan header dan close tetap

18. Paksa respons Changelog gagal lewat intercept
19. Klik icon Changelog
20. Verifikasi Alert `Unable to load this data.` dengan `[Try Again]` tampil inline
21. Verifikasi header dan `[✕]` Modal Changelog tetap
22. Hapus intercept respons Changelog
23. Klik `[✕]` pada Modal Changelog

### TC-FA-FAAM-644: Kegagalan baca setelah aksi tulis tetap menampilkan error load dan bukan empty state

24. Klik `[+ Asset Name]`
25. Isi field wajib: Asset Name `Resilience Item {runId}-017`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
26. Klik `[Submit]`
27. Verifikasi toast `Success, asset name has been created.`
28. Paksa respons list gagal 5xx lewat intercept jaringan
29. Muat ulang halaman dengan F5
30. Verifikasi Alert `Unable to load this data.` dengan `[Try Again]` tampil
31. Hapus intercept respons list

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAM-837 (resilience baca Popup Detail progres kepatuhan) berada di spec 022.
- Urutan TC di spec: 35, 314, 468, 644 (urutan menaruh TC yang membuat data di akhir, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2 (membuka tab setelah intercept terpasang sesuai Langkah uji "Buka tab Asset Name"), langkah 6, 16, 22, 31 (melepas intercept segera), langkah 7 (klik `[Try Again]` sesuai Langkah uji), langkah 10 (Search untuk menemukan baris target, R-16), langkah 17 dan 23 (menutup popup dan modal), langkah 29 (muat ulang sesuai Langkah uji "refresh").
- Langkah 4 (empty state tidak tampil) dan langkah 5 (notice tidak tampil selama Error Load) ditulis segera setelah pemicu dan memakai Alert pada langkah 3 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Langkah 27 (toast sukses Create) adalah anchor positif bahwa Create sukses sebelum list dipaksa gagal; TC-644 tidak menuliskan Expected untuk Create tersebut.
- Temuan untuk QA:
  - TC-644 Langkah 1 "Create Asset Name sukses" tidak menyebut nilai field; spec memakai Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit` dan nama bersuffix `{runId}-017` (S-12).
  - TC-644 Expected hanya menyebut Alert; judul TC menyebut "bukan empty state"; spec tidak menambahkan asersi empty state tidak tampil pada TC-644 (hanya pada TC-35 yang memuatnya di Expected).
  - TC-35, TC-314, TC-468, dan TC-644 tidak menyebut endpoint yang di-intercept; spec tidak menulis endpoint karangan dan mengatur intercept per permukaan (list, data tab Total Assets, Changelog).
  - TC-35 Expected c dan TC-314 bergantung pada Total Asset 42 dan hitungan Needs Update 1 yang bisa berubah bila spec lain mengubah fixture #10 dan #12; spec ini hanya membaca.
