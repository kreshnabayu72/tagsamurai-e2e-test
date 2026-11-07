---
id: TC-FA-SU-E2E-371-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-2
title: "Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-497
  - TC-FA-SU-533
  - TC-FA-SU-571
coverage:
  web: automated
---

# Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: f (binary buffer, isi berkas unduhan). Data Pre-setup: Client `FaUserMain` (#20), Responsibilities (#25), Non-Login User (#26) dan Custom Field `Shift` (#31). Pengguna target: Budi Santoso dari Client `FaUserMain`.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas XLSX (nilai sel, tipe sel, nama kolom, dan nilai kosong) disediakan tim FE. Format tanggal dan jam acuan dibaca dari General Settings Client `FaUserMain` lewat kemampuan tim FE. Folder unduhan dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend. Visibilitas kolom pada overlay Column Visibility tidak disimpan; preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-SU-497: Transformasi data Download Sub-tab Pending Approvals per tipe kolom

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Approvals
2. Klik icon Download
3. Pilih `Download as XLSX`
4. Buka berkas XLSX hasil unduhan
5. Verifikasi kolom bertipe date (Submission Date): tanggal dan jam mengikuti General Settings
6. Verifikasi kolom bertipe name (Requester): nama ditulis sebagai nama lengkap tanpa foto
7. Verifikasi kolom bertipe text (Transaction ID): teks ditulis apa adanya
8. Verifikasi kolom bertipe badge (Transaction) ditulis sebagai label teks tanpa warna
9. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-533: Transformasi data Download Sub-tab Pending Tasks per tipe kolom

10. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks
11. Klik icon Download
12. Pilih `Download as XLSX`
13. Buka berkas XLSX hasil unduhan
14. Verifikasi kolom bertipe badge (Status) ditulis sebagai label teks tanpa warna
15. Verifikasi kolom bertipe date (Request Date, Last Updated): tanggal dan jam mengikuti General Settings
16. Verifikasi kolom bertipe name (PIC): nama ditulis sebagai nama lengkap tanpa foto
17. Verifikasi kolom bertipe num (Total Asset): angka ditulis sebagai nilai numerik asli
18. Verifikasi kolom bertipe text (Transaction ID, Group): teks ditulis apa adanya
19. Verifikasi kolom bertipe badge (Transaction) ditulis sebagai label teks tanpa warna
20. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-571: Transformasi data Download Tab Non-Login User per tipe kolom

21. Buka Detail Budi Santoso > Tab Non-Login User
22. Klik header kolom Column Visibility (⋯)
23. Centang kolom curated yang belum tampil pada overlay Column Visibility sampai seluruh kolom pada Data TC tampil: Name, Email, Employee ID, Position, Division, Active, Last Update, Temporary User, Temporary Until, Shift
24. Tutup overlay Column Visibility dengan Esc
25. Klik icon Download
26. Pilih `Download as XLSX`
27. Buka berkas XLSX hasil unduhan
28. Verifikasi kolom bertipe badge (Active) ditulis sebagai label teks tanpa warna
29. Verifikasi kolom bertipe date (Last Update, Temporary Until): tanggal dan jam mengikuti General Settings
30. Verifikasi kolom bertipe name (Name): nama ditulis sebagai nama lengkap tanpa foto
31. Verifikasi kolom bertipe text (Email, Employee ID, Position, Division, Shift): teks ditulis apa adanya
32. Verifikasi kolom bertipe yesno (Temporary User): badge Yes atau No ditulis `Yes` atau `No`
33. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Kelas f (isi berkas) dipisah dari kegagalan ekspor dan dari asersi nama berkas, nama kolom, dan jumlah baris yang berada di spec fungsional per surface (bagian 3 prinsip 13 butir f).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengaktifkan kolom curated lewat overlay Column Visibility dan menutup overlay. Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-497: format dan nama berkas TC-FA-SU-495 di spec 167, empty state, loading, dan error load TC-FA-SU-500 di spec 361, Download gagal TC-FA-SU-498 di spec 366.
  - TC-FA-SU-533: format dan nama berkas TC-FA-SU-531 di spec 180, empty state, loading, dan error load TC-FA-SU-536 di spec 361, Download gagal TC-FA-SU-534 di spec 369.
  - TC-FA-SU-571: format dan nama berkas TC-FA-SU-569 di spec 191, empty state, loading, dan error load TC-FA-SU-574 di spec 362, Download gagal TC-FA-SU-572 di spec 367.
- Temuan untuk QA (S-15):
  - Acuan "ditulis apa adanya" (nilai di tabel UI atau data seed) tidak dinyatakan TC; spec membandingkan nilai sel berkas dengan nilai yang sama pada Pre-setup atau tabel surface lewat kemampuan baca berkas tim FE.
  - Format tanggal dan jam "mengikuti General Settings" tidak disebut nilainya; spec mengasersi kesesuaian dengan konfigurasi General Settings Client `FaUserMain` yang dibaca tim FE.
  - Klausa nilai kosong (`-`) hanya bermakna bila ada baris dengan sel kosong pada surface itu; Pre-setup yang dirujuk tidak menyatakan baris atau kolom yang kosong, sehingga klausa ini bergantung pada data yang sudah ada.
  - TC-FA-SU-571: TC tidak menyebut kolom curated mana yang "diaktifkan lebih dulu"; spec mengaktifkan kolom pada daftar Data TC yang belum tampil.
  - TC-FA-SU-497 butir c dan TC-FA-SU-533 butir e memuat dua klausa (text dan badge) dalam satu butir; spec memecahnya menjadi dua `Verifikasi`.
