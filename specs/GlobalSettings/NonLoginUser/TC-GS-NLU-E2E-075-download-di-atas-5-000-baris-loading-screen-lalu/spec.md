---
id: TC-GS-NLU-E2E-075-download-di-atas-5-000-baris-loading-screen-lalu
title: "Download di Atas 5.000 Baris: Loading Screen lalu Berkas Terunduh"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-482
coverage:
  web: automated
---

# Download di Atas 5.000 Baris: Loading Screen lalu Berkas Terunduh

## Prerequisites

- Mode: FE+BE (backend nyata). Spec memakai Client PT Volume Besar dengan 5.001 Non-Login User.
- Aktor: Total Control pada Client PT Volume Besar (Pre-setup No. 15 dan 18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.GS_VOLUME_TC_PASSWORD` (nama env baru yang diusulkan; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 18: Client PT Volume Besar memiliki 5.001 Non-Login User (`Volume 0001` sampai `Volume 5001`) yang dibuat lewat seed atau API sebelum run, dan Master Data Count Limit gabungan ≥ 5.001. Spec tidak membuat atau menghapus data. N = 5.001 berasal dari seeding.
- Kemampuan teknis: membaca berkas CSV yang terunduh dan menghitung jumlah baris data di bawah header (hanya nama berkas dan jumlah baris; isi sel tidak diasersi, bagian 3 prinsip 13f).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-482: Download di atas 5.000 baris

1. Klik icon `Download` pada Table Tools
2. Klik `Download as CSV`
3. Verifikasi loading screen tampil sampai berkas siap
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas langsung terunduh
6. Verifikasi nama berkas `Non-Login-Users.csv`
7. Buka berkas yang terunduh
8. Verifikasi berkas memuat 5.001 baris data di bawah header

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi absence toast sukses diletakkan segera setelah pemicu `Download as CSV` dan sebelum asersi berkas terunduh (bagian 8b butir 11); loading screen yang tampil menjadi anchor positif.
- Temuan untuk QA:
  - Email dan nama env password Total Control Client PT Volume Besar tidak tertulis di Pre-setup TC; `GS_VOLUME_TC_PASSWORD` adalah nama baru yang diusulkan dan akunnya disediakan tim FE.
  - TC-482 Langkah 3 "Buka file" tidak menyebut cara membaca berkas; spec memakai kemampuan baca berkas CSV (disediakan tim FE/BE) hanya untuk nama dan jumlah baris.
