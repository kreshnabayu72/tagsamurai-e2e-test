---
id: TC-FA-LBL-E2E-011-penugasan-manual-label-dan-refleksi-nama-di-aset
title: "Penugasan manual label pada aset dan refleksi perubahan nama label"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB-LOGIC-04e
  - E-FALB-11
coverage:
  web: automated
---

# Penugasan manual label pada aset dan refleksi perubahan nama label

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-26` (satu aset Active milik spec, bersuffix `{runId}-011`); `DU-49` (label seed milik spec bernama awal `Urgent-{runId}-011`); `DU-30` (nama baru `Critical-{runId}-011` yang diketik pada Edit di langkah 12). Aset dan label seed dibuat lewat API di hook `before` dan dihapus di hook `after` (aset lebih dulu, lalu label).
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan aset, disediakan tim FE/BE. Halaman Asset List dan Asset Detail dimiliki modul `asset/`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB-LOGIC-04e: Relasi manual ditugaskan pengguna dari Asset Detail dan bebas dilepas

1. Buka Asset Detail aset `DU-26` dari Asset List modul `asset/`
2. Pilih label seed (nama awal `DU-49`) dari dropdown label pada Asset Detail
3. Verifikasi chip label seed tampil dengan ikon `[✕]` pada Asset Detail aset `DU-26`
4. Klik `[✕]` pada chip label seed
5. Verifikasi nama aset `DU-26` tampil pada Asset Detail
6. Verifikasi chip label seed tidak tampil pada Asset Detail aset `DU-26`
7. Pilih label seed (nama awal `DU-49`) dari dropdown label pada Asset Detail
8. Tunggu aksi selesai

### E-FALB-11: Perubahan nama label terefleksi pada aset yang memiliki label

9. Buka Fixed Asset > Settings > Asset Master > tab Labels
10. Ketik Search label seed (nama awal `DU-49`), tekan Enter
11. Klik `[⋯]` pada baris label seed, pilih `Edit`
12. Ganti isi field Label Name dengan `DU-30`
13. Klik `[Save]`
14. Tunggu aksi selesai
15. Buka Asset Detail aset `DU-26` dari Asset List modul `asset/`
16. Verifikasi chip label pada Asset Detail aset `DU-26` menampilkan teks `DU-30`
17. Verifikasi chip label dengan nama awal `DU-49` tidak tampil pada Asset Detail aset `DU-26`

## Notes

- Langkah penghubung: langkah 1 dan 15 membuka Asset Detail dari Asset List modul `asset/`; langkah 7 menempelkan ulang label sebagai keadaan yang dibutuhkan blok `E-FALB-11`; langkah 8 dan 14 menunggu aksi tulis selesai sebelum berpindah surface; langkah 9 adalah navigasi umum; Search label seed (langkah 10) menemukan baris target; klik `[⋯]` membuka menu baris.
- Anchor absence: nama aset `DU-26` tampil (langkah 5) mendahului asersi chip tidak tampil (langkah 6); chip label `DU-30` tampil (langkah 16) mendahului asersi chip nama awal tidak tampil (langkah 17).
- Temuan PRD: dialog `[🏷 Add/Remove Label]`, Asset List, dan Asset Detail dimiliki PRD `asset/` dan tidak dinyatakan di PRD ini, sehingga penugasan lewat Bulk Add Label (disebut `FALB-LOGIC-04e`) tidak diasersi dan hanya jalur Asset Detail yang ditulis.
