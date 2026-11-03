---
id: TC-FA-CAT-E2E-101-sort-tie-breaker-pindah-kolom-dan-kolom-tanpa-sort
title: "Sort: Tie-Breaker Antar Halaman, Pindah Kolom Sort, dan Kolom Tanpa Ikon Sort"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-350
  - TC-FA-CAT-351
  - TC-FA-CAT-352
coverage:
  web: automated
---

# Sort: Tie-Breaker Antar Halaman, Pindah Kolom Sort, dan Kolom Tanpa Ikon Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Total Asset 0 sampai 29, Modified By bergantian `Jane Smith`, `Alex Brown`, `John Doe`, `System`). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-350: Tie-breaker baris bernilai sama

1. Klik header Total Asset satu kali (Ascending)
2. Catat urutan baris halaman 1 (baseline)
3. Pindah ke halaman 2 dan catat urutan barisnya
4. Pindah ke halaman 3 dan catat urutan barisnya
5. Verifikasi baris dengan Total Asset sama urut mengikuti Category A-Z lalu id, tidak ada baris ganda, dan tidak ada baris terlewat antar halaman 1 sampai 3
6. Klik header Total Asset kedua kali (Descending)
7. Verifikasi arah tie-breaker mengikuti arah sort aktif pada Descending

### TC-FA-CAT-351: Pindah kolom sort

8. Klik header Total Asset ketiga kali agar Netral
9. Klik header Code dua kali (Descending)
10. Klik header Total Asset
11. Verifikasi indikator sort pada Code hilang
12. Verifikasi Total Asset berstatus Ascending (↑)

### TC-FA-CAT-352: Kolom Checkbox dan Actions tanpa ikon sort

13. Klik header Total Asset dua kali lagi agar Netral
14. Verifikasi tidak ada ikon sort pada kolom Checkbox maupun Actions (⋯)
15. Verifikasi kelima kolom data (Category, Code, Total Asset, Modified By, Last Updated) memiliki ikon sort

## Notes

- Langkah penghubung (S-03): langkah 8 dan 13 (mengembalikan sort ke Netral, S-09); langkah 2 sampai 4 (mencatat urutan baris sebagai baseline).
- Temuan untuk QA:
  - TC-350 memakai Total Asset sebagai kolom dengan "baris bernilai sama", sedangkan data Pre-setup #24 memberi Total Asset 0 sampai 29 (nilai unik per baris), sehingga tie-breaker tidak teruji pada kolom itu. Kolom Modified By (empat nilai berulang) lebih cocok sebagai kolom uji tie-breaker; spec mengikuti TC.
  - TC-352 tidak menyebut baris header yang diperiksa pada kondisi sort Netral; spec mengembalikan sort ke Netral sebelumnya (langkah 13).
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
