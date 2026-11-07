---
id: TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4
title: "Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 4)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-731
  - TC-FA-SU-761
  - TC-FA-SU-792
  - TC-FA-SU-833
coverage:
  web: automated
---

# Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: f (binary buffer, isi berkas unduhan). Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27), System Log (#28), Transaction Admin Log (#29), User Log (#30). Pengguna target: Budi Santoso dari Client `FaUserMain`; surface User List memakai seluruh populasi 25 pengguna Client.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas XLSX (nilai sel, tipe sel, nama kolom, dan nilai kosong) disediakan tim FE. Format tanggal dan jam acuan dibaca dari General Settings Client `FaUserMain` lewat kemampuan tim FE. Folder unduhan dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-731: Transformasi data Download Modal Combined Changelog: User per tipe kolom

1. Klik icon Changelog di halaman User List
2. Klik icon Download
3. Pilih `Download as XLSX`
4. Buka berkas XLSX hasil unduhan
5. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
6. Verifikasi kolom bertipe name (Modified By): nama ditulis sebagai nama lengkap tanpa foto
7. Verifikasi kolom bertipe text (Action, User Name, Field, Old Value, New Value): teks ditulis apa adanya
8. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`
9. Tutup modal Changelog

### TC-FA-SU-761: Transformasi data Download Tab System Log per tipe kolom

10. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab System Log
11. Klik icon Download
12. Pilih `Download as XLSX`
13. Buka berkas XLSX hasil unduhan
14. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
15. Verifikasi kolom bertipe text (Action, Object, Name, Field, Old Value, New Value): teks ditulis apa adanya
16. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-792: Transformasi data Download Tab Transaction Admin Log sub-tab Borrowing & Assignment per tipe kolom

17. Buka Detail Budi Santoso > Tab Transaction Admin Log > Sub-tab Borrowing & Assignment
18. Klik icon Download
19. Pilih `Download as XLSX`
20. Buka berkas XLSX hasil unduhan
21. Verifikasi kolom bertipe badge (Role) ditulis sebagai label teks tanpa warna
22. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
23. Verifikasi kolom bertipe text (Transaction ID, Group, Action Taken, Transaction Status): teks ditulis apa adanya
24. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-833: Transformasi data Download Tab User Log sub-tab Borrow per tipe kolom

25. Buka Detail Budi Santoso > Tab User Log > Sub-tab Borrow
26. Klik icon Download
27. Pilih `Download as XLSX`
28. Buka berkas XLSX hasil unduhan
29. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
30. Verifikasi kolom bertipe name (PIC): nama ditulis sebagai nama lengkap tanpa foto
31. Verifikasi kolom bertipe text (Activity, Transaction ID, Name): teks ditulis apa adanya
32. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Kelas f (isi berkas) dipisah dari kegagalan ekspor dan dari asersi nama berkas, nama kolom, dan jumlah baris yang berada di spec fungsional per surface (bagian 3 prinsip 13 butir f).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup modal Changelog. Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 10, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-731: format dan nama berkas TC-FA-SU-729 di spec 240, empty state, loading, dan error load TC-FA-SU-734 di spec 375, Download gagal TC-FA-SU-732 di spec 368.
  - TC-FA-SU-761: format dan nama berkas TC-FA-SU-759 di spec 250, empty state, loading, dan error load TC-FA-SU-764 di spec 364, Download gagal TC-FA-SU-762 di spec 368.
  - TC-FA-SU-792: format dan nama berkas TC-FA-SU-790 di spec 262, empty state, loading, dan error load TC-FA-SU-795 di spec 364, Download gagal TC-FA-SU-793 di spec 368.
  - TC-FA-SU-833: format dan nama berkas TC-FA-SU-831 di spec 274, empty state, loading, dan error load TC-FA-SU-836 di spec 376, Download gagal TC-FA-SU-834 di spec 368.
- Temuan untuk QA (S-15):
  - Acuan "ditulis apa adanya" (nilai di tabel UI atau data seed) tidak dinyatakan TC; spec membandingkan nilai sel berkas dengan nilai yang sama pada Pre-setup atau tabel surface lewat kemampuan baca berkas tim FE.
  - Format tanggal dan jam "mengikuti General Settings" tidak disebut nilainya; spec mengasersi kesesuaian dengan konfigurasi General Settings Client `FaUserMain` yang dibaca tim FE.
  - Klausa nilai kosong (`-`) hanya bermakna bila ada baris dengan sel kosong pada surface itu; Pre-setup yang dirujuk tidak menyatakan baris atau kolom yang kosong, sehingga klausa ini bergantung pada data yang sudah ada.
  - TC-FA-SU-731: Combined Changelog memuat riwayat seluruh pengguna Client dan audit trail permanen yang tumbuh; asersi hanya berdasarkan tipe kolom, bukan posisi atau jumlah baris tertentu (S-14).
