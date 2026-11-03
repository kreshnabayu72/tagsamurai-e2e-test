---
id: TC-AC-DC-E2E-082-log-sinkron-tiga-surface-dan-aktor
title: "Satu Aksi Edit Sinkron di Tiga Surface Log dan Modified By Mengikuti Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-226
  - TC-AC-DC-229
coverage:
  web: automated
---

# Satu Aksi Edit Sinkron di Tiga Surface Log dan Modified By Mengikuti Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`. Akun kedua (langkah 18): Total Control #9 (Pre-setup #9) `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net` (Maya Putri; Modified By tampil `Maya P`), password `Spectra.env.AC_DC_TC2_PASSWORD`.
- Login akun pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control #1).
- Env var: `Spectra.env.AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `Spectra.env.AC_DC_TC2_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah. Aktor kedua Pre-setup #9 hanya dipakai untuk aksi Add pada langkah 22.
- Data Dinamis (suffix `{runId}-082`), dibuat lewat sesi API aktor di hook `before` sebagai leaf di bawah `Handheld Reader`: `Sumber Sinkron {runId}-082` (target Edit langkah 3, direname menjadi `Zebra Sinkron {runId}-082`) dan `Induk Uji {runId}-082` (induk Add langkah 21). Node yang dibuat spec lewat UI: `Pemindai Maya {runId}-082` (langkah 22). Baseline entri nol karena nama unik per run (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Zebra Sinkron {runId}-082`, `Induk Uji {runId}-082` (beserta anak `Pemindai Maya {runId}-082`), dan sisa node lain bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): membuka Detail User akun aktor tab System Log dan Activity Log Admin Console; jam server dan jam browser tidak diubah.
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-226: Satu aksi Edit tampil sinkron sebagai satu entri di ketiga surface

1. Expand `Hardware`, lalu expand `Handheld Reader`
2. Hover node `Sumber Sinkron {runId}-082`, lalu klik aksi Edit
3. Ubah nama menjadi "Zebra Sinkron {runId}-082", lalu klik `[Save]`
4. Tunggu aksi selesai
5. Klik ikon Changelog pada header Sidebar Category
6. Ketik Search `Zebra Sinkron {runId}-082`, tekan Enter
7. Verifikasi Changelog memuat tepat satu entri Edit untuk aksi ini
8. Verifikasi entri Edit di Changelog: Old Value "Sumber Sinkron {runId}-082" dan New Value "Zebra Sinkron {runId}-082"
9. Tutup modal Changelog lewat `[×]`
10. Buka Detail User akun aktor, lalu buka tab System Log
11. Ketik Search `Zebra Sinkron {runId}-082`, tekan Enter
12. Verifikasi System Log aktor memuat tepat satu entri Edit untuk aksi ini
13. Verifikasi entri Edit di System Log: Old Value "Sumber Sinkron {runId}-082" dan New Value "Zebra Sinkron {runId}-082"
14. Buka Activity Log Admin Console
15. Ketik Search `Zebra Sinkron {runId}-082`, tekan Enter
16. Verifikasi Activity Log memuat tepat satu entri Edit untuk aksi ini
17. Verifikasi entri Edit di Activity Log: Old Value "Sumber Sinkron {runId}-082" dan New Value "Zebra Sinkron {runId}-082"

### TC-AC-DC-229: Modified By mengikuti aktor yang melakukan aksi

18. Ganti akun: logout, lalu login sebagai Maya Putri dengan `Spectra.env.AC_DC_TC2_PASSWORD`
19. Buka halaman Settings > Device > Device Name
20. Expand `Hardware`, lalu expand `Handheld Reader`
21. Hover node `Induk Uji {runId}-082`, lalu klik aksi `+ Subcategory`
22. Ketik "Pemindai Maya {runId}-082", lalu klik `[Submit]`
23. Tunggu aksi selesai
24. Klik ikon Changelog pada header Sidebar Category
25. Ketik Search `Pemindai Maya {runId}-082`, tekan Enter
26. Verifikasi baris hasil Search menampilkan Modified By "Maya P"
27. Hover sel Modified By pada baris tersebut
28. Verifikasi tooltip "Maya Putri" tampil

## Notes

- Langkah penghubung (S-03): langkah 4 dan 23 (Tunggu aksi selesai sesudah `[Save]` dan `[Submit]` yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8), langkah 9 (menutup modal Changelog sebelum membuka surface lain), langkah 19 (membuka halaman Device Name sebagai Maya Putri), dan Search pada langkah 6, 11, 15, dan 25 untuk menemukan baris target (R-16).
- Pelaku langkah 18 sampai 28 adalah akun UI kedua yang diasersi (Modified By), sehingga ganti akun ditulis eksplisit (S-07).
- Pembagian TC lintas spec: pencatatan Create, Edit, Delete di System Log dan Activity Log ada di spec 081; absence ada di spec 083, 084, 097, dan 098 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-226 tidak menyebut tab Activity Log tempat entri Category tampil dan kolom yang dicakup Search pada System Log dan Activity Log; spec memakai Search dengan nama bersuffix (R-16). Bila Search tidak mencakup Old Value atau New Value, QA/FE perlu menetapkan cara menemukan entri.
  - TC-AC-DC-229 Expected menyebut "baris teratas"; spec memakai satu-satunya baris hasil Search untuk nama bersuffix unik, karena posisi teratas bergantung pada audit trail permanen yang tumbuh (S-14).
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai target; spec memakai node bersuffix milik spec (keputusan data tulis).
