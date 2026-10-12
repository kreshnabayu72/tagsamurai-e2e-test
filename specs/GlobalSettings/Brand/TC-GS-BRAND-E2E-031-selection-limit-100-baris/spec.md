---
id: TC-GS-BRAND-E2E-031-selection-limit-100-baris
title: "Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-127
  - TC-GS-BRAND-128
coverage:
  web: automated
---

# Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap

## Prerequisites

- Mode: FE+BE. Spec hanya membaca dan memilih baris; tidak ada data dibuat, diubah, atau dihapus.
- Akun: Total Control Client Limit, `Wulan Sari`, `totalControl_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_LIMIT_TC_PASSWORD` dan `GS_TC_PASSWORD` (pemulihan sesi di hook `after`). Password tidak ditulis di spec atau fixture.
- Fixture yang perlu disiapkan tim FE (belum ada): Client Limit dengan Selection Limit 100 dan Master Data Count Limit 1.000, berisi tepat 999 brand `Lim 001` sampai `Lim 999` (D-26) yang dibuat lewat Import Type Brand. Hook `before` memastikan jumlah brand 999 dan Selection Limit 100 sebelum spec berjalan.
- Opsi page size 100 tersedia pada paginasi tabel.
- State global bersama: spec 031, 032, dan 033 memakai tenant Client Limit yang sama dengan jumlah brand sebagai syarat. Ketiganya dijalankan serial (tidak paralel satu sama lain); spec ini mensyaratkan tepat 999 brand dan tidak mengubah jumlahnya. Spec 032 dan 033 memulihkan jumlah brand ke 999 di hook `after` masing-masing.
- Cleanup: hook `after` memulihkan page size dan seleksi tabel ke default (page size 10, tanpa seleksi). Spec tidak mengubah Selection Limit.
- TC-GS-BRAND-127: Selection Limit 100, 999 brand (D-26).
- TC-GS-BRAND-128: Selection Limit 100, 999 brand (D-26).

## Test Steps

### TC-GS-BRAND-127: Selection Limit: centang baris ke-101 secara manual diblokir

1. Ubah page size tabel menjadi 100
2. Centang seluruh 100 baris halaman 1 lewat checkbox header
3. Verifikasi 100 baris halaman 1 tercentang dan Bulk Action Bar tampil dengan counter `100 brands selected`
4. Pindah ke halaman 2
5. Arahkan kursor (hover) ke checkbox baris pertama halaman 2
6. Coba centang checkbox baris pertama halaman 2
7. Verifikasi checkbox baris ke-101 disabled dengan tooltip `You've reached the maximum selection of 100 rows.`
8. Verifikasi 100 baris tetap tercentang
9. Verifikasi Bulk Action Bar tetap aktif

### TC-GS-BRAND-128: Selection Limit: Select All di-cap ke 100 baris

10. Klik icon `(✕)` pada Bulk Action Bar
11. Centang satu baris
12. Klik `Select All (999 records)`
13. Verifikasi toast error: "Error, only the first 100 of 999 rows were selected. Narrow your filter to include the rest."
14. Verifikasi toast error tetap tampil dan tidak hilang otomatis (persisten)
15. Verifikasi counter `100 brands selected`
16. Klik `Bulk Action`
17. Verifikasi dropdown terbuka dan aksi `Delete` tersedia (Bulk Action Bar dapat dipakai)
18. Tutup dropdown `Bulk Action` tanpa memilih aksi
19. Klik icon `(✕)` pada Bulk Action Bar
20. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): 10 (reset seleksi sebelum TC-GS-BRAND-128), 16 (membuka dropdown `Bulk Action` untuk memeriksa Bulk Action Bar dapat dipakai, sebelum langkah 17), 18 sampai 20 (menutup dropdown tanpa memilih `Delete` supaya tidak ada data terhapus, membersihkan seleksi, dan memulihkan page size).
- Langkah 2: TC menulis "Centang 100 baris halaman 1"; spec memakai checkbox header karena memilih seluruh baris halaman aktif (TC-GS-BRAND-109).
- Asersi tambahan: langkah 3 (100 baris tercentang dan counter `100 brands selected`) memastikan batas 100 tercapai sebelum pindah halaman, sebagai kondisi bagi Expected Result a TC-GS-BRAND-127. Langkah 17 mengasersi `Delete` tersedia sebagai bentuk konkret "Bulk Action Bar dapat dipakai" pada Expected Result b TC-GS-BRAND-128.
- Kelas harness: volume data (999 brand, prinsip 13e), satu spec tersendiri. Spec Master Data Count Limit memakai fixture yang sama di spec `TC-GS-BRAND-E2E-032-master-data-count-limit-create-dan-dialog` dan `TC-GS-BRAND-E2E-033-master-data-count-limit-race-slot-terakhir`.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
