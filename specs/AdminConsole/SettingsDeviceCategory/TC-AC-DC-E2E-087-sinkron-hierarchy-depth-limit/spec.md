---
id: TC-AC-DC-E2E-087-sinkron-hierarchy-depth-limit
title: "Hierarchy Depth Limit: Penurunan Tidak Menghapus Node dan Kenaikan Langsung Berlaku pada Add"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-237
  - TC-AC-DC-238
coverage:
  web: automated
---

# Hierarchy Depth Limit: Penurunan Tidak Menghapus Node dan Kenaikan Langsung Berlaku pada Add

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`. Pelaku perubahan Hierarchy Depth Limit: Total Control #9 (Pre-setup #9) `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net` (Maya Putri; berhak mengubah Lifecycle Settings) lewat sesi API, password `Spectra.env.AC_DC_TC2_PASSWORD`.
- Login akun aktor di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Env var: `Spectra.env.AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `Spectra.env.AC_DC_TC2_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk rantai milik spec dan tidak diubah. Konfigurasi Pre-setup #18: Hierarchy Depth Limit awal 50 (nilai minimum yang diizinkan 5).
- Data Dinamis (suffix `{runId}-087`), dibuat lewat sesi API aktor di hook `before` dengan limit masih 50, baru kemudian limit diturunkan menjadi 5 (urutan ini wajib karena rantai kedalaman 6 dan 7 tidak dapat dibuat saat limit 5): rantai `Rantai L3 {runId}-087` (anak `Handheld Reader`, kedalaman 3) > `Rantai L4 {runId}-087` > `Rantai L5 {runId}-087` > `Rantai L6 {runId}-087` > `Rantai L7 {runId}-087` (kedalaman 7; `Hardware` = 1, `Handheld Reader` = 2). Hasil rename `Rantai L7 {runId}-087` menjadi `Rantai L7 Baru {runId}-087` (langkah 3).
- Hierarchy Depth Limit entitas uji diatur 5 di hook `before` dan dinaikkan menjadi 8 pada langkah 12 oleh Total Control #9 lewat sesi API aktor (kemampuan membaca dan mengubah Lifecycle Settings disediakan tim FE/BE; endpoint tidak dikarang di spec ini).
- State global yang diubah: Hierarchy Depth Limit entitas uji (Lifecycle Settings). Hook `after` memulihkan nilainya ke 50 (Pre-setup #18) dan menghapus rantai; suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan limit ke 50 lebih dahulu, lalu hapus lewat API rantai `Rantai L3 {runId}-087` beserta turunannya (termasuk `Rantai L7 Baru {runId}-087` dan node Add yang dibuat spec).
- State global lain: tidak ada.

## Test Steps

### TC-AC-DC-237: Penurunan Hierarchy Depth Limit tidak menghapus node yang sudah melampaui limit baru

1. Expand `Hardware`, `Handheld Reader`, lalu `Rantai L3 {runId}-087` sampai `Rantai L6 {runId}-087` secara berurutan
2. Hover node `Rantai L7 {runId}-087`, lalu klik aksi Edit
3. Ubah nama menjadi "Rantai L7 Baru {runId}-087", lalu klik `[Save]`
4. Verifikasi toast sukses "Success, category has been updated."
5. Verifikasi node `Rantai L6 {runId}-087` dan `Rantai L7 Baru {runId}-087` (di atas limit 5) tetap ada dan dapat diedit
6. Hover node `Rantai L6 {runId}-087`, lalu klik aksi `+ Subcategory`
7. Verifikasi dialog blok "Cannot Add Category" dengan isi "You've reached the platform limit of 5 levels. Contact support if you need a higher limit." dan satu tombol `[OK]`
8. Klik `[OK]`

### TC-AC-DC-238: Menaikkan Hierarchy Depth Limit langsung berlaku pada Add berikutnya

9. Hover node `Rantai L5 {runId}-087`, lalu klik aksi `+ Subcategory`
10. Verifikasi dialog blok "Cannot Add Category" tampil (sebelum limit dinaikkan, Add diblok)
11. Klik `[OK]`
12. Naikkan Hierarchy Depth Limit entitas uji menjadi 8 lewat sesi API aktor Total Control #9 hingga nilai 8 tersimpan
13. Hover node `Rantai L5 {runId}-087`, lalu klik aksi `+ Subcategory`
14. Verifikasi input inline Add terbuka
15. Verifikasi tidak ada dialog blok yang tampil (limit dibaca saat aksi)
16. Tutup input inline Add dengan menekan Esc

## Notes

- Langkah penghubung (S-03): langkah 8 dan 11 (menutup dialog blok), langkah 12 (pelaku perubahan limit memakai sesi API Total Control #9; hanya memicu perubahan state sehingga tidak butuh ganti akun UI), dan langkah 16 (menutup input inline Add yang tidak berisi perubahan, tanpa dialog Unsaved Changes).
- Anchor absence (bagian 8b butir 2): langkah 14 (input Add terbuka) mendahului langkah 15.
- Langkah 5 memverifikasi kemampuan edit lewat toast sukses langkah 4; node di atas limit tetap ada.
- Pembagian TC lintas spec: Add depth dan soft cap lain ada di spec CRUD suite ini; penurunan limit yang diuji di sini hanya untuk Edit dan Add pada rantai yang sudah ada.
- Temuan untuk QA:
  - TC-AC-DC-237 dan 238 memakai rantai literal Pre-setup #14 (`Rantai L3` sampai `Rantai L7` di bawah `Smart Fixed Reader`); spec memakai rantai bersuffix milik spec di bawah `Handheld Reader` dengan kedalaman yang sama (keputusan data tulis).
  - TC-AC-DC-238 Expected a menyebut "dialog D-01"; spec memakai judul dialog yang sama dengan TC-AC-DC-237 ("Cannot Add Category").
  - Pre-setup #9 hanya disebut berhak mengubah Lifecycle Settings; TC-AC-DC-238 langkah 3 ("Naikkan Hierarchy Depth Limit ... di Lifecycle Settings") tidak menyebut apakah Total Control #1 juga berhak. Spec memakai Total Control #9 lewat sesi API karena hanya memicu perubahan state.
