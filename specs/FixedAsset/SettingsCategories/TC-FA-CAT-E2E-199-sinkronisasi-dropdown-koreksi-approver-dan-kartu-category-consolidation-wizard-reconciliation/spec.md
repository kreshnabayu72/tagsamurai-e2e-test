---
id: TC-FA-CAT-E2E-199-sinkronisasi-dropdown-koreksi-approver-dan-kartu-category-consolidation-wizard-reconciliation
title: "Sinkronisasi ke Modul Konsumen: Dropdown Koreksi Approver pada Registrasi Aset dan Kartu Category Consolidation di Wizard Reconciliation"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-583
  - TC-FA-CAT-490
coverage:
  web: automated
---

# Sinkronisasi ke Modul Konsumen: Dropdown Koreksi Approver pada Registrasi Aset dan Kartu Category Consolidation di Wizard Reconciliation

## Prerequisites

- Mode: FE+BE.
- Akun login hook `before` spec ini: Approver Koreksi (Pre-setup #43) `approverCorrection_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_APPROVER_PASSWORD`. Halaman awal: hook `beforeEach` suite membuka Categories; langkah 1 membuka modul Asset Registration (pengecualian halaman awal, akun ini tidak punya capability Categories). Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai lewat langkah Ganti akun:

  | Langkah | Aktor | Pre-setup | Email | Password | Client |
  |---|---|---|---|---|---|
  | 6 | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | CatMain (#20) |
  | 17 | Approver Koreksi | #43 | `approverCorrection_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVER_PASSWORD` | CatMain (#20) |
  | 25 | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | CatPreT0 (#32) |

- Env var `FA_TC_PASSWORD` dan `FA_APPROVER_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec TC-FA-CAT-583 (di-seed hook `before` lewat API; kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`), nama berakhiran `{runId}-199`, client CatMain: `Furniture Appr {runId}-199` (Code `FA199`, leaf; direname menjadi `Furniture Appr Renamed {runId}-199`) dan `Vehicle Appr {runId}-199` (Code `VA199`, leaf; dihapus spec). Kategori `Approver Cat {runId}-199` dibuat spec. Registrasi aset berstatus Waiting for Approval pada kategori `Laptop` (Pre-setup #22) dipakai Approver sebagai precondition TC dan hanya dibaca (dropdown dibuka lalu ditutup tanpa mengubah). Pre-setup `Electronics` (Internal) dibaca.
- Data TC-FA-CAT-490: client CatPreT0 (Pre-setup #32: plan Professional dengan downgrade terjadwal ke Starter, T-0 belum tiba, cap plan baru 5, 8 kategori usable `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`, belum ada seleksi tersimpan). Spec menyimpan seleksi lima kategori pertama sehingga mengubah state Pre-setup #32 (S-06 pengecualian 2026-10-30): pemulihan seleksi tersimpan ke kosong dijamin fixture backend (disediakan tim FE/BE) yang dijalankan di hook `before` dan `after`; efeknya (entri Changelog seleksi dan Last Updated kategori) tercatat di sini; suite berjalan serial (`parallel: false`).
- Kemampuan teknis: seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite (termasuk akun Approver dan Total Control CatPreT0).

## Test Steps

### TC-FA-CAT-583: Dropdown koreksi Approver mencerminkan Create, Edit, dan Delete kategori

1. Buka koreksi Category pada registrasi aset Waiting for Approval di kategori `Laptop` pada modul Asset Registration
2. Buka dropdown pemilihan Category dan catat isinya
3. Verifikasi `Vehicle Appr {runId}-199` dan `Furniture Appr {runId}-199` (leaf) tampil dan dapat dipilih
4. Verifikasi `Electronics` (Internal) tampil tetapi tidak dapat dipilih
5. Tutup dropdown dan koreksi tanpa mengubah Category
6. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatMain dengan `Spectra.env.FA_TC_PASSWORD`
7. Buka Fixed Asset > Settings > Categories
8. Klik `[+] Category` pada sidebar
9. Isi Category Name `Approver Cat {runId}-199`
10. Klik `[Submit]`
11. Klik elipsis (⋯) pada baris `Furniture Appr {runId}-199` > `Edit`
12. Ganti isi Category Name dengan `Furniture Appr Renamed {runId}-199`
13. Klik `[Save]`
14. Klik elipsis (⋯) pada baris `Vehicle Appr {runId}-199` > `Delete`
15. Klik `[Delete]` pada dialog
16. Tunggu aksi selesai (dialog tertutup)
17. Ganti akun: logout, lalu login sebagai Approver Koreksi (Pre-setup #43) client CatMain dengan `Spectra.env.FA_APPROVER_PASSWORD`
18. Buka koreksi Category pada registrasi aset Waiting for Approval yang sama di kategori `Laptop`
19. Buka dropdown pemilihan Category
20. Verifikasi `Approver Cat {runId}-199` tampil dan dapat dipilih
21. Verifikasi `Furniture Appr Renamed {runId}-199` menggantikan `Furniture Appr {runId}-199` pada dropdown
22. Verifikasi `Vehicle Appr {runId}-199` tidak lagi tampil
23. Verifikasi `Electronics` (Internal) tetap tampil tetapi tidak dapat dipilih
24. Tutup dropdown dan koreksi tanpa mengubah Category

### TC-FA-CAT-490: Kartu Category Consolidation di Wizard Reconciliation

25. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatPreT0 dengan `Spectra.env.FA_TC_PASSWORD`
26. Buka Fixed Asset > Wizard Reconciliation
27. Verifikasi kartu `Category Consolidation` belum selesai (8 kategori melebihi cap plan baru 5 dan belum ada selection tersimpan)
28. Buka Category Consolidation dari kartu tersebut
29. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
30. Klik `[Save Selection]`
31. Tunggu aksi selesai (popup tertutup)
32. Buka Fixed Asset > Wizard Reconciliation
33. Verifikasi kartu `Category Consolidation` selesai (selection tersimpan lewat `[Save Selection]`)

## Notes

- Langkah penghubung (S-03): langkah 5, 24 (menutup dropdown dan koreksi, tidak dirty), langkah 6, 17, 25 (ganti akun), langkah 7, 26, 32 (membuka halaman), langkah 16 (menunggu aksi selesai sebelum ganti akun), langkah 28 sampai 31 (menyimpan seleksi sebagai pemicu perubahan status kartu; TC hanya menyebut "sebelum dan sesudah seleksi disimpan"), langkah 2 dan 19 (membuka dropdown; langkah 2 mencatat isi).
- Alasan ganti akun berulang (bagian 3 butir b): TC-FA-CAT-583 menuntut Total Control (pengubah) dan Approver Koreksi (pembaca) berganti dua kali; akun pertama login di hook `before` (bagian 3a, S-07).
- Langkah 20 sampai 23 memetakan Expected b, c, d, e TC-FA-CAT-583. Expected a ada di langkah 3 sampai 4. Absence `Vehicle Appr` (langkah 22) memakai langkah 20 dan 23 (opsi lain dropdown tampil) sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-CAT-583 menyebut `Vehicle`, `Furniture`, dan `Electronics` dari Pre-setup #20; spec memakai kategori milik spec untuk `Vehicle` dan `Furniture` (dihapus dan direname), dan `Electronics` Pre-setup dibaca.
  - TC-FA-CAT-583 tidak menyebut menu koreksi Category pada registrasi aset (path Asset Registration) dan label tombolnya; spec menulis "Buka koreksi Category".
  - TC-FA-CAT-490 hanya memuat satu langkah ("Perhatikan kartu sebelum dan sesudah seleksi disimpan") tanpa cara membuka popup Category Consolidation dan memilih kategori; langkah 28 sampai 31 disusun dari Expected dan Pre-setup #32 (lima kategori usable pertama, cap 5).
  - TC-FA-CAT-490 menyebut ACC kolom Wizard Reconciliation tanpa menyebut akun; spec memakai Total Control.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` dan `FA_APPROVER_PASSWORD` adalah usulan.
