---
id: TC-AC-LCS-E2E-100-search-modal-changelog-normalisasi-literal-dan-hide
title: "Search Modal Changelog: Case Insensitive, Spasi, Karakter Khusus, Tanpa Hasil, dan Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-381
  - TC-AC-LCS-382
  - TC-AC-LCS-383
  - TC-AC-LCS-384
  - TC-AC-LCS-385
coverage:
  web: automated
---

# Search Modal Changelog: Case Insensitive, Spasi, Karakter Khusus, Tanpa Hasil, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Kemampuan teknis: payload `<script>alert(1)</script>` diketik sebagai teks Search (pemicu TC-AC-LCS-383, objek uji ringan kelas defense-in-depth tanpa harness eksternal).
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Preferensi kolom modal Changelog (Column Visibility dan Setup Column) yang tersimpan di browser dihapus di hook `after` (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Pengecualian A-15: Fixture BE menyediakan kemampuan overwrite dan clear riwayat Changelog per tab (disediakan tim FE/BE, idempotent); total absolut Changelog (footer `1-N of N`, jumlah baris, empty state) diasersi pada riwayat yang dibentuk di hook `before` spec ini dan dikembalikan di hook `after` suite; suite berjalan serial (`parallel: false`).
- Data uji mengacu ke berkas `fixtures/lifecycle-settings.json` (`Fixture.lifecycleSettings`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-381: Search tidak peka huruf besar-kecil dan memangkas spasi di awal dan akhir kata kunci

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Ketik Search `  gRaCe  ` (dua spasi di awal dan akhir), tekan Enter
4. Verifikasi footer `1–3 of 3` (hasil sama dengan kata kunci `Grace`)
5. Verifikasi isi kotak search tetap `  gRaCe  ` pada layar

### TC-AC-LCS-382: Search kata kunci hanya spasi diperlakukan sebagai input kosong

6. Ganti isi kotak search dengan `Grace`, tekan Enter
7. Verifikasi footer `1–3 of 3`
8. Ganti isi kotak search dengan tiga spasi, tekan Enter
9. Verifikasi footer `1–10 of 27`

### TC-AC-LCS-383: Search memperlakukan karakter khusus dan payload script sebagai teks literal

10. Ganti isi kotak search dengan `%`, tekan Enter
11. Verifikasi empty state filtered Title "No results found"
12. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
13. Verifikasi empty state filtered Title "No results found"
14. Verifikasi tidak ada dialog script yang tampil
15. Verifikasi tidak ada markup yang dirender

### TC-AC-LCS-384: Search tanpa hasil menampilkan empty state filtered

16. Ganti isi kotak search dengan `zzzz`, tekan Enter
17. Verifikasi empty state filtered: Illustration, Title "No results found", Description "Try adjusting your search or filter."

### TC-AC-LCS-385: Kolom Field yang di-hide tidak dapat dicari lewat Search

18. Klik header Column Visibility `(⋯)`
19. Uncheck `Field`
20. Ganti isi kotak search dengan `Grace`, tekan Enter
21. Verifikasi empty state filtered Title "No results found"
22. Klik header `(⋯)`
23. Check `Field` kembali
24. Tekan Enter pada kotak search yang sama
25. Verifikasi footer `1–3 of 3`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); mengganti isi kotak search antar TC mengikuti butir 9 bagian 8b.
- P-5: TC-AC-LCS-383 (payload script sebagai teks Search, kelas defense-in-depth ringan tanpa harness eksternal dan tanpa state berat) adalah satu-satunya TC objek-uji ringan kelas a pada spec ini dan berada di spec Search dengan permukaan yang sama.
- Search dipakai sebagai objek uji pada seluruh TC spec ini, bukan untuk menemukan baris target.
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - TC-AC-LCS-381: Expected butir b "isi kotak pencarian tetap sama pada layar" tidak menyebut nilai persis; spec menulis nilai yang diketik pada langkah sebelumnya.
  - TC-AC-LCS-381 dan TC-AC-LCS-382: Expected bernomor "Langkah 1" dan "Langkah 2" padahal Langkah Uji TC bernomor 2 dan 3 (Langkah 1 membuka modal); spec mengikuti urutan state yang diamati.
  - TC-AC-LCS-383: Expected bernomor "Langkah 1" dan "Langkah 2" padahal Langkah Uji TC bernomor 2 dan 3; spec mengikuti urutan state yang diamati.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
