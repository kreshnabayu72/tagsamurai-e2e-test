---
id: TC-FA-RP-E2E-215-table-user-picker-setup-column-5
title: "Table User Picker: Setup Column (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-700
  - TC-FA-RP-701
coverage:
  web: automated
---

# Table User Picker: Setup Column (5/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat) dan #37 (Tab Read Only empat baris: Dewi Anggraini, Maya Anggraeni, Yoga Pratama, Gilang Prakoso). Pre-setup #36 dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Kolom bawaan tampil Tab Read Only (TC 701): `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.

## Test Steps

### Guard satu kolom tersisa (TC 700)

1. Klik `[+ Assign]`.
2. Klik header `(⋯)`, lalu klik `Setup Column...`.
3. Hapus centang semua kolom kecuali `Name`.
4. Arahkan kursor ke checkbox kolom terakhir (`Name`).
5. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
6. Klik `(X)` untuk menutup popup Setup Column tanpa menyimpan.

### Konfigurasi kolom tidak memengaruhi tabel lain (TC 701)

7. Klik header `(⋯)`, lalu klik `Setup Column...`.
8. Hapus centang kolom `Division`.
9. Klik `[Save]`.
10. Tutup popup Assign.
11. Klik Tab `Read Only`.
12. Verifikasi tabel Tab Read Only tetap memakai konfigurasi kolomnya sendiri: kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated` tampil.
13. Klik Tab `Total Control`.

## Notes

- Langkah penghubung (S-03): langkah 6 (menutup popup Setup Column tanpa menyimpan), 10 (menutup popup Assign), dan 13 (kembali ke Tab `Total Control`). Konfigurasi kolom hasil langkah 9 tidak dipulihkan di dalam spec; hook `after` menghapus preferensi kolom di browser.
- Tabel lain pada TC 701 dipilih Tab Read Only (opsi "tab lain" pada TC); tabel Tab Read Only menampilkan kolom bawaan sama dengan Tab Total Control.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 700 tidak menyebut kolom yang dipertahankan sebagai "satu kolom"; spec memilih `Name`.
  - TC 701 tidak menyebut perubahan konkret yang disimpan ("susunan kolom"); spec memilih menyembunyikan `Division` dan menyebut dua opsi tabel lain ("tab lain atau modal Changelog") hanya sebagai Tab Read Only.
