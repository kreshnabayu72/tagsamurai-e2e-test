---
id: TC-FA-NOTIF-E2E-115-tie-breaker-sort-notifikasi-bertimestamp-sama
title: "Tie-Breaker Sort: Notifikasi Bertimestamp Sama Berurutan Deterministik"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-219
coverage:
  web: automated
---

# Tie-Breaker Sort: Notifikasi Bertimestamp Sama Berurutan Deterministik

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18) ditambah N-39 dan N-40 (dua notifikasi dengan timestamp sama; Pre-setup #18), di-seed fixture BE penukar sebagai langkah penghubung. Urutan pembuatan N-39 dan N-40 ditentukan fixture (N-40 dibuat sesudah N-39). Seed dipulihkan fixture BE pemulih di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-219: Tie-breaker Sort: notifikasi bertimestamp sama berurutan deterministik

1. Pulihkan seed notifikasi lewat fixture BE pemulih, tambahkan N-39 dan N-40 dengan timestamp sama lewat fixture BE penukar, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
2. Scroll sampai akhir list hingga seluruh item termuat
3. Catat urutan N-39 dan N-40 pada Sort `Newest`
4. Verifikasi entri yang dibuat lebih akhir (N-40) berada di atas N-39 pada Sort `Newest`
5. Muat ulang halaman
6. Scroll sampai akhir list hingga seluruh item termuat
7. Verifikasi urutan N-39 dan N-40 sama dengan urutan yang dicatat pada langkah 3
8. Verifikasi N-39 dan N-40 masing-masing tampil tepat satu kali (tidak ada baris ganda dan tidak ada yang terlewat)
9. Klik toggle Sort hingga Sort `Oldest`
10. Scroll sampai akhir list hingga seluruh item termuat
11. Verifikasi N-39 dan N-40 masing-masing tampil tepat satu kali pada Sort `Oldest`
12. Pulihkan seed notifikasi lewat fixture BE pemulih, lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Spec ini memuat TC-219 yang berdiri sendiri karena memakai varian seed N-39 dan N-40; kontrol Sort lain ada di spec 052.
- Langkah penghubung (S-03): langkah 1 (pemulihan seed, penambahan N-39 dan N-40, muat ulang, dan precondition TC), 2, 6, 10 (memuat seluruh item), 3 (mencatat urutan untuk dibandingkan di langkah 7), 12 (pemulihan seed).
- Asersi tambahan di luar Expected TC (S-03): langkah 11 (tidak ada baris ganda atau terlewat pada Sort `Oldest`, klausa "tidak ada baris ganda atau terlewat antar muat" diperluas ke Sort kedua yang ditempuh langkah 5 TC).
- Temuan untuk QA:
  - TC-219 menulis "entri yang dibuat lebih akhir di atas pada Newest" tanpa menyebut mana yang dibuat lebih akhir; spec mengasumsikan N-40 dibuat sesudah N-39 (urutan seeding fixture).
  - TC-219 langkah 5 ("Ganti ke Oldest") tidak punya Expected urutan pada Sort `Oldest`; spec tidak mengasersi urutan itu.
