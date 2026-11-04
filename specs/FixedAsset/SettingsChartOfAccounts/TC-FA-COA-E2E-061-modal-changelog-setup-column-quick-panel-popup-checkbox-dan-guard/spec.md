---
id: TC-FA-COA-E2E-061-modal-changelog-setup-column-quick-panel-popup-checkbox-dan-guard
title: "Modal Changelog: Setup Column Quick Panel, Popup, Checkbox, dan Guard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-206
  - TC-FA-COA-207
  - TC-FA-COA-208
  - TC-FA-COA-213
coverage:
  web: automated
---

# Modal Changelog: Setup Column Quick Panel, Popup, Checkbox, dan Guard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat perubahan ada (minimal satu baris): riwayat Changelog P41 (asumsi pre-setup, bukan data PRD) atau entri lain yang dihasilkan spec lain; spec tidak mengasersi isi baris.
- Kolom tabel Changelog untuk langkah berulang 15 sampai 18:

  | Kolom |
  |---|
  | `Date` |
  | `Action` |
  | `Account Code` |
  | `Field` |
  | `Old Value` |
  | `New Value` |
  | `Modified By` |

- State yang diubah spec: tidak ada konfigurasi kolom yang disimpan; semua perubahan di popup dibuang dengan ikon ✕ tanpa `[Save]` (langkah 20 dan 28). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-206: Screening Quick Panel Column Visibility Changelog

1. Klik ikon Changelog di toolbar
2. Klik header kolom Actions ⋯ pada tabel Changelog
3. Verifikasi panel dropdown tampil dengan tujuh kolom data tercentang (Date, Action, Account Code, Field, Old Value, New Value, Modified By), masing-masing dengan checkbox dan kontrol drag
4. Verifikasi kolom Actions tidak muncul sebagai baris pada panel
5. Verifikasi item `Setup Column...` tampil di bagian bawah panel

### TC-FA-COA-207: Screening popup modal Setup Column Changelog

6. Klik `Setup Column...`
7. Verifikasi header berjudul `Setup Column` dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
8. Verifikasi ikon close ✕ tampil pada header
9. Verifikasi daftar tujuh kolom data berurutan Date, Action, Account Code, Field, Old Value, New Value, Modified By
10. Verifikasi tiap baris kolom memiliki checkbox, kontrol drag, dan kontrol pin
11. Verifikasi kolom Actions tidak muncul sebagai baris
12. Verifikasi footer berisi `Reset to Default` dan `Save`
13. Verifikasi tidak ada tombol `Cancel`

### TC-FA-COA-208: Ceklis dan unceklis kolom Changelog

14. Verifikasi sedikitnya satu kolom data tampil pada tabel Changelog di balik popup
15. Hapus centang kolom `Date` pada daftar popup
16. Verifikasi kolom `Date` hilang dari tabel Changelog di balik popup
17. Centang kembali kolom `Date`
18. Verifikasi kolom `Date` muncul kembali di tabel Changelog di balik popup
19. Ulangi langkah 15 sampai 18 untuk setiap kolom lain pada tabel Prerequisites (`Action`, `Account Code`, `Field`, `Old Value`, `New Value`, `Modified By`)
20. Tutup popup dengan ikon ✕

### TC-FA-COA-213: Guard satu kolom tersisa

21. Klik header kolom Actions ⋯ pada tabel Changelog, lalu klik `Setup Column...`
22. Hapus centang semua kolom kecuali Date
23. Arahkan kursor ke checkbox Date, lalu klik checkbox itu
24. Verifikasi checkbox Date Disabled dengan tooltip "At least one column must remain visible."
25. Verifikasi checkbox Date tetap tercentang
26. Centang kembali Action
27. Verifikasi checkbox Date Enabled kembali
28. Tutup popup dengan ikon ✕
29. Tutup modal Changelog dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (29 langkah nominal, sekitar 53 dengan ekspansi langkah 19): langkah 15 sampai 18 diulang untuk tujuh kolom (idiom 8b.7, parameter pada tabel Prerequisites, tanpa langkah bersyarat, `Verifikasi` tetap satu per klausa); seluruh blok memakai satu modal Changelog dan satu popup Setup Column (kelas fungsional Setup Column) dan tiap kolom berdiri sendiri.
- Langkah 19 mengulang langkah 15 sampai 18 untuk enam kolom lain.
- TC-208 langkah 2 (buka popup Setup Column) dipenuhi oleh popup yang masih terbuka dari langkah 6.
- Langkah penghubung (S-03): langkah 14 (anchor positif asersi hilangnya kolom, 8b.2), langkah 20 dan 28 (menutup popup tanpa `[Save]`), langkah 21 dan 22 (membuka ulang popup dan menyiapkan precondition TC-213), langkah 29 (menutup modal).
- Pemulihan Setup Column (R-24, 8b.14): spec tidak menyimpan konfigurasi kolom; semua perubahan dibuang dengan ✕ tanpa `[Save]`.
- Reorder, Reset to Default, dan tutup popup tanpa Save tabel Changelog dan pin dan unpin tabel Changelog ada di spec 062.
- Temuan untuk QA:
  - TC-208 tidak menyebut cara mengamati "tabel" di balik popup selain pratinjau; spec mengasersi tabel Changelog di balik popup.
  - Kolom Changelog tidak menyimpan konfigurasi pada TC-206, TC-207, TC-208, dan TC-213; tidak ada Post Condition yang membutuhkan observasi.
