---
id: TC-FA-RP-E2E-149-tab-total-control-setup-column-5
title: "Tab Total Control: Setup Column (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-513
  - TC-FA-RP-514
coverage:
  web: automated
---

# Tab Total Control: Setup Column (5/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Guard satu kolom tersisa (TC 513)

1. Buka popup Setup Column.
2. Hapus centang kolom `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated` sehingga hanya kolom `Name` yang tercentang.
3. Arahkan kursor ke checkbox kolom `Name`.
4. Verifikasi checkbox kolom `Name` Disabled dengan tooltip `At least one column must remain visible.`
5. Klik `(X)` untuk menutup popup tanpa menyimpan.

### Konfigurasi kolom tidak memengaruhi tabel lain (TC 514)

6. Buka popup Setup Column, hapus centang kolom `Division`, lalu klik `[Save]`.
7. Klik Tab `Read Only`.
8. Verifikasi tabel Tab Read Only tetap memakai konfigurasi kolomnya sendiri (kolom `Division` tampil).
9. Klik Tab `Total Control`.
10. Buka popup Setup Column, centang kolom `Division`, lalu klik `[Save]`.

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 3, 5, 6, 7, 9, dan 10. Langkah 5 menutup popup tanpa menyimpan supaya kolom tidak berubah; langkah 10 memulihkan kolom `Division` (S-09).
- Temuan untuk QA:
  - TC 514 menyebut "tabel lain pada modul (tab lain atau modal Changelog)" dan "ubah dan Save susunan kolom" tanpa merinci perubahan; spec memakai Tab Read Only sebagai tabel lain dan menyembunyikan kolom `Division` sebagai perubahan. Modal Changelog tidak diuji di spec ini.
  - TC 513 tidak menyebut kolom yang tersisa; spec menyisakan `Name`.
