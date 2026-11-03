---
id: TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2
title: "Modal Changelog: Pagination, Download, kombinasi, dan varian (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-747
  - TC-FA-RP-748
  - TC-FA-RP-749
  - TC-FA-RP-750
coverage:
  web: automated
---

# Modal Changelog: Pagination, Download, kombinasi, dan varian (2/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By di atas, dan asersi memakai urutan relatif, selisih terhadap baseline, atau hanya entri seed yang cocok. Spec ini tidak mengubah data.
- Kemampuan teknis: pembaca berkas unduhan (CSV dan XLSX) untuk memeriksa nama berkas, kolom, dan baris; disediakan tim FE/BE.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan di langkah 20 sampai 21 dan 24 sampai 25; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Download tanpa Search atau Filter mengekspor seluruh data (TC 747)

1. Klik ikon Changelog pada toolbar.
2. Catat total entri pada info pagination sebagai baseline.
3. Klik ikon Download, lalu klik `Download as CSV`.
4. Verifikasi tidak ada toast sukses.
5. Verifikasi berkas `Changelog-Role-Permission-Total-Control.csv` terunduh.
6. Verifikasi berkas memuat kolom Date, Action, User Name, Field, Old Value, New Value, Modified By.
7. Verifikasi jumlah baris data berkas sama dengan total baseline langkah 2 (bukan hanya satu halaman).
8. Verifikasi berkas memuat entri seed Pre-setup #42.

### Download dengan Search dan Filter aktif (TC 748)

9. Ketik Search `assign`, tekan Enter.
10. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
11. Klik ikon Download, lalu klik `Download as XLSX`.
12. Verifikasi berkas `Changelog-Role-Permission-Total-Control.xlsx` terunduh.
13. Verifikasi dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), berkas hanya memuat entri seed Assign Ahmad Fauzi dan Assign Rina Wulandari.
14. Klik `[Clear Field]`, lalu klik `[Apply]`.
15. Klik ikon `(←)` pada kotak Search.

### Kolom yang disembunyikan tidak ikut diekspor (TC 749)

16. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
17. Hapus centang kolom `Old Value`, lalu klik `[Save]`.
18. Klik ikon Download, lalu klik `Download as CSV`.
19. Verifikasi berkas tidak memuat kolom `Old Value` (sama dengan kolom yang sedang tampil).
20. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
21. Centang kembali kolom `Old Value`, lalu klik `[Save]`.

### Kolom yang ditampilkan kembali ikut diekspor (TC 750)

22. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
23. Hapus centang kolom `Old Value`, lalu klik `[Save]`.
24. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
25. Centang kembali kolom `Old Value`, lalu klik `[Save]`.
26. Klik ikon Download, lalu klik `Download as CSV`.
27. Verifikasi berkas memuat kembali kolom `Old Value` yang tadi disembunyikan.

## Notes

- Langkah penghubung (S-03): langkah 2 (mencatat baseline), 14 dan 15 (membersihkan Filter dan Search sebelum TC 749), 20 dan 21 (memulihkan kolom `Old Value` sebelum TC 750 menyembunyikannya sendiri). Langkah 4 mendahului artefak: asersi absence toast diletakkan segera setelah pemicu dan berpasangan dengan langkah 5 sebagai anchor positif (bagian 8b butir 11).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- TC 755 (Download di atas 5.000 baris), TC 753 (isi sel berkas), TC 751 (Download gagal), dan TC 752 ada di spec lain.
- Temuan untuk QA:
  - TC 749 dan 750 tidak menyebut apakah modal Changelog tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan modal tetap terbuka.
