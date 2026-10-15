---
id: TC-AC-PP-E2E-039-sort-tie-breaker-published-at-sama
title: "Sort Tie-Breaker: Dua Versi dengan Published At Sama Diurutkan Menurut Nomor Versi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-121
coverage:
  web: automated
---

# Sort Tie-Breaker: Dua Versi dengan Published At Sama Diurutkan Menurut Nomor Versi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat T, yaitu Version 1 (15 Jan 2026), serta Version 2 dan Version 3 dengan Published At identik pada detik yang sama (10 Aug 2026). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat T dengan Published At identik pada detik yang sama.
- State UI yang diubah spec dan dipulihkan: sort Published At Oldest First dikembalikan ke netral di akhir.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-121: Dua versi dengan Published At sama diurutkan dengan nomor versi lebih besar di atas

1. Buka Settings > Privacy Policy
2. Verifikasi urutan baris dari atas: `Version 3`, `Version 2`, `Version 1`
3. Muat ulang halaman dengan F5
4. Verifikasi urutan baris tetap `Version 3`, `Version 2`, `Version 1` (deterministik)
5. Klik header `Published At` satu kali (Oldest First)
6. Verifikasi urutan baris `Version 1` (15 Jan 26), lalu `Version 2`, lalu `Version 3`
7. Verifikasi nilai Published At yang sama diurutkan menurut nomor versi, searah dengan arah sort aktif
8. Klik header `Published At` dua kali lagi sampai indikator sort hilang (kembali ke default)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah membuka halaman di awal dan langkah mengembalikan sort ke netral di akhir.
- Temuan untuk QA:
  - TC-AC-PP-121 Expected c menyatakan hasil Oldest First sebagai `Version 1`, `Version 2`, `Version 3`, dan menafsirkan "searah dengan arah sort aktif" sebagai tie-breaker nomor versi ikut menaik; spec mengasersi urutan itu apa adanya dan memecah klausa kedua menjadi `Verifikasi` tersendiri.
  - TC-AC-PP-121 Precondition tidak menyebut cara menghasilkan dua Published At identik pada detik yang sama; spec menyerahkannya ke Fixture BE.
