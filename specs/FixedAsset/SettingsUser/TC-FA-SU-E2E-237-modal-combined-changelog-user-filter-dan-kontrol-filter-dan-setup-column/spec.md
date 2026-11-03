---
id: TC-FA-SU-E2E-237-modal-combined-changelog-user-filter-dan-kontrol-filter-dan-setup-column
title: "Modal Combined Changelog: User: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-721
  - TC-FA-SU-722
  - TC-FA-SU-723
coverage:
  web: automated
---

# Modal Combined Changelog: User: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-721: Chip dan checkbox dropdown Filter

1. Klik icon Changelog di Table Tools halaman User List
2. Klik icon Filter
3. Buka dropdown Action
4. Centang dua opsi (`Activate` dan `Assign`), klik `[Apply]`
5. Verifikasi dua chip tampil di dalam field
6. Verifikasi hasil adalah gabungan (OR) kedua opsi
7. Klik ✕ pada satu chip tanpa membuka dropdown
8. Verifikasi chip itu hilang
9. Verifikasi checkbox opsi terkait ter-uncheck
10. Verifikasi chip lain tetap
11. Buka dropdown Action
12. Hilangkan centang opsi yang tersisa
13. Verifikasi chip yang bersangkutan hilang
14. Centang dua opsi (`Activate` dan `Assign`) lalu hilangkan centang satu opsi
15. Verifikasi chip opsi yang di-uncheck hilang
16. Verifikasi chip lain tetap
17. Ketik `ass` pada kotak cari dropdown
18. Verifikasi opsi dipersempit (substring, tidak case-sensitive)
19. Ganti isi kotak cari dropdown dengan `zzzz`
20. Verifikasi `No results found` tampil di dropdown
21. Kosongkan kotak cari dropdown, tutup dropdown, lalu klik `[Clear Field]` dan `[Apply]`

### TC-FA-SU-722: Screening Overlay Column Visibility

22. Klik header kolom Actions (⋯)
23. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
24. Verifikasi daftar kolom berurutan Date, Action, User Name, Field, Old Value, New Value, Modified By dengan checkbox Hideable terpilih dan enabled serta drag handle
25. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-723: Screening Popup Setup Column dan Preview Table

26. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
27. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
28. Verifikasi body: daftar kolom Date, Action, User Name, Field, Old Value, New Value, Modified By dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
29. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
30. Klik ✕ untuk menutup popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC-FA-SU-721 langkah 6 menyebut kata kunci tanpa hasil di kotak cari dropdown tanpa nilai konkret; spec memakai `zzzz` dan `ass` sebagai pilihan sendiri. Opsi yang dicentang (`Activate` dan `Assign`) juga pilihan spec karena TC tidak menyebutnya.
