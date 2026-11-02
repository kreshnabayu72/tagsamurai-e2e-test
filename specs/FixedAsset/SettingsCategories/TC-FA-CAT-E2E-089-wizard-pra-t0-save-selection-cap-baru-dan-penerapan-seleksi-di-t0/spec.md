---
id: TC-FA-CAT-E2E-089-wizard-pra-t0-save-selection-cap-baru-dan-penerapan-seleksi-di-t0
title: "Wizard Pra-T-0 CatPreT0: Batas Cap Plan Baru, Save Selection Hanya Menyimpan, dan Penerapan Seleksi di T-0"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-306
  - TC-FA-CAT-305
  - TC-FA-CAT-307
coverage:
  web: automated
---

# Wizard Pra-T-0 CatPreT0: Batas Cap Plan Baru, Save Selection Hanya Menyimpan, dan Penerapan Seleksi di T-0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPreT0 (Pre-setup #32), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #32 (CatPreT0, downgrade terjadwal dari plan aktif Professional cap 100 ke plan baru Starter cap 5, T-0 belum tiba, belum ada seleksi tersimpan): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 16 (bagian 6 konvensi). Kemampuan mengatur jam dan memicu penerapan T-0 disediakan tim FE/BE; hook `after` memulihkan jam server, jam browser, dan seed Pre-setup #32.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog `Marked as Excess (Category Consolidation)` sebelum aksi (baseline NM, S-12).
- State global yang diubah spec: jam server dan seleksi tersimpan client CatPreT0. Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-306: Sebelum T-0 batas X <= cap memakai cap plan baru

1. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
2. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, dan `Zeta Vehicle`
3. Verifikasi counter `6 of 5 categories selected` berseverity danger (cap = cap plan baru 5, bukan cap plan aktif 100)
4. Verifikasi `[Save Selection]` disabled

### TC-FA-CAT-305: Sebelum T-0 Save Selection hanya menyimpan seleksi tanpa mengubah status Excess

5. Hapus centang `Keep usable` pada `Zeta Vehicle` sehingga 5 kategori dicentang
6. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
7. Klik `[Save Selection]`
8. Verifikasi toast sukses `Success, category consolidation has been updated.` tampil
9. Verifikasi kartu `Category Consolidation` di Wizard Reconciliation bertanda selesai
10. Buka Fixed Asset > Settings > Categories
11. Verifikasi kedelapan kategori masih berstatus usable (belum ada Excess)
12. Verifikasi Alert Category Consolidation tidak tampil (jumlah kategori tidak melebihi cap plan aktif 100)
13. Buka Modal Changelog
14. Verifikasi jumlah baris Changelog `Marked as Excess (Category Consolidation)` sama dengan NM
15. Tutup Modal Changelog

### TC-FA-CAT-307: Seleksi tersimpan diterapkan di T-0 dalam satu transaksi dengan Modified By aktor yang men-submit

16. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
17. Buka Fixed Asset > Settings > Categories
18. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` berstatus usable
19. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess
20. Buka Modal Changelog
21. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (NM + 3) untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy`
22. Verifikasi Modified By tiap baris baru adalah aktor Total Control yang men-submit, bukan `System`
23. Verifikasi Date tiap baris baru adalah tanggal T-0
24. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-306 (validasi diblokir), TC-FA-CAT-305 (aksi sukses), lalu TC-FA-CAT-307 yang memakai seleksi hasil TC-FA-CAT-305 sebagai preconditionnya sendiri ("seleksi 5 kategori sudah disimpan sebelum T-0"); keduanya state berat berurutan, `P-1`: seleksi tersimpan dan T-0 dibangun langkah sebelumnya di spec asal.
- TC-FA-CAT-306 dan TC-FA-CAT-305 berbagi popup Wizard yang sama: langkah 5 menghapus centang `Zeta Vehicle` dari 6 centang TC-FA-CAT-306 supaya terbentuk 5 centang TC-FA-CAT-305 tanpa membuka ulang Wizard (S-09, halaman yang sama dipakai berulang).
- TC-FA-CAT-308 sampai TC-FA-CAT-311 (Fallback T-0 dan downgrade baru) ada di spec 190; TC-FA-CAT-601 sampai TC-FA-CAT-612 ada di spec 090 sampai 093.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5 (menyesuaikan centang), 6 (baseline), 10 dan 17 (navigasi), 15 dan 24 (menutup Modal Changelog), 16 (pemicu T-0).
- Asersi absence langkah 12 dan 14 memakai langkah 11 (kategori usable tampil pada halaman yang sama) sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-305 dan TC-FA-CAT-306 tidak menyebut keadaan Wizard setelah seleksi tersimpan (apakah centang terisi saat dibuka ulang); spec menghindarinya dengan mengurutkan TC-FA-CAT-306 sebelum TC-FA-CAT-305.
  - TC-FA-CAT-307 menyebut "tanggal T-0" tanpa format; spec mengasersi tanggal baris sama dengan tanggal T-0 dalam format General Settings.
