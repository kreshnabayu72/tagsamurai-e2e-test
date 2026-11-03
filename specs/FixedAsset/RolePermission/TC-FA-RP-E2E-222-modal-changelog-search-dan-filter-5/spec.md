---
id: TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5
title: "Modal Changelog: Search dan Filter (5/6)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-723
  - TC-FA-RP-724
  - TC-FA-RP-725
  - TC-FA-RP-726
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (5/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap dan tidak mengasersi total seluruh entri; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value. Spec ini tidak mengubah data.

## Test Steps

### Chip opsi terpilih: hapus lewat `(X)` pada chip (TC 723)

1. Klik ikon Changelog pada toolbar.
2. Klik ikon Filter.
3. Pilih opsi `Auto-Revert` dan `Remove` pada field Action.
4. Klik `(X)` pada chip `Remove` tanpa membuka dropdown.
5. Verifikasi chip `Remove` hilang dari field.
6. Verifikasi chip `Auto-Revert` tetap ada.
7. Buka dropdown field Action.
8. Verifikasi checkbox opsi `Remove` di dalam dropdown tidak tercentang.
9. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Chip opsi terpilih: hapus lewat uncheck di dalam dropdown (TC 724)

10. Pilih opsi `Auto-Revert` dan `Remove` pada field Action.
11. Buka dropdown field Action.
12. Hapus centang opsi `Remove`.
13. Verifikasi chip `Remove` hilang dari field.
14. Verifikasi chip `Auto-Revert` tetap ada.
15. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Penghapusan chip mengubah hasil hanya setelah `[Apply]` (TC 725)

16. Pilih opsi `Auto-Revert` dan `Remove` pada field Action, lalu klik `[Apply]`.
17. Hapus chip `Remove` dengan klik `(X)` pada chip.
18. Verifikasi tabel masih menampilkan entri Auto-Revert Fitri Handayani dan Remove Budi Santoso (kriteria lama).
19. Klik `[Apply]`.
20. Verifikasi dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya entri Auto-Revert Fitri Handayani (opsi `Auto-Revert`) yang tampil.
21. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Overflow banyak chip (TC 726)

22. Pilih kelima opsi field User Name: `Rina Wulandari`, `Ahmad Fauzi`, `Budi Santoso`, `Fitri Handayani`, `Maya Anggraeni`.
23. Verifikasi chip yang tidak muat diringkas menjadi chip `+N more` sesuai komponen MultiSelect.
24. Verifikasi field tidak terpotong.
25. Klik `[Clear Field]`, lalu klik `[Apply]`.
26. Klik ikon Filter untuk menutup panel.

## Notes

- Langkah penghubung (S-03): langkah 9, 15, 21, dan 25 (membersihkan Filter antar TC, sesuai S-09) dan 26 (menutup panel).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 726 menulis Expected secara kondisional ("Bila ruang field habis"); spec mengasersi chip `+N more` untuk lima chip tanpa menetapkan lebar field atau viewport, karena TC tidak menetapkannya.
  - TC 723 sampai 726 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengasumsikan panel tetap terbuka.
