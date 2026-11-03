---
id: TC-FA-RP-E2E-231-modal-changelog-pagination-download-kombinasi-dan-varian-4
title: "Modal Changelog: Pagination, Download, kombinasi, dan varian (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-759
  - TC-FA-RP-760
coverage:
  web: automated
---

# Modal Changelog: Pagination, Download, kombinasi, dan varian (4/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By di atas, dan asersi memakai urutan relatif, selisih terhadap baseline, atau hanya entri seed yang cocok. Spec ini tidak mengubah data.

## Test Steps

### Ganti kolom Sort saat Search dan Filter aktif (TC 759)

1. Klik ikon Changelog pada toolbar.
2. Ketik Search `assign`, tekan Enter.
3. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
4. Klik header kolom Date sekali (Date ascending).
5. Verifikasi Sort berpindah ke kolom Date ascending: dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), Assign Rina Wulandari lalu Assign Ahmad Fauzi (terlama lebih dulu).
6. Verifikasi Search `assign` dan Filter Modified By `Siti Rahmawati` tidak direset: kotak Search berisi `assign` dan panel Filter menampilkan chip `Siti Rahmawati` pada field Modified By.

### Pemulihan dari empty state Search dan Filter (TC 760)

7. Pulihkan state: klik `[Clear Field]`, lalu klik `[Apply]`; klik ikon `(←)` pada kotak Search; klik header kolom Date dua kali hingga sort kembali ke default.
8. Terapkan Filter Action `Remove` (pilih opsi `Remove` pada field Action, klik `[Apply]`).
9. Ketik Search `assign`, tekan Enter.
10. Verifikasi kombinasi Filter Action `Remove` dan Search `assign` menampilkan `No results found`.
11. Klik `[Clear Field]`, lalu klik `[Apply]` untuk melepas Filter Action.
12. Verifikasi tabel pulih menampilkan, dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya Assign Maya Anggraeni, Assign Budi Santoso, Assign Ahmad Fauzi, dan Assign Rina Wulandari dengan urutan relatif itu.
13. Klik ikon `(←)` pada kotak Search.

## Notes

- Langkah penghubung (S-03): langkah 7 (memulihkan Search, Filter, dan Sort antar TC, sesuai S-09; satu aksi gabungan tanpa `Verifikasi`) dan 13 (mengosongkan Search).
- TC 761 ada di spec `TC-FA-RP-E2E-311-modal-changelog-title-kolom-object-dan-placeholder-per-varian` dan TC 1030 ada di spec `TC-FA-RP-E2E-312-modal-changelog-transaction-role-terpisah-per-jenis-transaksi`.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 759 dan 760 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengasumsikan panel tetap terbuka.
  - TC 760 butir b menyebut urutan hasil pemulihan tanpa menyebut Sort; spec mengasumsikan Sort default (Date descending) setelah langkah 7.
