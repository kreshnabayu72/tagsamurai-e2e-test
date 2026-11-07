---
id: TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3
title: "Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-603
  - TC-FA-SU-635
  - TC-FA-SU-667
  - TC-FA-SU-699
coverage:
  web: automated
---

# Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: f (binary buffer, isi berkas unduhan). Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27). Pengguna target: Budi Santoso dari Client `FaUserMain`.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas XLSX (nilai sel, tipe sel, nama kolom, dan nilai kosong) disediakan tim FE. Format tanggal dan jam acuan dibaca dari General Settings Client `FaUserMain` lewat kemampuan tim FE. Folder unduhan dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-603: Transformasi data Download Tab Changelog per tipe kolom

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Changelog
2. Klik icon Download
3. Pilih `Download as XLSX`
4. Buka berkas XLSX hasil unduhan
5. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
6. Verifikasi kolom bertipe name (Modified By): nama ditulis sebagai nama lengkap tanpa foto
7. Verifikasi kolom bertipe text (Action, Field, Old Value, New Value): teks ditulis apa adanya
8. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-635: Transformasi data Download Modal Changelog User > Global Role per tipe kolom

9. Buka Detail Budi Santoso > Tab Role > Sub-tab Global Role > icon Changelog
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Buka berkas XLSX hasil unduhan
13. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
14. Verifikasi kolom bertipe name (Modified By): nama ditulis sebagai nama lengkap tanpa foto
15. Verifikasi kolom bertipe text (Action, Role Name, Field, Old Value, New Value): teks ditulis apa adanya
16. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`
17. Tutup modal Changelog

### TC-FA-SU-667: Transformasi data Download Modal Changelog User > Group Role per tipe kolom

18. Buka Detail Budi Santoso > Tab Role > Sub-tab Group Role > icon Changelog
19. Klik icon Download
20. Pilih `Download as XLSX`
21. Buka berkas XLSX hasil unduhan
22. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
23. Verifikasi kolom bertipe name (Modified By): nama ditulis sebagai nama lengkap tanpa foto
24. Verifikasi kolom bertipe text (Action, Field, Old Value, New Value): teks ditulis apa adanya
25. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`
26. Tutup modal Changelog

### TC-FA-SU-699: Transformasi data Download Modal Changelog User > Transaction Role per tipe kolom

27. Buka Detail Budi Santoso > Tab Role > Sub-tab Transaction Role > icon Changelog
28. Klik icon Download
29. Pilih `Download as XLSX`
30. Buka berkas XLSX hasil unduhan
31. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
32. Verifikasi kolom bertipe name (Modified By): nama ditulis sebagai nama lengkap tanpa foto
33. Verifikasi kolom bertipe text (Action, Field, Old Value, New Value): teks ditulis apa adanya
34. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`
35. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Kelas f (isi berkas) dipisah dari kegagalan ekspor dan dari asersi nama berkas, nama kolom, dan jumlah baris yang berada di spec fungsional per surface (bagian 3 prinsip 13 butir f).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup modal Changelog. Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-603: format dan nama berkas TC-FA-SU-601 di spec 201, empty state, loading, dan error load TC-FA-SU-606 di spec 362, Download gagal TC-FA-SU-604 di spec 367.
  - TC-FA-SU-635: format dan nama berkas TC-FA-SU-633 di spec 211, empty state, loading, dan error load TC-FA-SU-638 di spec 376, Download gagal TC-FA-SU-636 di spec 369.
  - TC-FA-SU-667: format dan nama berkas TC-FA-SU-665 di spec 221, empty state, loading, dan error load TC-FA-SU-670 di spec 363, Download gagal TC-FA-SU-668 di spec 367.
  - TC-FA-SU-699: format dan nama berkas TC-FA-SU-697 di spec 229, empty state, loading, dan error load TC-FA-SU-702 di spec 363, Download gagal TC-FA-SU-700 di spec 367.
- Temuan untuk QA (S-15):
  - Acuan "ditulis apa adanya" (nilai di tabel UI atau data seed) tidak dinyatakan TC; spec membandingkan nilai sel berkas dengan nilai yang sama pada Pre-setup atau tabel surface lewat kemampuan baca berkas tim FE.
  - Format tanggal dan jam "mengikuti General Settings" tidak disebut nilainya; spec mengasersi kesesuaian dengan konfigurasi General Settings Client `FaUserMain` yang dibaca tim FE.
  - Klausa nilai kosong (`-`) hanya bermakna bila ada baris dengan sel kosong pada surface itu; Pre-setup yang dirujuk tidak menyatakan baris atau kolom yang kosong, sehingga klausa ini bergantung pada data yang sudah ada.
