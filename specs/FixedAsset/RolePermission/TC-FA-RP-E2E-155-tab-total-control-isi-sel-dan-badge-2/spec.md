---
id: TC-FA-RP-E2E-155-tab-total-control-isi-sel-dan-badge-2
title: "Tab Total Control: isi sel dan badge (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1100
  - TC-FA-RP-1101
coverage:
  web: automated
---

# Tab Total Control: isi sel dan badge (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi), #37 (Tab Read Only), #38 (Tab Group Manager), #39 (Detail Role Group Role `Manage files`), #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`), dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- State yang diubah: konfigurasi kolom Setup Column Tab Total Control (kolom Activation Status ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Sel Name memuat avatar dan nama lengkap (TC-FA-RP-1100)

1. Klik Tab `Total Control`
2. Verifikasi sel Name Tab Total Control memuat avatar dan nama lengkap dalam satu sel
3. Verifikasi tidak ada kolom `Photo` pada tabel Tab Total Control
4. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
5. Verifikasi tidak ada kolom `Photo` pada daftar Setup Column
6. Klik `(X)` untuk menutup popup
7. Klik Tab `Group Manager`
8. Verifikasi sel Name Tab Group Manager memuat avatar dan nama lengkap dalam satu sel
9. Klik Tab `System`, lalu klik Role Name `Manage files` pada section Group Role
10. Verifikasi sel Name Detail Role memuat avatar dan nama lengkap dalam satu sel
11. Klik menu Settings > Role & Permission di sidebar, lalu klik Tab `Transaction Role`
12. Klik node `IT Infrastructure` di Sidebar Group Tree, klik sub-tab `Disposal`, lalu buka section `Asset Admin`
13. Verifikasi sel Name tabel Role Transaksi memuat avatar dan nama lengkap dalam satu sel

### Badge Activation Status (TC-FA-RP-1101)

14. Klik menu Settings > Role & Permission di sidebar
15. Klik Tab `Total Control`
16. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, centang `Activation Status`, lalu klik `[Save]`
17. Verifikasi badge `Activated` baris Ahmad Fauzi memakai severity success
18. Verifikasi badge `Pending Activation` baris Eka Saputra memakai severity warning
19. Verifikasi badge `Pending Email Confirmation` baris Fitri Handayani memakai severity warning

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, navigasi sidebar, membuka dan menutup Setup Column, serta langkah menuju node, sub-tab, dan section Role Transaksi (langkah 1, 4, 6, 7, 9, 11, 12, 14, 15, 16).
- Langkah 4 dan 5 memuat daftar Setup Column pada Tab Total Control sebagaimana Expected a TC-FA-RP-1100 ("tabel maupun daftar Setup Column").
- Temuan untuk QA:
  - TC-FA-RP-1100 langkah 3 menyebut "Buka Detail Role `Manage files`" tanpa menyebut jalur; spec membukanya lewat Tab `System` dan Role Name `Manage files` pada section Group Role (Pre-setup #39).
  - TC-FA-RP-1100 langkah 4 memuat section `Asset Admin` yang harus dibuka; spec membukanya eksplisit.
  - Expected TC-FA-RP-1100 dan TC-FA-RP-1101 tidak menyebut cara membaca severity badge (kelas gaya); spec mengasersi severity success atau warning sebagaimana tertulis di TC.
  - TC-FA-RP-1101 tidak menyebut apakah baris Ahmad Fauzi, Eka Saputra, dan Fitri Handayani berada pada halaman pertama; sembilan baris Pre-setup #36 muat dalam satu halaman ukuran 10.
