---
id: TC-AC-PP-E2E-037-filter-published-by-or
title: "Filter Published By dengan Dua Opsi Memakai Logika OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-111
coverage:
  web: automated
---

# Filter Published By dengan Dua Opsi Memakai Logika OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat B varian: Version 1 sampai 120, Published At Version 1 pada 01 Jan 2026 dan tiap versi berikutnya satu hari lebih akhir, Version 120 Active. Published By: Version ganjil `John Doe` (60 baris), Version genap sampai 118 `Jane Smith` (59 baris), dan Version 120 `Budi Santoso` (varian TC ini). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat B varian.
- State UI yang diubah spec: page size diubah dari 10 menjadi 100 (langkah penghubung supaya seluruh 61 baris hasil Filter ada pada satu halaman untuk asersi "seluruh halaman hasil"); filter dikosongkan di akhir. Hook `after` mengembalikan page size 10 sebagai cadangan.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-111: Filter Published By dengan dua opsi memakai logika OR dalam satu field

1. Buka panel Filter
2. Pada field `Published By` centang `John Doe` dan `Budi Santoso`
3. Klik `[Apply]`
4. Verifikasi footer `1–10 of 61`
5. Verifikasi baris teratas `Version 120` (`Budi S`)
6. Verifikasi baris kedua `Version 119` (`John D`)
7. Ubah page size menjadi 100 supaya seluruh hasil berada pada satu halaman
8. Verifikasi tidak ada baris dengan Published By `Jane S` pada seluruh hasil
9. Verifikasi baris dengan Published By `John Doe` tampil (logika OR dalam satu field)
10. Verifikasi baris dengan Published By `Budi Santoso` tampil (logika OR dalam satu field)
11. Buka panel Filter, klik `[Clear Field]`, klik `[Apply]`, lalu kembalikan page size menjadi 10

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah mengubah page size menjadi 100 (agar asersi "seluruh halaman hasil" dapat dibaca dalam satu halaman) dan langkah terakhir (membersihkan filter dan mengembalikan page size).
- Temuan untuk QA:
  - TC-AC-PP-111 Expected b menyebut "pada seluruh halaman hasil" (7 halaman pada page size 10) tanpa langkah menelusuri halaman; spec menelusurinya dengan page size 100 dan footer awal `1–10 of 61` diasersi sebelum page size diubah.
  - TC-AC-PP-111 Precondition menyebut "Version genap hingga 118 `Jane Smith`: 59 baris"; Version 120 sengaja diganti `Budi Santoso` sehingga total hasil Filter `John Doe` + `Budi Santoso` = 60 + 1 = 61.
