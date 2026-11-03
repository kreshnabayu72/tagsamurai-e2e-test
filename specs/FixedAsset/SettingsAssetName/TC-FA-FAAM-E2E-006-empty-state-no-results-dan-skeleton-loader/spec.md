---
id: TC-FA-FAAM-E2E-006-empty-state-no-results-dan-skeleton-loader
title: "Empty State Katalog Kosong, Search Tanpa Hasil, dan Skeleton Loader"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-32
  - TC-FA-FAAM-33
  - TC-FA-FAAM-34
coverage:
  web: automated
---

# Empty State Katalog Kosong, Search Tanpa Hasil, dan Skeleton Loader

## Prerequisites

- Mode: FE+BE (backend nyata). TC-FA-FAAM-34 menahan respons list lewat `Spectra.intercept()` di atas backend nyata hanya untuk mengamati state Loading (bukan kegagalan yang dipaksakan).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): client utama dengan `MacBook Pro` (#12) sebagai satu-satunya Asset Name Category Locked (hitungan Needs Update 1); client tanpa Asset Name, tanpa Changelog, dan tanpa kategori (#16b) untuk TC-FA-FAAM-32 dengan aktor Total Control yang sama.
- Kemampuan teknis (disediakan tim FE/BE): berpindah client untuk aktor Total Control (langkah 12 dan 17) dan menahan respons list 3 detik lewat `Spectra.intercept()` (langkah 4). Hook `after` memulihkan sesi ke client utama dan melepas intercept.
- State global: tidak ada yang diubah selain client aktif sesi (dipulihkan langkah 17 dan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-33: Search tanpa hasil menampilkan empty state no results

1. Ketik Search `zzzzqq`, tekan Enter
2. Verifikasi ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.` tampil
3. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAM-34: Tabel menampilkan skeleton loader saat data dimuat

4. Tahan respons list 3 detik lewat intercept jaringan
5. Buka tab Asset Name lewat klik menu sidebar `Settings > Asset Master`
6. Verifikasi skeleton loader tampil selama menunggu respons
7. Verifikasi notice Category Locked tidak tampil selama Loading awal
8. Tunggu intercept 3 detik selesai dan respons list diterima
9. Verifikasi baris tampil pada tabel
10. Verifikasi notice `1 asset name needs a category update.` tampil
11. Lepas intercept respons list

### TC-FA-FAAM-32: Katalog kosong menampilkan empty state genuinely

12. Ganti client ke client tanpa Asset Name (Pre-setup #16b) dengan aktor Total Control
13. Buka tab Asset Name lewat klik menu sidebar `Settings > Asset Master`
14. Verifikasi ilustrasi dengan Title `No asset names yet` dan Description `Get started by creating your first asset name.` tampil
15. Verifikasi tidak ada tombol CTA di dalam empty state
16. Verifikasi `[+ Asset Name]` tetap tampil di toolbar
17. Ganti client kembali ke client utama

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 33, 34, 32. TC-32 diletakkan terakhir karena berpindah client (S-10); hasilnya TC-33 dan TC-34 berjalan di client utama yang berisi katalog.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 3 (menutup input Search), langkah 5 dan 13 (membuka tab Asset Name ulang sesuai Langkah uji "Buka tab Asset Name"), langkah 8 (menunggu respons ditahan), langkah 11 (melepas intercept segera, S-09), langkah 12 dan 17 (ganti client eksplisit).
- Langkah 7 (absence state sementara) ditulis segera setelah pemicu dan sebelum asersi artefak; skeleton loader (langkah 6) menjadi anchor positifnya (8b butir 5 dan 11).
- Langkah 16 mengasersi `[+ Asset Name]` di toolbar sebagai bagian dari Expected TC-32 c.
- Temuan untuk QA:
  - TC-32 tidak menyebut mekanisme berpindah ke client tanpa Asset Name (Pre-setup #16b) maupun akun yang dipakai; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-34 Langkah 1 menunda respons list 3 detik tanpa menyebut endpoint; spec tidak menulis endpoint karangan.
