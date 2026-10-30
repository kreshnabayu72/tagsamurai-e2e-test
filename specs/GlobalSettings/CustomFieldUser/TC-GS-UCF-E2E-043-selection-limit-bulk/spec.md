---
id: TC-GS-UCF-E2E-043-selection-limit-bulk
title: "Selection Limit Bulk: Seleksi Manual ke-101 Diblok dan Select All Di-cap ke 100 dengan Toast Error Persist"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-145
  - TC-GS-UCF-146
coverage:
  web: automated
---

# Selection Limit Bulk: Seleksi Manual ke-101 Diblok dan Select All Di-cap ke 100 dengan Toast Error Persist

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas volume data (e): spec membutuhkan tepat 1.000 Custom Field pada Client Limit.
- Suite serial (`parallel: false`): volume Custom Field Client Limit diatur backend dan dipulihkan sesudah spec; tidak berjalan bersamaan dengan spec lain yang memakai Client Limit.
- Layar awal: hook `before` login dan hook `beforeEach` membuka Global Settings > User > Custom Field pada Client Limit; langkah tidak mengulang pembukaan layar.
- Akun aktor: Total Control Client Limit `Wulan Sari` `totalControl_automated_qaTeam4@qwertysystem.net` (Pre-setup, Master Data Count Limit 1.000, Selection Limit 100), kredensial `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun Total Control default suite (`totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client Limit memiliki 999 Custom Field `Lim 001` sampai `Lim 999` (fixture backend; definisi Custom Field tidak dapat dibuat lewat Import). Spec ini mengandalkan tepat 1.000 Custom Field; volume 1.000 diatur backend sebelum spec dijalankan (disediakan tim BE) dan dikembalikan sesudahnya. Spec tidak mengubah atau menghapus Custom Field.
- Data Dinamis: tidak ada.
- Cleanup (hook `after`): kosongkan seleksi, dismiss toast, pulihkan page size tabel ke 10, dan kembalikan volume Custom Field Client Limit oleh backend (disediakan tim BE); kembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini (Total Control Client Limit) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: hover pada checkbox Disabled dan pembacaan tooltip; pindah halaman tabel; pengamatan toast error yang tidak hilang otomatis. Menunggu 10 detik nyata pada langkah 15 (jeda pendek, kurang dari 30 detik, mengikuti TC-GS-UCF-146 langkah 3).
- State global: page size tabel (cache browser) diubah ke 100 dan dipulihkan ke 10 pada langkah akhir; flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-UCF-145: Selection Limit, seleksi manual ke-(limit+1) diblok live

1. Ubah page size menjadi 100
2. Untuk setiap baris 1 sampai 100 pada halaman 1, centang checkbox baris satu per satu
3. Verifikasi baris 1 sampai 100 tercentang
4. Verifikasi Bulk Action Bar aktif
5. Pindah ke halaman 2
6. Coba centang baris ke-101 (baris pertama halaman 2)
7. Verifikasi checkbox baris ke-101 Disabled
8. Hover checkbox yang Disabled
9. Verifikasi tooltip "You've reached the maximum selection of 100 rows."
10. Klik `(✕)` pada Bulk Action Bar

### TC-GS-UCF-146: Selection Limit, Select All di-cap ke limit dengan toast error persist

11. Klik `Select All (1000 records)`
12. Verifikasi seleksi di-cap 100 baris pertama (counter `100 custom fields selected`)
13. Verifikasi Bulk Action Bar tetap aktif
14. Verifikasi toast error persist: "Error, only the first 100 of 1000 rows were selected. Narrow your filter to include the rest."
15. Tunggu 10 detik tanpa menutup toast
16. Verifikasi toast tidak hilang otomatis
17. Dismiss toast, klik `(✕)` pada Bulk Action Bar, lalu ubah page size kembali menjadi 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: volume data (prinsip 13e): kedua TC berbagi satu volume 1.000 Custom Field Client Limit dan satu akun, sehingga tidak dipecah.
- Urutan TC mengikuti TC sumber (145, 146). Seleksi dikosongkan di langkah 10 sebelum TC-GS-UCF-146 mengandalkan seleksi kosong (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (page size 100 mengikuti TC-GS-UCF-145 langkah 1), langkah 10 dan 17 (membersihkan seleksi, toast, dan page size). Langkah 2 adalah idiom "untuk setiap baris" yang diulang 100 kali (satu centang per baris, tanpa langkah bersyarat).
- Temuan untuk QA:
  - Pre-setup Client Limit mendefinisikan 999 Custom Field (`Lim 001` sampai `Lim 999`), sedangkan TC-GS-UCF-145 dan 146 mensyaratkan tepat 1.000 Custom Field (`Select All (1000 records)`); satu Custom Field tambahan diatur backend ("volume diatur backend sebelum TC").
  - TC-GS-UCF-146 butir a ("Seleksi di-cap 100 baris pertama") tidak menyebut teks counter; spec mengasersi counter `100 custom fields selected` mengikuti format counter keputusan NC-27.
  - TC-GS-UCF-145 langkah 3 menyebut "baris ke-101" pada halaman 2 tanpa menyebut baris spesifik; spec memakai baris pertama halaman 2 (page size 100).
  - Nilai Data Uji `10 detik` (TC-GS-UCF-146) tidak tertulis verbatim di PRD (ditandai `PRD?`); spec mengikuti nilai TC.
