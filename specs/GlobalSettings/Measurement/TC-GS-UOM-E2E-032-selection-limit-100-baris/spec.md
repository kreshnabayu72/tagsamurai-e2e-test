---
id: TC-GS-UOM-E2E-032-selection-limit-100-baris
title: "Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-112
  - TC-GS-UOM-278
coverage:
  web: automated
---

# Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap

## Prerequisites

- Mode: FE+BE. Spec hanya membaca dan memilih baris; tidak ada data dibuat, diubah, atau dihapus.
- Akun: Total Control Client Limit, Wulan Sari, `totalControl_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_LIMIT_TC_PASSWORD` dan `GS_TC_PASSWORD` (pemulihan sesi di hook `after`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement untuk akun Client Limit: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Fixture yang perlu disiapkan tim FE (belum ada): Client Limit dengan Selection Limit 100 dan Master Data Count Limit 1.000 (nilai minimum, System Limits di Admin Console > Plans & Licensing > Lifecycle Settings), berisi tepat 999 unit `Lim 001` sampai `Lim 999` (D-28) yang dibuat lewat Import Type Measurement. Hook `before` memastikan jumlah unit 999 dan Selection Limit 100 sebelum spec berjalan. Total baris tabel N = 999 diturunkan dari seeding (butir 10 bagian 8b).
- Opsi page size 100 tersedia pada pagination tabel.
- State global bersama: spec 022 (Master Data Count Limit) dan spec ini memakai tenant Client Limit yang sama dengan jumlah unit sebagai syarat. Keduanya dijalankan serial (suite `parallel: false`); spec ini mensyaratkan tepat 999 unit dan tidak mengubah jumlahnya.
- Cleanup: hook `after` memulihkan page size dan seleksi tabel ke default (page size 10, tanpa seleksi). Spec tidak mengubah Selection Limit.

## Test Steps

### TC-GS-UOM-112: Selection Limit memblokir checkbox ke-(limit+1) saat seleksi manual

1. Ubah page size tabel menjadi 100
2. Klik checkbox header pada halaman 1 (100 baris tercentang)
3. Verifikasi 100 baris halaman 1 tercentang
4. Verifikasi Bulk Action Bar menampilkan `100 units selected`
5. Pindah ke halaman 2
6. Arahkan kursor ke checkbox baris pertama halaman 2
7. Coba centang checkbox baris pertama halaman 2
8. Verifikasi checkbox baris pertama halaman 2 tampil namun disabled
9. Verifikasi tooltip `You've reached the maximum selection of 100 rows.`
10. Verifikasi 100 baris halaman 1 tetap tercentang
11. Verifikasi Bulk Action Bar menampilkan `100 units selected`
12. Verifikasi Bulk Action Bar tetap aktif untuk 100 baris terpilih
13. Klik icon `✕` pada Bulk Action Bar

### TC-GS-UOM-278: Selection Limit: Select All di-cap otomatis ke limit dengan toast error

14. Centang satu baris
15. Klik `Select All (999 records)`
16. Verifikasi hanya 100 baris pertama terpilih
17. Verifikasi counter menampilkan `100 units selected`
18. Verifikasi toast error: `Error, only the first 100 of 999 rows were selected. Narrow your filter to include the rest.`
19. Verifikasi Bulk Action Bar tetap tampil
20. Klik `Bulk Action`
21. Verifikasi aksi `Delete` tersedia pada overlay `Bulk Action` (Bulk Action Bar dapat dipakai untuk 100 baris terpilih)
22. Tekan Esc (menutup overlay tanpa memilih aksi)
23. Klik icon `✕` pada Bulk Action Bar
24. Verifikasi toast error tetap tampil dan tidak hilang otomatis (persisten sampai di-dismiss)
25. Tutup toast error
26. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 26.
- Kelas harness: volume data (999 unit, prinsip 13e), satu spec tersendiri. Spec Master Data Count Limit (spec 022) memakai tenant yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 (membatalkan seleksi sebelum TC-278, TC sumber mencatatnya di Post Condition), 22 dan 23 (menutup overlay tanpa memilih `Delete` supaya tidak ada data terhapus dan membersihkan seleksi), 25 (mendismiss toast persisten), dan 26 (memulihkan page size).
- Langkah 3 dan 4 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC-GS-UOM-112: membuktikan 100 baris halaman 1 tercentang sebelum pindah ke halaman 2.
- Langkah 24 (asersi toast error persisten, Expected TC-GS-UOM-278 butir b) ditaruh sesudah langkah 19 sampai 23 supaya toast terbukti masih tampil sesudah jeda aksi, tidak langsung sesudah toast muncul.
- Langkah 2: TC menulis "klik checkbox header pada halaman 1 (100 baris tercentang)"; sesuai.
- Langkah 21 mengasersi `Delete` tersedia sebagai bentuk konkret "Bulk Action Bar tetap tampil dan dapat dipakai" pada Expected TC-278 butir c; langkah 19 mengasersi bar tetap tampil.
- Tooltip pada langkah 9 diasersi sebelum klik berikutnya yang mengubah state (butir 5 bagian 8b).
- Tidak ada pembagian TC lintas spec; seluruh TC sumber spec ini dikerjakan di sini.
- Temuan untuk QA: TC-GS-UOM-112 dan TC-GS-UOM-278 mengasumsikan tabel Client Limit berisi tepat 999 unit (D-28); jika ada sisa unit dari spec lain di tenant itu, N pada toast berubah. Bergantung pada hook `before` yang memastikan 999 unit.
