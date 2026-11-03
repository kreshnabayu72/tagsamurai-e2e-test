---
id: TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6
title: "Modal Changelog: Search dan Filter (6/6)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-727
  - TC-FA-RP-728
  - TC-FA-RP-729
  - TC-FA-RP-730
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (6/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value, dan total pada info pagination dibandingkan dengan baseline yang dicatat di langkah spec. Spec ini tidak mengubah data.

## Test Steps

### Kombinasi Search lalu Filter (TC 727)

1. Klik ikon Changelog pada toolbar.
2. Catat total entri pada info pagination sebagai baseline.
3. Ketik Search `Auto`, tekan Enter.
4. Klik ikon Filter.
5. Pilih opsi `Siti Rahmawati` pada field Modified By.
6. Klik `[Apply]`.
7. Verifikasi tabel menampilkan irisan Search `Auto` dan Filter Modified By `Siti Rahmawati`: dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya entri seed Auto-Revert Fitri Handayani yang tampil.
8. Verifikasi Filter tidak mereset keyword Search: kotak Search masih berisi `Auto`.
9. Klik `[Clear Field]`, lalu klik `[Apply]`.
10. Klik ikon `(←)` pada kotak Search.

### Kombinasi Filter lalu Search (TC 728)

11. Pilih opsi `Siti Rahmawati` pada field Modified By.
12. Klik `[Apply]`.
13. Ketik Search `Auto`, tekan Enter.
14. Verifikasi tabel menampilkan irisan Filter Modified By `Siti Rahmawati` dan Search `Auto`: dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya entri seed Auto-Revert Fitri Handayani yang tampil.
15. Verifikasi kriteria Filter tetap aktif: panel Filter menampilkan chip `Siti Rahmawati` pada field Modified By.
16. Klik `[Clear Field]`, lalu klik `[Apply]`.
17. Klik ikon `(←)` pada kotak Search.

### Menutup Filter Panel tanpa `[Apply]` membuang draft (TC 729)

18. Pilih opsi `Assign` pada field Action tanpa `[Apply]`.
19. Klik ikon Filter lagi untuk menutup panel.
20. Verifikasi tabel tidak berubah: total pada info pagination sama dengan baseline langkah 2.
21. Klik ikon Filter untuk membuka panel kembali.
22. Verifikasi panel menampilkan nilai ter-Apply terakhir: field Action kosong (`All actions`) dan draft opsi `Assign` dibuang.

### Indikator filter aktif (TC 730)

23. Pilih opsi `Assign` pada field Action.
24. Klik `[Apply]`.
25. Verifikasi badge titik (tanpa angka) muncul pada ikon Filter saat panel terbuka.
26. Klik ikon Filter untuk menutup panel.
27. Verifikasi badge titik (tanpa angka) muncul pada ikon Filter saat panel tertutup.
28. Klik ikon Filter untuk membuka panel.
29. Klik `[Clear Field]`, lalu klik `[Apply]`.
30. Verifikasi badge titik hilang setelah filter di-clear.

## Notes

- Langkah penghubung (S-03): langkah 2 (mencatat total entri sebagai baseline untuk Expected TC 729 butir a "tabel tidak berubah"), 9, 10, 16, 17 (membersihkan Filter dan Search antar TC, sesuai S-09), 26 dan 28 (menutup dan membuka panel agar badge teramati pada kedua keadaan sesuai Expected TC 730).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 727 dan 728 menyebut Expected "irisan" tanpa pembanding baris selain Auto-Revert Fitri Handayani; hasil gabungan identik dengan Search `Auto` saja, sehingga asersi tidak membedakan Filter dari Search.
  - TC 727 sampai 730 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengasumsikan panel tetap terbuka (langkah 26 menutup dan 28 membuka kembali panel).
