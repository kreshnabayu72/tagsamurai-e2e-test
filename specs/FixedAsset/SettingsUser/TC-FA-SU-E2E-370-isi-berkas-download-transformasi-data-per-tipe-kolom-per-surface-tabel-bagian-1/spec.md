---
id: TC-FA-SU-E2E-370-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-1
title: "Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-362
  - TC-FA-SU-437
  - TC-FA-SU-466
coverage:
  web: automated
---

# Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: f (binary buffer, isi berkas unduhan). Data Pre-setup: Client `FaUserMain` (#20), Custom Field `Shift` (#31), Responsibilities (#24). Pengguna target: Budi Santoso dari Client `FaUserMain`; surface User List memakai seluruh populasi 25 pengguna Client.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas XLSX (nilai sel, tipe sel, nama kolom, dan nilai kosong) disediakan tim FE. Format tanggal dan jam acuan dibaca dari General Settings Client `FaUserMain` lewat kemampuan tim FE. Folder unduhan dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend. Visibilitas kolom pada overlay Column Visibility tidak disimpan; preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-SU-362: Transformasi data Download User List per tipe kolom

1. Klik header kolom Column Visibility (⋯)
2. Centang kolom curated yang belum tampil pada overlay Column Visibility sampai seluruh kolom pada Data TC tampil: Active, Name, Email, Role, Home Group, Position, Division, Employee ID, Modified By, Last Updated, Activation Status, Temporary User, Temporary Until, TAG, Shift
3. Tutup overlay Column Visibility dengan Esc
4. Klik icon Download
5. Pilih `Download as XLSX`
6. Buka berkas XLSX hasil unduhan
7. Verifikasi kolom bertipe badge (Activation Status) ditulis sebagai label teks tanpa warna dengan nilai literal `Activated`, `Pending Activation`, atau `Pending Email Confirmation`
8. Verifikasi kolom bertipe date (Last Updated, Temporary Until): tanggal dan jam mengikuti General Settings
9. Verifikasi kolom bertipe name (Name): nama ditulis sebagai nama lengkap tanpa foto dan tanpa badge Pending (`Hana Kusuma` dan `Indra Wijaya` yang berstatus Pending tertulis nama saja)
10. Verifikasi kolom bertipe rolecount (Role): label jumlah peran atau badge tier ditulis apa adanya
11. Verifikasi kolom bertipe text (Email, Home Group, Position, Division, Employee ID, Modified By, TAG, Shift): teks ditulis apa adanya
12. Verifikasi kolom bertipe toggle (Active): switch ditulis `Active` atau `Inactive`
13. Verifikasi kolom bertipe yesno (Temporary User): badge Yes atau No ditulis `Yes` atau `No`
14. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-437: Transformasi data Download Sub-tab Borrowed Assets per tipe kolom

15. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
16. Klik icon Download
17. Pilih `Download as XLSX`
18. Buka berkas XLSX hasil unduhan
19. Verifikasi kolom bertipe badge (Brand, Model / Type) ditulis sebagai label teks tanpa warna
20. Verifikasi kolom bertipe date (Due Return Date): tanggal dan jam mengikuti General Settings
21. Verifikasi kolom bertipe name (PIC): nama ditulis sebagai nama lengkap tanpa foto
22. Verifikasi kolom bertipe photo (Photo): kolom foto tidak diikutsertakan
23. Verifikasi kolom bertipe text (Name, Asset ID, Transaction ID): teks ditulis apa adanya
24. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-466: Transformasi data Download Sub-tab Assigned Assets per tipe kolom

25. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Assigned Assets
26. Klik icon Download
27. Pilih `Download as XLSX`
28. Buka berkas XLSX hasil unduhan
29. Verifikasi kolom bertipe badge (Brand, Model / Type) ditulis sebagai label teks tanpa warna
30. Verifikasi kolom bertipe name (PIC): nama ditulis sebagai nama lengkap tanpa foto
31. Verifikasi kolom bertipe photo (Photo): kolom foto tidak diikutsertakan
32. Verifikasi kolom bertipe text (Name, Asset ID, Transaction ID): teks ditulis apa adanya
33. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Kelas f (isi berkas) dipisah dari kegagalan ekspor dan dari asersi nama berkas, nama kolom, dan jumlah baris yang berada di spec fungsional per surface (bagian 3 prinsip 13 butir f).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengaktifkan kolom curated lewat overlay Column Visibility dan menutup overlay.
- Pembagian TC lintas spec:
  - TC-FA-SU-362: format dan nama berkas TC-FA-SU-360 di spec 127, empty state, loading, dan error load TC-FA-SU-365 di spec 375, Download gagal TC-FA-SU-363 di spec 366.
  - TC-FA-SU-437: format dan nama berkas TC-FA-SU-435 di spec 147, empty state, loading, dan error load TC-FA-SU-440 di spec 360, Download gagal TC-FA-SU-438 di spec 366.
  - TC-FA-SU-466: format dan nama berkas TC-FA-SU-464 di spec 159, empty state, loading, dan error load TC-FA-SU-469 di spec 361, Download gagal TC-FA-SU-467 di spec 366.
- Temuan untuk QA (S-15):
  - Acuan "ditulis apa adanya" (nilai di tabel UI atau data seed) tidak dinyatakan TC; spec membandingkan nilai sel berkas dengan nilai yang sama pada Pre-setup atau tabel surface lewat kemampuan baca berkas tim FE.
  - Format tanggal dan jam "mengikuti General Settings" tidak disebut nilainya; spec mengasersi kesesuaian dengan konfigurasi General Settings Client `FaUserMain` yang dibaca tim FE.
  - Klausa nilai kosong (`-`) hanya bermakna bila ada baris dengan sel kosong pada surface itu; Pre-setup yang dirujuk tidak menyatakan baris atau kolom yang kosong, sehingga klausa ini bergantung pada data yang sudah ada.
  - TC-FA-SU-362: TC tidak menyebut kolom curated mana yang "diaktifkan lebih dulu"; spec mengaktifkan kolom pada daftar Data TC yang belum tampil.
  - TC-FA-SU-437 dan 466: daftar Data menyebut kolom Photo, sedangkan butir Expected menyatakan kolom foto tidak diikutsertakan; spec mengasersi kolom Photo tidak ada pada berkas.
