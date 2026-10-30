---
id: TC-GS-TAG-E2E-080-download-registri-lebih-5000-baris
title: "Download Registri lebih dari 5.000 Baris: Loading Screen sampai Berkas Siap"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-346
coverage:
  web: automated
---

# Download Registri lebih dari 5.000 Baris: Loading Screen sampai Berkas Siap

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Yusuf Rahman (Pre-setup TC, Client Large) `totalControl_automated_qaLarge@qwertysystem.net`; kredensial `Spectra.env.GS_TC_LARGE_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; tercantum di bagian Kredensial `suite.md` untuk didaftarkan pemilik repositori; password tidak ditulis di spec atau fixture). Login sekali di hook `before` sebagai akun default spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Data Pre-setup: Client Large memuat 5.200 tag RFID – Object TAG (fixture backend, Pre-setup TC). Registri Client Large tidak diubah dan terpisah dari Seed Registri A. Fixture di-seed atau direset idempotent oleh tim FE/BE (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Spec hanya membaca data.
- Kelas harness e (volume lebih dari 5.000 baris) dan f (binary buffer: nama dan isi berkas) dalam satu spec karena satu TC.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta; spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` untuk akun Client Large dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): berkas unduhan dihapus dan sesi dikembalikan ke akun default suite.
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser ke direktori bersih dan membaca jumlah baris data CSV (5.200 baris); mengamati loading screen selama unduhan (bila respons terlalu singkat untuk diamati, memperlambat respons export lewat `Spectra.intercept()` tanpa mengubah isinya); membaca state job background BE (kemampuan "disediakan tim FE/BE", tanpa mengarang endpoint, hanya untuk butir Expected TC yang menyebutnya; S-11).

## Test Steps

### TC-GS-TAG-346: Download registri lebih dari 5.000 baris

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi loading screen tampil
4. Verifikasi tidak ada toast sukses
5. Verifikasi tidak ada notifikasi
6. Verifikasi loading screen tampil sampai berkas siap
7. Verifikasi berkas `All-TAGs` langsung terunduh setelah loading screen hilang
8. Verifikasi berkas berisi 5.200 baris data
9. Verifikasi tidak ada job background

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Panjang spec: 9 langkah, di bawah ambang sekitar 35 langkah.
- Absence toast sukses dan notifikasi (langkah 4 dan 5) diletakkan segera setelah pemicu, saat loading screen tampil (langkah 3 sebagai anchor positif), dan sebelum asersi berkas (bagian 8b butir 11). Absence job background (langkah 9) mengandalkan kemampuan baca state BE yang disediakan tim FE/BE dan dibuktikan oleh berkas yang sudah terunduh (langkah 7 sebagai anchor positif).
- Temuan untuk QA:
  - TC-GS-TAG-346 butir b ("Tidak ada job background maupun notifikasi") tidak memberi cara mengamati job background lewat UI; spec memakai kemampuan baca state BE yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-TAG-346 butir a menyebut berkas `All-TAGs` tanpa ekstensi; pilihan format CSV pada langkah 2 menentukan ekstensi `.csv`. Spec mengasersi nama dasar `All-TAGs` saja.
  - TC-GS-TAG-346 tidak menyebut apakah "5.200 baris data" termasuk baris header; spec memakai 5.200 baris data tanpa header (sejalan dengan TC-GS-TAG-239).
  - TC-GS-TAG-346 tidak menyebut durasi minimum loading screen; pengamatannya bergantung pada kecepatan respons environment.
  - Akun Client Large memakai env var `GS_TC_LARGE_PASSWORD` yang belum terdaftar di `spectra.config.ts` dan `.env.example`.
