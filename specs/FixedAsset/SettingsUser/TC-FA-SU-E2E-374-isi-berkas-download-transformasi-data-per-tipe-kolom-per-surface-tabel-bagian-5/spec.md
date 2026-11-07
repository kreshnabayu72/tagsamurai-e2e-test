---
id: TC-FA-SU-E2E-374-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-5
title: "Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 5)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-866
  - TC-FA-SU-890
coverage:
  web: automated
---

# Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: f (binary buffer, isi berkas unduhan). Data Pre-setup: Client `FaUserMain` (#20), User Log (#30). Pengguna target: Budi Santoso dari Client `FaUserMain`.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas XLSX (nilai sel, tipe sel, nama kolom, dan nilai kosong) disediakan tim FE. Format tanggal dan jam acuan dibaca dari General Settings Client `FaUserMain` lewat kemampuan tim FE. Folder unduhan dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-866: Transformasi data Download Tab User Log sub-tab Assignment per tipe kolom

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab User Log > Sub-tab Assignment
2. Klik icon Download
3. Pilih `Download as XLSX`
4. Buka berkas XLSX hasil unduhan
5. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
6. Verifikasi kolom bertipe name (PIC): nama ditulis sebagai nama lengkap tanpa foto
7. Verifikasi kolom bertipe text (Activity, Transaction ID, Name): teks ditulis apa adanya
8. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

### TC-FA-SU-890: Transformasi data Download Tab User Log sub-tab Session per tipe kolom

9. Buka Detail Budi Santoso > Tab User Log > Sub-tab Session
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Buka berkas XLSX hasil unduhan
13. Verifikasi kolom bertipe date (Date): tanggal dan jam mengikuti General Settings
14. Verifikasi kolom bertipe text (Activity, Status, Note, IP Address, Device/Browser): teks ditulis apa adanya
15. Verifikasi nilai kosong ditulis `-` (hyphen tunggal), bukan blank atau `—`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Kelas f (isi berkas) dipisah dari kegagalan ekspor dan dari asersi nama berkas, nama kolom, dan jumlah baris yang berada di spec fungsional per surface (bagian 3 prinsip 13 butir f). Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-866: format dan nama berkas TC-FA-SU-864 di spec 284, empty state, loading, dan error load TC-FA-SU-869 di spec 365, Download gagal TC-FA-SU-867 di spec 369.
  - TC-FA-SU-890: format dan nama berkas TC-FA-SU-888 di spec 291, empty state, loading, dan error load TC-FA-SU-893 di spec 365, Download gagal TC-FA-SU-891 di spec 369.
- Temuan untuk QA (S-15):
  - Acuan "ditulis apa adanya" (nilai di tabel UI atau data seed) tidak dinyatakan TC; spec membandingkan nilai sel berkas dengan nilai yang sama pada Pre-setup atau tabel surface lewat kemampuan baca berkas tim FE.
  - Format tanggal dan jam "mengikuti General Settings" tidak disebut nilainya; spec mengasersi kesesuaian dengan konfigurasi General Settings Client `FaUserMain` yang dibaca tim FE.
  - Klausa nilai kosong (`-`) hanya bermakna bila ada baris dengan sel kosong pada surface itu; Pre-setup yang dirujuk tidak menyatakan baris atau kolom yang kosong, sehingga klausa ini bergantung pada data yang sudah ada.
