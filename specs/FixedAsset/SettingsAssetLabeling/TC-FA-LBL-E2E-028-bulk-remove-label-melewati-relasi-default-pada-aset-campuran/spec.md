---
id: TC-FA-LBL-E2E-028-bulk-remove-label-melewati-relasi-default-pada-aset-campuran
title: "Bulk Remove Label: relasi default dilewati dan relasi manual terlepas pada aset campuran"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - E-FALB-06
  - F-FALB-11.k1
  - FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d
coverage:
  web: automated
---

# Bulk Remove Label: relasi default dilewati dan relasi manual terlepas pada aset campuran

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji, semuanya bersuffix `{runId}-028`, dibuat lewat API di hook `before` dan dihapus di hook `after` (aset, Asset Name, lalu label):
  - `DU-53`: label seed (`Seed-{runId}-028`), Default Label dari Asset Name `DU-27`; ditempel manual pada aset manual `DU-28`.
  - `DU-27`: Asset Name yang memakai label seed `DU-53` sebagai Default Label; aset default `DU-28` adalah aset Active dari Asset Name itu, sehingga memegang relasi `default` untuk label `DU-53`.
  - `DU-28`: himpunan aset untuk Bulk Remove campuran: aset default `DU-28` (relasi `default` untuk label `DU-53`) dan aset manual `DU-28` (aset Active dengan label `DU-53` ditempel manual).
  - `DU-26`: seluruh aset Active spec ini (aset default `DU-28` dan aset manual `DU-28`, dua aset).
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, Asset Name, dan aset, disediakan tim FE/BE. Halaman Asset List, Asset Detail, dan dialog Remove Label dimiliki modul `asset/`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### E-FALB-06: Bulk Remove Label pada aset campuran default dan manual

1. Buka Asset List modul `asset/` yang memuat aset Active milik spec `DU-26`
2. Ketik Search himpunan aset `DU-28`, tekan Enter
3. Centang baris aset default `DU-28` dan baris aset manual `DU-28`
4. Klik `[🏷 Remove Label]`, pilih label `DU-53`, dan konfirmasi aksi pada dialog milik modul `asset/`
5. Tunggu aksi selesai
6. Buka Asset Detail aset manual `DU-28`
7. Verifikasi nama aset manual `DU-28` tampil pada Asset Detail
8. Verifikasi chip label `DU-53` tidak tampil pada aset manual `DU-28`
9. Buka Asset Detail aset default `DU-28`
10. Verifikasi chip label `DU-53` masih tampil pada aset default `DU-28`

### F-FALB-11.k1: Pelepasan relasi default ditolak

11. Verifikasi chip label `DU-53` tetap menempel pada aset default `DU-28` setelah Remove Label

### FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d: Pelepasan label default dari level aset ditolak

12. Verifikasi ikon `[✕]` tidak tampil pada chip label `DU-53` di Asset Detail aset default `DU-28`

## Notes

- Langkah penghubung: langkah 1 sampai 4 menyiapkan Bulk Remove; langkah 2 adalah Search untuk menemukan baris target (R-23) dan tetap berisi saat kembali ke Asset List (bagian 8b butir 9); langkah 5 menunggu aksi tulis selesai sebelum berpindah surface; langkah 6 dan 9 membuka Asset Detail dari Asset List modul `asset/`.
- Anchor absence: nama aset tampil pada Asset Detail (langkah 7) mendahului asersi chip `DU-53` tidak tampil (langkah 8); chip `DU-53` tampil pada aset default (langkah 10) mendahului asersi ikon `[✕]` tidak tampil (langkah 12).
- Pembagian klausa lintas spec: `F-FALB-11.k1` dan `FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d` dikutip spec 012 dan spec ini; spec ini mengasersi sisi UI (Bulk Remove melewati relasi default), spec 012 mengasersi sisi permintaan langsung ke server (penolakan oleh server). Sisi UI `E-FALB-05` (ikon `[✕]` tidak tampil di Asset Detail) ada di spec 010.
- Dipakai sebagai keadaan yang disyaratkan aturan, tidak diasersi: relasi `default` pada aset default `DU-28` dibuat oleh seeding lewat template Asset Name `DU-27`.
- Temuan PRD: dialog `[🏷 Remove Label]`, Asset List, dan Asset Detail dimiliki PRD `asset/` dan tidak dinyatakan di PRD ini, sehingga langkah 1 sampai 4 hanya menyebut nama tombol dari §3.5; teks toast sukses `E-FALB-06` mengikuti `AST-LOGIC-04` (PRD `asset/`) dan tidak ada teksnya di PRD ini, sehingga toast itu tidak diasersi.
